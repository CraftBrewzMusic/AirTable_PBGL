# Songwriters

**Table ID:** `tbl2KLh2RIrS5AmSX`  
**Base ID:** `appEurfA8kXQE3slK`

---

## Fields

| Field Name                  | Field ID            | Type                   | Description                                                                      |
| --------------------------- | ------------------- | ---------------------- | -------------------------------------------------------------------------------- |
| Name as listed in PRO       | `fld50qVly0wjnxL8t` | Formula                | Computed value: { Last Name } & " " & { Suffix } & " " & { First Name } & " " & { Middle Name } & " " & { Interested Party } . |
| IPI Number                  | `fld712K46CgGyjAEQ` | Text                   | A single line of text.                                                           |
| Verified name, PRO, and IPI | `fldvOqKgfAWZZhZ0d` | Checkbox               | This field is "true" when checked and otherwise empty.                           |
| Notes                       | `fldgYC4IjCcx77VKU` | Long text              | Multiple lines of text, which may contain "mention tokens", e.g. <airtable:mention id="menE1i9oBaGX3DseR">@Alex</airtable:mention> |
| First Name                  | `fldynnsFy2uSBpifH` | Text                   | A single line of text.                                                           |
| Middle Name                 | `fldUbHMnW5KnLRPh6` | Text                   | A single line of text.                                                           |
| Last Name                   | `fldo5pT323Fg9vrvX` | Text                   | A single line of text.                                                           |
| Suffix                      | `fldxUR55wBw9jclxS` | Text                   | A single line of text.                                                           |
| Interested Party            | `fld5Zt8QYRPNL1wpC` | Text                   | A single line of text.                                                           |
| Alias(es) in PRO            | `fldsNiY7FUJjvSEd8` | Long text              | Multiple lines of text, which may contain "mention tokens", e.g. <airtable:mention id="menE1i9oBaGX3DseR">@Alex</airtable:mention> |
| PRO Affiliation             | `fldj2bMLt8EY2yPAM` | Single select          | Selected option name. When creating or updating records, if the choice string does not exactly match an existing option, the request will fail with an INVALID_MULTIPLE_CHOICE_OPTIONS error unless the typecast parameter is enabled. If typecast is enabled, a new choice will be created if one does not exactly match. |
| Compositions                | `fldEoEyYlIjaKwrkq` | Link to another record | Array of linked records IDs from the Compositions table. Because this field is configured to show records in reversed order, the order of records in the app will be reversed compared to what you see here. |
| Published by                | `fld5mmxZv286NzYCs` | Link to another record | Array of linked records IDs from the Publishers table.                           |
| Legal Docs                  | `fldwccASH977BT3le` | Link to another record | Array of linked records IDs from the Legal Docs table.                           |
| Compositions 2              | `fld0bWrdHt8Z8ONQz` | Link to another record | Array of linked records IDs from the Compositions table.                         |
| Compositions 3              | `fldwlANx0ME3oq8Ir` | Link to another record | Array of linked records IDs from the Compositions table.                         |
| Compositions 4              | `fld9gU0iajX6WkAXL` | Link to another record | Array of linked records IDs from the Compositions table.                         |
| Compositions 5              | `fldYlChRBjIjrCR1V` | Link to another record | Array of linked records IDs from the Compositions table.                         |
| Compositions 6              | `fldT9yT04PWmi7p1T` | Link to another record | Array of linked records IDs from the Compositions table.                         |
| Compositions 7              | `fld28DiKnKlCMG76H` | Link to another record | Array of linked records IDs from the Compositions table.                         |
| Compositions 8              | `fld06Logrgm1PYtJO` | Link to another record | Array of linked records IDs from the Compositions table.                         |
| Compositions 7 copy         | `fldKl1LiSp8T5mJIT` | Link to another record | Array of linked records IDs from the Compositions table.                         |
| Compositions 7 copy copy    | `fldSdlzArrF30VgBR` | Link to another record | Array of linked records IDs from the Compositions table.                         |

---

## List Records

**Endpoint:** `GET /v0/appEurfA8kXQE3slK/songwriters`

