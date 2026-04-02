# Legal Docs

**Table ID:** `tbl0JjCNEaGmFGAkx`  
**Base ID:** `appEurfA8kXQE3slK`

---

## Fields

| Field Name                     | Field ID            | Type                   | Description                                                                      |
| ------------------------------ | ------------------- | ---------------------- | -------------------------------------------------------------------------------- |
| Legal Document                 | `fldmoQzt8ffAPtWCV` | Text                   | A single line of text.                                                           |
| Notes                          | `fldjruRCbq2rRn5b0` | Long text              | Multiple lines of text, which may contain "mention tokens", e.g. <airtable:mention id="menE1i9oBaGX3DseR">@Alex</airtable:mention> |
| Link to Document(s)            | `fldLQRo1T8X4RGpj5` | URL                    | A valid URL (e.g. airtable.com or https://airtable.com/universe).                |
| Related Legal Docs             | `fldTIZRdifmWsei2p` | Link to another record | Array of linked records IDs from the Legal Docs table.                           |
| Document Type                  | `fldL0MpAt1r3OJfZN` | Multiple select        | Array of selected option names. When creating or updating records, if a choice string does not exactly match an existing option, the request will fail with an INVALID_MULTIPLE_CHOICE_OPTIONS error unless the typecast parameter is enabled. If typecast is enabled, a new choice will be created if one does not exactly match. |
| Contract Status                | `fldEwhRSpay7n4edv` | Single select          | Selected option name. When creating or updating records, if the choice string does not exactly match an existing option, the request will fail with an INVALID_MULTIPLE_CHOICE_OPTIONS error unless the typecast parameter is enabled. If typecast is enabled, a new choice will be created if one does not exactly match. |
| Effective Date                 | `fldTzSY2siUPNxRPy` | Date                   | UTC date, e.g. "2014-09-05".                                                     |
| Expiration Date                | `fldimOj9fbSairsOp` | Date                   | UTC date, e.g. "2014-09-05".                                                     |
| Territory                      | `fldoCSxk16H4F6bzz` | Text                   | A single line of text.                                                           |
| Master Owner                   | `fldXUjQvuEbtzF2y6` | Link to another record | Array of linked records IDs from the Master Owners table.                        |
| Artists                        | `fld589CVNN3Dz4LIo` | Link to another record | Array of linked records IDs from the Artists table.                              |
| Linked Compositions            | `fldD2pmUU5QiXFHSx` | Link to another record | Array of linked records IDs from the Compositions table.                         |
| Publisher(s)                   | `fldE9rUE0HpFuoxGX` | Link to another record | Array of linked records IDs from the Publishers table.                           |
| Songwriter(s)                  | `fld1qPXmNU8VlgWOj` | Link to another record | Array of linked records IDs from the Songwriters table.                          |
| Recordings                     | `fldPBENvLLuCsdN7g` | Link to another record | Array of linked records IDs from the Recordings table.                           |
| Releases                       | `fldoyrjPJv0VJzsns` | Link to another record | Array of linked records IDs from the Releases table.                             |
| From field: Related Legal Docs | `flddf50UzWyJzJA7G` | Link to another record | Array of linked records IDs from the Legal Docs table.                           |

---

## List Records

**Endpoint:** `GET /v0/appEurfA8kXQE3slK/legal%20docs`

To list records in Legal Docs , issue a GET request to the Legal Docs endpoint. Note that table names and table ids can be used interchangeably. Using table ids means table name changes do not require modifications to your API request.

Returned records do not include any fields with "empty" values, e.g. "" , [] , or false .

```bash
curl "https://api.airtable.com/v0/appEurfA8kXQE3slK/Legal%20Docs?maxRecords=3&view=Grid%20view" \
  -H "Authorization: Bearer YOUR_SECRET_API_TOKEN"
```

### Query Parameters

| Parameter               | Type             | Required   | Description                                                                      |
| ----------------------- | ---------------- | ---------- | -------------------------------------------------------------------------------- |
| `fields`                | array of strings | optional   | Only data for fields whose names are in this list will be included in the result. If you don't need every field, you can use this parameter to reduce the amount of data transferred. For example, to only return data from Legal Document and Notes , send these two query parameters: fields%5B%5D=Legal%2 |
| `filterByFormula`       | string           | optional   | A formula used to filter records. The formula will be evaluated for each record, and if the result is not 0 , false , "" , NaN , [] , or #Error! the record will be included in the response. We recommend testing your formula in the Formula field UI before using it in your API request. If combined wit |
| `maxRecords`            | number           | optional   | The maximum total number of records that will be returned in your requests. If this value is larger than pageSize (which is 100 by default), you may have to load multiple pages to reach this total. See the Pagination section below for more. |
| `pageSize`              | number           | optional   | The number of records returned in each request. Must be less than or equal to 100. Default is 100. See the Pagination section below for more. |
| `sort`                  | array of objects | optional   | A list of sort objects that specifies how the records will be ordered. Each sort object must have a field key specifying the name of the field to sort on, and an optional direction key that is either "asc" or "desc" . The default direction is "asc" . The sort parameter overrides the sorting of the v |
| `view`                  | string           | optional   | The name or ID of a view in the Legal Docs table. If set, only the records in that view will be returned. The records will be sorted according to the order of the view unless the sort parameter is included, which overrides that order. Fields hidden in this view will be returned in the results. To on |
| `cellFormat`            | string           | optional   | The format that should be used for cell values. Supported values are: json : cells will be formatted as JSON, depending on the field type. string : cells will be formatted as user-facing strings, regardless of the field type. The timeZone and userLocale parameters are required when using string as t |
| `timeZone`              | string           | optional   | The time zone that should be used to format dates when using string as the cellFormat . This parameter is required when using string as the cellFormat . |
| `userLocale`            | string           | optional   | The user locale that should be used to format dates when using string as the cellFormat . This parameter is required when using string as the cellFormat . |
| `returnFieldsByFieldId` | boolean          | optional   | An optional boolean value that lets you return field objects where the key is the field id. This defaults to false , which returns field objects where the key is the field name. |
| `recordMetadata`        | array of strings | optional   | An optional field that, if includes commentCount , adds a commentCount read only property on each record returned. |

---

## Retrieve a Record

**Endpoint:** `GET /v0/appEurfA8kXQE3slK/legal%20docs`

To retrieve an existing record in Legal Docs table, issue a GET request to the record endpoint.

Any "empty" fields (e.g. "" , [] , or false ) in the record will not be returned.

```bash
curl https://api.airtable.com/v0/appEurfA8kXQE3slK/Legal%20Docs/recUMZMcVMzwiu50I \
  -H "Authorization: Bearer YOUR_SECRET_API_TOKEN"
```

---

## Create Records

**Endpoint:** `POST /v0/appEurfA8kXQE3slK/legal%20docs`

To create new records, issue a POST request to the Legal Docs endpoint. Note that table names and table ids can be used interchangeably. Using table ids means table name changes do not require modifications to your API request.

Your request body should include an array of up to 10 record objects. Each of these objects should have one key whose value is an inner object containing your record's cell values, keyed by either field name or field id.

```bash
curl -X POST https://api.airtable.com/v0/appEurfA8kXQE3slK/Legal%20Docs \
  -H "Authorization: Bearer YOUR_SECRET_API_TOKEN" \
  -H "Content-Type: application/json" \
  --data '{
  "records": [
    {
      "fields": {
        "Legal Document": "Dot Records Notice of Termination",
        "Notes": "This document affects recordings between 1954 and December 31, 1963. They were originally owned by Dot (Universal) and are now owned by PBGL.",
        "Link to Document(s)": "https://app.box.com/s/8c56xlsviqeb9e99zsy7pe5lkyjrknva",
        "Document Type": [
          "Notice of Termination"
        ],
        "Contract Status": "Terminated",
        "Master Owner": [
          "recFsgtFh5ff9SxTo",
          "recT0ecpuEpwlNIRj",
          "recmbD0S2y6gdZY0M"
        ],
        "Artists": [
          "recLWgt9qnlgDkkAo"
        ]
      }
    },
    {
      "fields": {
        "Legal Document": "Termination of Publishing Administration Agreement (Sweet On Top)",
        "Link to Document(s)": "https://app.box.com/s/23vsfyhnnvs1af4slz2dxsfwgjlci08p",
        "Document Type": [
          "Notice of Termination"
        ],
        "Contract Status": "Active",
        "Effective Date": "2024-08-01",
        "Master Owner": [
          "recmbD0S2y6gdZY0M"
        ],
        "Publisher(s)": [
          "rec4gUR7stMFkj10q",
          "recdo7hEep1rfVDCC",
          "recpbxExDaBhGyWkS",
          "recJQPGTBcdpMAwqB"
        ],
        "From field: Related Legal Docs": [
          "recduGrUuXK8y9zsw",
          "rec27paI1G3JkghDp"
        ]
      }
    }
  ]
}'
```

---

## Update / Upsert Records

**Endpoint:** `PATCH /v0/appEurfA8kXQE3slK/legal%20docs`

To update Legal Docs records, issue a request to the Legal Docs endpoint. Table names and table IDs can be used interchangeably. Using table IDs means table name changes won't require modifying your API request code. A PATCH request will only update the fields included in the request. Fields not included in the request will be unchanged. A PUT request will perform a destructive update and clear all unincluded cell values.

Your request body should include an array of up to 10 record objects. Each of these objects should have an id property representing the record ID and a fields property which contains all of your record's cell values by field name or field id for all of your record's cell values by field name.

```bash
curl -X PATCH https://api.airtable.com/v0/appEurfA8kXQE3slK/Legal%20Docs \
  -H "Authorization: Bearer YOUR_SECRET_API_TOKEN" \
  -H "Content-Type: application/json" \
  --data '{
  "records": [
    {
      "id": "recUMZMcVMzwiu50I",
      "fields": {
        "Legal Document": "Dot Records Notice of Termination",
        "Notes": "This document affects recordings between 1954 and December 31, 1963. They were originally owned by Dot (Universal) and are now owned by PBGL.",
        "Link to Document(s)": "https://app.box.com/s/8c56xlsviqeb9e99zsy7pe5lkyjrknva",
        "Document Type": [
          "Notice of Termination"
        ],
        "Contract Status": "Terminated",
        "Master Owner": [
          "recFsgtFh5ff9SxTo",
          "recT0ecpuEpwlNIRj",
          "recmbD0S2y6gdZY0M"
        ],
        "Artists": [
          "recLWgt9qnlgDkkAo"
        ]
      }
    },
    {
      "id": "recZsahORphdy8KdM",
      "fields": {
        "Legal Document": "Termination of Publishing Administration Agreement (Sweet On Top)",
        "Link to Document(s)": "https://app.box.com/s/23vsfyhnnvs1af4slz2dxsfwgjlci08p",
        "Document Type": [
          "Notice of Termination"
        ],
        "Contract Status": "Active",
        "Effective Date": "2024-08-01",
        "Master Owner": [
          "recmbD0S2y6gdZY0M"
        ],
        "Publisher(s)": [
          "rec4gUR7stMFkj10q",
          "recdo7hEep1rfVDCC",
          "recpbxExDaBhGyWkS",
          "recJQPGTBcdpMAwqB"
        ],
        "From field: Related Legal Docs": [
          "recduGrUuXK8y9zsw",
          "rec27paI1G3JkghDp"
        ]
      }
    },
    {
      "id": "recduGrUuXK8y9zsw",
      "fields": {
        "Legal Document": "COOGA MUSIC CORP~SWEET ON TOP LOD (BMI) AUG 8 2022 Signed",
        "Link to Document(s)": "https://app.box.com/s/9hf22s10pfq4xabogls0scdnl9mv5qjd",
        "Related Legal Docs": [
          "recZsahORphdy8KdM"
        ],
        "Document Type": [
          "Publishing Agreement"
        ],
        "Contract Status": "Terminated",
        "Effective Date": "2022-02-25",
        "Expiration Date": "2024-08-01",
        "Publisher(s)": [
          "recJQPGTBcdpMAwqB",
          "rec4gUR7stMFkj10q",
          "recdo7hEep1rfVDCC"
        ]
      }
    }
  ]
}'
```

---

## Delete Records

**Endpoint:** `DELETE /v0/appEurfA8kXQE3slK/legal%20docs`

To delete Legal Docs records, issue a DELETE request to the Legal Docs endpoint. Note that table names and table ids can be used interchangeably. Using table ids means table name changes do not require modifications to your API request.

Your request should include a URL-encoded array of up to 10 record IDs to delete.

```bash
curl -X DELETE https://api.airtable.com/v0/appEurfA8kXQE3slK/Legal%20Docs \
  -H "Authorization: Bearer YOUR_SECRET_API_TOKEN" \
  -G \
  --data-urlencode 'records[]=recUMZMcVMzwiu50I' \
  --data-urlencode 'records[]=recZsahORphdy8KdM'
```

