# REGISTRATION PROJECT (SOUNDEXCHANGE)

**Table ID:** `tbliX5cAVK47tYsL8`  
**Base ID:** `appEurfA8kXQE3slK`

---

## Fields

| Field Name                                                       | Field ID            | Type                   | Description                                                                      |
| ---------------------------------------------------------------- | ------------------- | ---------------------- | -------------------------------------------------------------------------------- |
| Name                                                             | `fldMNc0vObIKi3jHX` | Text                   | A single line of text.                                                           |
| Notes                                                            | `fldG2kDhfvrFPe3oY` | Long text              | Multiple lines of text, which may contain "mention tokens", e.g. <airtable:mention id="menE1i9oBaGX3DseR">@Alex</airtable:mention> |
| Album                                                            | `fldyIXZ2GruVkIcCC` | Text                   | A single line of text.                                                           |
| Label Owned                                                      | `fld48h9oXRsU84TpZ` | Long text              | Multiple lines of text, which may contain "mention tokens", e.g. <airtable:mention id="menE1i9oBaGX3DseR">@Alex</airtable:mention> |
| SX (Rights Owner)                                                | `fldwk3ye1YgdBmRgf` | Multiple select        | Array of selected option names. When creating or updating records, if a choice string does not exactly match an existing option, the request will fail with an INVALID_MULTIPLE_CHOICE_OPTIONS error unless the typecast parameter is enabled. If typecast is enabled, a new choice will be created if one does not exactly match. |
| SX (Artist)                                                      | `fldwCzooBZxy2mdbV` | Multiple select        | Array of selected option names. When creating or updating records, if a choice string does not exactly match an existing option, the request will fail with an INVALID_MULTIPLE_CHOICE_OPTIONS error unless the typecast parameter is enabled. If typecast is enabled, a new choice will be created if one does not exactly match. |
| Recordings                                                       | `fld2j5Wejenu7sbM4` | Link to another record | Array of linked records IDs from the Recordings table.                           |
| Title of Recording (from Recordings)                             | `fldqOGw788bhOC3Uu` | Lookup                 | Array of Title of Recording fields in linked Recordings records.                 |
| All Releases (from Recordings)                                   | `fldIMUZgXS7x4Dbu2` | Lookup                 | Array of All Releases fields in linked Recordings records.                       |
| Primary Artist (from Recordings)                                 | `fldd0wIZi79xyswWT` | Lookup                 | Array of Primary Artist fields in linked Recordings records.                     |
| Featured Artist (from Recordings)                                | `fldwG49aMHD3WCgWT` | Lookup                 | Array of Featured Artist fields in linked Recordings records.                    |
| ISRC (from Recordings)                                           | `fldpIo5kHVxRRBCfE` | Lookup                 | Array of ISRC fields in linked Recordings records.                               |
| Spotify (from Recordings)                                        | `fld4FeUjzRgiew2FN` | Lookup                 | Array of Spotify fields in linked Recordings records.                            |
| Master Owner 1 (from Recordings)                                 | `fld3dJ0p1tQNdnUBK` | Lookup                 | Array of Master Owner 1 fields in linked Recordings records.                     |
| % Master 1 Ownership                                             | `fldoNHY5GTT5uwTYb` | Lookup                 | Array of Master 1 Ownership fields in linked Recordings records.                 |
| Notes (from Recordings)                                          | `fldpi8FS02T746l2F` | Lookup                 | Array of Notes fields in linked Recordings records.                              |
| Duration (from Recordings)                                       | `fldCRFi0yxT4mEh8r` | Lookup                 | Array of Duration fields in linked Recordings records.                           |
| Genre Tag (from Recordings)                                      | `fldDeMyNbY0PckL4j` | Lookup                 | Array of Genre Tag fields in linked Recordings records.                          |
| Recording year (from Recordings)                                 | `fldePy1jUKPCqMYHi` | Lookup                 | Array of Recording year fields in linked Recordings records.                     |
| Date of original Release (from Recordings)                       | `fldY757FKyjiTQPTU` | Lookup                 | Array of Date of original Release fields in linked Recordings records.           |
| ISWC (from Compositions) (from Recordings)                       | `fld30jpDmhTlSljwp` | Lookup                 | Array of ISWC (from Compositions) fields in linked Recordings records.           |
| UPC (from Releases) (from Recordings)                            | `fldidmpkvsGAhimGf` | Lookup                 | Array of UPC (from Releases) fields in linked Recordings records.                |
| Original release label (from Original release) (from Recordings) | `fld4yI3HU8QQVTifM` | Lookup                 | Array of Original release label (from Original release) fields in linked Recordings records. |
| Current release label (from Original Release) (from Recordings)  | `fldnSB2qwxQ0lITlI` | Lookup                 | Array of Current release label (from Original Release) fields in linked Recordings records. |
| Last Modified                                                    | `fldOs1Csu8wmfmt2c` | Formula                | Computed value: LAST_MODIFIED_TIME() .                                           |
| PBGL Owned                                                       | `fldWxrR2rjZpKZlTe` | Lookup                 | Array of PBGL Owned fields in linked Recordings records.                         |

