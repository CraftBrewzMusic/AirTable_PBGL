# Compositions

**Table ID:** `tblomWINKPjfgAVpo`  
**Base ID:** `appEurfA8kXQE3slK`

---

## Fields

| Field Name                                                      | Field ID            | Type                   | Description                                                                      |
| --------------------------------------------------------------- | ------------------- | ---------------------- | -------------------------------------------------------------------------------- |
| Song Title In PRO                                               | `fldBLBpVsd3kBKapM` | Text                   | A single line of text.                                                           |
| Notes                                                           | `fld0D3S3I77KWWIMM` | Long text              | Multiple lines of text, which may contain "mention tokens", e.g. <airtable:mention id="menE1i9oBaGX3DseR">@Alex</airtable:mention> |
| REGISTRATION PROJECT                                            | `fldN5elY1M8qIXXZ4` | Link to another record | Array of linked records IDs from the REGISTRATION PROJECT (PRO +MLC) table.      |
| ISWC                                                            | `fldVv5OnnDxzqcmIA` | Long text              | Multiple lines of text, which may contain "mention tokens", e.g. <airtable:mention id="menE1i9oBaGX3DseR">@Alex</airtable:mention> |
| MLC Song Code                                                   | `fld2WmSMkPTGWOhVh` | Text                   | A single line of text.                                                           |
| MLC work links                                                  | `fldPHd0XjNLVAbzmW` | URL                    | A valid URL (e.g. airtable.com or https://airtable.com/universe).                |
| Recordings                                                      | `fldVjjMa9H9Zpx9p0` | Link to another record | Array of linked records IDs from the Recordings table.                           |
| Duration (from Recordings)                                      | `fldOOnejpImbNJ2l2` | Lookup                 | Array of Duration fields in linked Recordings records.                           |
| Verified Info                                                   | `fldzjgPgUAGkkE6fy` | Single select          | Selected option name. When creating or updating records, if the choice string does not exactly match an existing option, the request will fail with an INVALID_MULTIPLE_CHOICE_OPTIONS error unless the typecast parameter is enabled. If typecast is enabled, a new choice will be created if one does not exactly match. |
| PRO Registration Status                                         | `fldfOZcMxH4OLCMiU` | Lookup                 | Array of PROs fields in linked REGISTRATION PROJECT (PRO +MLC) records.          |
| MLC Registration Status                                         | `fldH7AnLMPfiJDcV9` | Lookup                 | Array of fields in linked REGISTRATION PROJECT (PRO +MLC) records.               |
| Ready for Sync                                                  | `fldExx4NthXNGImyi` | Lookup                 | Array of Ready for Sync fields in linked Recordings records.                     |
| All Songwriters                                                 | `fldRfWFbfjTZXzfKP` | Link to another record | Array of linked records IDs from the Songwriters table.                          |
| IPI Number (from All Songwriters)                               | `fldI1DzNcShZI3raL` | Lookup                 | Array of IPI Number fields in linked Songwriters records.                        |
| All Original Publishers                                         | `fldkIOo7kToJaT5zm` | Link to another record | Array of linked records IDs from the Publishers table.                           |
| Recording Title                                                 | `fldGwLne6e5FZzn1Q` | Lookup                 | Array of Title of Recording fields in linked Recordings records.                 |
| Alternate Title                                                 | `fld2z6RCiksnybQZC` | Long text              | Multiple lines of text, which may contain "mention tokens", e.g. <airtable:mention id="menE1i9oBaGX3DseR">@Alex</airtable:mention> |
| Primary Artist (from Recordings)                                | `fldbeWmTOAt5r9kBI` | Lookup                 | Array of Primary Artist fields in linked Recordings records.                     |
| ISRC (from Recordings)                                          | `fldK3wvMstiKhS9Gm` | Lookup                 | Array of ISRC fields in linked Recordings records.                               |
| Current release label (from Original Release) (from Recordings) | `fldXrE14dN9EPy1a8` | Lookup                 | Array of Current release label (from Original Release) fields in linked Recordings records. |
| Releases check                                                  | `fldJwPdhgS1EdvocV` | Lookup                 | Array of All Releases fields in linked Recordings records.                       |
| Releases                                                        | `fldJj9yZLZEdu8qS8` | Link to another record | Array of linked records IDs from the Releases table.                             |
| Songwriter summary                                              | `fldP5h9q03wu8d728` | Formula                | Computed value: CONCATENATE({ Songwriter 1 } & '\n' & '\n' & { Songwriter 2 } & '\n' & '\n' & { Songwriter 3 } & '\n' & '\n' & { Songwriter 4 } & '\n' & '\n' & { Songwriter 5 } & '\n' & '\n' & { Songwriter 6 } & '\n' & '\n' & { Songwriter 7 } & '\n' & '\n' & { Songwriter 8 } & '\n' & '\n' & { Songwriter 9 }) . |
| Original Pub Summary                                            | `fldobngOfA47LjZTm` | Formula                | Computed value: CONCATENATE({ Songwriter 1 Original Pub 1 } & '\n' & '\n' & { Songwriter 1 Original Pub 2 } & '\n' & '\n' & { Songwriter 1 Original Pub 3 } & '\n' & '\n' & { Songwriter 1 Original Pub 4 } & '\n' & '\n' & { Songwriter 2 Original Pub. 1 } & '\n' & '\n' & { Songwriter 2 Original Pub. 2 } & '\n' & '\n' & { Songwriter 2 Original Pub. 3 } & '\n' & '\n' & { Songwriter 2 Original Pub 4 } & '\n' & '\n' & { Songwriter 3 Original Pub. 1 } & '\n' & '\n' & { Songwriter 3 Original Pub. 2 } & '\n' & '\n' & { Songwriter 4 Original Pub. 1 } & '\n' & '\n' & { Songwriter 4 Original Pub 2 } & '\n' & '\n' & { Songwriter 5 Original Pub. 1 } & '\n' & '\n' & { Songwriter 5 Original Pub 2 } & '\n' & '\n' & { Songwriter 6 Original Pub 1 } & '\n' & '\n' & { Songwriter 6 Original Pub. 2 } & '\n' & '\n' & { Songwriter 7 Original Pub. 1 } & '\n' & '\n' & { Songwriter 7 Original Pub. 2 } & '\n' & '\n' & { Songwriter 8 Original Pub. 1 } & '\n' & '\n' & { Songwriter 8 Original Pub. 2 } & '\n' & '\n' & { Songwriter 9 Original Pub. 1 } & '\n' & '\n' & { Songwriter 9 Original Pub. 2 }) . |
| All Admin Publishers                                            | `fld58IACBmYnW9DJu` | Link to another record | Array of linked records IDs from the Publishers table.                           |
| Admin Pub summary                                               | `fldhb2N8dzswr8X6K` | Formula                | Computed value: CONCATENATE({ Songwriter 1 Admin Pub 1 } & '\n' & { Songwriter 1 Admin Pub 2 } & '\n' & { Songwriter 1 Admin Pub 3 } & '\n' & { Songwriter 1 Admin Pub 4 } & '\n' & { Songwriter 2 Admin Pub 1 } & '\n' & { Songwriter 2 Admin Pub. 2 } & '\n' & { Songwriter 2 Admin Pub. 3 } & '\n' & { Songwriter 2 Admin Pub 4 } & '\n' & { Songwriter 3 Admin Pub. 1 } & '\n' & { Songwriter 3 Admin Pub. 2 } & '\n' & { Songwriter 4 Admin Pub. 1 } & '\n' & { Songwriter 4 Admin Pub. 2 } & '\n' & { Songwriter 5 Admin Pub 1 } & '\n' & { Songwriter 5 Admin Pub. 2 } & '\n' & { Songwriter 6 Admin Pub. 1 } & '\n' & { Songwriter 6 Admin Pub. 2 } & '\n' & { Songwriter 7 Admin Pub. 1 } & '\n' & { Songwriter 7 Admin Pub. 2 } & '\n' & { Songwriter 8 Admin Pub. 1 } & '\n' & { Songwriter 8 Admin Pub. 2 } & '\n' & { Songwriter 9 Admin Pub. 1 } & '\n' & { Songwriter 9 Admin Pub. 2 }) . |
| All Sub-Publishers                                              | `fldMf59kc6MdOns1n` | Link to another record | Array of linked records IDs from the Publishers table.                           |
| Sub-Pub Summary                                                 | `fld3vWOwZjiZdXTco` | Formula                | Computed value: CONCATENATE({ Songwriter 1 Sub-Pub 1 } & '\n' & '\n' & { Songwriter 2 Sub-Pub 1 } & '\n' & '\n' & { Songwriter 3 Sub-Pub 1 }) . |
| Controlled                                                      | `fldDyYxGEbHPJuUPm` | Checkbox               | This field is "true" when checked and otherwise empty.                           |
| PROs Involved                                                   | `fldRewvu2vu08e3aj` | Rollup                 | Computed value: ARRAYUNIQUE(values) for PRO Affiliation in Songwriters .         |
| Involved PROs                                                   | `fldNszvBz13vnNq5h` | Multiple select        | Array of selected option names. When creating or updating records, if a choice string does not exactly match an existing option, the request will fail with an INVALID_MULTIPLE_CHOICE_OPTIONS error unless the typecast parameter is enabled. If typecast is enabled, a new choice will be created if one does not exactly match. |
| PRO Summary                                                     | `fldZ0LGrupTF7ll8j` | Formula                | Computed value: CONCATENATE({ PRO Affiliation (from Songwriter 1) }, " - ", { PRO Affiliation (from Songwriter 1 Original Pub. 1) }, " - ", { PRO Affiliation (from Songwriter 1 Original Pub. 2) }, " - ", { PRO Affiliation (from Songwriter 1 Original Pub 3) }, " - ", { PRO Affiliation (from Songwriter 1 Original Pub 4) },{ PRO Affiliation (from Songwriter 2) }, " - ", { PRO Affiliation (from Songwriter 2 Original Pub. 1) }, " - ", { PRO Affiliation (from Songwriter 2 Original Pub. 2) }, " - ", { PRO Affiliation (from Songwriter 2 Original Pub. 3) }, " - ", { PRO Affiliation (from Songwriter 2 Original Pub 4) }, " - ", { PRO Affiliation (from Songwriter 3 Original Pub. 1) }, " - ", { PRO Affiliation (from Songwriter 3 Original Pub. 2) }, " - ", { PRO Affiliation (from Songwriter 4) }, " - ", { PRO Affiliation (from Songwriter 4 Original Pub.) }, " - ", { PRO Affiliation (from Songwriter 4 Original Pub 2) }, " - ", { PRO Affiliation (from Songwriter 5) }, " - ", { PRO Affiliation (from Songwriter 5 Original Pub.) }, " - ", { PRO Affiliation (from Songwriter 5 Original Pub. 2) }, " - ", { PRO Affiliation (from Songwriter 6) }, " - ", { PRO Affiliation (from Songwriter 6 Original Pub.) }, " - ", { PRO Affiliation (from Songwriter 6 Original Pub. 2) }, " - ", { PRO Affiliation (from Songwriter 7) }, " - ", { PRO Affiliation (from Songwriter 7 Original Pub.) }, " - ", { PRO Affiliation (from Songwriter 7 Original Pub. 2) }, " - ", { PRO Affiliation (from Songwriter 8) }, " - ", { PRO Affiliation (from Songwriter 8 Original Pub. 1) }, " - ", { PRO Affiliation (from Songwriter 8 Original Pub. 2) }, " - ", { PRO Affiliation (from Songwriter 9) }, " - ", { PRO Affiliation (from Songwriter 9 Original Pub. 1) }, " - ", { PRO Affiliation (from Songwriter 9 Original Pub. 2) }) . |
| Sampled In                                                      | `fldxbJTF0hprVgoNy` | Long text              | Multiple lines of text, which may contain "mention tokens", e.g. <airtable:mention id="menE1i9oBaGX3DseR">@Alex</airtable:mention> |
| Synchronized In                                                 | `fldbw22E1rFcWWZGO` | Long text              | Multiple lines of text, which may contain "mention tokens", e.g. <airtable:mention id="menE1i9oBaGX3DseR">@Alex</airtable:mention> |
| Date of First Use                                               | `fldM3UkZ4xMgmSkb5` | Long text              | Multiple lines of text, which may contain "mention tokens", e.g. <airtable:mention id="menE1i9oBaGX3DseR">@Alex</airtable:mention> |
| Intended Purpose                                                | `fldKKGcBQ0eRk7BoR` | Single select          | Selected option name. When creating or updating records, if the choice string does not exactly match an existing option, the request will fail with an INVALID_MULTIPLE_CHOICE_OPTIONS error unless the typecast parameter is enabled. If typecast is enabled, a new choice will be created if one does not exactly match. |
| Production Title                                                | `fldjB5BRTSHOXSQjX` | Text                   | A single line of text.                                                           |
| PD Work Status                                                  | `fldVQAiwsIi0m1EAA` | Single select          | Selected option name. When creating or updating records, if the choice string does not exactly match an existing option, the request will fail with an INVALID_MULTIPLE_CHOICE_OPTIONS error unless the typecast parameter is enabled. If typecast is enabled, a new choice will be created if one does not exactly match. |
| Original PD Work Title                                          | `fldIfelxyqGVr9ZmQ` | Text                   | A single line of text.                                                           |
| Uncredited PD Writers                                           | `fldUFeBEXjI4gjufB` | Long text              | Multiple lines of text, which may contain "mention tokens", e.g. <airtable:mention id="menE1i9oBaGX3DseR">@Alex</airtable:mention> |
| Pub Shares Sum                                                  | `fldwjJVhTCRGzXQQ2` | Formula                | Computed value: SUM({ Songwriter 1 Original Pub 1 Share }, { Songwriter 1 Original Pub 2 Share }, { Songwriter 1 Original Pub 3 Share },{ Songwriter 1 Original Pub 4 Share }, { Songwriter 2 Original Pub. 1 Share }, { Songwriter 2 Original Pub. 2 Share }, { Songwriter 2 Original Pub 3 Share }, { Songwriter 2 Original Pub 4 Share }, { Songwriter 3 Original Pub. 1 Share }, { Songwriter 3 Original Pub. 2 Share }, { Songwriter 4 Original Pub. 1 Share }, { Songwriter 4 Original Pub 2 Share }, { Songwriter 5 Original Pub 1 Share }, { Songwriter 5 Original Pub 2 Share }, { Songwriter 6 Original Pub. 1 Share }, { Songwriter 6 Original Pub 2 Share }, { Songwriter 7 Original Pub. 1 Share }, { Songwriter 7 Original Pub. 2 Share }, { Songwriter 8 Original Pub. 1 Share }, { Songwriter 8 Original Pub. 2 Share }, { Songwriter 9 Original Pub. 1 Share }, { Songwriter 9 Original Pub. 2 Share }) . |
| Songwriter 1                                                    | `fldLhXZcoaevUSLlA` | Link to another record | Array of linked records IDs from the Songwriters table.                          |
| Songwriter 1 Share                                              | `fldqFoYcdP4QpRtlF` | Percent                | Decimal number representing a percentage value. For example, the underlying cell value for 12.3% is 0.123. This field only allows positive numbers. |
| Songwriter 1 Role                                               | `fld2hxd4Snp1BYSar` | Multiple select        | Array of selected option names. When creating or updating records, if a choice string does not exactly match an existing option, the request will fail with an INVALID_MULTIPLE_CHOICE_OPTIONS error unless the typecast parameter is enabled. If typecast is enabled, a new choice will be created if one does not exactly match. |
| Songwriter 1 Original Pub 1                                     | `fldcx8y9D1KbIfCCj` | Link to another record | Array of linked records IDs from the Publishers table.                           |
| Songwriter 1 Original Pub 1 Share                               | `fldcjWL6czrFQfEtU` | Percent                | Decimal number representing a percentage value. For example, the underlying cell value for 12.3% is 0.123. This field only allows positive numbers. |
| Songwriter 1 Admin Pub 1                                        | `fldeNG9WWWEeKzHpN` | Link to another record | Array of linked records IDs from the Publishers table.                           |
| Email (from Songwriter 1 Admin Pub 1)                           | `fldLYqBaQn7RI0b47` | Lookup                 | Array of Email fields in linked Publishers records.                              |
| Address (from Songwriter 1 Admin Pub 1)                         | `fldQxH0nR1LdbRSCS` | Lookup                 | Array of Address fields in linked Publishers records.                            |
| Songwriter 1 Sub-Pub 1                                          | `fldMi4ctlHPOaPFMD` | Link to another record | Array of linked records IDs from the Publishers table.                           |
| Songwriter 1 Original Pub 2                                     | `fldmeUuHY6dE7eRuq` | Link to another record | Array of linked records IDs from the Publishers table.                           |
| Songwriter 1 Original Pub 2 Share                               | `fldT7ce7D97Avdfb0` | Percent                | Decimal number representing a percentage value. For example, the underlying cell value for 12.3% is 0.123. This field only allows positive numbers. |
| Songwriter 1 Admin Pub 2                                        | `fldidUvdgDagDJ1rf` | Link to another record | Array of linked records IDs from the Publishers table.                           |
| Email (from Songwriter 1 Admin Pub 2)                           | `fld80psfK3ChBpfGQ` | Lookup                 | Array of Email fields in linked Publishers records.                              |
| Address (from Songwriter 1 Admin Pub 2)                         | `fldkh6goyYT6R180j` | Lookup                 | Array of Address fields in linked Publishers records.                            |
| Songwriter 1 Original Pub 3                                     | `fldsKbymynSOfi6rQ` | Link to another record | Array of linked records IDs from the Publishers table.                           |
| Songwriter 1 Original Pub 3 Share                               | `fld5BAlh8bUNmROPu` | Percent                | Decimal number representing a percentage value. For example, the underlying cell value for 12.3% is 0.123. This field only allows positive numbers. |
| Songwriter 1 Admin Pub 3                                        | `fldYrbODcYavzhqbM` | Link to another record | Array of linked records IDs from the Publishers table.                           |
| Songwriter 1 Original Pub 4                                     | `fldgHvCEX0OIRYscT` | Link to another record | Array of linked records IDs from the Publishers table.                           |
| Songwriter 1 Original Pub 4 Share                               | `fldLIgL3205HD0t4Y` | Percent                | Decimal number representing a percentage value. For example, the underlying cell value for 12.3% is 0.123. This field only allows positive numbers. |
| Songwriter 1 Admin Pub 4                                        | `fldNnONxuj9KnFxnu` | Link to another record | Array of linked records IDs from the Publishers table.                           |
| Songwriter 2                                                    | `fldeivT63AcOXMinA` | Link to another record | Array of linked records IDs from the Songwriters table.                          |
| Songwriter 2 Share                                              | `fldwYiUeQgQID1ehO` | Percent                | Decimal number representing a percentage value. For example, the underlying cell value for 12.3% is 0.123. This field only allows positive numbers. |
| Songwriter 2 Role                                               | `fldjTMZcewms7A4Y9` | Multiple select        | Array of selected option names. When creating or updating records, if a choice string does not exactly match an existing option, the request will fail with an INVALID_MULTIPLE_CHOICE_OPTIONS error unless the typecast parameter is enabled. If typecast is enabled, a new choice will be created if one does not exactly match. |
| Songwriter 2 Original Pub. 1                                    | `fld4085JeJSnRKbhA` | Link to another record | Array of linked records IDs from the Publishers table.                           |
| Songwriter 2 Original Pub. 1 Share                              | `fldqMemokLaBF4OaK` | Percent                | Decimal number representing a percentage value. For example, the underlying cell value for 12.3% is 0.123. This field only allows positive numbers. |
| Songwriter 2 Admin Pub 1                                        | `fld2pifFJ2sg6UMRo` | Link to another record | Array of linked records IDs from the Publishers table.                           |
| Email (from Songwriter 2 Admin Pub 1)                           | `fldtuS8FF7yFxCzin` | Lookup                 | Array of Email fields in linked Publishers records.                              |
| Address (from Songwriter 2 Admin Pub 1)                         | `fldLykzU0L6kfGi3A` | Lookup                 | Array of Address fields in linked Publishers records.                            |
| Songwriter 2 Sub-Pub 1                                          | `fld9zTSYx2pv31dxT` | Link to another record | Array of linked records IDs from the Publishers table.                           |
| Songwriter 2 Original Pub. 2                                    | `fld42MeLzoYB1jYC4` | Link to another record | Array of linked records IDs from the Publishers table.                           |
| Songwriter 2 Original Pub. 2 Share                              | `fldxFU6Xcq3BINcc5` | Percent                | Decimal number representing a percentage value. For example, the underlying cell value for 12.3% is 0.123. This field only allows positive numbers. |
| Songwriter 2 Admin Pub. 2                                       | `fldKbVO7wYpvXzpUK` | Link to another record | Array of linked records IDs from the Publishers table.                           |
| Email (from Songwriter 2 Admin Pub. 2)                          | `fldsMjS4XKAJpBhSq` | Lookup                 | Array of Email fields in linked Publishers records.                              |
| Address (from Songwriter 2 Admin Pub. 2)                        | `fldmkPbUQODmoB72j` | Lookup                 | Array of Address fields in linked Publishers records.                            |
| Songwriter 2 Original Pub. 3                                    | `fldV0guqfaRzYaOql` | Link to another record | Array of linked records IDs from the Publishers table.                           |
| Songwriter 2 Original Pub 3 Share                               | `fld9TU2v36ZlYsm0v` | Percent                | Decimal number representing a percentage value. For example, the underlying cell value for 12.3% is 0.123. This field only allows positive numbers. |
| Songwriter 2 Admin Pub. 3                                       | `fldEwxZB6t2ApprA9` | Link to another record | Array of linked records IDs from the Publishers table.                           |
| Songwriter 2 Original Pub 4                                     | `fldZjIC9fyswqRfOa` | Link to another record | Array of linked records IDs from the Publishers table.                           |
| Songwriter 2 Original Pub 4 Share                               | `fldovV2KQZyo8a8CR` | Percent                | Decimal number representing a percentage value. For example, the underlying cell value for 12.3% is 0.123. This field only allows positive numbers. |
| Songwriter 2 Admin Pub 4                                        | `fld0fCbtnmVTHcKC8` | Link to another record | Array of linked records IDs from the Publishers table.                           |
| Songwriter 3                                                    | `fldpQwAEw0mATtMW4` | Link to another record | Array of linked records IDs from the Songwriters table.                          |
| Songwriter 3 Ownership                                          | `fldPwg7CGdho4EERI` | Percent                | Decimal number representing a percentage value. For example, the underlying cell value for 12.3% is 0.123. This field only allows positive numbers. |
| Songwriter 3 Role                                               | `fldp5WGgspZEA4iTF` | Multiple select        | Array of selected option names. When creating or updating records, if a choice string does not exactly match an existing option, the request will fail with an INVALID_MULTIPLE_CHOICE_OPTIONS error unless the typecast parameter is enabled. If typecast is enabled, a new choice will be created if one does not exactly match. |
| Songwriter 3 Original Pub. 1                                    | `fldVAiZ0RFyEih9HO` | Link to another record | Array of linked records IDs from the Publishers table.                           |
| Songwriter 3 Original Pub. 1 Share                              | `fld6pjTCxLGLL9jsQ` | Percent                | Decimal number representing a percentage value. For example, the underlying cell value for 12.3% is 0.123. This field only allows positive numbers. |
| Songwriter 3 Admin Pub. 1                                       | `fldiKRkycbb71x06O` | Link to another record | Array of linked records IDs from the Publishers table.                           |
| Email (from Songwriter 3 Admin Pub. 1)                          | `fld3CtgxdUGHCRhFl` | Lookup                 | Array of Email fields in linked Publishers records.                              |
| Address (from Songwriter 3 Admin Pub. 1)                        | `fldAyXZIIQcuMD7xz` | Lookup                 | Array of Address fields in linked Publishers records.                            |
| Songwriter 3 Sub-Pub 1                                          | `fld8ssi2tFWvUy7WO` | Link to another record | Array of linked records IDs from the Publishers table.                           |
| Songwriter 3 Original Pub. 2                                    | `fldH8we533t41M6B7` | Link to another record | Array of linked records IDs from the Publishers table.                           |
| Songwriter 3 Original Pub. 2 Share                              | `fld0rjCDUUqVWi4dj` | Percent                | Decimal number representing a percentage value. For example, the underlying cell value for 12.3% is 0.123. This field only allows positive numbers. |
| Songwriter 3 Admin Pub. 2                                       | `fldY3XaFcn8EZD8Sw` | Link to another record | Array of linked records IDs from the Publishers table.                           |
| Email (from Songwriter 3 Admin Pub. 2)                          | `fldCdSlkIXmdImCx8` | Lookup                 | Array of Email fields in linked Publishers records.                              |
| Address (from Songwriter 3 Admin Pub. 2)                        | `fldBYKaEFIVSiFIDX` | Lookup                 | Array of Address fields in linked Publishers records.                            |
| Songwriter 4                                                    | `fldfi9zF7k7eyzN3E` | Link to another record | Array of linked records IDs from the Songwriters table.                          |
| Songwriter 4 Ownership                                          | `fldZLBA62pZY5BCWC` | Percent                | Decimal number representing a percentage value. For example, the underlying cell value for 12.3% is 0.123. This field only allows positive numbers. |
| Songwriter 4 Role                                               | `fldXkpl6ajr53tAZX` | Multiple select        | Array of selected option names. When creating or updating records, if a choice string does not exactly match an existing option, the request will fail with an INVALID_MULTIPLE_CHOICE_OPTIONS error unless the typecast parameter is enabled. If typecast is enabled, a new choice will be created if one does not exactly match. |
| Songwriter 4 Original Pub. 1                                    | `fldqbaFomnWoWwRwi` | Link to another record | Array of linked records IDs from the Publishers table.                           |
| Songwriter 4 Original Pub. 1 Share                              | `fldRxaAOwxMiq9hKG` | Percent                | Decimal number representing a percentage value. For example, the underlying cell value for 12.3% is 0.123. This field only allows positive numbers. |
| Songwriter 4 Admin Pub. 1                                       | `fldqXGTiRaLiF4ZKx` | Link to another record | Array of linked records IDs from the Publishers table.                           |
| Email (from Songwriter 4 Admin Pub. 1)                          | `fldbuuosV9OG539NU` | Lookup                 | Array of Email fields in linked Publishers records.                              |
| Address (from Songwriter 4 Admin Pub. 1)                        | `fldSB0rNIem3bpPiN` | Lookup                 | Array of Address fields in linked Publishers records.                            |
| Songwriter 4 Original Pub 2                                     | `fldgSXi7ij2SZGL28` | Link to another record | Array of linked records IDs from the Publishers table.                           |
| Songwriter 4 Original Pub 2 Share                               | `fldbJ3lCeOiTRrEbH` | Percent                | Decimal number representing a percentage value. For example, the underlying cell value for 12.3% is 0.123. This field only allows positive numbers. |
| Songwriter 4 Admin Pub. 2                                       | `fldmhqgbvPmw6OZZz` | Link to another record | Array of linked records IDs from the Publishers table.                           |
| Email (from Songwriter 4 Admin Pub. 2)                          | `fld6VWSTLWM73f60P` | Lookup                 | Array of Email fields in linked Publishers records.                              |
| Address (from Songwriter 4 Admin Pub. 2)                        | `fld6RUAtHxZGyo9MG` | Lookup                 | Array of Address fields in linked Publishers records.                            |
| Songwriter 5                                                    | `fld94WOrOzwY3ZZr4` | Link to another record | Array of linked records IDs from the Songwriters table.                          |
| Songwriter 5 Ownership                                          | `fldcPl10fIN2QCzQs` | Percent                | Decimal number representing a percentage value. For example, the underlying cell value for 12.3% is 0.123. This field only allows positive numbers. |
| Songwriter 5 Role                                               | `fldrwWbIA93TfKcYj` | Single select          | Selected option name. When creating or updating records, if the choice string does not exactly match an existing option, the request will fail with an INVALID_MULTIPLE_CHOICE_OPTIONS error unless the typecast parameter is enabled. If typecast is enabled, a new choice will be created if one does not exactly match. |
| Songwriter 5 Original Pub. 1                                    | `fldwZSHeismDTtoRm` | Link to another record | Array of linked records IDs from the Publishers table.                           |
| Songwriter 5 Original Pub 1 Share                               | `fld9kyPJFdX1BP4Qq` | Percent                | Decimal number representing a percentage value. For example, the underlying cell value for 12.3% is 0.123. This field only allows positive numbers. |
| Songwriter 5 Admin Pub 1                                        | `fldTBUGYFJFk2GA0k` | Link to another record | Array of linked records IDs from the Publishers table.                           |
| Email (from Songwriter 5 Admin Pub 1)                           | `fldHjL9fugVZfypap` | Lookup                 | Array of Email fields in linked Publishers records.                              |
| Address (from Songwriter 5 Admin Pub 1)                         | `fld8iqm9SgXThiXV5` | Lookup                 | Array of Address fields in linked Publishers records.                            |
| Songwriter 5 Original Pub 2                                     | `fldRnZsO4lwV3KZUI` | Link to another record | Array of linked records IDs from the Publishers table.                           |
| Songwriter 5 Original Pub 2 Share                               | `fldNT3ZnLcv0YWTcT` | Percent                | Decimal number representing a percentage value. For example, the underlying cell value for 12.3% is 0.123. This field only allows positive numbers. |
| Songwriter 5 Admin Pub. 2                                       | `fld6vKaTX4kahUg8Z` | Link to another record | Array of linked records IDs from the Publishers table.                           |
| Songwriter 6                                                    | `fldspvCZJR5LI2KMM` | Link to another record | Array of linked records IDs from the Songwriters table.                          |
| Songwriter 6 Ownership                                          | `fldmGV25Xmn52pOFk` | Percent                | Decimal number representing a percentage value. For example, the underlying cell value for 12.3% is 0.123. This field only allows positive numbers. |
| Songwriter 6 Role                                               | `fldi6f61AFXfQdDQc` | Single select          | Selected option name. When creating or updating records, if the choice string does not exactly match an existing option, the request will fail with an INVALID_MULTIPLE_CHOICE_OPTIONS error unless the typecast parameter is enabled. If typecast is enabled, a new choice will be created if one does not exactly match. |
| Songwriter 6 Original Pub 1                                     | `fldGo6i2jCDh3VWYM` | Link to another record | Array of linked records IDs from the Publishers table.                           |
| Songwriter 6 Original Pub. 1 Share                              | `fldTcZbo0OnEz2W35` | Percent                | Decimal number representing a percentage value. For example, the underlying cell value for 12.3% is 0.123. This field only allows positive numbers. |
| Songwriter 6 Admin Pub. 1                                       | `fldupwtvdkBPnmeUv` | Link to another record | Array of linked records IDs from the Publishers table.                           |
| Email (from Songwriter 6 Admin Pub. 1)                          | `fldJsfFMTnbIsVwSm` | Lookup                 | Array of Email fields in linked Publishers records.                              |
| Address (from Songwriter 6 Admin Pub. 1)                        | `fldqTMPuXXYfI2kxA` | Lookup                 | Array of Address fields in linked Publishers records.                            |
| Songwriter 6 Original Pub. 2                                    | `fldsff6W3SRZP94yZ` | Link to another record | Array of linked records IDs from the Publishers table.                           |
| Songwriter 6 Original Pub 2 Share                               | `flds3ZoHEQmF8BiiV` | Percent                | Decimal number representing a percentage value. For example, the underlying cell value for 12.3% is 0.123. This field only allows positive numbers. |
| Songwriter 6 Admin Pub. 2                                       | `fld7CY20AWkc1SIxL` | Link to another record | Array of linked records IDs from the Publishers table.                           |
| Songwriter 7                                                    | `fldd3R26JG9uqgw9P` | Link to another record | Array of linked records IDs from the Songwriters table.                          |
| Songwriter 7 Ownership                                          | `fldQUWOo35DLUH5n0` | Percent                | Decimal number representing a percentage value. For example, the underlying cell value for 12.3% is 0.123. This field only allows positive numbers. |
| Songwriter 7 Role                                               | `fldAItKGSrHOI3acu` | Single select          | Selected option name. When creating or updating records, if the choice string does not exactly match an existing option, the request will fail with an INVALID_MULTIPLE_CHOICE_OPTIONS error unless the typecast parameter is enabled. If typecast is enabled, a new choice will be created if one does not exactly match. |
| Songwriter 7 Original Pub. 1                                    | `fldVFyqtVZKZFDxUc` | Link to another record | Array of linked records IDs from the Publishers table.                           |
| Songwriter 7 Original Pub. 1 Share                              | `fldH8mlANOgZirTry` | Percent                | Decimal number representing a percentage value. For example, the underlying cell value for 12.3% is 0.123. This field only allows positive numbers. |
| Songwriter 7 Admin Pub. 1                                       | `fldsCeVEfrGptKpJc` | Link to another record | Array of linked records IDs from the Publishers table.                           |
| Songwriter 7 Original Pub. 2                                    | `fldazkIgA8HSKPFzf` | Link to another record | Array of linked records IDs from the Publishers table.                           |
| Songwriter 7 Original Pub. 2 Share                              | `fld9C5blDReVxqTA5` | Percent                | Decimal number representing a percentage value. For example, the underlying cell value for 12.3% is 0.123. This field only allows positive numbers. |
| Songwriter 7 Admin Pub. 2                                       | `fld5X2SFPOQxz3mmS` | Link to another record | Array of linked records IDs from the Publishers table.                           |
| Songwriter 8                                                    | `fldCtxeKcFoop5kpv` | Link to another record | Array of linked records IDs from the Songwriters table.                          |
| Songwriter 8 Ownership                                          | `fldF0cPRWx2Vj2LkO` | Percent                | Decimal number representing a percentage value. For example, the underlying cell value for 12.3% is 0.123. This field only allows positive numbers. |
| Songwriter 8 Role                                               | `fldZTovycBXkCEsnf` | Single select          | Selected option name. When creating or updating records, if the choice string does not exactly match an existing option, the request will fail with an INVALID_MULTIPLE_CHOICE_OPTIONS error unless the typecast parameter is enabled. If typecast is enabled, a new choice will be created if one does not exactly match. |
| Songwriter 8 Original Pub. 1                                    | `fldg4VsKIA2ABmEY7` | Link to another record | Array of linked records IDs from the Publishers table.                           |
| Songwriter 8 Original Pub. 1 Share                              | `fldV3wsYTeC80U9eW` | Percent                | Decimal number representing a percentage value. For example, the underlying cell value for 12.3% is 0.123. This field only allows positive numbers. |
| Songwriter 8 Admin Pub. 1                                       | `fld4Q0oVqasrLgOPZ` | Link to another record | Array of linked records IDs from the Publishers table.                           |
| Songwriter 8 Original Pub. 2                                    | `fldTo9U34nKjusDtc` | Link to another record | Array of linked records IDs from the Publishers table.                           |
| Songwriter 8 Original Pub. 2 Share                              | `fldZUnxSLNhQVqpT2` | Percent                | Decimal number representing a percentage value. For example, the underlying cell value for 12.3% is 0.123. This field only allows positive numbers. |
| Songwriter 8 Admin Pub. 2                                       | `flduz0piEiv2ES4Xi` | Link to another record | Array of linked records IDs from the Publishers table.                           |
| Songwriter 9                                                    | `fld3prOTF7TdS4cdj` | Link to another record | Array of linked records IDs from the Songwriters table.                          |
| Songwriter 9 Ownership                                          | `fldNRMQs43NLo7Vqy` | Percent                | Decimal number representing a percentage value. For example, the underlying cell value for 12.3% is 0.123. This field only allows positive numbers. |
| Songwriter 9 Role                                               | `fldOyDUgBJ6QaVtqc` | Single select          | Selected option name. When creating or updating records, if the choice string does not exactly match an existing option, the request will fail with an INVALID_MULTIPLE_CHOICE_OPTIONS error unless the typecast parameter is enabled. If typecast is enabled, a new choice will be created if one does not exactly match. |
| Songwriter 9 Original Pub. 1                                    | `fldPr6m9Tnf83vlJ0` | Link to another record | Array of linked records IDs from the Publishers table.                           |
| Songwriter 9 Original Pub. 1 Share                              | `fld02yPYOQFjZnSE6` | Percent                | Decimal number representing a percentage value. For example, the underlying cell value for 12.3% is 0.123. This field only allows positive numbers. |
| Songwriter 9 Admin Pub. 1                                       | `fldM8ji8hdvlOs2qX` | Link to another record | Array of linked records IDs from the Publishers table.                           |
| Songwriter 9 Original Pub. 2                                    | `fldqpQsw8XYay8Etm` | Link to another record | Array of linked records IDs from the Publishers table.                           |
| Songwriter 9 Original Pub. 2 Share                              | `fldnjAbT0VpICSyQX` | Percent                | Decimal number representing a percentage value. For example, the underlying cell value for 12.3% is 0.123. This field only allows positive numbers. |
| Songwriter 9 Admin Pub. 2                                       | `fldwqtEg520xFlCRz` | Link to another record | Array of linked records IDs from the Publishers table.                           |
| PRO Affiliation (from Songwriter 1)                             | `fldZpAplK0s7RpOcQ` | Lookup                 | Array of PRO Affiliation fields in linked Songwriters records.                   |
| IPI Number (from Songwriter 1)                                  | `fldUVUp6yVxCyP7Kj` | Lookup                 | Array of IPI Number fields in linked Songwriters records.                        |
| PRO Affiliation (from Songwriter 1 Original Pub. 1)             | `fldaVyfSSWqMoyb6C` | Lookup                 | Array of PRO Affiliation fields in linked Publishers records.                    |
| IPI/CAE Number (from Songwriter 1 Original Pub. 1)              | `fldOPpEeK8Ixpb7GC` | Lookup                 | Array of IPI/CAE Number fields in linked Publishers records.                     |
| Featured Artist (from Recordings)                               | `fldeI1ylIFh8CDeHi` | Lookup                 | Array of Featured Artist fields in linked Recordings records.                    |
| PRO Affiliation (from Songwriter 2)                             | `fld1y1SUwQnTraFga` | Lookup                 | Array of PRO Affiliation fields in linked Songwriters records.                   |
| IPI Number (from Songwriter 2)                                  | `fldhgeTSKSG8LnzZF` | Lookup                 | Array of IPI Number fields in linked Songwriters records.                        |
| PRO Affiliation (from Songwriter 2 Original Pub. 1)             | `fldsH4InPf44LKqFn` | Lookup                 | Array of PRO Affiliation fields in linked Publishers records.                    |
| IPI/CAE Number (from Songwriter 2 Original Pub. 1)              | `fldFXZjq9kZG6e9Qw` | Lookup                 | Array of IPI/CAE Number fields in linked Publishers records.                     |
| PRO Affiliation (from Songwriter 2 Original Pub. 2)             | `fldj0tfaWhUSV7Oha` | Lookup                 | Array of PRO Affiliation fields in linked Publishers records.                    |
| IPI/CAE Number (from Songwriter 2 Original Pub. 2)              | `fldPyQXMz0UUuXN04` | Lookup                 | Array of IPI/CAE Number fields in linked Publishers records.                     |
| PRO Affiliation (from Songwriter 3)                             | `fldYHZj7kClFnib8z` | Lookup                 | Array of PRO Affiliation fields in linked Songwriters records.                   |
| IPI Number (from Songwriter 3)                                  | `fldrywzlTAuEkZm7y` | Lookup                 | Array of IPI Number fields in linked Songwriters records.                        |
| PRO Affiliation (from Songwriter 3 Original Pub. 1)             | `fldmxjYuJBKaq8THm` | Lookup                 | Array of PRO Affiliation fields in linked Publishers records.                    |
| IPI/CAE Number (from Songwriter 3 Original Pub. 1)              | `fldTczYCRTz3XhEcR` | Lookup                 | Array of IPI/CAE Number fields in linked Publishers records.                     |
| PRO Affiliation (from Songwriter 4)                             | `fldzAIgH7JcKhq2xF` | Lookup                 | Array of PRO Affiliation fields in linked Songwriters records.                   |
| IPI Number (from Songwriter 4)                                  | `fldFHdc0gyxrvTjmb` | Lookup                 | Array of IPI Number fields in linked Songwriters records.                        |
| PRO Affiliation (from Songwriter 4 Original Pub.)               | `fldb28DI0h05M3YxJ` | Lookup                 | Array of PRO Affiliation fields in linked Publishers records.                    |
| IPI/CAE Number (from Songwriter 4 Original Pub.)                | `fldv0RdxqO8BLAdzA` | Lookup                 | Array of IPI/CAE Number fields in linked Publishers records.                     |
| PRO Affiliation (from Songwriter 5)                             | `fldIZVC6TDWeFsmE1` | Lookup                 | Array of PRO Affiliation fields in linked Songwriters records.                   |
| IPI Number (from Songwriter 5)                                  | `fld3Sxtjs0wwmonwD` | Lookup                 | Array of IPI Number fields in linked Songwriters records.                        |
| PRO Affiliation (from Songwriter 5 Original Pub.)               | `fldUf6pgQ69WTSPvQ` | Lookup                 | Array of PRO Affiliation fields in linked Publishers records.                    |
| IPI/CAE Number (from Songwriter 5 Original Pub.)                | `fldFHTtUptVn8QxVe` | Lookup                 | Array of IPI/CAE Number fields in linked Publishers records.                     |
| PRO Affiliation (from Songwriter 6)                             | `fldRFn0eQZZJtTylm` | Lookup                 | Array of PRO Affiliation fields in linked Songwriters records.                   |
| IPI Number (from Songwriter 6)                                  | `fldrrOqnyPscVXLo9` | Lookup                 | Array of IPI Number fields in linked Songwriters records.                        |
| PRO Affiliation (from Songwriter 6 Original Pub.)               | `fldNZ1kTvmwUJItYy` | Lookup                 | Array of PRO Affiliation fields in linked Publishers records.                    |
| IPI/CAE Number (from Songwriter 6 Original Pub.)                | `fldxJXDmgTo3eaJfP` | Lookup                 | Array of IPI/CAE Number fields in linked Publishers records.                     |
| PRO Affiliation (from Songwriter 7)                             | `fldak8wx4TeBZbDnP` | Lookup                 | Array of PRO Affiliation fields in linked Songwriters records.                   |
| IPI Number (from Songwriter 7)                                  | `fldchUbmHnPlnKtGi` | Lookup                 | Array of IPI Number fields in linked Songwriters records.                        |
| PRO Affiliation (from Songwriter 7 Original Pub.)               | `fldjwdGta3MveOiGx` | Lookup                 | Array of PRO Affiliation fields in linked Publishers records.                    |
| IPI/CAE Number (from Songwriter 7 Original Pub.)                | `fldK684XXyjvnE2xK` | Lookup                 | Array of IPI/CAE Number fields in linked Publishers records.                     |
| Controlled (from Songwriter 1 Original Pub. 1)                  | `fldJktT1FPSQyBrwD` | Lookup                 | Array of Controlled fields in linked Publishers records.                         |
| Controlled (from Songwriter 2 Original Pub. 1)                  | `fldl8vSiEmVTaHwTh` | Lookup                 | Array of Controlled fields in linked Publishers records.                         |
| Controlled (from Songwriter 1 Original Pub. 2)                  | `fldySuCEP7We7gqes` | Lookup                 | Array of Controlled fields in linked Publishers records.                         |
| PRO Affiliation (from Songwriter 1 Original Pub. 2)             | `fld4rzUIs0QP1VBHM` | Lookup                 | Array of PRO Affiliation fields in linked Publishers records.                    |
| IPI/CAE Number (from Songwriter 1 Original Pub. 2)              | `fldjzQgjRKrQQqZXD` | Lookup                 | Array of IPI/CAE Number fields in linked Publishers records.                     |
| Controlled (from Songwriter 1 Original Pub 3)                   | `fldPtyucbtgmFB2Q3` | Lookup                 | Array of Controlled fields in linked Publishers records.                         |
| PRO Affiliation (from Songwriter 1 Original Pub 3)              | `fldF06ZCm5Mr0iDVJ` | Lookup                 | Array of PRO Affiliation fields in linked Publishers records.                    |
| Controlled (from Songwriter 2 Original Pub. 2)                  | `fldClmLaMFg5ocfbw` | Lookup                 | Array of Controlled fields in linked Publishers records.                         |
| Controlled (from Songwriter 2 Original Pub. 3)                  | `fldqhdAlrV44Ge1qj` | Lookup                 | Array of Controlled fields in linked Publishers records.                         |
| PRO Affiliation (from Songwriter 2 Original Pub. 3)             | `fldWWXq8rIjWIWdxV` | Lookup                 | Array of PRO Affiliation fields in linked Publishers records.                    |
| IPI/CAE Number (from Songwriter 2 Original Pub. 3)              | `fldqfocP9ZOPgLwp8` | Lookup                 | Array of IPI/CAE Number fields in linked Publishers records.                     |
| Controlled (from Songwriter 3 Original Pub. 1)                  | `fldb0MhnCyRnl63FU` | Lookup                 | Array of Controlled fields in linked Publishers records.                         |
| Controlled (from Songwriter 3 Original Pub. 2)                  | `fldfvzzrZUi6d0dCC` | Lookup                 | Array of Controlled fields in linked Publishers records.                         |
| PRO Affiliation (from Songwriter 3 Original Pub. 2)             | `fld75btrRxj3FMbHz` | Lookup                 | Array of PRO Affiliation fields in linked Publishers records.                    |
| IPI/CAE Number (from Songwriter 3 Original Pub. 2)              | `fldmAOyXOnPACQj3Q` | Lookup                 | Array of IPI/CAE Number fields in linked Publishers records.                     |
| IPI/CAE Number (from Songwriter 1 Original Pub 3)               | `fldsU3nry63zKgf5B` | Lookup                 | Array of IPI/CAE Number fields in linked Publishers records.                     |
| Controlled (from Songwriter 4 Original Pub. 1)                  | `fldIhr8g0BUZ9ZCnB` | Lookup                 | Array of Controlled fields in linked Publishers records.                         |
| PRO Affiliation (from Songwriter 4 Original Pub 2)              | `fld9v9sXRHUxhDLSp` | Lookup                 | Array of PRO Affiliation fields in linked Publishers records.                    |
| IPI/CAE Number (from Songwriter 4 Original Pub 2)               | `fldPCBNaijdtTI6JA` | Lookup                 | Array of IPI/CAE Number fields in linked Publishers records.                     |
| Box Spreadsheet (from Releases)                                 | `fldxNglrwk777jG3p` | Lookup                 | Array of Box Spreadsheet fields in linked Releases records.                      |
| Controlled (from Songwriter 4 Original Pub 2)                   | `fldTrq8syNb9canOr` | Lookup                 | Array of Controlled fields in linked Publishers records.                         |
| Controlled (from Songwriter 5 Original Pub. 1)                  | `fldqkDZvegpEQ2Kgf` | Lookup                 | Array of Controlled fields in linked Publishers records.                         |
| Controlled (from Songwriter 5 Original Pub. 2)                  | `fldD2jQbeBVKG3YR4` | Lookup                 | Array of Controlled fields in linked Publishers records.                         |
| PRO Affiliation (from Songwriter 5 Original Pub. 2)             | `fldTGLWugJYgoOK5U` | Lookup                 | Array of PRO Affiliation fields in linked Publishers records.                    |
| IPI/CAE Number (from Songwriter 5 Original Pub. 2)              | `fldQE9uEOw4cYuRy9` | Lookup                 | Array of IPI/CAE Number fields in linked Publishers records.                     |
| Controlled (from Songwriter 6 Original Pub. 1)                  | `fldpv4XdcVzHHGotT` | Lookup                 | Array of Controlled fields in linked Publishers records.                         |
| Controlled (from Songwriter 6 Original Pub. 2)                  | `fldURLSPxMOkcTAF2` | Lookup                 | Array of Controlled fields in linked Publishers records.                         |
| PRO Affiliation (from Songwriter 6 Original Pub. 2)             | `fldN6AJhMESt1XUpE` | Lookup                 | Array of PRO Affiliation fields in linked Publishers records.                    |
| IPI/CAE Number (from Songwriter 6 Original Pub. 2)              | `fldm6NAVvKfbjh5na` | Lookup                 | Array of IPI/CAE Number fields in linked Publishers records.                     |
| Controlled (from Songwriter 7 Original Pub. 1)                  | `fldV4cNP6O3op9HXL` | Lookup                 | Array of Controlled fields in linked Publishers records.                         |
| Controlled (from Songwriter 7 Original Pub. 2)                  | `fld79XiBuNrixCWkW` | Lookup                 | Array of Controlled fields in linked Publishers records.                         |
| PRO Affiliation (from Songwriter 7 Original Pub. 2)             | `fldfv11ObHYZPqxP4` | Lookup                 | Array of PRO Affiliation fields in linked Publishers records.                    |
| IPI/CAE Number (from Songwriter 7 Original Pub. 2)              | `fldBTgR7IrdL0Beg0` | Lookup                 | Array of IPI/CAE Number fields in linked Publishers records.                     |
| PRO Affiliation (from Songwriter 8)                             | `fldKv3aQB3IUpLjZ5` | Lookup                 | Array of PRO Affiliation fields in linked Songwriters records.                   |
| IPI Number (from Songwriter 8)                                  | `fld9JMRRVmKiVVS0q` | Lookup                 | Array of IPI Number fields in linked Songwriters records.                        |
| Controlled (from Songwriter 8 Original Pub. 1)                  | `fldBGq21mnjSaTOko` | Lookup                 | Array of Controlled fields in linked Publishers records.                         |
| PRO Affiliation (from Songwriter 8 Original Pub. 1)             | `fldbIeO6X5ECJ6HA5` | Lookup                 | Array of PRO Affiliation fields in linked Publishers records.                    |
| IPI/CAE Number (from Songwriter 8 Original Pub. 1)              | `fldoztvhwEcQAxrzc` | Lookup                 | Array of IPI/CAE Number fields in linked Publishers records.                     |
| Controlled (from Songwriter 8 Original Pub. 2)                  | `fld3cFxRmvm9xzCbU` | Lookup                 | Array of Controlled fields in linked Publishers records.                         |
| PRO Affiliation (from Songwriter 8 Original Pub. 2)             | `fldk5m3Y3CU3VBrH2` | Lookup                 | Array of PRO Affiliation fields in linked Publishers records.                    |
| IPI/CAE Number (from Songwriter 8 Original Pub. 2)              | `fld0lAGDHMXuQOo3p` | Lookup                 | Array of IPI/CAE Number fields in linked Publishers records.                     |
| PRO Affiliation (from Songwriter 9)                             | `fldgDPGjZuJ8jOxEL` | Lookup                 | Array of PRO Affiliation fields in linked Songwriters records.                   |
| IPI Number (from Songwriter 9)                                  | `fldKbnh7YZF3bApkf` | Lookup                 | Array of IPI Number fields in linked Songwriters records.                        |
| Controlled (from Songwriter 9 Original Pub. 1)                  | `fld1e0mq4sL9UnZaT` | Lookup                 | Array of Controlled fields in linked Publishers records.                         |
| PRO Affiliation (from Songwriter 9 Original Pub. 1)             | `fldp364WYVkTyO195` | Lookup                 | Array of PRO Affiliation fields in linked Publishers records.                    |
| IPI/CAE Number (from Songwriter 9 Original Pub. 1)              | `fldd07rtpQP1sJgN7` | Lookup                 | Array of IPI/CAE Number fields in linked Publishers records.                     |
| Controlled (from Songwriter 9 Original Pub. 2)                  | `fld4ITQVARHrvCTQe` | Lookup                 | Array of Controlled fields in linked Publishers records.                         |
| PRO Affiliation (from Songwriter 9 Original Pub. 2)             | `fldxVPdyalvC18WtA` | Lookup                 | Array of PRO Affiliation fields in linked Publishers records.                    |
| IPI/CAE Number (from Songwriter 9 Original Pub. 2)              | `fld1YUpRBaoe1duaY` | Lookup                 | Array of IPI/CAE Number fields in linked Publishers records.                     |
| Controlled (from Songwriter 1 Original Pub 4)                   | `fld2Q6xn4XYDJvK7s` | Lookup                 | Array of Controlled fields in linked Publishers records.                         |
| PRO Affiliation (from Songwriter 1 Original Pub 4)              | `fldlg5jKyjX2UeHIG` | Lookup                 | Array of PRO Affiliation fields in linked Publishers records.                    |
| IPI/CAE Number (from Songwriter 1 Original Pub 4)               | `fldXfUSgn4QZ3LKhW` | Lookup                 | Array of IPI/CAE Number fields in linked Publishers records.                     |
| Controlled (from Songwriter 2 Original Pub 4)                   | `fldOc8soymVNUt888` | Lookup                 | Array of Controlled fields in linked Publishers records.                         |
| PRO Affiliation (from Songwriter 2 Original Pub 4)              | `fldb8BhQ5AEbsE3FZ` | Lookup                 | Array of PRO Affiliation fields in linked Publishers records.                    |
| IPI/CAE Number (from Songwriter 2 Original Pub 4)               | `fldDAE1u56iBXkoUJ` | Lookup                 | Array of IPI/CAE Number fields in linked Publishers records.                     |
| REGISTRATION PROJECT (PRO +MLC) copy                            | `fldYnDMpmxRN1vBeQ` | Text                   | A single line of text.                                                           |
| Recordings 2                                                    | `fldxWNmJpXpvsObEg` | Link to another record | Array of linked records IDs from the Recordings table.                           |
| Releases 2                                                      | `fldQlJmvFWq4ipS17` | Link to another record | Array of linked records IDs from the Releases table.                             |
| Release Date (from Releases 2)                                  | `fldlNWy5sLA4YHzjK` | Lookup                 | Array of Release Date fields in linked Releases records.                         |
| Releases 3                                                      | `fldF908RO6LCB39D5` | Link to another record | Array of linked records IDs from the Releases table.                             |
| Recordings (from Releases 3)                                    | `fldjzsZvJd1yTWudx` | Lookup                 | Array of Recordings fields in linked Releases records.                           |
| Release Date (from Releases 3)                                  | `fldYDKLUSWQJylLXA` | Lookup                 | Array of Release Date fields in linked Releases records.                         |
| Release Title (from Releases 3)                                 | `fldE0hfQZUoiDePU4` | Lookup                 | Array of Release Title fields in linked Releases records.                        |
| Recordings 3                                                    | `fldYObdWITjl5fAAO` | Link to another record | Array of linked records IDs from the Recordings table.                           |
| Controlled by HFA (from Songwriter 1 Original Pub 1)            | `fldN5aPWhP55kgX3s` | Lookup                 | Array of Controlled by HFA fields in linked Publishers records.                  |
| Controlled by HFA (from Songwriter 1 Admin Pub 1)               | `fld4DKw7zdAJZGe2T` | Lookup                 | Array of Controlled by HFA fields in linked Publishers records.                  |
| Controlled by HFA (from Songwriter 1 Original Pub 2)            | `fldPT7BEHId5wNzJG` | Lookup                 | Array of Controlled by HFA fields in linked Publishers records.                  |
| Controlled by HFA (from Songwriter 1 Admin Pub 2)               | `fldS4xQXLj1tKxmGH` | Lookup                 | Array of Controlled by HFA fields in linked Publishers records.                  |
| Controlled by HFA (from Songwriter 2 Original Pub. 1)           | `fldgDqd3sKA5jdGKT` | Lookup                 | Array of Controlled by HFA fields in linked Publishers records.                  |
| Controlled by HFA (from Songwriter 2 Admin Pub 1)               | `fld6WbYUVRNt7nw69` | Lookup                 | Array of Controlled by HFA fields in linked Publishers records.                  |
| Controlled by HFA (from Songwriter 2 Original Pub. 2)           | `fldo3J7VccQiNP5Fd` | Lookup                 | Array of Controlled by HFA fields in linked Publishers records.                  |
| Controlled by HFA (from Songwriter 2 Admin Pub. 2)              | `fldyJsiEKxkCSZhxE` | Lookup                 | Array of Controlled by HFA fields in linked Publishers records.                  |
| Controlled by HFA (from Songwriter 3 Original Pub. 1)           | `fldKZkuyGDZ543HJi` | Lookup                 | Array of Controlled by HFA fields in linked Publishers records.                  |
| Controlled by HFA (from Songwriter 3 Admin Pub. 1)              | `fld1pWUO1LKNhOkgz` | Lookup                 | Array of Controlled by HFA fields in linked Publishers records.                  |
| Controlled by HFA (from Songwriter 3 Original Pub. 2)           | `fldrZqvXVvzpX1e44` | Lookup                 | Array of Controlled by HFA fields in linked Publishers records.                  |
| Controlled by HFA (from Songwriter 3 Admin Pub. 2)              | `fldnbUCHZ2LoILIkc` | Lookup                 | Array of Controlled by HFA fields in linked Publishers records.                  |
| Controlled by HFA (from Songwriter 4 Original Pub. 1)           | `fldugZiK0H2MZRPGQ` | Lookup                 | Array of Controlled by HFA fields in linked Publishers records.                  |
| Controlled by HFA (from Songwriter 4 Admin Pub. 1)              | `fldacIAYuLTMjoGTt` | Lookup                 | Array of Controlled by HFA fields in linked Publishers records.                  |
| Controlled by HFA (from Songwriter 4 Original Pub 2)            | `fldQudEQaBHDOBCwF` | Lookup                 | Array of Controlled by HFA fields in linked Publishers records.                  |
| Controlled by HFA (from Songwriter 4 Admin Pub. 2)              | `flduW59GMKsVyqIVL` | Lookup                 | Array of Controlled by HFA fields in linked Publishers records.                  |
| SoT Transition Status                                           | `fldBIeO6MbeeCKGRx` | Multiple select        | Array of selected option names. When creating or updating records, if a choice string does not exactly match an existing option, the request will fail with an INVALID_MULTIPLE_CHOICE_OPTIONS error unless the typecast parameter is enabled. If typecast is enabled, a new choice will be created if one does not exactly match. |
| Legal Docs                                                      | `fldh0MvKdlr37yU6N` | Link to another record | Array of linked records IDs from the Legal Docs table.                           |

---

## List Records

**Endpoint:** `GET /v0/appEurfA8kXQE3slK/compositions`

To list records in Compositions , issue a GET request to the Compositions endpoint. Note that table names and table ids can be used interchangeably. Using table ids means table name changes do not require modifications to your API request.

Returned records do not include any fields with "empty" values, e.g. "" , [] , or false .

```bash
curl "https://api.airtable.com/v0/appEurfA8kXQE3slK/Compositions?maxRecords=3&view=When%20You%20Wish%20-%20ASCAP%20Registration" \
  -H "Authorization: Bearer YOUR_SECRET_API_TOKEN"
```

### Query Parameters

| Parameter               | Type             | Required   | Description                                                                      |
| ----------------------- | ---------------- | ---------- | -------------------------------------------------------------------------------- |
| `fields`                | array of strings | optional   | Only data for fields whose names are in this list will be included in the result. If you don't need every field, you can use this parameter to reduce the amount of data transferred. For example, to only return data from Song Title In PRO and Notes , send these two query parameters: fields%5B%5D=Song |
| `filterByFormula`       | string           | optional   | A formula used to filter records. The formula will be evaluated for each record, and if the result is not 0 , false , "" , NaN , [] , or #Error! the record will be included in the response. We recommend testing your formula in the Formula field UI before using it in your API request. If combined wit |
| `maxRecords`            | number           | optional   | The maximum total number of records that will be returned in your requests. If this value is larger than pageSize (which is 100 by default), you may have to load multiple pages to reach this total. See the Pagination section below for more. |
| `pageSize`              | number           | optional   | The number of records returned in each request. Must be less than or equal to 100. Default is 100. See the Pagination section below for more. |
| `sort`                  | array of objects | optional   | A list of sort objects that specifies how the records will be ordered. Each sort object must have a field key specifying the name of the field to sort on, and an optional direction key that is either "asc" or "desc" . The default direction is "asc" . The sort parameter overrides the sorting of the v |
| `view`                  | string           | optional   | The name or ID of a view in the Compositions table. If set, only the records in that view will be returned. The records will be sorted according to the order of the view unless the sort parameter is included, which overrides that order. Fields hidden in this view will be returned in the results. To |
| `cellFormat`            | string           | optional   | The format that should be used for cell values. Supported values are: json : cells will be formatted as JSON, depending on the field type. string : cells will be formatted as user-facing strings, regardless of the field type. The timeZone and userLocale parameters are required when using string as t |
| `timeZone`              | string           | optional   | The time zone that should be used to format dates when using string as the cellFormat . This parameter is required when using string as the cellFormat . |
| `userLocale`            | string           | optional   | The user locale that should be used to format dates when using string as the cellFormat . This parameter is required when using string as the cellFormat . |
| `returnFieldsByFieldId` | boolean          | optional   | An optional boolean value that lets you return field objects where the key is the field id. This defaults to false , which returns field objects where the key is the field name. |
| `recordMetadata`        | array of strings | optional   | An optional field that, if includes commentCount , adds a commentCount read only property on each record returned. |

---

## Retrieve a Record

**Endpoint:** `GET /v0/appEurfA8kXQE3slK/compositions`

To retrieve an existing record in Compositions table, issue a GET request to the record endpoint.

Any "empty" fields (e.g. "" , [] , or false ) in the record will not be returned.

```bash
curl https://api.airtable.com/v0/appEurfA8kXQE3slK/Compositions/recpfoXpd6eXqejHT \
  -H "Authorization: Bearer YOUR_SECRET_API_TOKEN"
```

---

## Create Records

**Endpoint:** `POST /v0/appEurfA8kXQE3slK/compositions`

To create new records, issue a POST request to the Compositions endpoint. Note that table names and table ids can be used interchangeably. Using table ids means table name changes do not require modifications to your API request.

Your request body should include an array of up to 10 record objects. Each of these objects should have one key whose value is an inner object containing your record's cell values, keyed by either field name or field id.

```bash
curl -X POST https://api.airtable.com/v0/appEurfA8kXQE3slK/Compositions \
  -H "Authorization: Bearer YOUR_SECRET_API_TOKEN" \
  -H "Content-Type: application/json" \
  --data '{
  "records": [
    {
      "fields": {
        "Song Title In PRO": "5 10 15 HOURS",
        "ISWC": "T0709409551\n",
        "Recordings": [
          "recrrRaUSA1Ylwao0",
          "recpYSxdWCSj7g6i4"
        ],
        "All Songwriters": [
          "recjwnR93dvVoDEzf"
        ],
        "All Original Publishers": [
          "recf9b8XcWWtNVbzq"
        ],
        "All Admin Publishers": [
          "rectT66YlZP9naK6B"
        ],
        "Involved PROs": [
          "BMI"
        ],
        "Songwriter 1": [
          "recjwnR93dvVoDEzf"
        ],
        "Songwriter 1 Share": 1,
        "Songwriter 1 Role": [
          "Composer"
        ],
        "Songwriter 1 Original Pub 1": [
          "recf9b8XcWWtNVbzq"
        ],
        "Songwriter 1 Original Pub 1 Share": 1,
        "Songwriter 1 Admin Pub 1": [
          "rectT66YlZP9naK6B"
        ]
      }
    },
    {
      "fields": {
        "Song Title In PRO": "A B C CHEVY THEME",
        "Notes": "ASCAP Work ID: 310000110",
        "ISWC": "T0700000527",
        "All Songwriters": [
          "rech43fjOfIJh8XJt"
        ],
        "Songwriter 1": [
          "rech43fjOfIJh8XJt"
        ],
        "Songwriter 1 Share": 1,
        "Songwriter 1 Original Pub 1": [
          "recpbxExDaBhGyWkS"
        ],
        "Songwriter 1 Original Pub 1 Share": 1
      }
    }
  ]
}'
```

---

## Update / Upsert Records

**Endpoint:** `PATCH /v0/appEurfA8kXQE3slK/compositions`

To update Compositions records, issue a request to the Compositions endpoint. Table names and table IDs can be used interchangeably. Using table IDs means table name changes won't require modifying your API request code. A PATCH request will only update the fields included in the request. Fields not included in the request will be unchanged. A PUT request will perform a destructive update and clear all unincluded cell values.

Your request body should include an array of up to 10 record objects. Each of these objects should have an id property representing the record ID and a fields property which contains all of your record's cell values by field name or field id for all of your record's cell values by field name.

```bash
curl -X PATCH https://api.airtable.com/v0/appEurfA8kXQE3slK/Compositions \
  -H "Authorization: Bearer YOUR_SECRET_API_TOKEN" \
  -H "Content-Type: application/json" \
  --data '{
  "records": [
    {
      "id": "recpfoXpd6eXqejHT",
      "fields": {
        "Song Title In PRO": "5 10 15 HOURS",
        "ISWC": "T0709409551\n",
        "Recordings": [
          "recrrRaUSA1Ylwao0",
          "recpYSxdWCSj7g6i4"
        ],
        "All Songwriters": [
          "recjwnR93dvVoDEzf"
        ],
        "All Original Publishers": [
          "recf9b8XcWWtNVbzq"
        ],
        "All Admin Publishers": [
          "rectT66YlZP9naK6B"
        ],
        "Involved PROs": [
          "BMI"
        ],
        "Songwriter 1": [
          "recjwnR93dvVoDEzf"
        ],
        "Songwriter 1 Share": 1,
        "Songwriter 1 Role": [
          "Composer"
        ],
        "Songwriter 1 Original Pub 1": [
          "recf9b8XcWWtNVbzq"
        ],
        "Songwriter 1 Original Pub 1 Share": 1,
        "Songwriter 1 Admin Pub 1": [
          "rectT66YlZP9naK6B"
        ]
      }
    },
    {
      "id": "rec2XT7Snrjqjz6Lk",
      "fields": {
        "Song Title In PRO": "A B C CHEVY THEME",
        "Notes": "ASCAP Work ID: 310000110",
        "ISWC": "T0700000527",
        "All Songwriters": [
          "rech43fjOfIJh8XJt"
        ],
        "Songwriter 1": [
          "rech43fjOfIJh8XJt"
        ],
        "Songwriter 1 Share": 1,
        "Songwriter 1 Original Pub 1": [
          "recpbxExDaBhGyWkS"
        ],
        "Songwriter 1 Original Pub 1 Share": 1
      }
    },
    {
      "id": "rec7gRiSnrewh609G",
      "fields": {
        "Song Title In PRO": "A CONCERTO FOR CHOPSTICKS ",
        "Notes": "Public Domain work: https://en.wikipedia.org/wiki/Chopsticks_(waltz)\nComposer: Euphemia Allen",
        "Recordings": [
          "rechetrnVRLHCZte5"
        ],
        "Date of First Use": "1877",
        "PD Work Status": "Arrangement of Original PD Work",
        "Uncredited PD Writers": "Euphemia Allen"
      }
    }
  ]
}'
```

---

## Delete Records

**Endpoint:** `DELETE /v0/appEurfA8kXQE3slK/compositions`

To delete Compositions records, issue a DELETE request to the Compositions endpoint. Note that table names and table ids can be used interchangeably. Using table ids means table name changes do not require modifications to your API request.

Your request should include a URL-encoded array of up to 10 record IDs to delete.

```bash
curl -X DELETE https://api.airtable.com/v0/appEurfA8kXQE3slK/Compositions \
  -H "Authorization: Bearer YOUR_SECRET_API_TOKEN" \
  -G \
  --data-urlencode 'records[]=recpfoXpd6eXqejHT' \
  --data-urlencode 'records[]=rec2XT7Snrjqjz6Lk'
```