To list records in Songwriters , issue a GET request to the Songwriters endpoint. Note that table names and table ids can be used interchangeably. Using table ids means table name changes do not require modifications to your API request.

Returned records do not include any fields with "empty" values, e.g. "" , [] , or false .

```bash
curl "https://api.airtable.com/v0/appEurfA8kXQE3slK/Songwriters?maxRecords=3&view=Default" \
  -H "Authorization: Bearer YOUR_SECRET_API_TOKEN"
```

### Query Parameters

| Parameter               | Type             | Required   | Description                                                                      |
| ----------------------- | ---------------- | ---------- | -------------------------------------------------------------------------------- |
| `fields`                | array of strings | optional   | Only data for fields whose names are in this list will be included in the result. If you don't need every field, you can use this parameter to reduce the amount of data transferred. For example, to only return data from Name as listed in PRO and IPI Number , send these two query parameters: fields%5 |
| `filterByFormula`       | string           | optional   | A formula used to filter records. The formula will be evaluated for each record, and if the result is not 0 , false , "" , NaN , [] , or #Error! the record will be included in the response. We recommend testing your formula in the Formula field UI before using it in your API request. If combined wit |
| `maxRecords`            | number           | optional   | The maximum total number of records that will be returned in your requests. If this value is larger than pageSize (which is 100 by default), you may have to load multiple pages to reach this total. See the Pagination section below for more. |
| `pageSize`              | number           | optional   | The number of records returned in each request. Must be less than or equal to 100. Default is 100. See the Pagination section below for more. |
| `sort`                  | array of objects | optional   | A list of sort objects that specifies how the records will be ordered. Each sort object must have a field key specifying the name of the field to sort on, and an optional direction key that is either "asc" or "desc" . The default direction is "asc" . The sort parameter overrides the sorting of the v |
| `view`                  | string           | optional   | The name or ID of a view in the Songwriters table. If set, only the records in that view will be returned. The records will be sorted according to the order of the view unless the sort parameter is included, which overrides that order. Fields hidden in this view will be returned in the results. To o |
| `cellFormat`            | string           | optional   | The format that should be used for cell values. Supported values are: json : cells will be formatted as JSON, depending on the field type. string : cells will be formatted as user-facing strings, regardless of the field type. The timeZone and userLocale parameters are required when using string as t |
| `timeZone`              | string           | optional   | The time zone that should be used to format dates when using string as the cellFormat . This parameter is required when using string as the cellFormat . |
| `userLocale`            | string           | optional   | The user locale that should be used to format dates when using string as the cellFormat . This parameter is required when using string as the cellFormat . |
| `returnFieldsByFieldId` | boolean          | optional   | An optional boolean value that lets you return field objects where the key is the field id. This defaults to false , which returns field objects where the key is the field name. |
| `recordMetadata`        | array of strings | optional   | An optional field that, if includes commentCount , adds a commentCount read only property on each record returned. |

---

## Retrieve a Record

**Endpoint:** `GET /v0/appEurfA8kXQE3slK/songwriters`

To retrieve an existing record in Songwriters table, issue a GET request to the record endpoint.

Any "empty" fields (e.g. "" , [] , or false ) in the record will not be returned.

```bash
curl https://api.airtable.com/v0/appEurfA8kXQE3slK/Songwriters/recJThUCbUnwEm0IO \
  -H "Authorization: Bearer YOUR_SECRET_API_TOKEN"
```

---

## Create Records

**Endpoint:** `POST /v0/appEurfA8kXQE3slK/songwriters`

To create new records, issue a POST request to the Songwriters endpoint. Note that table names and table ids can be used interchangeably. Using table ids means table name changes do not require modifications to your API request.

Your request body should include an array of up to 10 record objects. Each of these objects should have one key whose value is an inner object containing your record's cell values, keyed by either field name or field id.

