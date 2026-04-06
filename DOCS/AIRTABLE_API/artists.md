# Artists

**Table ID:** `tbla7zxpHm76x0Aj9`  
**Base ID:** `appEurfA8kXQE3slK`

---

## Fields

| Field Name                     | Field ID            | Type                   | Description                                                                      |
| ------------------------------ | ------------------- | ---------------------- | -------------------------------------------------------------------------------- |
| Name                           | `fldF4ZWQAGe4rmDOA` | Formula                | Computed value: { Artist First Name } & " " & { Artist Last Name/Band Name } .   |
| Notes                          | `fldS4kuMTIm2bX5XW` | Long text              | Multiple lines of text, which may contain "mention tokens", e.g. <airtable:mention id="menE1i9oBaGX3DseR">@Alex</airtable:mention> |
| Artist First Name              | `fld0MOqw1LTw7uPV8` | Text                   | A single line of text.                                                           |
| Artist Last Name/Band Name     | `fldhbPXA2b0LMVf2m` | Text                   | A single line of text.                                                           |
| Primary Recordings             | `fld9Eyowsg94qVrJe` | Link to another record | Array of linked records IDs from the Recordings table.                           |
| Featured Recordings            | `flddCYswYDG3kkOY8` | Link to another record | Array of linked records IDs from the Recordings table.                           |
| Primary Releases               | `fldMZrQCVME3cIBnE` | Link to another record | Array of linked records IDs from the Releases table. Because this field is configured to show records in reversed order, the order of records in the app will be reversed compared to what you see here. |
| Featured Releases              | `fldXrX9pcvBTDf7YF` | Link to another record | Array of linked records IDs from the Releases table. Because this field is configured to show records in reversed order, the order of records in the app will be reversed compared to what you see here. |
| APM Dist Mgmt                  | `fldWZBcn8HIdOwZnc` | Text                   | A single line of text.                                                           |
| Legal Docs                     | `fldnpu57KRbN8DIAg` | Link to another record | Array of linked records IDs from the Legal Docs table.                           |
| Spotify Artist ID              | `fldY7faosSIy0HAIs` | Text                   | A single line of text.                                                           |
| Listed On GoldLabelArtists.com | `fld972ZFSPcmWJbDs` | Checkbox               | This field is "true" when checked and otherwise empty.                           |
| Spotify Artist URL             | `fld7OktIOmK4YZQWL` | URL                    | A valid URL (e.g. airtable.com or https://airtable.com/universe).                |

---

## List Records

**Endpoint:** `GET /v0/appEurfA8kXQE3slK/artists`

To list records in Artists , issue a GET request to the Artists endpoint. Note that table names and table ids can be used interchangeably. Using table ids means table name changes do not require modifications to your API request.

Returned records do not include any fields with "empty" values, e.g. "" , [] , or false .

```bash
curl "https://api.airtable.com/v0/appEurfA8kXQE3slK/Artists?maxRecords=3&view=Default" \
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
| `view`                  | string           | optional   | The name or ID of a view in the Artists table. If set, only the records in that view will be returned. The records will be sorted according to the order of the view unless the sort parameter is included, which overrides that order. Fields hidden in this view will be returned in the results. To only |
| `cellFormat`            | string           | optional   | The format that should be used for cell values. Supported values are: json : cells will be formatted as JSON, depending on the field type. string : cells will be formatted as user-facing strings, regardless of the field type. The timeZone and userLocale parameters are required when using string as t |
| `timeZone`              | string           | optional   | The time zone that should be used to format dates when using string as the cellFormat . This parameter is required when using string as the cellFormat . |
| `userLocale`            | string           | optional   | The user locale that should be used to format dates when using string as the cellFormat . This parameter is required when using string as the cellFormat . |
| `returnFieldsByFieldId` | boolean          | optional   | An optional boolean value that lets you return field objects where the key is the field id. This defaults to false , which returns field objects where the key is the field name. |
| `recordMetadata`        | array of strings | optional   | An optional field that, if includes commentCount , adds a commentCount read only property on each record returned. |

---

## Retrieve a Record

**Endpoint:** `GET /v0/appEurfA8kXQE3slK/artists`

To retrieve an existing record in Artists table, issue a GET request to the record endpoint.

Any "empty" fields (e.g. "" , [] , or false ) in the record will not be returned.

```bash
curl https://api.airtable.com/v0/appEurfA8kXQE3slK/Artists/recIp9KshxzJgCfH8 \
  -H "Authorization: Bearer YOUR_SECRET_API_TOKEN"
```

---

## Create Records

**Endpoint:** `POST /v0/appEurfA8kXQE3slK/artists`

To create new records, issue a POST request to the Artists endpoint. Note that table names and table ids can be used interchangeably. Using table ids means table name changes do not require modifications to your API request.

Your request body should include an array of up to 10 record objects. Each of these objects should have one key whose value is an inner object containing your record's cell values, keyed by either field name or field id.

```bash
curl -X POST https://api.airtable.com/v0/appEurfA8kXQE3slK/Artists \
  -H "Authorization: Bearer YOUR_SECRET_API_TOKEN" \
  -H "Content-Type: application/json" \
  --data '{
  "records": [
    {
      "fields": {
        "Artist Last Name/Band Name": "2nd Chapter Of Acts",
        "Primary Recordings": [
          "rectH1q4KEoCmsyjv",
          "recx5ETAQxSdakUWq"
        ],
        "Primary Releases": [
          "recQQ7zqlKb6ojPYk"
        ]
      }
    },
    {
      "fields": {
        "Artist Last Name/Band Name": "Abilene Christian College A Cappella Chorus",
        "Primary Recordings": [
          "recRlYpxC4hl4SjoM",
          "recCzHyEO9vDHggWa",
          "reciPOjHKVNZtNjVo",
          "recYa0DvsABggA5ax",
          "rec5ebFo785QJlGXg",
          "recU25AWTYRQYlfUa",
          "recbfVg1HJEcbDFWL",
          "rec3qFXbsK8QlbHyE",
          "recoDtUOjPKbdvyse",
          "recWv655B9CMaOBGE",
          "recztMbyFD6Gv5KZq",
          "recA3tVjuaE1LrRjd"
        ],
        "Primary Releases": [
          "reckg4ihxipgfLwaG"
        ]
      }
    }
  ]
}'
```

---

## Update / Upsert Records

**Endpoint:** `PATCH /v0/appEurfA8kXQE3slK/artists`

To update Artists records, issue a request to the Artists endpoint. Table names and table IDs can be used interchangeably. Using table IDs means table name changes won't require modifying your API request code. A PATCH request will only update the fields included in the request. Fields not included in the request will be unchanged. A PUT request will perform a destructive update and clear all unincluded cell values.

Your request body should include an array of up to 10 record objects. Each of these objects should have an id property representing the record ID and a fields property which contains all of your record's cell values by field name or field id for all of your record's cell values by field name.

```bash
curl -X PATCH https://api.airtable.com/v0/appEurfA8kXQE3slK/Artists \
  -H "Authorization: Bearer YOUR_SECRET_API_TOKEN" \
  -H "Content-Type: application/json" \
  --data '{
  "records": [
    {
      "id": "recIp9KshxzJgCfH8",
      "fields": {
        "Artist Last Name/Band Name": "2nd Chapter Of Acts",
        "Primary Recordings": [
          "rectH1q4KEoCmsyjv",
          "recx5ETAQxSdakUWq"
        ],
        "Primary Releases": [
          "recQQ7zqlKb6ojPYk"
        ]
      }
    },
    {
      "id": "reczifaRa5S5vyCn4",
      "fields": {
        "Artist Last Name/Band Name": "Abilene Christian College A Cappella Chorus",
        "Primary Recordings": [
          "recRlYpxC4hl4SjoM",
          "recCzHyEO9vDHggWa",
          "reciPOjHKVNZtNjVo",
          "recYa0DvsABggA5ax",
          "rec5ebFo785QJlGXg",
          "recU25AWTYRQYlfUa",
          "recbfVg1HJEcbDFWL",
          "rec3qFXbsK8QlbHyE",
          "recoDtUOjPKbdvyse",
          "recWv655B9CMaOBGE",
          "recztMbyFD6Gv5KZq",
          "recA3tVjuaE1LrRjd"
        ],
        "Primary Releases": [
          "reckg4ihxipgfLwaG"
        ]
      }
    },
    {
      "id": "recz4zL6zUK5awktL",
      "fields": {
        "Notes": "https://open.spotify.com/artist/6rJqqRce0Kvo2dJUXoHleC?si=SjlgX7-OTMagDfdPKThE6Q",
        "Artist Last Name/Band Name": "Alabama",
        "Featured Recordings": [
          "recxd50ETB5ZD1QCI",
          "rec9EUc5YvTbDEajJ"
        ],
        "Featured Releases": [
          "recYTUWpVF0ZXSuLR",
          "rec0z6GYgSbJOOBHM",
          "recOnTdJxvaTVQmpY"
        ]
      }
    }
  ]
}'
```

---

## Delete Records

**Endpoint:** `DELETE /v0/appEurfA8kXQE3slK/artists`

To delete Artists records, issue a DELETE request to the Artists endpoint. Note that table names and table ids can be used interchangeably. Using table ids means table name changes do not require modifications to your API request.

Your request should include a URL-encoded array of up to 10 record IDs to delete.

```bash
curl -X DELETE https://api.airtable.com/v0/appEurfA8kXQE3slK/Artists \
  -H "Authorization: Bearer YOUR_SECRET_API_TOKEN" \
  -G \
  --data-urlencode 'records[]=recIp9KshxzJgCfH8' \
  --data-urlencode 'records[]=reczifaRa5S5vyCn4'
```

