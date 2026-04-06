# Chevy Showroom Dist Mgmt

**Table ID:** `tblRqFtQrPCNB1fwT`  
**Base ID:** `appEurfA8kXQE3slK`

---

## Fields

| Field Name               | Field ID            | Type                   | Description                                                                      |
| ------------------------ | ------------------- | ---------------------- | -------------------------------------------------------------------------------- |
| Recording Title          | `fldZhsS8bGm4LGxLS` | Text                   | A single line of text.                                                           |
| Release                  | `fld8ZRGggXaSZ6WPr` | Link to another record | Array of linked records IDs from the Releases table.                             |
| Notes                    | `fld7kLLkIUiPmfy3M` | Long text              | Multiple lines of text, which may contain "mention tokens", e.g. <airtable:mention id="menE1i9oBaGX3DseR">@Alex</airtable:mention> |
| Episode #                | `fldTzZVVUDpCBYhDo` | Text                   | A single line of text.                                                           |
| Album Release Title      | `fldvNBJ8rLb8uUpNL` | Text                   | A single line of text.                                                           |
| Title Version            | `fldCbkW2mpolcnYle` | Text                   | A single line of text.                                                           |
| Featured Artist          | `fld3VHweZjXKPe63e` | Multiple select        | Array of selected option names. When creating or updating records, if a choice string does not exactly match an existing option, the request will fail with an INVALID_MULTIPLE_CHOICE_OPTIONS error unless the typecast parameter is enabled. If typecast is enabled, a new choice will be created if one does not exactly match. |
| Date First Aired         | `fldjweCFBABr72S1n` | Date                   | UTC date, e.g. "2014-09-05".                                                     |
| Release Date             | `fldVKtAmpmdL9v2WY` | Date                   | UTC date, e.g. "2014-09-05".                                                     |
| UPC                      | `fldeuaXpQVlO1OxDS` | Barcode                | The barcode object may contain the following two properties, both of which are optional. text string barcode data type string barcode symbology, e.g. "upce" or "code39" |
| PRODUCT CODE             | `fldJOnZr2BOyT3Ebb` | Barcode                | The barcode object may contain the following two properties, both of which are optional. text string barcode data type string barcode symbology, e.g. "upce" or "code39" |
| ISRC                     | `fldyfDCWl8w5uVcFb` | Text                   | A single line of text.                                                           |
| ISWC                     | `fldEQ1iIkvxelBnsQ` | Long text              | Multiple lines of text, which may contain "mention tokens", e.g. <airtable:mention id="menE1i9oBaGX3DseR">@Alex</airtable:mention> |
| Orchard                  | `fldGjZniYnGwZ3CSl` | Multiple select        | Array of selected option names. When creating or updating records, if a choice string does not exactly match an existing option, the request will fail with an INVALID_MULTIPLE_CHOICE_OPTIONS error unless the typecast parameter is enabled. If typecast is enabled, a new choice will be created if one does not exactly match. |
| Apple                    | `fld2uyYBypJOWceJc` | Multiple select        | Array of selected option names. When creating or updating records, if a choice string does not exactly match an existing option, the request will fail with an INVALID_MULTIPLE_CHOICE_OPTIONS error unless the typecast parameter is enabled. If typecast is enabled, a new choice will be created if one does not exactly match. |
| Recordings               | `fldu3zfcd8SW7QJwG` | Link to another record | Array of linked records IDs from the Recordings table.                           |
| Verified Publishing Info | `fldzdRFrDKCSuUmqo` | Single select          | Selected option name. When creating or updating records, if the choice string does not exactly match an existing option, the request will fail with an INVALID_MULTIPLE_CHOICE_OPTIONS error unless the typecast parameter is enabled. If typecast is enabled, a new choice will be created if one does not exactly match. |
| DISCO                    | `fldwb0wYhqCfmzA09` | Multiple select        | Array of selected option names. When creating or updating records, if a choice string does not exactly match an existing option, the request will fail with an INVALID_MULTIPLE_CHOICE_OPTIONS error unless the typecast parameter is enabled. If typecast is enabled, a new choice will be created if one does not exactly match. |

---

## List Records

**Endpoint:** `GET /v0/appEurfA8kXQE3slK/chevy%20showroom%20dist%20mgmt`

To list records in Chevy Showroom Dist Mgmt , issue a GET request to the Chevy Showroom Dist Mgmt endpoint. Note that table names and table ids can be used interchangeably. Using table ids means table name changes do not require modifications to your API request.

Returned records do not include any fields with "empty" values, e.g. "" , [] , or false .

