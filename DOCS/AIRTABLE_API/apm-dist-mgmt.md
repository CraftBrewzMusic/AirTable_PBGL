# APM Dist Mgmt

**Table ID:** `tbllGX2Hxg3SGhJMa`  
**Base ID:** `appEurfA8kXQE3slK`

---

## Fields

| Field Name                         | Field ID            | Type                   | Description                                                                      |
| ---------------------------------- | ------------------- | ---------------------- | -------------------------------------------------------------------------------- |
| Track Title                        | `fldw6XoYUYYWMGLr6` | Text                   | A single line of text.                                                           |
| Submission Status                  | `fld5G5W7HhiCncJJL` | Single select          | Selected option name. When creating or updating records, if the choice string does not exactly match an existing option, the request will fail with an INVALID_MULTIPLE_CHOICE_OPTIONS error unless the typecast parameter is enabled. If typecast is enabled, a new choice will be created if one does not exactly match. |
| CD ID                              | `fldKwsNdbf12KbLJ8` | Text                   | A single line of text.                                                           |
| ISRC (from Recording)              | `fldLEkwvdPr6lmv0T` | Lookup                 | Array of ISRC fields in linked Recordings records.                               |
| ISWC                               | `fldYunRRdpQC3l0zd` | Lookup                 | Array of ISWC (from Compositions) fields in linked Recordings records.           |
| Date Submitted                     | `fldZnRtxfeiOgBekS` | Date                   | UTC date, e.g. "2014-09-05".                                                     |
| From Release                       | `fldJNJzhWluDYWDTS` | Link to another record | Array of linked records IDs from the Releases table.                             |
| Recording                          | `fldHwS1bgXbIMxljd` | Link to another record | Array of linked records IDs from the Recordings table.                           |
| Notes                              | `fldQbOWgt0Z0KFD5N` | Long text              | Multiple lines of text, which may contain "mention tokens", e.g. <airtable:mention id="menE1i9oBaGX3DseR">@Alex</airtable:mention> |
| APM Submission Spreadsheet         | `fldNl4XkUw4djAaJt` | Long text              | Multiple lines of text, which may contain "mention tokens", e.g. <airtable:mention id="menE1i9oBaGX3DseR">@Alex</airtable:mention> |
| Track Number                       | `fldAYGYUgYGhzdkGa` | Text                   | A single line of text.                                                           |
| Label                              | `fldEJLnJXVFpt5eKe` | Text                   | A single line of text.                                                           |
| Library ID                         | `fldMxBobhfU94zG8c` | Text                   | A single line of text.                                                           |
| Primary Artist (from CD Title)     | `fld7GBEdOrATDvKDK` | Lookup                 | Array of Primary Artist fields in linked Recordings records.                     |
| Featured Artist(s) (from CD Title) | `fldJHVnAq3DueyaZy` | Lookup                 | Array of Featured Artist(s) fields in linked Releases records.                   |
| Duration (from Recording)          | `fldWfqRUI1xYlf6fF` | Lookup                 | Array of Duration fields in linked Recordings records.                           |
| UPC (from From Release)            | `fldFGKuFIjtJ35dro` | Lookup                 | Array of UPC fields in linked Releases records.                                  |

---

## List Records

**Endpoint:** `GET /v0/appEurfA8kXQE3slK/apm%20dist%20mgmt`

To list records in APM Dist Mgmt , issue a GET request to the APM Dist Mgmt endpoint. Note that table names and table ids can be used interchangeably. Using table ids means table name changes do not require modifications to your API request.

Returned records do not include any fields with "empty" values, e.g. "" , [] , or false .

```bash
curl "https://api.airtable.com/v0/appEurfA8kXQE3slK/APM%20Dist%20Mgmt?maxRecords=3&view=Grid%20view" \
  -H "Authorization: Bearer YOUR_SECRET_API_TOKEN"
```

### Query Parameters

