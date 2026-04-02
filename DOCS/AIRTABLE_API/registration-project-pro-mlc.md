# REGISTRATION PROJECT (PRO +MLC)

**Table ID:** `tbl7FGL9AZlKaqOwm`  
**Base ID:** `appEurfA8kXQE3slK`

---

## Fields

| Field Name                                    | Field ID            | Type                   | Description                                                                      |
| --------------------------------------------- | ------------------- | ---------------------- | -------------------------------------------------------------------------------- |
| Name                                          | `fldBvNz4tqZnZvFsb` | Text                   | A single line of text.                                                           |
| Compositions                                  | `fldHiMGgWMpTNCQmV` | Link to another record | Array of linked records IDs from the Compositions table.                         |
| Notes                                         | `fldTQSIXC6JxPwfad` | Long text              | Multiple lines of text, which may contain "mention tokens", e.g. <airtable:mention id="menE1i9oBaGX3DseR">@Alex</airtable:mention> |
| Album                                         | `fldnqyyBlGLy1aynQ` | Text                   | A single line of text.                                                           |
| Song Title In PRO (from Compositions)         | `fldzX2NrXWLrLP7VJ` | Lookup                 | Array of Song Title In PRO fields in linked Compositions records.                |
| Recordings (from Compositions)                | `fldwiWBv6UPr8QhoN` | Lookup                 | Array of Recordings fields in linked Compositions records.                       |
| All Songwriters (from Compositions)           | `fldssbpk1rZaIH8JQ` | Lookup                 | Array of All Songwriters fields in linked Compositions records.                  |
| All Original Publishers (from Compositions)   | `fldmHr6i3FsHrYpj0` | Lookup                 | Array of All Original Publishers fields in linked Compositions records.          |
| All Admin Publishers (from Compositions)      | `fldcvv5IX1gyWBL4W` | Lookup                 | Array of All Admin Publishers fields in linked Compositions records.             |
| Involved PROs (from Compositions)             | `fldaItWbLND7ehdgP` | Lookup                 | Array of Involved PROs fields in linked Compositions records.                    |
| Releases (from Compositions)                  | `fldFvEichGHuAMsqH` | Lookup                 | Array of Releases fields in linked Compositions records.                         |
| ISWC (from Compositions)                      | `fldDdwjU6NevzbHUo` | Lookup                 | Array of ISWC fields in linked Compositions records.                             |
| PROs                                          | `fld9cuXBmdB2JWasO` | Multiple select        | Array of selected option names. When creating or updating records, if a choice string does not exactly match an existing option, the request will fail with an INVALID_MULTIPLE_CHOICE_OPTIONS error unless the typecast parameter is enabled. If typecast is enabled, a new choice will be created if one does not exactly match. |
| Recordings (from Composition)                 | `fldzapq4yl5ZSkcg5` | Lookup                 | Array of Recordings fields in linked Compositions records.                       |
| MLC Song Code (from Compositions)             | `fldqYlEiwg1FNJS3R` | Lookup                 | Array of MLC Song Code fields in linked Compositions records.                    |
| MLC work links (from Compositions)            | `fldXU3Nz2BnzAWMqr` | Lookup                 | Array of MLC work links fields in linked Compositions records.                   |
| Last Modified                                 | `fld1xXEiNXAoEXUbK` | Formula                | Computed value: LAST_MODIFIED_TIME() .                                           |
| MLC Status                                    | `fld9ybfZN4DlAjpKh` | Multiple select        | Array of selected option names. When creating or updating records, if a choice string does not exactly match an existing option, the request will fail with an INVALID_MULTIPLE_CHOICE_OPTIONS error unless the typecast parameter is enabled. If typecast is enabled, a new choice will be created if one does not exactly match. |
| Matched Recording on MLC                      | `fldTTsqgKn6xtbFKy` | Link to another record | Array of linked records IDs from the Recordings table.                           |
| Recordings that need to be matched on The MLC | `fld3f4yh84I7JowYu` | Lookup                 | Array of Recordings fields in linked Compositions records.                       |

---

## List Records

**Endpoint:** `GET /v0/appEurfA8kXQE3slK/registration%20project%20(pro%20+mlc)`

