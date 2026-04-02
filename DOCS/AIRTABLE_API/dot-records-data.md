# Dot Records Data

**Table ID:** `tblqz34c9YV44cqGl`  
**Base ID:** `appEurfA8kXQE3slK`

---

## Fields

| Field Name           | Field ID            | Type          | Description                                                                      |
| -------------------- | ------------------- | ------------- | -------------------------------------------------------------------------------- |
| Release Label        | `fldIO5M0x4lneznJv` | Text          | A single line of text.                                                           |
| Album / Single Title | `fldgifOqao5Jkge79` | Text          | A single line of text.                                                           |
| Date                 | `fldyMurLJpqd3uXkv` | Text          | A single line of text.                                                           |
| Status               | `fldB2E0npPyWF5J3v` | Checkbox      | This field is "true" when checked and otherwise empty.                           |
| Collaborator         | `fldwzzfARNka11UAP` | Single select | Selected option name. When creating or updating records, if the choice string does not exactly match an existing option, the request will fail with an INVALID_MULTIPLE_CHOICE_OPTIONS error unless the typecast parameter is enabled. If typecast is enabled, a new choice will be created if one does not exactly match. |

---

## List Records

**Endpoint:** `GET /v0/appEurfA8kXQE3slK/dot%20records%20data`

To list records in Dot Records Data , issue a GET request to the Dot Records Data endpoint. Note that table names and table ids can be used interchangeably. Using table ids means table name changes do not require modifications to your API request.

Returned records do not include any fields with "empty" values, e.g. "" , [] , or false .

```bash
curl "https://api.airtable.com/v0/appEurfA8kXQE3slK/Dot%20Records%20Data?maxRecords=3&view=Grid%20view" \
  -H "Authorization: Bearer YOUR_SECRET_API_TOKEN"
```

### Query Parameters

| Parameter               | Type             | Required   | Description                                                                      |
| ----------------------- | ---------------- | ---------- | -------------------------------------------------------------------------------- |
| `fields`                | array of strings | optional   | Only data for fields whose names are in this list will be included in the result. If you don't need every field, you can use this parameter to reduce the amount of data transferred. For example, to only return data from Release Label and Album / Single Title , send these two query parameters: fields |
| `filterByFormula`       | string           | optional   | A formula used to filter records. The formula will be evaluated for each record, and if the result is not 0 , false , "" , NaN , [] , or #Error! the record will be included in the response. We recommend testing your formula in the Formula field UI before using it in your API request. If combined wit |
| `maxRecords`            | number           | optional   | The maximum total number of records that will be returned in your requests. If this value is larger than pageSize (which is 100 by default), you may have to load multiple pages to reach this total. See the Pagination section below for more. |
| `pageSize`              | number           | optional   | The number of records returned in each request. Must be less than or equal to 100. Default is 100. See the Pagination section below for more. |
| `sort`                  | array of objects | optional   | A list of sort objects that specifies how the records will be ordered. Each sort object must have a field key specifying the name of the field to sort on, and an optional direction key that is either "asc" or "desc" . The default direction is "asc" . The sort parameter overrides the sorting of the v |
| `view`                  | string           | optional   | The name or ID of a view in the Dot Records Data table. If set, only the records in that view will be returned. The records will be sorted according to the order of the view unless the sort parameter is included, which overrides that order. Fields hidden in this view will be returned in the results. |
| `cellFormat`            | string           | optional   | The format that should be used for cell values. Supported values are: json : cells will be formatted as JSON, depending on the field type. string : cells will be formatted as user-facing strings, regardless of the field type. The timeZone and userLocale parameters are required when using string as t |
| `timeZone`              | string           | optional   | The time zone that should be used to format dates when using string as the cellFormat . This parameter is required when using string as the cellFormat . |
| `userLocale`            | string           | optional   | The user locale that should be used to format dates when using string as the cellFormat . This parameter is required when using string as the cellFormat . |
| `returnFieldsByFieldId` | boolean          | optional   | An optional boolean value that lets you return field objects where the key is the field id. This defaults to false , which returns field objects where the key is the field name. |
| `recordMetadata`        | array of strings | optional   | An optional field that, if includes commentCount , adds a commentCount read only property on each record returned. |