| Parameter               | Type             | Required   | Description                                                                      |
| ----------------------- | ---------------- | ---------- | -------------------------------------------------------------------------------- |
| `fields`                | array of strings | optional   | Only data for fields whose names are in this list will be included in the result. If you don't need every field, you can use this parameter to reduce the amount of data transferred. For example, to only return data from Track Title and Submission Status , send these two query parameters: fields%5B%5 |
| `filterByFormula`       | string           | optional   | A formula used to filter records. The formula will be evaluated for each record, and if the result is not 0 , false , "" , NaN , [] , or #Error! the record will be included in the response. We recommend testing your formula in the Formula field UI before using it in your API request. If combined wit |
| `maxRecords`            | number           | optional   | The maximum total number of records that will be returned in your requests. If this value is larger than pageSize (which is 100 by default), you may have to load multiple pages to reach this total. See the Pagination section below for more. |
| `pageSize`              | number           | optional   | The number of records returned in each request. Must be less than or equal to 100. Default is 100. See the Pagination section below for more. |
| `sort`                  | array of objects | optional   | A list of sort objects that specifies how the records will be ordered. Each sort object must have a field key specifying the name of the field to sort on, and an optional direction key that is either "asc" or "desc" . The default direction is "asc" . The sort parameter overrides the sorting of the v |
| `view`                  | string           | optional   | The name or ID of a view in the APM Dist Mgmt table. If set, only the records in that view will be returned. The records will be sorted according to the order of the view unless the sort parameter is included, which overrides that order. Fields hidden in this view will be returned in the results. To |
| `cellFormat`            | string           | optional   | The format that should be used for cell values. Supported values are: json : cells will be formatted as JSON, depending on the field type. string : cells will be formatted as user-facing strings, regardless of the field type. The timeZone and userLocale parameters are required when using string as t |
| `timeZone`              | string           | optional   | The time zone that should be used to format dates when using string as the cellFormat . This parameter is required when using string as the cellFormat . |
| `userLocale`            | string           | optional   | The user locale that should be used to format dates when using string as the cellFormat . This parameter is required when using string as the cellFormat . |
| `returnFieldsByFieldId` | boolean          | optional   | An optional boolean value that lets you return field objects where the key is the field id. This defaults to false , which returns field objects where the key is the field name. |
| `recordMetadata`        | array of strings | optional   | An optional field that, if includes commentCount , adds a commentCount read only property on each record returned. |

---

## Retrieve a Record

**Endpoint:** `GET /v0/appEurfA8kXQE3slK/apm%20dist%20mgmt`

To retrieve an existing record in APM Dist Mgmt table, issue a GET request to the record endpoint.

Any "empty" fields (e.g. "" , [] , or false ) in the record will not be returned.

```bash
curl https://api.airtable.com/v0/appEurfA8kXQE3slK/APM%20Dist%20Mgmt/rec3tq2hwx8hoUkfk \
  -H "Authorization: Bearer YOUR_SECRET_API_TOKEN"
```

---

## Create Records

**Endpoint:** `POST /v0/appEurfA8kXQE3slK/apm%20dist%20mgmt`

To create new records, issue a POST request to the APM Dist Mgmt endpoint. Note that table names and table ids can be used interchangeably. Using table ids means table name changes do not require modifications to your API request.

Your request body should include an array of up to 10 record objects. Each of these objects should have one key whose value is an inner object containing your record's cell values, keyed by either field name or field id.

```bash
curl -X POST https://api.airtable.com/v0/appEurfA8kXQE3slK/APM%20Dist%20Mgmt \
  -H "Authorization: Bearer YOUR_SECRET_API_TOKEN" \
  -H "Content-Type: application/json" \
  --data '{
  "records": [
    {
      "fields": {
        "Track Title": "Love Fever",
        "Submission Status": "Done",
        "CD ID": "APMC-0267 Love Fever",
        "Date Submitted": "2025-05-07",
        "From Release": [
          "recXsooBINci69iNL"
        ],
        "Recording": [
          "recuvy6EBHKGez45Q"
        ],
        "APM Submission Spreadsheet": "https://docs.google.com/spreadsheets/d/1NDyQxqTIt_ET2jVEYhlMIz79Oxk0Rq9U/edit?gid=1859837858#gid=1859837858\n",
        "Track Number": "1",
        "Library ID": "APM"
      }
    },
    {
      "fields": {
        "Track Title": "We Would Fall In Love",
        "Submission Status": "Done",
        "CD ID": "APMC-0268 Hopeless Romantic",
        "Date Submitted": "2025-05-16",
        "From Release": [
          "recYPdn9oppMGYoWZ"
        ],
        "Recording": [
          "recBd4KUsyEbH5Mwp"
        ],
        "APM Submission Spreadsheet": "https://docs.google.com/spreadsheets/d/1i4OCBN9V32ow2KXh7UpeUX7g9dtJpGDg/edit?gid=1859837858#gid=1859837858",
        "Track Number": "1",
        "Library ID": "APM"
      }
    }
  ]
}'
```

