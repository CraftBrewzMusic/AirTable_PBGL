# PROGRESS REPORT

**Table ID:** `tblPBXgEXtDH6TaRR`  
**Base ID:** `appEurfA8kXQE3slK`

---

## Fields

| Field Name            | Field ID            | Type                   | Description                                                                      |
| --------------------- | ------------------- | ---------------------- | -------------------------------------------------------------------------------- |
| Release Title         | `fldFb7YFRUNKDKQdp` | Text                   | A single line of text.                                                           |
| Release type          | `fldeIOemLOoixI0U5` | Single select          | Selected option name. When creating or updating records, if the choice string does not exactly match an existing option, the request will fail with an INVALID_MULTIPLE_CHOICE_OPTIONS error unless the typecast parameter is enabled. If typecast is enabled, a new choice will be created if one does not exactly match. |
| Artist                | `fldtNgc6KEbNgrgGg` | Text                   | A single line of text.                                                           |
| PRIORITY              | `fldIQZFwVBKLhCbWC` | Single select          | Selected option name. When creating or updating records, if the choice string does not exactly match an existing option, the request will fail with an INVALID_MULTIPLE_CHOICE_OPTIONS error unless the typecast parameter is enabled. If typecast is enabled, a new choice will be created if one does not exactly match. |
| Status                | `fldKmbbiS5A8XK92K` | Single select          | Selected option name. When creating or updating records, if the choice string does not exactly match an existing option, the request will fail with an INVALID_MULTIPLE_CHOICE_OPTIONS error unless the typecast parameter is enabled. If typecast is enabled, a new choice will be created if one does not exactly match. |
| NOTES                 | `fld7f2ziMrqMRAebl` | Long text              | Multiple lines of text, which may contain "mention tokens", e.g. <airtable:mention id="menE1i9oBaGX3DseR">@Alex</airtable:mention> |
| Physical copy on hand | `fldlgVdq6Bf7gGOS2` | Checkbox               | This field is "true" when checked and otherwise empty.                           |
| CBz Pub Research      | `flduOLHR5zgIYaNhk` | Checkbox               | This field is "true" when checked and otherwise empty.                           |
| Splits Confirmed      | `fldcq2jB9wEcMCrZi` | Checkbox               | This field is "true" when checked and otherwise empty.                           |
| Tagged                | `fldrCK2V7XjGvmfP6` | Checkbox               | This field is "true" when checked and otherwise empty.                           |
| Lyric Sheets          | `fldLKpmuxWZ6Hxq4X` | Checkbox               | This field is "true" when checked and otherwise empty.                           |
| Spreadsheet Verified  | `fld4rsw4q6tJoXM1L` | Checkbox               | This field is "true" when checked and otherwise empty.                           |
| PBGL Approved         | `fldZbby1Q4esefLhr` | Checkbox               | This field is "true" when checked and otherwise empty.                           |
| SoundExchange Onboard | `flduhK6psUxE5RyXi` | Checkbox               | This field is "true" when checked and otherwise empty.                           |
| Missing Files         | `fldlxqWNDAXgVWgUt` | Text                   | A single line of text.                                                           |
| Unreconciled Songs    | `fld8sYklhyeZnoAau` | Text                   | A single line of text.                                                           |
| SOP Delivery          | `fldiqU9Z7MNv1wcFt` | Checkbox               | This field is "true" when checked and otherwise empty.                           |
| Releases              | `fldYG5yQVaoJrH8LE` | Link to another record | Array of linked records IDs from the Releases table.                             |
| UPC (from Releases)   | `fldqDkEctL0Hdjyvg` | Lookup                 | Array of UPC fields in linked Releases records.                                  |

---

## List Records

**Endpoint:** `GET /v0/appEurfA8kXQE3slK/progress%20report`

To list records in PROGRESS REPORT , issue a GET request to the PROGRESS REPORT endpoint. Note that table names and table ids can be used interchangeably. Using table ids means table name changes do not require modifications to your API request.

Returned records do not include any fields with "empty" values, e.g. "" , [] , or false .

```bash
curl "https://api.airtable.com/v0/appEurfA8kXQE3slK/PROGRESS%20REPORT?maxRecords=3&view=Default" \
  -H "Authorization: Bearer YOUR_SECRET_API_TOKEN"
```

### Query Parameters