---

## Retrieve a Record

**Endpoint:** `GET /v0/appEurfA8kXQE3slK/dot%20records%20data`

To retrieve an existing record in Dot Records Data table, issue a GET request to the record endpoint.

Any "empty" fields (e.g. "" , [] , or false ) in the record will not be returned.

```bash
curl https://api.airtable.com/v0/appEurfA8kXQE3slK/Dot%20Records%20Data/recL8FQe7krO5U6xs \
  -H "Authorization: Bearer YOUR_SECRET_API_TOKEN"
```

---

## Create Records

**Endpoint:** `POST /v0/appEurfA8kXQE3slK/dot%20records%20data`

To create new records, issue a POST request to the Dot Records Data endpoint. Note that table names and table ids can be used interchangeably. Using table ids means table name changes do not require modifications to your API request.

Your request body should include an array of up to 10 record objects. Each of these objects should have one key whose value is an inner object containing your record's cell values, keyed by either field name or field id.

```bash
curl -X POST https://api.airtable.com/v0/appEurfA8kXQE3slK/Dot%20Records%20Data \
  -H "Authorization: Bearer YOUR_SECRET_API_TOKEN" \
  -H "Content-Type: application/json" \
  --data '{
  "records": [
    {
      "fields": {
        "Album / Single Title": "L.P. Albums released in U.S.A."
      }
    },
    {
      "fields": {
        "Release Label": "Dot DLP 3012",
        "Album / Single Title": "Pat Boone",
        "Date": "1956",
        "Status": true,
        "Collaborator": "Chaz"
      }
    }
  ]
}'
```

---

## Update / Upsert Records

**Endpoint:** `PATCH /v0/appEurfA8kXQE3slK/dot%20records%20data`

To update Dot Records Data records, issue a request to the Dot Records Data endpoint. Table names and table IDs can be used interchangeably. Using table IDs means table name changes won't require modifying your API request code. A PATCH request will only update the fields included in the request. Fields not included in the request will be unchanged. A PUT request will perform a destructive update and clear all unincluded cell values.

Your request body should include an array of up to 10 record objects. Each of these objects should have an id property representing the record ID and a fields property which contains all of your record's cell values by field name or field id for all of your record's cell values by field name.

```bash
curl -X PATCH https://api.airtable.com/v0/appEurfA8kXQE3slK/Dot%20Records%20Data \
  -H "Authorization: Bearer YOUR_SECRET_API_TOKEN" \
  -H "Content-Type: application/json" \
  --data '{
  "records": [
    {
      "id": "recL8FQe7krO5U6xs",
      "fields": {
        "Album / Single Title": "L.P. Albums released in U.S.A."
      }
    },
    {
      "id": "recYcWPqfFS7YeATT",
      "fields": {
        "Release Label": "Dot DLP 3012",
        "Album / Single Title": "Pat Boone",
        "Date": "1956",
        "Status": true,
        "Collaborator": "Chaz"
      }
    },
    {
      "id": "rec7jilJrMd9zPxAp",
      "fields": {
        "Release Label": "Dot DLP 3030",
        "Album / Single Title": "Howdy!",
        "Date": "1957",
        "Status": true,
        "Collaborator": "Chaz"
      }
    }
  ]
}'
```

---

## Delete Records

**Endpoint:** `DELETE /v0/appEurfA8kXQE3slK/dot%20records%20data`

To delete Dot Records Data records, issue a DELETE request to the Dot Records Data endpoint. Note that table names and table ids can be used interchangeably. Using table ids means table name changes do not require modifications to your API request.

Your request should include a URL-encoded array of up to 10 record IDs to delete.

```bash
curl -X DELETE https://api.airtable.com/v0/appEurfA8kXQE3slK/Dot%20Records%20Data \
  -H "Authorization: Bearer YOUR_SECRET_API_TOKEN" \
  -G \
  --data-urlencode 'records[]=recL8FQe7krO5U6xs' \
  --data-urlencode 'records[]=recYcWPqfFS7YeATT'
```