```bash
curl "https://api.airtable.com/v0/appEurfA8kXQE3slK/Chevy%20Showroom%20Dist%20Mgmt?maxRecords=3&view=Grid%20view" \
  -H "Authorization: Bearer YOUR_SECRET_API_TOKEN"
```

### Query Parameters

| Parameter               | Type             | Required   | Description                                                                      |
| ----------------------- | ---------------- | ---------- | -------------------------------------------------------------------------------- |
| `fields`                | array of strings | optional   | Only data for fields whose names are in this list will be included in the result. If you don't need every field, you can use this parameter to reduce the amount of data transferred. For example, to only return data from Recording Title and Release , send these two query parameters: fields%5B%5D=Reco |
| `filterByFormula`       | string           | optional   | A formula used to filter records. The formula will be evaluated for each record, and if the result is not 0 , false , "" , NaN , [] , or #Error! the record will be included in the response. We recommend testing your formula in the Formula field UI before using it in your API request. If combined wit |
| `maxRecords`            | number           | optional   | The maximum total number of records that will be returned in your requests. If this value is larger than pageSize (which is 100 by default), you may have to load multiple pages to reach this total. See the Pagination section below for more. |
| `pageSize`              | number           | optional   | The number of records returned in each request. Must be less than or equal to 100. Default is 100. See the Pagination section below for more. |
| `sort`                  | array of objects | optional   | A list of sort objects that specifies how the records will be ordered. Each sort object must have a field key specifying the name of the field to sort on, and an optional direction key that is either "asc" or "desc" . The default direction is "asc" . The sort parameter overrides the sorting of the v |
| `view`                  | string           | optional   | The name or ID of a view in the Chevy Showroom Dist Mgmt table. If set, only the records in that view will be returned. The records will be sorted according to the order of the view unless the sort parameter is included, which overrides that order. Fields hidden in this view will be returned in the |
| `cellFormat`            | string           | optional   | The format that should be used for cell values. Supported values are: json : cells will be formatted as JSON, depending on the field type. string : cells will be formatted as user-facing strings, regardless of the field type. The timeZone and userLocale parameters are required when using string as t |
| `timeZone`              | string           | optional   | The time zone that should be used to format dates when using string as the cellFormat . This parameter is required when using string as the cellFormat . |
| `userLocale`            | string           | optional   | The user locale that should be used to format dates when using string as the cellFormat . This parameter is required when using string as the cellFormat . |
| `returnFieldsByFieldId` | boolean          | optional   | An optional boolean value that lets you return field objects where the key is the field id. This defaults to false , which returns field objects where the key is the field name. |
| `recordMetadata`        | array of strings | optional   | An optional field that, if includes commentCount , adds a commentCount read only property on each record returned. |

---

## Retrieve a Record

**Endpoint:** `GET /v0/appEurfA8kXQE3slK/chevy%20showroom%20dist%20mgmt`

To retrieve an existing record in Chevy Showroom Dist Mgmt table, issue a GET request to the record endpoint.

Any "empty" fields (e.g. "" , [] , or false ) in the record will not be returned.

```bash
curl https://api.airtable.com/v0/appEurfA8kXQE3slK/Chevy%20Showroom%20Dist%20Mgmt/recFDfo8UviaFKyvZ \
  -H "Authorization: Bearer YOUR_SECRET_API_TOKEN"
```

---

## Create Records

**Endpoint:** `POST /v0/appEurfA8kXQE3slK/chevy%20showroom%20dist%20mgmt`

To create new records, issue a POST request to the Chevy Showroom Dist Mgmt endpoint. Note that table names and table ids can be used interchangeably. Using table ids means table name changes do not require modifications to your API request.

Your request body should include an array of up to 10 record objects. Each of these objects should have one key whose value is an inner object containing your record's cell values, keyed by either field name or field id.

```bash
curl -X POST https://api.airtable.com/v0/appEurfA8kXQE3slK/Chevy%20Showroom%20Dist%20Mgmt \
  -H "Authorization: Bearer YOUR_SECRET_API_TOKEN" \
  -H "Content-Type: application/json" \
  --data '{
  "records": [
    {
      "fields": {
        "Recording Title": "Santa Claus Is Coming To Town",
        "Notes": "Not Released ",
        "Episode #": "10",
        "Album Release Title": "Santa Claus Is Coming To Town (Live On The Pat Boone Chevy Showroom, December 5, 1957)",
        "Title Version": "Live On The Pat Boone Chevy Showroom, December 5, 1957",
        "Date First Aired": "1957-12-05",
        "ISWC": "T0701341458",
        "Recordings": [
          "recwaCl6e4EfWDeUv"
        ]
      }
    },
    {
      "fields": {
        "Recording Title": "Lost In The Stars ",
        "Episode #": "30",
        "Album Release Title": "Lost In The Stars (Live On The Pat Boone Chevy Showroom, May 5, 1958)",
        "Title Version": "Live On The Pat Boone Chevy Showroom, May 5, 1958",
        "Date First Aired": "1958-05-01",
        "UPC": {
          "text": "786052581055"
        },
        "PRODUCT CODE": {
          "text": "GLDA581055"
        },
        "ISRC": "QT27V2500155",
        "Orchard": [
          "Lyric Sheet Edited"
        ]
      }
    }
  ]
}'
```