| Parameter               | Type             | Required   | Description                                                                      |
| ----------------------- | ---------------- | ---------- | -------------------------------------------------------------------------------- |
| `fields`                | array of strings | optional   | Only data for fields whose names are in this list will be included in the result. If you don't need every field, you can use this parameter to reduce the amount of data transferred. For example, to only return data from Release Title and Release type , send these two query parameters: fields%5B%5D=R |
| `filterByFormula`       | string           | optional   | A formula used to filter records. The formula will be evaluated for each record, and if the result is not 0 , false , "" , NaN , [] , or #Error! the record will be included in the response. We recommend testing your formula in the Formula field UI before using it in your API request. If combined wit |
| `maxRecords`            | number           | optional   | The maximum total number of records that will be returned in your requests. If this value is larger than pageSize (which is 100 by default), you may have to load multiple pages to reach this total. See the Pagination section below for more. |
| `pageSize`              | number           | optional   | The number of records returned in each request. Must be less than or equal to 100. Default is 100. See the Pagination section below for more. |
| `sort`                  | array of objects | optional   | A list of sort objects that specifies how the records will be ordered. Each sort object must have a field key specifying the name of the field to sort on, and an optional direction key that is either "asc" or "desc" . The default direction is "asc" . The sort parameter overrides the sorting of the v |
| `view`                  | string           | optional   | The name or ID of a view in the PROGRESS REPORT table. If set, only the records in that view will be returned. The records will be sorted according to the order of the view unless the sort parameter is included, which overrides that order. Fields hidden in this view will be returned in the results. |
| `cellFormat`            | string           | optional   | The format that should be used for cell values. Supported values are: json : cells will be formatted as JSON, depending on the field type. string : cells will be formatted as user-facing strings, regardless of the field type. The timeZone and userLocale parameters are required when using string as t |
| `timeZone`              | string           | optional   | The time zone that should be used to format dates when using string as the cellFormat . This parameter is required when using string as the cellFormat . |
| `userLocale`            | string           | optional   | The user locale that should be used to format dates when using string as the cellFormat . This parameter is required when using string as the cellFormat . |
| `returnFieldsByFieldId` | boolean          | optional   | An optional boolean value that lets you return field objects where the key is the field id. This defaults to false , which returns field objects where the key is the field name. |
| `recordMetadata`        | array of strings | optional   | An optional field that, if includes commentCount , adds a commentCount read only property on each record returned. |

---

## Retrieve a Record

**Endpoint:** `GET /v0/appEurfA8kXQE3slK/progress%20report`

To retrieve an existing record in PROGRESS REPORT table, issue a GET request to the record endpoint.

Any "empty" fields (e.g. "" , [] , or false ) in the record will not be returned.

```bash
curl https://api.airtable.com/v0/appEurfA8kXQE3slK/PROGRESS%20REPORT/recFGa7MniT0S2buD \
  -H "Authorization: Bearer YOUR_SECRET_API_TOKEN"
```

---

## Create Records

**Endpoint:** `POST /v0/appEurfA8kXQE3slK/progress%20report`

To create new records, issue a POST request to the PROGRESS REPORT endpoint. Note that table names and table ids can be used interchangeably. Using table ids means table name changes do not require modifications to your API request.

Your request body should include an array of up to 10 record objects. Each of these objects should have one key whose value is an inner object containing your record's cell values, keyed by either field name or field id.

```bash
curl -X POST https://api.airtable.com/v0/appEurfA8kXQE3slK/PROGRESS%20REPORT \
  -H "Authorization: Bearer YOUR_SECRET_API_TOKEN" \
  -H "Content-Type: application/json" \
  --data '{
  "records": [
    {
      "fields": {
        "Release Title": "\"Pat\" On Mike",
        "Release type": "EP",
        "Artist": "Pat Boone",
        "SoundExchange Onboard": true
      }
    },
    {
      "fields": {
        "Release Title": "A Foggy Day (Live On The Pat Boone Chevy Showroom, November 7, 1957)",
        "Release type": "Single",
        "Artist": "Pat Boone",
        "SoundExchange Onboard": true
      }
    }
  ]
}'
```

---

## Update / Upsert Records

**Endpoint:** `PATCH /v0/appEurfA8kXQE3slK/progress%20report`

To update PROGRESS REPORT records, issue a request to the PROGRESS REPORT endpoint. Table names and table IDs can be used interchangeably. Using table IDs means table name changes won't require modifying your API request code. A PATCH request will only update the fields included in the request. Fields not included in the request will be unchanged. A PUT request will perform a destructive update and clear all unincluded cell values.

Your request body should include an array of up to 10 record objects. Each of these objects should have an id property representing the record ID and a fields property which contains all of your record's cell values by field name or field id for all of your record's cell values by field name.

```bash
curl -X PATCH https://api.airtable.com/v0/appEurfA8kXQE3slK/PROGRESS%20REPORT \
  -H "Authorization: Bearer YOUR_SECRET_API_TOKEN" \
  -H "Content-Type: application/json" \
  --data '{
  "records": [
    {
      "id": "recFGa7MniT0S2buD",
      "fields": {
        "Release Title": "\"Pat\" On Mike",
        "Release type": "EP",
        "Artist": "Pat Boone",
        "SoundExchange Onboard": true
      }
    },
    {
      "id": "recvP68aGHzyU2zc9",
      "fields": {
        "Release Title": "A Foggy Day (Live On The Pat Boone Chevy Showroom, November 7, 1957)",
        "Release type": "Single",
        "Artist": "Pat Boone",
        "SoundExchange Onboard": true
      }
    },
    {
      "id": "recLFahsaozJh3jky",
      "fields": {
        "Release Title": "Angel Talk",
        "Release type": "EP",
        "Artist": "Pat Boone",
        "SoundExchange Onboard": true
      }
    }
  ]
}'
```

---

## Delete Records

**Endpoint:** `DELETE /v0/appEurfA8kXQE3slK/progress%20report`

To delete PROGRESS REPORT records, issue a DELETE request to the PROGRESS REPORT endpoint. Note that table names and table ids can be used interchangeably. Using table ids means table name changes do not require modifications to your API request.

Your request should include a URL-encoded array of up to 10 record IDs to delete.

```bash
curl -X DELETE https://api.airtable.com/v0/appEurfA8kXQE3slK/PROGRESS%20REPORT \
  -H "Authorization: Bearer YOUR_SECRET_API_TOKEN" \
  -G \
  --data-urlencode 'records[]=recFGa7MniT0S2buD' \
  --data-urlencode 'records[]=recvP68aGHzyU2zc9'
```