To list records in REGISTRATION PROJECT (PRO +MLC) , issue a GET request to the REGISTRATION PROJECT (PRO +MLC) endpoint. Note that table names and table ids can be used interchangeably. Using table ids means table name changes do not require modifications to your API request.

Returned records do not include any fields with "empty" values, e.g. "" , [] , or false .

```bash
curl "https://api.airtable.com/v0/appEurfA8kXQE3slK/REGISTRATION%20PROJECT%20(PRO%20%2BMLC)?maxRecords=3&view=Grid%20view" \
  -H "Authorization: Bearer YOUR_SECRET_API_TOKEN"
```

### Query Parameters

| Parameter               | Type             | Required   | Description                                                                      |
| ----------------------- | ---------------- | ---------- | -------------------------------------------------------------------------------- |
| `fields`                | array of strings | optional   | Only data for fields whose names are in this list will be included in the result. If you don't need every field, you can use this parameter to reduce the amount of data transferred. For example, to only return data from Name and Compositions , send these two query parameters: fields%5B%5D=Name&field |
| `filterByFormula`       | string           | optional   | A formula used to filter records. The formula will be evaluated for each record, and if the result is not 0 , false , "" , NaN , [] , or #Error! the record will be included in the response. We recommend testing your formula in the Formula field UI before using it in your API request. If combined wit |
| `maxRecords`            | number           | optional   | The maximum total number of records that will be returned in your requests. If this value is larger than pageSize (which is 100 by default), you may have to load multiple pages to reach this total. See the Pagination section below for more. |
| `pageSize`              | number           | optional   | The number of records returned in each request. Must be less than or equal to 100. Default is 100. See the Pagination section below for more. |
| `sort`                  | array of objects | optional   | A list of sort objects that specifies how the records will be ordered. Each sort object must have a field key specifying the name of the field to sort on, and an optional direction key that is either "asc" or "desc" . The default direction is "asc" . The sort parameter overrides the sorting of the v |
| `view`                  | string           | optional   | The name or ID of a view in the REGISTRATION PROJECT (PRO +MLC) table. If set, only the records in that view will be returned. The records will be sorted according to the order of the view unless the sort parameter is included, which overrides that order. Fields hidden in this view will be returned |
| `cellFormat`            | string           | optional   | The format that should be used for cell values. Supported values are: json : cells will be formatted as JSON, depending on the field type. string : cells will be formatted as user-facing strings, regardless of the field type. The timeZone and userLocale parameters are required when using string as t |
| `timeZone`              | string           | optional   | The time zone that should be used to format dates when using string as the cellFormat . This parameter is required when using string as the cellFormat . |
| `userLocale`            | string           | optional   | The user locale that should be used to format dates when using string as the cellFormat . This parameter is required when using string as the cellFormat . |
| `returnFieldsByFieldId` | boolean          | optional   | An optional boolean value that lets you return field objects where the key is the field id. This defaults to false , which returns field objects where the key is the field name. |
| `recordMetadata`        | array of strings | optional   | An optional field that, if includes commentCount , adds a commentCount read only property on each record returned. |

---

## Retrieve a Record

**Endpoint:** `GET /v0/appEurfA8kXQE3slK/registration%20project%20(pro%20+mlc)`

To retrieve an existing record in REGISTRATION PROJECT (PRO +MLC) table, issue a GET request to the record endpoint.

Any "empty" fields (e.g. "" , [] , or false ) in the record will not be returned.

```bash
curl https://api.airtable.com/v0/appEurfA8kXQE3slK/REGISTRATION%20PROJECT%20(PRO%20%2BMLC)/recIDEqF2cwZpLdL3 \
  -H "Authorization: Bearer YOUR_SECRET_API_TOKEN"
```

---

## Create Records

**Endpoint:** `POST /v0/appEurfA8kXQE3slK/registration%20project%20(pro%20+mlc)`

To create new records, issue a POST request to the REGISTRATION PROJECT (PRO +MLC) endpoint. Note that table names and table ids can be used interchangeably. Using table ids means table name changes do not require modifications to your API request.

Your request body should include an array of up to 10 record objects. Each of these objects should have one key whose value is an inner object containing your record's cell values, keyed by either field name or field id.