---

## Update / Upsert Records

**Endpoint:** `PATCH /v0/appEurfA8kXQE3slK/apm%20dist%20mgmt`

To update APM Dist Mgmt records, issue a request to the APM Dist Mgmt endpoint. Table names and table IDs can be used interchangeably. Using table IDs means table name changes won't require modifying your API request code. A PATCH request will only update the fields included in the request. Fields not included in the request will be unchanged. A PUT request will perform a destructive update and clear all unincluded cell values.

Your request body should include an array of up to 10 record objects. Each of these objects should have an id property representing the record ID and a fields property which contains all of your record's cell values by field name or field id for all of your record's cell values by field name.

```bash
curl -X PATCH https://api.airtable.com/v0/appEurfA8kXQE3slK/APM%20Dist%20Mgmt \
  -H "Authorization: Bearer YOUR_SECRET_API_TOKEN" \
  -H "Content-Type: application/json" \
  --data '{
  "records": [
    {
      "id": "rec3tq2hwx8hoUkfk",
      "fields": {
        "Track Title": "Love Fever",
        "Submission Status": "Done",
        "CD ID": "APMC-0267 Love Fever",
        "Date Submitted": "2025-05-07",
        "From Release": [
          "recXsooBINci69iNL"
        ],
        "Recording": [
          "recuvy6EBHKGez45Q"
        ],
        "APM Submission Spreadsheet": "https://docs.google.com/spreadsheets/d/1NDyQxqTIt_ET2jVEYhlMIz79Oxk0Rq9U/edit?gid=1859837858#gid=1859837858\n",
        "Track Number": "1",
        "Library ID": "APM"
      }
    },
    {
      "id": "recPgmjdD9HiNftar",
      "fields": {
        "Track Title": "We Would Fall In Love",
        "Submission Status": "Done",
        "CD ID": "APMC-0268 Hopeless Romantic",
        "Date Submitted": "2025-05-16",
        "From Release": [
          "recYPdn9oppMGYoWZ"
        ],
        "Recording": [
          "recBd4KUsyEbH5Mwp"
        ],
        "APM Submission Spreadsheet": "https://docs.google.com/spreadsheets/d/1i4OCBN9V32ow2KXh7UpeUX7g9dtJpGDg/edit?gid=1859837858#gid=1859837858",
        "Track Number": "1",
        "Library ID": "APM"
      }
    },
    {
      "id": "recAvwjx4zfiB3ukY",
      "fields": {
        "Track Title": "I Saw Santa Prayin'\''",
        "Submission Status": "Done",
        "CD ID": "APMC-0270 The True Spirit of Christmas",
        "Date Submitted": "2025-06-03",
        "From Release": [
          "recIHFCTKTZOCs7U6"
        ],
        "Recording": [
          "recZR4dmKscLFWFnZ"
        ],
        "APM Submission Spreadsheet": "https://docs.google.com/spreadsheets/d/1u-zbEz8smZoVw31eHufKOgYsQvgP_aGj/edit?gid=1859837858#gid=1859837858",
        "Track Number": "1",
        "Library ID": "APM"
      }
    }
  ]
}'
```

---

## Delete Records

**Endpoint:** `DELETE /v0/appEurfA8kXQE3slK/apm%20dist%20mgmt`

To delete APM Dist Mgmt records, issue a DELETE request to the APM Dist Mgmt endpoint. Note that table names and table ids can be used interchangeably. Using table ids means table name changes do not require modifications to your API request.

Your request should include a URL-encoded array of up to 10 record IDs to delete.

```bash
curl -X DELETE https://api.airtable.com/v0/appEurfA8kXQE3slK/APM%20Dist%20Mgmt \
  -H "Authorization: Bearer YOUR_SECRET_API_TOKEN" \
  -G \
  --data-urlencode 'records[]=rec3tq2hwx8hoUkfk' \
  --data-urlencode 'records[]=recPgmjdD9HiNftar'
```