---

## Update / Upsert Records

**Endpoint:** `PATCH /v0/appEurfA8kXQE3slK/chevy%20showroom%20dist%20mgmt`

To update Chevy Showroom Dist Mgmt records, issue a request to the Chevy Showroom Dist Mgmt endpoint. Table names and table IDs can be used interchangeably. Using table IDs means table name changes won't require modifying your API request code. A PATCH request will only update the fields included in the request. Fields not included in the request will be unchanged. A PUT request will perform a destructive update and clear all unincluded cell values.

Your request body should include an array of up to 10 record objects. Each of these objects should have an id property representing the record ID and a fields property which contains all of your record's cell values by field name or field id for all of your record's cell values by field name.

```bash
curl -X PATCH https://api.airtable.com/v0/appEurfA8kXQE3slK/Chevy%20Showroom%20Dist%20Mgmt \
  -H "Authorization: Bearer YOUR_SECRET_API_TOKEN" \
  -H "Content-Type: application/json" \
  --data '{
  "records": [
    {
      "id": "recFDfo8UviaFKyvZ",
      "fields": {
        "Recording Title": "Santa Claus Is Coming To Town",
        "Notes": "Not Released ",
        "Episode #": "10",
        "Album Release Title": "Santa Claus Is Coming To Town (Live On The Pat Boone Chevy Showroom, December 5, 1957)",
        "Title Version": "Live On The Pat Boone Chevy Showroom, December 5, 1957",
        "Date First Aired": "1957-12-05",
        "ISWC": "T0701341458",
        "Recordings": [
          "recwaCl6e4EfWDeUv"
        ]
      }
    },
    {
      "id": "recEc9cxPn8LdEjUi",
      "fields": {
        "Recording Title": "Lost In The Stars ",
        "Episode #": "30",
        "Album Release Title": "Lost In The Stars (Live On The Pat Boone Chevy Showroom, May 5, 1958)",
        "Title Version": "Live On The Pat Boone Chevy Showroom, May 5, 1958",
        "Date First Aired": "1958-05-01",
        "UPC": {
          "text": "786052581055"
        },
        "PRODUCT CODE": {
          "text": "GLDA581055"
        },
        "ISRC": "QT27V2500155",
        "Orchard": [
          "Lyric Sheet Edited"
        ]
      }
    },
    {
      "id": "recEpp5RtZlJf9NU7",
      "fields": {
        "Recording Title": "Too Young",
        "Release": [
          "recc2xkqF3CIwyYpm"
        ],
        "Episode #": "28",
        "Album Release Title": "Too Young (Live On The Pat Boone Chevy Showroom, April 10, 1958)",
        "Title Version": "Live On The Pat Boone Chevy Showroom, April 10, 1958",
        "Date First Aired": "1958-04-10",
        "UPC": {
          "text": "786052580942"
        },
        "PRODUCT CODE": {
          "text": "GLDA580942"
        },
        "ISRC": "QT27V2500144",
        "Orchard": [
          "Lyric Sheet Edited"
        ],
        "Recordings": [
          "rechYjEXKEkxRMHat"
        ]
      }
    }
  ]
}'
```

---

## Delete Records

**Endpoint:** `DELETE /v0/appEurfA8kXQE3slK/chevy%20showroom%20dist%20mgmt`

To delete Chevy Showroom Dist Mgmt records, issue a DELETE request to the Chevy Showroom Dist Mgmt endpoint. Note that table names and table ids can be used interchangeably. Using table ids means table name changes do not require modifications to your API request.

Your request should include a URL-encoded array of up to 10 record IDs to delete.

```bash
curl -X DELETE https://api.airtable.com/v0/appEurfA8kXQE3slK/Chevy%20Showroom%20Dist%20Mgmt \
  -H "Authorization: Bearer YOUR_SECRET_API_TOKEN" \
  -G \
  --data-urlencode 'records[]=recFDfo8UviaFKyvZ' \
  --data-urlencode 'records[]=recEc9cxPn8LdEjUi'
```