```bash
curl -X POST https://api.airtable.com/v0/appEurfA8kXQE3slK/REGISTRATION%20PROJECT%20(PRO%20%2BMLC) \
  -H "Authorization: Bearer YOUR_SECRET_API_TOKEN" \
  -H "Content-Type: application/json" \
  --data '{
  "records": [
    {
      "fields": {
        "Name": "ABIDE WITH ME",
        "Compositions": [
          "recdFggjDdHANgq0p"
        ],
        "PROs": [
          "ASCAP - Doublecheck or Claim"
        ],
        "MLC Status": [
          "No Registration Found"
        ]
      }
    },
    {
      "fields": {
        "Name": "ABIDE WITH ME",
        "Compositions": [
          "recHn8Zy71HNYu8Cf"
        ],
        "Notes": "Already registered by SPOONE. ",
        "PROs": [
          "ASCAP claimed"
        ],
        "MLC Status": [
          "Doublecheck or claim on MLC"
        ]
      }
    }
  ]
}'
```

---

## Update / Upsert Records

**Endpoint:** `PATCH /v0/appEurfA8kXQE3slK/registration%20project%20(pro%20+mlc)`

To update REGISTRATION PROJECT (PRO +MLC) records, issue a request to the REGISTRATION PROJECT (PRO +MLC) endpoint. Table names and table IDs can be used interchangeably. Using table IDs means table name changes won't require modifying your API request code. A PATCH request will only update the fields included in the request. Fields not included in the request will be unchanged. A PUT request will perform a destructive update and clear all unincluded cell values.

Your request body should include an array of up to 10 record objects. Each of these objects should have an id property representing the record ID and a fields property which contains all of your record's cell values by field name or field id for all of your record's cell values by field name.

```bash
curl -X PATCH https://api.airtable.com/v0/appEurfA8kXQE3slK/REGISTRATION%20PROJECT%20(PRO%20%2BMLC) \
  -H "Authorization: Bearer YOUR_SECRET_API_TOKEN" \
  -H "Content-Type: application/json" \
  --data '{
  "records": [
    {
      "id": "recIDEqF2cwZpLdL3",
      "fields": {
        "Name": "ABIDE WITH ME",
        "Compositions": [
          "recdFggjDdHANgq0p"
        ],
        "PROs": [
          "ASCAP - Doublecheck or Claim"
        ],
        "MLC Status": [
          "No Registration Found"
        ]
      }
    },
    {
      "id": "recHTjxwxRjF9gZuQ",
      "fields": {
        "Name": "ABIDE WITH ME",
        "Compositions": [
          "recHn8Zy71HNYu8Cf"
        ],
        "Notes": "Already registered by SPOONE. ",
        "PROs": [
          "ASCAP claimed"
        ],
        "MLC Status": [
          "Doublecheck or claim on MLC"
        ]
      }
    },
    {
      "id": "reclItmqccgZSlU8t",
      "fields": {
        "Name": "ADESTE FIDELES ",
        "Compositions": [
          "recPVDBwFj577mY3c"
        ],
        "Notes": "12/11/25 This composition has been reverted from SWEET ON TOP PUBLISHING back to SPOONE MUSIC CORPORATION.",
        "Album": "Family Christmas",
        "PROs": [
          "ASCAP claimed"
        ],
        "MLC Status": [
          "Claimed by SONGS OF PEER",
          "Claimed by SWEET ON TOP PUB"
        ]
      }
    }
  ]
}'
```

---

## Delete Records

**Endpoint:** `DELETE /v0/appEurfA8kXQE3slK/registration%20project%20(pro%20+mlc)`

To delete REGISTRATION PROJECT (PRO +MLC) records, issue a DELETE request to the REGISTRATION PROJECT (PRO +MLC) endpoint. Note that table names and table ids can be used interchangeably. Using table ids means table name changes do not require modifications to your API request.

Your request should include a URL-encoded array of up to 10 record IDs to delete.

```bash
curl -X DELETE https://api.airtable.com/v0/appEurfA8kXQE3slK/REGISTRATION%20PROJECT%20(PRO%20%2BMLC) \
  -H "Authorization: Bearer YOUR_SECRET_API_TOKEN" \
  -G \
  --data-urlencode 'records[]=recIDEqF2cwZpLdL3' \
  --data-urlencode 'records[]=recHTjxwxRjF9gZuQ'
```