```bash
curl -X POST https://api.airtable.com/v0/appEurfA8kXQE3slK/Songwriters \
  -H "Authorization: Bearer YOUR_SECRET_API_TOKEN" \
  -H "Content-Type: application/json" \
  --data '{
  "records": [
    {
      "fields": {
        "IPI Number": "65258",
        "First Name": "LEE",
        "Middle Name": "ROY",
        "Last Name": "ABERNATHY",
        "Alias(es) in PRO": "N/A",
        "PRO Affiliation": "ASCAP",
        "Compositions": [
          "recjZgKFuQMkWrrah"
        ],
        "Published by": [
          "rec2zj4SHT72jPwBN",
          "recTseZCQEgXUe8DX"
        ],
        "Compositions 2": [
          "recjZgKFuQMkWrrah"
        ]
      }
    },
    {
      "fields": {
        "IPI Number": "70759",
        "First Name": "EWART",
        "Middle Name": "G",
        "Last Name": "ABNER",
        "Suffix": "JR",
        "PRO Affiliation": "BMI",
        "Compositions": [
          "recjuzT8JZaQYJMl5"
        ],
        "Published by": [
          "recA8i9RZDhiooJTk"
        ],
        "Compositions 2": [
          "recjuzT8JZaQYJMl5"
        ]
      }
    }
  ]
}'
```

---

## Update / Upsert Records

**Endpoint:** `PATCH /v0/appEurfA8kXQE3slK/songwriters`

To update Songwriters records, issue a request to the Songwriters endpoint. Table names and table IDs can be used interchangeably. Using table IDs means table name changes won't require modifying your API request code. A PATCH request will only update the fields included in the request. Fields not included in the request will be unchanged. A PUT request will perform a destructive update and clear all unincluded cell values.

Your request body should include an array of up to 10 record objects. Each of these objects should have an id property representing the record ID and a fields property which contains all of your record's cell values by field name or field id for all of your record's cell values by field name.

```bash
curl -X PATCH https://api.airtable.com/v0/appEurfA8kXQE3slK/Songwriters \
  -H "Authorization: Bearer YOUR_SECRET_API_TOKEN" \
  -H "Content-Type: application/json" \
  --data '{
  "records": [
    {
      "id": "recJThUCbUnwEm0IO",
      "fields": {
        "IPI Number": "65258",
        "First Name": "LEE",
        "Middle Name": "ROY",
        "Last Name": "ABERNATHY",
        "Alias(es) in PRO": "N/A",
        "PRO Affiliation": "ASCAP",
        "Compositions": [
          "recjZgKFuQMkWrrah"
        ],
        "Published by": [
          "rec2zj4SHT72jPwBN",
          "recTseZCQEgXUe8DX"
        ],
        "Compositions 2": [
          "recjZgKFuQMkWrrah"
        ]
      }
    },
    {
      "id": "recDIAhzNYFnleORH",
      "fields": {
        "IPI Number": "70759",
        "First Name": "EWART",
        "Middle Name": "G",
        "Last Name": "ABNER",
        "Suffix": "JR",
        "PRO Affiliation": "BMI",
        "Compositions": [
          "recjuzT8JZaQYJMl5"
        ],
        "Published by": [
          "recA8i9RZDhiooJTk"
        ],
        "Compositions 2": [
          "recjuzT8JZaQYJMl5"
        ]
      }
    },
    {
      "id": "recnAbCCLQgZsRFSx",
      "fields": {
        "IPI Number": "170362",
        "First Name": "STANLEY ",
        "Last Name": "ADAMS",
        "PRO Affiliation": "ASCAP",
        "Compositions": [
          "recwkrj6r5lXKIyXw"
        ],
        "Published by": [
          "recivR09HCpJrhv3y"
        ],
        "Compositions 4": [
          "recwkrj6r5lXKIyXw"
        ]
      }
    }
  ]
}'
```

---

## Delete Records

**Endpoint:** `DELETE /v0/appEurfA8kXQE3slK/songwriters`

To delete Songwriters records, issue a DELETE request to the Songwriters endpoint. Note that table names and table ids can be used interchangeably. Using table ids means table name changes do not require modifications to your API request.

Your request should include a URL-encoded array of up to 10 record IDs to delete.

```bash
curl -X DELETE https://api.airtable.com/v0/appEurfA8kXQE3slK/Songwriters \
  -H "Authorization: Bearer YOUR_SECRET_API_TOKEN" \
  -G \
  --data-urlencode 'records[]=recJThUCbUnwEm0IO' \
  --data-urlencode 'records[]=recDIAhzNYFnleORH'
```

