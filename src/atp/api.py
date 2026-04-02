"""Requests-based AirTable API client."""
from __future__ import annotations

import time
from collections import deque

import requests


class AirtableClient:
    BASE_URL = "https://api.airtable.com/v0"
    _RATE_LIMIT = 5  # max requests per second

    def __init__(
        self,
        token: str,
        base_id: str,
        session: requests.Session | None = None,
        timeout: int = 30,
    ) -> None:
        self.base_id = base_id
        self._timeout = timeout
        self._session = session or requests.Session()
        self._session.headers.update({
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        })
        # GET-only response cache; keyed on (url, *sorted_params).
        self._cache: dict[tuple[str, ...], dict[str, object]] = {}
        # Timestamps of the last _RATE_LIMIT requests (monotonic seconds).
        self._timestamps: deque[float] = deque(maxlen=self._RATE_LIMIT)

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _throttle(self) -> None:
        """Block until sending one more request won't exceed the rate limit."""
        if len(self._timestamps) == self._RATE_LIMIT:
            wait = 1.0 - (time.monotonic() - self._timestamps[0])
            if wait > 0:
                time.sleep(wait)
        self._timestamps.append(time.monotonic())

    def _cache_key(self, url: str, params: dict[str, str | int] | None) -> tuple[str, ...]:
        if not params:
            return (url,)
        return (url,) + tuple(sorted((str(k), str(v)) for k, v in params.items()))

    def _get(self, url: str, params: dict[str, str | int] | None = None) -> dict[str, object]:
        """GET with caching and rate-limiting."""
        key = self._cache_key(url, params)
        if key in self._cache:
            return self._cache[key]
        self._throttle()
        result: dict[str, object] = self._session.get(url, params=params, timeout=self._timeout).json()  # type: ignore[no-any-return]
        self._cache[key] = result
        return result

    def _url(self, table_id: str) -> str:
        return f"{self.BASE_URL}/{self.base_id}/{table_id}"

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def list_records(
        self,
        table_id: str,
        filter_formula: str = "",
        max_records: int = 0,
        view: str = "",
        offset: str = "",
    ) -> dict[str, object]:
        params: dict[str, str | int] = {}
        if filter_formula:
            params["filterByFormula"] = filter_formula
        if max_records > 0:
            params["maxRecords"] = max_records
        if view:
            params["view"] = view
        if offset:
            params["offset"] = offset
        return self._get(self._url(table_id), params or None)

    def retrieve_record(self, table_id: str, record_id: str) -> dict[str, object]:
        return self._get(f"{self._url(table_id)}/{record_id}")

    def create_records(
        self,
        table_id: str,
        fields_list: list[dict[str, object]],
        typecast: bool = False,
    ) -> dict[str, object]:
        self._throttle()
        body: dict[str, object] = {"records": [{"fields": f} for f in fields_list]}
        if typecast:
            body["typecast"] = True
        return self._session.post(self._url(table_id), json=body, timeout=self._timeout).json()  # type: ignore[no-any-return]

    def update_records(self, table_id: str, records: list[dict[str, object]]) -> dict[str, object]:
        """records: [{"id": "recXXX", "fields": {...}}, ...]"""
        self._throttle()
        return self._session.patch(self._url(table_id), json={"records": records}, timeout=self._timeout).json()  # type: ignore[no-any-return]

    def delete_records(self, table_id: str, record_ids: list[str]) -> dict[str, object]:
        self._throttle()
        params = [("records[]", rid) for rid in record_ids]
        return self._session.delete(self._url(table_id), params=params, timeout=self._timeout).json()  # type: ignore[no-any-return]