---

## List Records

**Endpoint:** `GET /v0/appEurfA8kXQE3slK/registration%20project%20(soundexchange)`

To list records in REGISTRATION PROJECT (SOUNDEXCHANGE) , issue a GET request to the REGISTRATION PROJECT (SOUNDEXCHANGE) endpoint. Note that table names and table ids can be used interchangeably. Using table ids means table name changes do not require modifications to your API request.

Returned records do not include any fields with "empty" values, e.g. "" , [] , or false .

```bash
curl "https://api.airtable.com/v0/appEurfA8kXQE3slK/REGISTRATION%20PROJECT%20(SOUNDEXCHANGE)?maxRecords=3&view=Grid%20view" \
  -H "Authorization: Bearer YOUR_SECRET_API_TOKEN"
```

### Query Parameters

| Parameter               | Type             | Required   | Description                                                                      |
| ----------------------- | ---------------- | ---------- | -------------------------------------------------------------------------------- |
| `fields`                | array of strings | optional   | Only data for fields whose names are in this list will be included in the result. If you don't need every field, you can use this parameter to reduce the amount of data transferred. For example, to only return data from Name and Notes , send these two query parameters: fields%5B%5D=Name&fields%5B%5D |
| `filterByFormula`       | string           | optional   | A formula used to filter records. The formula will be evaluated for each record, and if the result is not 0 , false , "" , NaN , [] , or #Error! the record will be included in the response. We recommend testing your formula in the Formula field UI before using it in your API request. If combined wit |
| `maxRecords`            | number           | optional   | The maximum total number of records that will be returned in your requests. If this value is larger than pageSize (which is 100 by default), you may have to load multiple pages to reach this total. See the Pagination section below for more. |
| `pageSize`              | number           | optional   | The number of records returned in each request. Must be less than or equal to 100. Default is 100. See the Pagination section below for more. |
| `sort`                  | array of objects | optional   | A list of sort objects that specifies how the records will be ordered. Each sort object must have a field key specifying the name of the field to sort on, and an optional direction key that is either "asc" or "desc" . The default direction is "asc" . The sort parameter overrides the sorting of the v |
| `view`                  | string           | optional   | The name or ID of a view in the REGISTRATION PROJECT (SOUNDEXCHANGE) table. If set, only the records in that view will be returned. The records will be sorted according to the order of the view unless the sort parameter is included, which overrides that order. Fields hidden in this view will be retu |
| `cellFormat`            | string           | optional   | The format that should be used for cell values. Supported values are: json : cells will be formatted as JSON, depending on the field type. string : cells will be formatted as user-facing strings, regardless of the field type. The timeZone and userLocale parameters are required when using string as t |
| `timeZone`              | string           | optional   | The time zone that should be used to format dates when using string as the cellFormat . This parameter is required when using string as the cellFormat . |
| `userLocale`            | string           | optional   | The user locale that should be used to format dates when using string as the cellFormat . This parameter is required when using string as the cellFormat . |
| `returnFieldsByFieldId` | boolean          | optional   | An optional boolean value that lets you return field objects where the key is the field id. This defaults to false , which returns field objects where the key is the field name. |
| `recordMetadata`        | array of strings | optional   | An optional field that, if includes commentCount , adds a commentCount read only property on each record returned. |

---

## Retrieve a Record

**Endpoint:** `GET /v0/appEurfA8kXQE3slK/registration%20project%20(soundexchange)`

To retrieve an existing record in REGISTRATION PROJECT (SOUNDEXCHANGE) table, issue a GET request to the record endpoint.

Any "empty" fields (e.g. "" , [] , or false ) in the record will not be returned.

```bash
curl https://api.airtable.com/v0/appEurfA8kXQE3slK/REGISTRATION%20PROJECT%20(SOUNDEXCHANGE)/recj1SM8RsYu6EXq6 \
  -H "Authorization: Bearer YOUR_SECRET_API_TOKEN"
```

---

## Create Records

