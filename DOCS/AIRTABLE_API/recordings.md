# Recordings

**Table ID:** `tblESvQQmOBbEXAH0`  
**Base ID:** `appEurfA8kXQE3slK`

---

## Fields

| Field Name                                                                 | Field ID            | Type                   | Description                                                                      |
| -------------------------------------------------------------------------- | ------------------- | ---------------------- | -------------------------------------------------------------------------------- |
| Title of Recording                                                         | `fldFslc4FKUDcfuk6` | Text                   | A single line of text.                                                           |
| ISRC                                                                       | `fldNDD3nkxYymArNx` | Text                   | A single line of text.                                                           |
| Missing songwriter on Spotify                                              | `fldRu6itZWVfd6XF9` | Single select          | Selected option name. When creating or updating records, if the choice string does not exactly match an existing option, the request will fail with an INVALID_MULTIPLE_CHOICE_OPTIONS error unless the typecast parameter is enabled. If typecast is enabled, a new choice will be created if one does not exactly match. |
| All Releases                                                               | `fld57hhrA0PBM88o6` | Link to another record | Array of linked records IDs from the Releases table. Because this field is configured to show records in reversed order, the order of records in the app will be reversed compared to what you see here. |
| Producer                                                                   | `fldOjjRaAHh1Aq557` | Multiple select        | Array of selected option names. When creating or updating records, if a choice string does not exactly match an existing option, the request will fail with an INVALID_MULTIPLE_CHOICE_OPTIONS error unless the typecast parameter is enabled. If typecast is enabled, a new choice will be created if one does not exactly match. |
| All Songwriters (from Compositions)                                        | `fldiDU0dYFZvCXTcK` | Lookup                 | Array of All Songwriters fields in linked Compositions records.                  |
| Compositions                                                               | `fldEAl8K8Sn0gvC98` | Link to another record | Array of linked records IDs from the Compositions table.                         |
| Master Owner 1                                                             | `fldMKw9veaxGqmWJy` | Link to another record | Array of linked records IDs from the Master Owners table.                        |
| Master 1 Ownership                                                         | `fldh8WlYjYZiOLvJp` | Percent                | Decimal number representing a percentage value. For example, the underlying cell value for 12.3% is 0.123. This field only allows positive numbers. |
| Master Owner 2                                                             | `fldtEeYpvscGJUiCf` | Link to another record | Array of linked records IDs from the Master Owners table.                        |
| Master 2 Ownership                                                         | `fldaULVlFMeGcBolS` | Percent                | Decimal number representing a percentage value. For example, the underlying cell value for 12.3% is 0.123. This field only allows positive numbers. |
| Spotify                                                                    | `fldPGiI1VFfdgZ0g3` | URL                    | A valid URL (e.g. airtable.com or https://airtable.com/universe).                |
| REGISTRATION PROJECT (SOUNDEXCHANGE) 3                                     | `fldvX8g1YQ40aEtW4` | Link to another record | Array of linked records IDs from the REGISTRATION PROJECT (SOUNDEXCHANGE) table. |
| Notes                                                                      | `fldQhFmxq7UKipROI` | Long text              | Multiple lines of text, which may contain "mention tokens", e.g. <airtable:mention id="menE1i9oBaGX3DseR">@Alex</airtable:mention> |
| PBGL Owned                                                                 | `fldtZw9RzXJesBdJa` | Checkbox               | This field is "true" when checked and otherwise empty.                           |
| SX (Rights Owner) (from REGISTRATION PROJECT (SOUNDEXCHANGE) 3)            | `fldeC3JotTgNKVsnn` | Lookup                 | Array of SX (Rights Owner) fields in linked REGISTRATION PROJECT (SOUNDEXCHANGE) records. |
| SX (Artist) (from REGISTRATION PROJECT (SOUNDEXCHANGE) 3)                  | `fldgeSBWuvxlwenhH` | Lookup                 | Array of SX (Artist) fields in linked REGISTRATION PROJECT (SOUNDEXCHANGE) records. |
| Distributed (from All Releases)                                            | `fldKiC3WFIx6nTkdl` | Lookup                 | Array of Distributed fields in linked Releases records.                          |
| Primary Artist                                                             | `fld9vMhhhV6aAZPZP` | Link to another record | Array of linked records IDs from the Artists table.                              |
| Featured Artist                                                            | `fldr6WmY3lmlfnTrb` | Link to another record | Array of linked records IDs from the Artists table.                              |
| Master Owner 3                                                             | `fldEw8iScPnOFWTx0` | Link to another record | Array of linked records IDs from the Master Owners table.                        |
| Master 3 Ownership                                                         | `fldjWbcozdEZOQkPU` | Percent                | Decimal number representing a percentage value. For example, the underlying cell value for 12.3% is 0.123. This field only allows positive numbers. |
| Original Release                                                           | `fldV2X7dziu3HDfw8` | Link to another record | Array of linked records IDs from the Releases table.                             |
| Master                                                                     | `fldxPAO3UZMI4QJal` | URL                    | A valid URL (e.g. airtable.com or https://airtable.com/universe).                |
| Date of original Release                                                   | `fldbDhB8zzWzv8zIu` | Date                   | UTC date, e.g. "2014-09-05".                                                     |
| Original recording title                                                   | `fldM5OsIrFiwyAUmP` | Text                   | A single line of text.                                                           |
| Tempo Tag                                                                  | `fldBQ2uBIgfrvGO4g` | Single select          | Selected option name. When creating or updating records, if the choice string does not exactly match an existing option, the request will fail with an INVALID_MULTIPLE_CHOICE_OPTIONS error unless the typecast parameter is enabled. If typecast is enabled, a new choice will be created if one does not exactly match. |
| Mood Tag                                                                   | `fldGLPgeMuyCdFVI8` | Multiple select        | Array of selected option names. When creating or updating records, if a choice string does not exactly match an existing option, the request will fail with an INVALID_MULTIPLE_CHOICE_OPTIONS error unless the typecast parameter is enabled. If typecast is enabled, a new choice will be created if one does not exactly match. |
| Genre Tag                                                                  | `fldh4NuUtNapRJFUL` | Multiple select        | Array of selected option names. When creating or updating records, if a choice string does not exactly match an existing option, the request will fail with an INVALID_MULTIPLE_CHOICE_OPTIONS error unless the typecast parameter is enabled. If typecast is enabled, a new choice will be created if one does not exactly match. |
| Vocal Tag                                                                  | `flduQlucxqef6NlbK` | Multiple select        | Array of selected option names. When creating or updating records, if a choice string does not exactly match an existing option, the request will fail with an INVALID_MULTIPLE_CHOICE_OPTIONS error unless the typecast parameter is enabled. If typecast is enabled, a new choice will be created if one does not exactly match. |
| Instruments Tag                                                            | `fldfoMMkxh7IWfuW6` | Multiple select        | Array of selected option names. When creating or updating records, if a choice string does not exactly match an existing option, the request will fail with an INVALID_MULTIPLE_CHOICE_OPTIONS error unless the typecast parameter is enabled. If typecast is enabled, a new choice will be created if one does not exactly match. |
| Lyrical Theme Tag                                                          | `fldd0VUazaZ0umpSv` | Multiple select        | Array of selected option names. When creating or updating records, if a choice string does not exactly match an existing option, the request will fail with an INVALID_MULTIPLE_CHOICE_OPTIONS error unless the typecast parameter is enabled. If typecast is enabled, a new choice will be created if one does not exactly match. |
| Duration                                                                   | `fldcILmBh0XXuJCPs` | Duration               | An integer representing number of seconds. This field allows negative and positive numbers. |
| DISCO                                                                      | `fldaeSYMSXiBd6yKe` | URL                    | A valid URL (e.g. airtable.com or https://airtable.com/universe).                |
| UPC (from Releases)                                                        | `fldJL8W8wi9PgnRmG` | Lookup                 | Array of UPC fields in linked Releases records.                                  |
| BPM                                                                        | `fldhfKrj6VzUWwzkb` | Number                 | A decimal number showing 1 decimal digit. This field only allows positive numbers. |
| Apple Music                                                                | `fldpjXyMfeCDz0sDj` | URL                    | A valid URL (e.g. airtable.com or https://airtable.com/universe).                |
| YouTube Music                                                              | `fldQRVCKtiQmHASbO` | URL                    | A valid URL (e.g. airtable.com or https://airtable.com/universe).                |
| Soundcloud                                                                 | `fldSgqIszkWHqLiHy` | URL                    | A valid URL (e.g. airtable.com or https://airtable.com/universe).                |
| Amazon Music                                                               | `fldY1Mm5szTZhg7Dp` | URL                    | A valid URL (e.g. airtable.com or https://airtable.com/universe).                |
| Released (from All Releases)                                               | `fldB3jbtTOcXKSiTo` | Lookup                 | Array of Released fields in linked Releases records.                             |
| Original release label (from Original release)                             | `fldboU3YZUpCCcwOK` | Lookup                 | Array of Original release label fields in linked Releases records.               |
| Era                                                                        | `fldMznuTwRCIKPhEl` | Single select          | Selected option name. When creating or updating records, if the choice string does not exactly match an existing option, the request will fail with an INVALID_MULTIPLE_CHOICE_OPTIONS error unless the typecast parameter is enabled. If typecast is enabled, a new choice will be created if one does not exactly match. |
| Ready for Sync                                                             | `fld6XX8N0G5WLM2Pz` | Single select          | Selected option name. When creating or updating records, if the choice string does not exactly match an existing option, the request will fail with an INVALID_MULTIPLE_CHOICE_OPTIONS error unless the typecast parameter is enabled. If typecast is enabled, a new choice will be created if one does not exactly match. |
| Lyric Sheet                                                                | `fld0vvx3V1uScenIn` | URL                    | A valid URL (e.g. airtable.com or https://airtable.com/universe).                |
| Type Tag                                                                   | `fldrjwgYHIbj2mkw9` | Multiple select        | Array of selected option names. When creating or updating records, if a choice string does not exactly match an existing option, the request will fail with an INVALID_MULTIPLE_CHOICE_OPTIONS error unless the typecast parameter is enabled. If typecast is enabled, a new choice will be created if one does not exactly match. |
| Current release label (from Original Release)                              | `fldCDfGQPzGHEtpsM` | Lookup                 | Array of Current release label fields in linked Releases records.                |
| Recording year                                                             | `fldjJOfSCUpvryUwF` | Text                   | A single line of text.                                                           |
| Status                                                                     | `fldj3fMbU5zOZgyf3` | Multiple select        | Array of selected option names. When creating or updating records, if a choice string does not exactly match an existing option, the request will fail with an INVALID_MULTIPLE_CHOICE_OPTIONS error unless the typecast parameter is enabled. If typecast is enabled, a new choice will be created if one does not exactly match. |
| Priority                                                                   | `fldm7nqe1sTAoR2Pi` | Single select          | Selected option name. When creating or updating records, if the choice string does not exactly match an existing option, the request will fail with an INVALID_MULTIPLE_CHOICE_OPTIONS error unless the typecast parameter is enabled. If typecast is enabled, a new choice will be created if one does not exactly match. |
| Verified Info (from Compositions)                                          | `flddLlV4VjmxZafUl` | Lookup                 | Array of Verified Info fields in linked Compositions records.                    |
| Notes (from Compositions)                                                  | `fldJyzFef2mf0oBLY` | Lookup                 | Array of Notes fields in linked Compositions records.                            |
| Original PD Work Title (from Compositions)                                 | `fldFNG8EdKA6ycmxP` | Lookup                 | Array of Original PD Work Title fields in linked Compositions records.           |
| PD Work Status (from Compositions)                                         | `fldQzYc2ncCXqOGza` | Lookup                 | Array of PD Work Status fields in linked Compositions records.                   |
| Production Title (from Compositions)                                       | `fldQwwHhLPBnqaiu6` | Lookup                 | Array of Production Title fields in linked Compositions records.                 |
| Intended Purpose (from Compositions)                                       | `fldtYhu7ttbdaOhHg` | Lookup                 | Array of Intended Purpose fields in linked Compositions records.                 |
| Date of First Use (from Compositions)                                      | `fldvoDRJBnjxhNVfN` | Lookup                 | Array of Date of First Use fields in linked Compositions records.                |
| ISWC (from Compositions)                                                   | `fldu2832uigj0Cj7b` | Lookup                 | Array of ISWC fields in linked Compositions records.                             |
| Published by PBGL                                                          | `fldRUN9gqcFDqezp8` | Lookup                 | Array of Controlled fields in linked Compositions records.                       |
| All Admin Publishers (from Compositions)                                   | `fldAsjwXRXEiylltc` | Lookup                 | Array of All Admin Publishers fields in linked Compositions records.             |
| All Original Publishers (from Compositions)                                | `fldzaPBXlUCId1Hvt` | Lookup                 | Array of All Original Publishers fields in linked Compositions records.          |
| Uncredited PD Writers (from Compositions)                                  | `fld1GGnSFCFPgh8hC` | Lookup                 | Array of Uncredited PD Writers fields in linked Compositions records.            |
| Song title in PRO                                                          | `fldVgLNtwRAZtArrg` | Lookup                 | Array of Song Title In PRO fields in linked Compositions records.                |
| All Sub-Publishers (from Compositions)                                     | `fldU0n8US1A880O4P` | Lookup                 | Array of All Sub-Publishers fields in linked Compositions records.               |
| Songwriter 1                                                               | `fldCA6dYLRDR7xPnb` | Lookup                 | Array of Songwriter 1 fields in linked Compositions records.                     |
| Songwriter 1 Share                                                         | `fldjvmcxvO5hX2UKf` | Lookup                 | Array of Songwriter 1 Share fields in linked Compositions records.               |
| Songwriter 1 Original Pub 1                                                | `fldRhipRn4M1aG4Fx` | Lookup                 | Array of Songwriter 1 Original Pub 1 fields in linked Compositions records.      |
| Songwriter 1 Admin Pub 1 (from Compositions)                               | `fldcsfTSZUtnoQ90X` | Lookup                 | Array of Songwriter 1 Admin Pub 1 fields in linked Compositions records.         |
| REGISTRATION PROJECT (SOUNDEXCHANGE) 2                                     | `fldQMrMMAmwti7Ggz` | Text                   | A single line of text.                                                           |
| Compositions 2                                                             | `fld3gjnOrMPcFZalU` | Link to another record | Array of linked records IDs from the Compositions table.                         |
| Compositions 3                                                             | `fldn4r74Eub5FushA` | Link to another record | Array of linked records IDs from the Compositions table.                         |
| Songwriter 4 Admin Pub. 1 (from Compositions 3)                            | `fldONSv35u6Jmbi3i` | Lookup                 | Array of Songwriter 4 Admin Pub. 1 fields in linked Compositions records.        |
| Songwriter 4 Original Pub. 1 Share (from Compositions 3)                   | `fldblG1ehtiMx09z5` | Lookup                 | Array of Songwriter 4 Original Pub. 1 Share fields in linked Compositions records. |
| Songwriter 4 Original Pub. 1 (from Compositions 3)                         | `fld2aXCS0bGXIG3IZ` | Lookup                 | Array of Songwriter 4 Original Pub. 1 fields in linked Compositions records.     |
| Songwriter 4 Ownership (from Compositions 3)                               | `fld3jJgddbKznn9oW` | Lookup                 | Array of Songwriter 4 Ownership fields in linked Compositions records.           |
| Songwriter 4 (from Compositions 3)                                         | `fld5aNXIayXgUayqd` | Lookup                 | Array of Songwriter 4 fields in linked Compositions records.                     |
| Songwriter 3 Admin Pub. 2 (from Compositions 3)                            | `fld2cKaDMiJAyy86P` | Lookup                 | Array of Songwriter 3 Admin Pub. 2 fields in linked Compositions records.        |
| Songwriter 3 Original Pub. 2 Share (from Compositions 3)                   | `fld2VAMMcA8Wvru9j` | Lookup                 | Array of Songwriter 3 Original Pub. 2 Share fields in linked Compositions records. |
| Songwriter 3 Original Pub. 2 (from Compositions 3)                         | `fld53jdtYFooQLKkU` | Lookup                 | Array of Songwriter 3 Original Pub. 2 fields in linked Compositions records.     |
| Songwriter 3 Admin Pub. 1 (from Compositions 3)                            | `fldSaf0x3TudFzxCW` | Lookup                 | Array of Songwriter 3 Admin Pub. 1 fields in linked Compositions records.        |
| Songwriter 3 Original Pub. 1 Share (from Compositions 3)                   | `fldJcEVpOUZMlzuoe` | Lookup                 | Array of Songwriter 3 Original Pub. 1 Share fields in linked Compositions records. |
| Songwriter 3 Original Pub. 1 (from Compositions 3)                         | `fldSTX9gBFsrNSJs1` | Lookup                 | Array of Songwriter 3 Original Pub. 1 fields in linked Compositions records.     |
| Songwriter 3 Ownership (from Compositions 3)                               | `fldh7PogF6xtGfHZT` | Lookup                 | Array of Songwriter 3 Ownership fields in linked Compositions records.           |
| Songwriter 3 (from Compositions 3)                                         | `fldzmlgoAfJPt7yDb` | Lookup                 | Array of Songwriter 3 fields in linked Compositions records.                     |
| Songwriter 2 Original Pub 3 Share (from Compositions 3)                    | `fldS4JaF0jG0ebGmz` | Lookup                 | Array of Songwriter 2 Original Pub 3 Share fields in linked Compositions records. |
| Songwriter 2 Original Pub. 3 (from Compositions 3)                         | `fldHTEEnSFfeL5oED` | Lookup                 | Array of Songwriter 2 Original Pub. 3 fields in linked Compositions records.     |
| Songwriter 2 Admin Pub. 2 (from Compositions 3)                            | `fldk2eZkFwKyoLLMv` | Lookup                 | Array of Songwriter 2 Admin Pub. 2 fields in linked Compositions records.        |
| Songwriter 2 Original Pub. 2 Share (from Compositions 3)                   | `fldStQd0MevxiZDzE` | Lookup                 | Array of Songwriter 2 Original Pub. 2 Share fields in linked Compositions records. |
| Songwriter 2 Original Pub. 2 (from Compositions 3)                         | `fldaGgIYxbJnB7WEm` | Lookup                 | Array of Songwriter 2 Original Pub. 2 fields in linked Compositions records.     |
| Songwriter 2 Admin Pub 1 (from Compositions 3)                             | `fldllbYPy1lTa5bOu` | Lookup                 | Array of Songwriter 2 Admin Pub 1 fields in linked Compositions records.         |
| Songwriter 2 Original Pub. 1 Share (from Compositions 3)                   | `fldtlwURA4fsjJszs` | Lookup                 | Array of Songwriter 2 Original Pub. 1 Share fields in linked Compositions records. |
| Songwriter 2 Original Pub. 1 (from Compositions 3)                         | `fld9bwtPB0gOFiNgY` | Lookup                 | Array of Songwriter 2 Original Pub. 1 fields in linked Compositions records.     |
| Songwriter 2 Share (from Compositions 3)                                   | `fldC30jlJIFd9x7DS` | Lookup                 | Array of Songwriter 2 Share fields in linked Compositions records.               |
| Songwriter 2 (from Compositions 3)                                         | `fldpGjA2Toxf6QAjo` | Lookup                 | Array of Songwriter 2 fields in linked Compositions records.                     |
| Songwriter 1 Admin Pub 3 (from Compositions 3)                             | `fldTOPVECeTZqd6R4` | Lookup                 | Array of Songwriter 1 Admin Pub 3 fields in linked Compositions records.         |
| Songwriter 1 Original Pub 3 Share (from Compositions 3)                    | `fldCswARNEvCieTOT` | Lookup                 | Array of Songwriter 1 Original Pub 3 Share fields in linked Compositions records. |
| Songwriter 1 Original Pub 3 (from Compositions 3)                          | `fldah64qGdVJAcEAS` | Lookup                 | Array of Songwriter 1 Original Pub 3 fields in linked Compositions records.      |
| Songwriter 1 Admin Pub 2 (from Compositions 3)                             | `fldGAJVFC2AOaVLxQ` | Lookup                 | Array of Songwriter 1 Admin Pub 2 fields in linked Compositions records.         |
| Songwriter 1 Original Pub 2 Share (from Compositions 3)                    | `fldHGsr00T0PvIKSc` | Lookup                 | Array of Songwriter 1 Original Pub 2 Share fields in linked Compositions records. |
| Publishers                                                                 | `fldOnlBxEWrms5wK9` | Text                   | A single line of text.                                                           |
| Address (from Songwriter 1 Admin Pub 1) (from Compositions)                | `fldV0Ec1vvjsIGEFT` | Lookup                 | Array of Address (from Songwriter 1 Admin Pub 1) fields in linked Compositions records. |
| Email (from Songwriter 1 Admin Pub 1) (from Compositions)                  | `fldQsampavUVZBSSy` | Lookup                 | Array of Email (from Songwriter 1 Admin Pub 1) fields in linked Compositions records. |
| Songwriter 2                                                               | `fldFdjAv05PGmHB1B` | Lookup                 | Array of Songwriter 2 fields in linked Compositions records.                     |
| Songwriter 2 Share                                                         | `fldIGUs3EAoS7lM4r` | Lookup                 | Array of Songwriter 2 Share fields in linked Compositions records.               |
| Songwriter 2 Original Pub 1                                                | `fldZel72It1bkOTdP` | Lookup                 | Array of Songwriter 2 Original Pub. 1 fields in linked Compositions records.     |
| Songwriter 2 Admin Pub 1 (from Compositions)                               | `fldmDmDx7XzylBVD7` | Lookup                 | Array of Songwriter 2 Admin Pub 1 fields in linked Compositions records.         |
| Address (from Songwriter 2 Admin Pub 1) (from Compositions)                | `fldMqzHnajmvfxnGV` | Lookup                 | Array of Address (from Songwriter 2 Admin Pub 1) fields in linked Compositions records. |
| Email (from Songwriter 2 Admin Pub 1) (from Compositions)                  | `fldvfo7EwvVNvXcVG` | Lookup                 | Array of Email (from Songwriter 2 Admin Pub 1) fields in linked Compositions records. |
| Songwriter 3                                                               | `fldUlgwjHScBOE7bC` | Lookup                 | Array of Songwriter 3 fields in linked Compositions records.                     |
| Songwriter 3 Share                                                         | `fldPcYUR3fVXRLEPC` | Lookup                 | Array of Songwriter 3 Ownership fields in linked Compositions records.           |
| Songwriter 3 Original Pub 1                                                | `fld66JPRd6OYmWqjV` | Lookup                 | Array of Songwriter 3 Original Pub. 1 fields in linked Compositions records.     |
| Songwriter 3 Admin Pub 1 (from Compositions)                               | `fldvrnaL7dHgvwk8v` | Lookup                 | Array of Songwriter 3 Admin Pub. 1 fields in linked Compositions records.        |
| Address (from Songwriter 3 Admin Pub 1) (from Compositions) copy           | `fldIQqqUlLmfCxYgL` | Lookup                 | Array of Address (from Songwriter 3 Admin Pub. 1) fields in linked Compositions records. |
| Email (from Songwriter 3 Admin Pub 1) (from Compositions)                  | `fldUM1TeDK1gubphP` | Lookup                 | Array of Email (from Songwriter 3 Admin Pub. 1) fields in linked Compositions records. |
| Songwriter 4                                                               | `fldiAvxWW6Z18r47j` | Lookup                 | Array of Songwriter 4 fields in linked Compositions records.                     |
| Songwriter 4 Share                                                         | `fldonI9pItThOiHTc` | Lookup                 | Array of Songwriter 4 Ownership fields in linked Compositions records.           |
| Songwriter 4 Original Pub 1                                                | `fldGwKMtL2yXdgCDB` | Lookup                 | Array of Songwriter 4 Original Pub. 1 fields in linked Compositions records.     |
| Songwriter 4 Admin Pub 1 (from Compositions)                               | `fld4vxi4NUCT5mixJ` | Lookup                 | Array of Songwriter 4 Admin Pub. 1 fields in linked Compositions records.        |
| Address (from Songwriter 4 Admin Pub 1) (from Compositions)                | `fldLHe4aP8n6IcY8q` | Lookup                 | Array of Address (from Songwriter 4 Admin Pub. 1) fields in linked Compositions records. |
| Email (from Songwriter 4 Admin Pub 1) (from Compositions)                  | `fldcQyiyLJyTcBjNd` | Lookup                 | Array of Email (from Songwriter 4 Admin Pub. 1) fields in linked Compositions records. |
| Songwriter 1 Original Pub 1 Share                                          | `fld8aEbU3LEw8tM0t` | Lookup                 | Array of Songwriter 1 Original Pub 1 Share fields in linked Compositions records. |
| Songwriter 2 Original Pub 1 Share                                          | `fldUFESp3KoJ5JDSt` | Lookup                 | Array of Songwriter 2 Original Pub. 1 Share fields in linked Compositions records. |
| Songwriter 2 Original Pub 2                                                | `fldkbGBVJDtaa4PJ3` | Lookup                 | Array of Songwriter 2 Original Pub. 2 fields in linked Compositions records.     |
| Songwriter 2 Original Pub 2 Share                                          | `fldgLQUp0FNQk3dFO` | Lookup                 | Array of Songwriter 2 Original Pub. 2 Share fields in linked Compositions records. |
| Songwriter 2 Admin Pub 2 (from Compositions)                               | `fldyOkV7xmWJOEejH` | Lookup                 | Array of Songwriter 2 Admin Pub. 2 fields in linked Compositions records.        |
| Address (from Songwriter 2 Admin Pub 2) (from Compositions) copy           | `fldZIV83LicrrL6pg` | Lookup                 | Array of Address (from Songwriter 2 Admin Pub. 2) fields in linked Compositions records. |
| Email (from Songwriter 2 Admin Pub 2) (from Compositions)                  | `fldB8hG1fz4ES5azS` | Lookup                 | Array of Email (from Songwriter 2 Admin Pub. 2) fields in linked Compositions records. |
| Songwriter 1 Original Pub 2                                                | `fldizhy41Trowgkaw` | Lookup                 | Array of Songwriter 1 Original Pub 2 fields in linked Compositions records.      |
| Songwriter 1 Admin Pub 2 (from Compositions)                               | `fldJ2MkBq0EFsCLPe` | Lookup                 | Array of Songwriter 1 Admin Pub 2 fields in linked Compositions records.         |
| Address (from Songwriter 1 Admin Pub 2) (from Compositions)                | `fldm1ERS0JH6TM8QN` | Lookup                 | Array of Address (from Songwriter 1 Admin Pub 2) fields in linked Compositions records. |
| Email (from Songwriter 1 Admin Pub 2) (from Compositions)                  | `fldEHUrL0HltClruH` | Lookup                 | Array of Email (from Songwriter 1 Admin Pub 2) fields in linked Compositions records. |
| Songwriter 3 Original Pub 1 Share                                          | `fldZ8nwVHcdhSgB1a` | Lookup                 | Array of Songwriter 3 Original Pub. 1 Share fields in linked Compositions records. |
| Songwriter 4 Original Pub 1 Share                                          | `fld697YMVrOs5w2ye` | Lookup                 | Array of Songwriter 4 Original Pub. 1 Share fields in linked Compositions records. |
| Songwriter 3 Original Pub 2                                                | `fldkyxlUt0dwBvxA1` | Lookup                 | Array of Songwriter 3 Original Pub. 2 fields in linked Compositions records.     |
| Songwriter 3 Original Pub 2 Share                                          | `fld4BIX7cPa3N9Mqo` | Lookup                 | Array of Songwriter 3 Original Pub. 2 Share fields in linked Compositions records. |
| Songwriter 3 Admin Pub 2 (from Compositions)                               | `fldY45SlOWqxk21Bk` | Lookup                 | Array of Songwriter 3 Admin Pub. 2 fields in linked Compositions records.        |
| Address (from Songwriter 3 Admin Pub 2) (from Compositions)                | `fldpVsFyzLorG0BWJ` | Lookup                 | Array of Address (from Songwriter 3 Admin Pub. 2) fields in linked Compositions records. |
| Email (from Songwriter 3 Admin Pub 2) (from Compositions)                  | `fldrGUYK5kJPn43IO` | Lookup                 | Array of Email (from Songwriter 3 Admin Pub. 2) fields in linked Compositions records. |
| Songwriter 4 Original Pub 2                                                | `fldHK79x9ayZ4zd63` | Lookup                 | Array of Songwriter 4 Original Pub 2 fields in linked Compositions records.      |
| Songwriter 4 Original Pub 2 Share                                          | `fldgxGuyGT3Pzzg4R` | Lookup                 | Array of Songwriter 4 Original Pub 2 Share fields in linked Compositions records. |
| Songwriter 4 Admin Pub 2 (from Compositions)                               | `fldwmKIgBEzf4bxry` | Lookup                 | Array of Songwriter 4 Admin Pub. 2 fields in linked Compositions records.        |
| Address (from Songwriter 4 Admin Pub 4) (from Compositions)                | `fldER2erykqBXogm3` | Lookup                 | Array of Address (from Songwriter 4 Admin Pub. 2) fields in linked Compositions records. |
| Email (from Songwriter 4 Admin Pub 2) (from Compositions)                  | `fld5Qv0383IhIF6NJ` | Lookup                 | Array of Email (from Songwriter 4 Admin Pub. 2) fields in linked Compositions records. |
| disco updated                                                              | `fldJO5qT2kUG9xLvx` | Checkbox               | This field is "true" when checked and otherwise empty.                           |
| Controlled by HFA (from Songwriter 1 Original Pub 1) (from Compositions)   | `fldXmFTDrMqC5RRO7` | Lookup                 | Array of Controlled by HFA (from Songwriter 1 Original Pub 1) fields in linked Compositions records. |
| Controlled by HFA (from Songwriter 1 Admin Pub 1) (from Compositions)      | `flduFTwgf2giksdOE` | Lookup                 | Array of Controlled by HFA (from Songwriter 1 Admin Pub 1) fields in linked Compositions records. |
| Controlled by HFA (from Songwriter 1 Original Pub 1) (from Compositions) 2 | `fldAOIZNEV9zBAuPq` | Lookup                 | Array of Controlled by HFA (from Songwriter 1 Original Pub 2) fields in linked Compositions records. |
| Controlled by HFA (from Songwriter 1 Admin Pub 2) (from Compositions)      | `fldRUyr40Ne3WKXZu` | Lookup                 | Array of Controlled by HFA (from Songwriter 1 Admin Pub 2) fields in linked Compositions records. |
| Controlled by HFA (from Songwriter 2 Original Pub. 1) (from Compositions)  | `fld4z0lHeV0ux5G76` | Lookup                 | Array of Controlled by HFA (from Songwriter 2 Original Pub. 1) fields in linked Compositions records. |
| Controlled by HFA (from Songwriter 2 Admin Pub 1) (from Compositions)      | `fldClAgha2xV7qMXv` | Lookup                 | Array of Controlled by HFA (from Songwriter 2 Admin Pub 1) fields in linked Compositions records. |
| Controlled by HFA (from Songwriter 2 Original Pub. 2) (from Compositions)  | `fld3zzUZbK23Lzj2D` | Lookup                 | Array of Controlled by HFA (from Songwriter 2 Original Pub. 2) fields in linked Compositions records. |
| Controlled by HFA (from Songwriter 2 Admin Pub. 2) (from Compositions)     | `fldfO7BOjtyQfvVDu` | Lookup                 | Array of Controlled by HFA (from Songwriter 2 Admin Pub. 2) fields in linked Compositions records. |
| Controlled by HFA (from Songwriter 3 Original Pub. 1) (from Compositions)  | `fldkEivwSubMqHPJl` | Lookup                 | Array of Controlled by HFA (from Songwriter 3 Original Pub. 1) fields in linked Compositions records. |
| Controlled by HFA (from Songwriter 3 Admin Pub. 1) (from Compositions)     | `fldNx8VwSviNfdeSv` | Lookup                 | Array of Controlled by HFA (from Songwriter 3 Admin Pub. 1) fields in linked Compositions records. |
| Controlled by HFA (from Songwriter 3 Original Pub. 2) (from Compositions)  | `fld3FvPAS0gxb7e4q` | Lookup                 | Array of Controlled by HFA (from Songwriter 3 Original Pub. 2) fields in linked Compositions records. |
| Controlled by HFA (from Songwriter 3 Admin Pub. 2) (from Compositions)     | `fldmcrHwtqP09zA4I` | Lookup                 | Array of Controlled by HFA (from Songwriter 3 Admin Pub. 2) fields in linked Compositions records. |
| Controlled by HFA (from Songwriter 4 Original Pub. 1) (from Compositions)  | `fldH8egiamDc2xSXx` | Lookup                 | Array of Controlled by HFA (from Songwriter 4 Original Pub. 1) fields in linked Compositions records. |
| Controlled by HFA (from Songwriter 4 Admin Pub. 1) (from Compositions)     | `fldBHQuI0Hjzdld4M` | Lookup                 | Array of Controlled by HFA (from Songwriter 4 Admin Pub. 1) fields in linked Compositions records. |
| Controlled by HFA (from Songwriter 4 Original Pub 2) (from Compositions)   | `fldc1tagiGVCkURMt` | Lookup                 | Array of Controlled by HFA (from Songwriter 4 Original Pub 2) fields in linked Compositions records. |
| Controlled by HFA (from Songwriter 4 Admin Pub. 2) (from Compositions)     | `fldVJshLiDRpdujNV` | Lookup                 | Array of Controlled by HFA (from Songwriter 4 Admin Pub. 2) fields in linked Compositions records. |
| Streaming Platforms                                                        | `fldIeQcESbP02bbkv` | Multiple select        | Array of selected option names. When creating or updating records, if a choice string does not exactly match an existing option, the request will fail with an INVALID_MULTIPLE_CHOICE_OPTIONS error unless the typecast parameter is enabled. If typecast is enabled, a new choice will be created if one does not exactly match. |
| APM Dist Mgmt                                                              | `flddt6bS2GN56LUQY` | Link to another record | Array of linked records IDs from the APM Dist Mgmt table.                        |
| Chevy Showroom Dist Mgmt                                                   | `flddAZaL7CL5QwgH1` | Link to another record | Array of linked records IDs from the Chevy Showroom Dist Mgmt table.             |
| Key                                                                        | `fld0Ao29ExvUiQU6U` | Text                   | A single line of text.                                                           |
| Legal Docs                                                                 | `fldVZMnGqosAZKLjf` | Link to another record | Array of linked records IDs from the Legal Docs table.                           |
| Update Disco.ac                                                            | `fldROBYkBoJhMiBoL` | Button                 | Object providing details about the button configuration. label string button label url string for "Open URL" actions, the computed url value |
| Disco Track ID                                                             | `fldgOnrMjSpiLjaaU` | Text                   | A single line of text.                                                           |
| REGISTRATION PROJECT (PRO +MLC)                                            | `fldEUVTZBGYl5tb0v` | Link to another record | Array of linked records IDs from the REGISTRATION PROJECT (PRO +MLC) table.      |
| Union Representation                                                       | `fldYYoXVIcZdVHptC` | Multiple select        | Array of selected option names. When creating or updating records, if a choice string does not exactly match an existing option, the request will fail with an INVALID_MULTIPLE_CHOICE_OPTIONS error unless the typecast parameter is enabled. If typecast is enabled, a new choice will be created if one does not exactly match. |

---

## List Records

**Endpoint:** `GET /v0/appEurfA8kXQE3slK/recordings`

To list records in Recordings , issue a GET request to the Recordings endpoint. Note that table names and table ids can be used interchangeably. Using table ids means table name changes do not require modifications to your API request.

Returned records do not include any fields with "empty" values, e.g. "" , [] , or false .

```bash
curl "https://api.airtable.com/v0/appEurfA8kXQE3slK/Recordings?maxRecords=3&view=Update%20missing%20songwriters%20%28Orchard%2FSpotify%29" \
  -H "Authorization: Bearer YOUR_SECRET_API_TOKEN"
```

### Query Parameters

| Parameter               | Type             | Required   | Description                                                                      |
| ----------------------- | ---------------- | ---------- | -------------------------------------------------------------------------------- |
| `fields`                | array of strings | optional   | Only data for fields whose names are in this list will be included in the result. If you don't need every field, you can use this parameter to reduce the amount of data transferred. For example, to only return data from Title of Recording and ISRC , send these two query parameters: fields%5B%5D=Titl |
| `filterByFormula`       | string           | optional   | A formula used to filter records. The formula will be evaluated for each record, and if the result is not 0 , false , "" , NaN , [] , or #Error! the record will be included in the response. We recommend testing your formula in the Formula field UI before using it in your API request. If combined wit |
| `maxRecords`            | number           | optional   | The maximum total number of records that will be returned in your requests. If this value is larger than pageSize (which is 100 by default), you may have to load multiple pages to reach this total. See the Pagination section below for more. |
| `pageSize`              | number           | optional   | The number of records returned in each request. Must be less than or equal to 100. Default is 100. See the Pagination section below for more. |
| `sort`                  | array of objects | optional   | A list of sort objects that specifies how the records will be ordered. Each sort object must have a field key specifying the name of the field to sort on, and an optional direction key that is either "asc" or "desc" . The default direction is "asc" . The sort parameter overrides the sorting of the v |
| `view`                  | string           | optional   | The name or ID of a view in the Recordings table. If set, only the records in that view will be returned. The records will be sorted according to the order of the view unless the sort parameter is included, which overrides that order. Fields hidden in this view will be returned in the results. To on |
| `cellFormat`            | string           | optional   | The format that should be used for cell values. Supported values are: json : cells will be formatted as JSON, depending on the field type. string : cells will be formatted as user-facing strings, regardless of the field type. The timeZone and userLocale parameters are required when using string as t |
| `timeZone`              | string           | optional   | The time zone that should be used to format dates when using string as the cellFormat . This parameter is required when using string as the cellFormat . |
| `userLocale`            | string           | optional   | The user locale that should be used to format dates when using string as the cellFormat . This parameter is required when using string as the cellFormat . |
| `returnFieldsByFieldId` | boolean          | optional   | An optional boolean value that lets you return field objects where the key is the field id. This defaults to false , which returns field objects where the key is the field name. |
| `recordMetadata`        | array of strings | optional   | An optional field that, if includes commentCount , adds a commentCount read only property on each record returned. |

---

## Retrieve a Record

**Endpoint:** `GET /v0/appEurfA8kXQE3slK/recordings`

To retrieve an existing record in Recordings table, issue a GET request to the record endpoint.

Any "empty" fields (e.g. "" , [] , or false ) in the record will not be returned.

```bash
curl https://api.airtable.com/v0/appEurfA8kXQE3slK/Recordings/recQcYvBnCfLZQfOe \
  -H "Authorization: Bearer YOUR_SECRET_API_TOKEN"
```

---

## Create Records

**Endpoint:** `POST /v0/appEurfA8kXQE3slK/recordings`

To create new records, issue a POST request to the Recordings endpoint. Note that table names and table ids can be used interchangeably. Using table ids means table name changes do not require modifications to your API request.

Your request body should include an array of up to 10 record objects. Each of these objects should have one key whose value is an inner object containing your record's cell values, keyed by either field name or field id.

```bash
curl -X POST https://api.airtable.com/v0/appEurfA8kXQE3slK/Recordings \
  -H "Authorization: Bearer YOUR_SECRET_API_TOKEN" \
  -H "Content-Type: application/json" \
  --data '{
  "records": [
    {
      "fields": {
        "Title of Recording": "It'\''s Too Soon To Know - Live On The Pat Boone Chevy Showroom, January 23, 1958",
        "ISRC": "QT27V2500069",
        "Missing songwriter on Spotify": "Not yet assessed",
        "All Releases": [
          "recgtlNBGGu08mUot"
        ],
        "Compositions": [
          "recbOVTanUjBSvUwI"
        ],
        "Master Owner 1": [
          "recmbD0S2y6gdZY0M"
        ],
        "Master 1 Ownership": 1,
        "REGISTRATION PROJECT (SOUNDEXCHANGE) 3": [
          "reckGberWwlebdUXg"
        ],
        "PBGL Owned": true,
        "Primary Artist": [
          "recLWgt9qnlgDkkAo"
        ],
        "Original Release": [
          "recgtlNBGGu08mUot"
        ],
        "Master": "https://app.box.com/s/lobp56o8kpwilth0rm99r7e3xtcr1kas",
        "Date of original Release": "2025-10-31",
        "Tempo Tag": "Downtempo",
        "Mood Tag": [
          "Dreamy",
          "Romantic",
          "Warm"
        ],
        "Genre Tag": [
          "R&B",
          "Rock N Roll"
        ],
        "Vocal Tag": [
          "Male vocal",
          "Background vocals"
        ],
        "Instruments Tag": [
          "Electric Bass",
          "Orchestral",
          "Piano",
          "Strings"
        ],
        "Lyrical Theme Tag": [
          "Desire",
          "Heartbreak",
          "Love"
        ],
        "Duration": 164,
        "DISCO": "https://s.disco.ac/njwcsfbkonse",
        "Era": "1950s",
        "Ready for Sync": "Yes",
        "Recording year": "1958",
        "Status": [
          "In progress"
        ],
        "Priority": "N/A",
        "disco updated": true,
        "Chevy Showroom Dist Mgmt": [
          "reczvmZSIkqvTmciC"
        ],
        "Disco Track ID": "123502181",
        "Union Representation": [
          "Not yet assessed"
        ]
      }
    },
    {
      "fields": {
        "Title of Recording": "Under God",
        "Missing songwriter on Spotify": "Not distributed on Spotify",
        "All Releases": [
          "recIJwdEoRhNM5a7r"
        ],
        "Primary Artist": [
          "recLWgt9qnlgDkkAo"
        ],
        "Original Release": [
          "recIJwdEoRhNM5a7r"
        ],
        "Date of original Release": "2020-11-20",
        "Tempo Tag": "Midtempo",
        "Mood Tag": [
          "Happy",
          "Joyful",
          "Celebratory"
        ],
        "Genre Tag": [
          "Gospel",
          "Pop",
          "Rock N Roll"
        ],
        "Vocal Tag": [
          "Male Lead",
          "Female Backup"
        ],
        "Instruments Tag": [
          "Drums",
          "Electric Bass",
          "Electric Guitar",
          "Organ",
          "Synth"
        ],
        "Lyrical Theme Tag": [
          "Freedom",
          "Religious",
          "Storytelling"
        ],
        "Duration": 259,
        "Era": "2020s",
        "Ready for Sync": "No",
        "Type Tag": [
          "Rerecord"
        ],
        "Union Representation": [
          "Not yet assessed"
        ]
      }
    }
  ]
}'
```

---

## Update / Upsert Records

**Endpoint:** `PATCH /v0/appEurfA8kXQE3slK/recordings`

To update Recordings records, issue a request to the Recordings endpoint. Table names and table IDs can be used interchangeably. Using table IDs means table name changes won't require modifying your API request code. A PATCH request will only update the fields included in the request. Fields not included in the request will be unchanged. A PUT request will perform a destructive update and clear all unincluded cell values.

Your request body should include an array of up to 10 record objects. Each of these objects should have an id property representing the record ID and a fields property which contains all of your record's cell values by field name or field id for all of your record's cell values by field name.

```bash
curl -X PATCH https://api.airtable.com/v0/appEurfA8kXQE3slK/Recordings \
  -H "Authorization: Bearer YOUR_SECRET_API_TOKEN" \
  -H "Content-Type: application/json" \
  --data '{
  "records": [
    {
      "id": "recQcYvBnCfLZQfOe",
      "fields": {
        "Title of Recording": "It'\''s Too Soon To Know - Live On The Pat Boone Chevy Showroom, January 23, 1958",
        "ISRC": "QT27V2500069",
        "Missing songwriter on Spotify": "Not yet assessed",
        "All Releases": [
          "recgtlNBGGu08mUot"
        ],
        "Compositions": [
          "recbOVTanUjBSvUwI"
        ],
        "Master Owner 1": [
          "recmbD0S2y6gdZY0M"
        ],
        "Master 1 Ownership": 1,
        "REGISTRATION PROJECT (SOUNDEXCHANGE) 3": [
          "reckGberWwlebdUXg"
        ],
        "PBGL Owned": true,
        "Primary Artist": [
          "recLWgt9qnlgDkkAo"
        ],
        "Original Release": [
          "recgtlNBGGu08mUot"
        ],
        "Master": "https://app.box.com/s/lobp56o8kpwilth0rm99r7e3xtcr1kas",
        "Date of original Release": "2025-10-31",
        "Tempo Tag": "Downtempo",
        "Mood Tag": [
          "Dreamy",
          "Romantic",
          "Warm"
        ],
        "Genre Tag": [
          "R&B",
          "Rock N Roll"
        ],
        "Vocal Tag": [
          "Male vocal",
          "Background vocals"
        ],
        "Instruments Tag": [
          "Electric Bass",
          "Orchestral",
          "Piano",
          "Strings"
        ],
        "Lyrical Theme Tag": [
          "Desire",
          "Heartbreak",
          "Love"
        ],
        "Duration": 164,
        "DISCO": "https://s.disco.ac/njwcsfbkonse",
        "Era": "1950s",
        "Ready for Sync": "Yes",
        "Recording year": "1958",
        "Status": [
          "In progress"
        ],
        "Priority": "N/A",
        "disco updated": true,
        "Chevy Showroom Dist Mgmt": [
          "reczvmZSIkqvTmciC"
        ],
        "Disco Track ID": "123502181",
        "Union Representation": [
          "Not yet assessed"
        ]
      }
    },
    {
      "id": "recPwb70VYoaxT1an",
      "fields": {
        "Title of Recording": "Under God",
        "Missing songwriter on Spotify": "Not distributed on Spotify",
        "All Releases": [
          "recIJwdEoRhNM5a7r"
        ],
        "Primary Artist": [
          "recLWgt9qnlgDkkAo"
        ],
        "Original Release": [
          "recIJwdEoRhNM5a7r"
        ],
        "Date of original Release": "2020-11-20",
        "Tempo Tag": "Midtempo",
        "Mood Tag": [
          "Happy",
          "Joyful",
          "Celebratory"
        ],
        "Genre Tag": [
          "Gospel",
          "Pop",
          "Rock N Roll"
        ],
        "Vocal Tag": [
          "Male Lead",
          "Female Backup"
        ],
        "Instruments Tag": [
          "Drums",
          "Electric Bass",
          "Electric Guitar",
          "Organ",
          "Synth"
        ],
        "Lyrical Theme Tag": [
          "Freedom",
          "Religious",
          "Storytelling"
        ],
        "Duration": 259,
        "Era": "2020s",
        "Ready for Sync": "No",
        "Type Tag": [
          "Rerecord"
        ],
        "Union Representation": [
          "Not yet assessed"
        ]
      }
    },
    {
      "id": "recXeaNwgu672wE1H",
      "fields": {
        "Title of Recording": "The Old Rugged Cross ",
        "ISRC": "US2R30912212",
        "Missing songwriter on Spotify": "Not distributed on Spotify",
        "All Releases": [
          "rechJrbwuGtmmX3mq"
        ],
        "Compositions": [
          "recqJ4gCumDthZJEl"
        ],
        "Master Owner 1": [
          "rec52XnBYFVE0RgZ8"
        ],
        "Master 1 Ownership": 1,
        "Spotify": "N/A",
        "REGISTRATION PROJECT (SOUNDEXCHANGE) 3": [
          "recEjTMy2xZLU2fP2"
        ],
        "PBGL Owned": true,
        "Primary Artist": [
          "recLWgt9qnlgDkkAo"
        ],
        "Original Release": [
          "rechJrbwuGtmmX3mq"
        ],
        "Master": "https://app.box.com/s/ta6lo1vnwejfz4gb66ucm0ytgngl7q80",
        "Date of original Release": "2015-05-12",
        "Tempo Tag": "Downtempo",
        "Mood Tag": [
          "Wistful",
          "Contemplative",
          "Positive",
          "Warm"
        ],
        "Genre Tag": [
          "Christian",
          "Gospel"
        ],
        "Vocal Tag": [
          "Male Lead",
          "Background vocals",
          "Spoken"
        ],
        "Instruments Tag": [
          "Bells",
          "Acoustic Guitar",
          "Piano",
          "Upright Bass ",
          "Organ",
          "Drums"
        ],
        "Lyrical Theme Tag": [
          "Religious",
          "Appreciation",
          "Love",
          "Storytelling",
          "Nature",
          "Death",
          "Life"
        ],
        "Duration": 250,
        "DISCO": "https://s.disco.ac/bnudssskmxzb",
        "Apple Music": "https://music.apple.com/in/album/the-old-rugged-cross/342564024?i=342564103",
        "YouTube Music": "N/A",
        "Soundcloud": "N/A",
        "Amazon Music": "N/A",
        "Era": "1990s",
        "Ready for Sync": "No",
        "Lyric Sheet": "https://app.box.com/s/3pbmo2nhi246w114nnuz3r3ej07nq92g",
        "Type Tag": [
          "Cover",
          "Recognizable",
          "Rerecord"
        ],
        "Streaming Platforms": [
          "NOT YET ASSESSED"
        ],
        "APM Dist Mgmt": [
          "recsU8h433Uaa5txE"
        ],
        "Disco Track ID": "90612188",
        "Union Representation": [
          "Non-Union"
        ]
      }
    }
  ]
}'
```

---

## Delete Records

**Endpoint:** `DELETE /v0/appEurfA8kXQE3slK/recordings`

To delete Recordings records, issue a DELETE request to the Recordings endpoint. Note that table names and table ids can be used interchangeably. Using table ids means table name changes do not require modifications to your API request.

Your request should include a URL-encoded array of up to 10 record IDs to delete.

```bash
curl -X DELETE https://api.airtable.com/v0/appEurfA8kXQE3slK/Recordings \
  -H "Authorization: Bearer YOUR_SECRET_API_TOKEN" \
  -G \
  --data-urlencode 'records[]=recQcYvBnCfLZQfOe' \
  --data-urlencode 'records[]=recPwb70VYoaxT1an'
```