**Endpoint:** `POST /v0/appEurfA8kXQE3slK/registration%20project%20(soundexchange)`

To create new records, issue a POST request to the REGISTRATION PROJECT (SOUNDEXCHANGE) endpoint. Note that table names and table ids can be used interchangeably. Using table ids means table name changes do not require modifications to your API request.

Your request body should include an array of up to 10 record objects. Each of these objects should have one key whose value is an inner object containing your record's cell values, keyed by either field name or field id.

```bash
curl -X POST https://api.airtable.com/v0/appEurfA8kXQE3slK/REGISTRATION%20PROJECT%20(SOUNDEXCHANGE) \
  -H "Authorization: Bearer YOUR_SECRET_API_TOKEN" \
  -H "Content-Type: application/json" \
  --data '{
  "records": [
    {
      "fields": {
        "Name": "He Leadeth Me",
        "Album": "Golden Treasury of Hymns ",
        "SX (Rights Owner)": [
          "N/A"
        ],
        "SX (Artist)": [
          "Claimed"
        ]
      }
    },
    {
      "fields": {
        "Name": "Merry Christmas ",
        "Notes": "https://open.spotify.com/album/3RfMfyPLea5WD7lk0SpSXd?si=TexcLUEgTnm396FldEVJdg",
        "Album": "Merry Christmas",
        "SX (Rights Owner)": [
          "N/A"
        ],
        "SX (Artist)": [
          "Needs to be Submitted by RO"
        ]
      }
    }
  ]
}'
```

---

## Update / Upsert Records

**Endpoint:** `PATCH /v0/appEurfA8kXQE3slK/registration%20project%20(soundexchange)`

To update REGISTRATION PROJECT (SOUNDEXCHANGE) records, issue a request to the REGISTRATION PROJECT (SOUNDEXCHANGE) endpoint. Table names and table IDs can be used interchangeably. Using table IDs means table name changes won't require modifying your API request code. A PATCH request will only update the fields included in the request. Fields not included in the request will be unchanged. A PUT request will perform a destructive update and clear all unincluded cell values.

Your request body should include an array of up to 10 record objects. Each of these objects should have an id property representing the record ID and a fields property which contains all of your record's cell values by field name or field id for all of your record's cell values by field name.

```bash
curl -X PATCH https://api.airtable.com/v0/appEurfA8kXQE3slK/REGISTRATION%20PROJECT%20(SOUNDEXCHANGE) \
  -H "Authorization: Bearer YOUR_SECRET_API_TOKEN" \
  -H "Content-Type: application/json" \
  --data '{
  "records": [
    {
      "id": "recj1SM8RsYu6EXq6",
      "fields": {
        "Name": "He Leadeth Me",
        "Album": "Golden Treasury of Hymns ",
        "SX (Rights Owner)": [
          "N/A"
        ],
        "SX (Artist)": [
          "Claimed"
        ]
      }
    },
    {
      "id": "recTzO38mlOqygW9D",
      "fields": {
        "Name": "Merry Christmas ",
        "Notes": "https://open.spotify.com/album/3RfMfyPLea5WD7lk0SpSXd?si=TexcLUEgTnm396FldEVJdg",
        "Album": "Merry Christmas",
        "SX (Rights Owner)": [
          "N/A"
        ],
        "SX (Artist)": [
          "Needs to be Submitted by RO"
        ]
      }
    },
    {
      "id": "recneBwCYKIqvluxJ",
      "fields": {
        "Name": "White Christmas ",
        "Album": "Merry Christmas",
        "SX (Rights Owner)": [
          "N/A"
        ],
        "SX (Artist)": [
          "Needs to be Submitted by RO"
        ]
      }
    }
  ]
}'
```

---

## Delete Records

**Endpoint:** `DELETE /v0/appEurfA8kXQE3slK/registration%20project%20(soundexchange)`

To delete REGISTRATION PROJECT (SOUNDEXCHANGE) records, issue a DELETE request to the REGISTRATION PROJECT (SOUNDEXCHANGE) endpoint. Note that table names and table ids can be used interchangeably. Using table ids means table name changes do not require modifications to your API request.

Your request should include a URL-encoded array of up to 10 record IDs to delete.

```bash
curl -X DELETE https://api.airtable.com/v0/appEurfA8kXQE3slK/REGISTRATION%20PROJECT%20(SOUNDEXCHANGE) \
  -H "Authorization: Bearer YOUR_SECRET_API_TOKEN" \
  -G \
  --data-urlencode 'records[]=recj1SM8RsYu6EXq6' \
  --data-urlencode 'records[]=recTzO38mlOqygW9D'
```

