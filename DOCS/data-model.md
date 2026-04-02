# Gold Label Artists — AirTable Data Model

Reference for all "Link to another record" fields across the 12 active tables. Field IDs are from the AirTable Metadata API; descriptions in quotes are verbatim from the AirTable UI.

---

## 1. The Two Rights Sides

Every piece of recorded music involves two distinct rights stacks. This database's tables map onto them as follows:

| Side | Tables |
|------|--------|
| **Recording / Master** | Releases, Recordings, Artists, Master Owners, APM Dist Mgmt, Chevy Showroom Dist Mgmt, PROGRESS REPORT, REGISTRATION PROJECT (SOUNDEXCHANGE) |
| **Composition / Publishing** | Compositions, Songwriters, Publishers, REGISTRATION PROJECT (PRO +MLC) |
| **Cross-cutting** | Legal Docs |

---

## 2. Core Ownership Chain

```
Release ────────────────────── Recording ──────────── Composition ──── Songwriter
  │                                │                       │                │
  ├─ Primary Artist                ├─ Primary Artist        ├─ Songwriter 1  └─ Published by ──► Publisher
  ├─ Featured Artist(s)            ├─ Featured Artist       ├─ Songwriter 2         (Original Pub / Admin Pub / Sub-Pub per slot)
  ├─ Original release label        ├─ Master Owner 1        └─ Songwriter 3–9
  └─ Current release label         ├─ Master Owner 2
       (→ Master Owners)           └─ Master Owner 3
                                        (→ Master Owners)
```

**Key rule:** The canonical path from a Release to its underlying Compositions is:

```
Release → Recordings → Compositions → Songwriters → Publishers
```

The Releases table also has direct `Compositions` link fields (denormalized shortcut — see §6).

---

## 3. Per-Table Linked Fields

### Releases (`tbl7rjVKUd5faZ7fV`)

| Field | field_id | → Table | Notes |
|-------|----------|---------|-------|
| Recordings | `fldcrSUSKSeL84t0N` | Recordings | All recordings on this release |
| Compositions | `fldy0DXSoqbUN1LXl` | Compositions | Denormalized shortcut; inverse of Compositions.Releases |
| Compositions 2 | `flds3xoOLuDcoO9XQ` | Compositions | Overflow slot |
| Compositions 3 | `fldJM2AZnEXwFIW3p` | Compositions | Overflow slot |
| Primary Artist | `fldyz0BJ21bNKgFcK` | Artists | Exactly one primary credited act |
| Featured Artist(s) | `fldvYrNxuyvpDgksg` | Artists | Zero or more "feat." acts |
| Original release label | `fld9sglzyDRTWE3qk` | Master Owners | Master Owner that originally released this |
| Current release label | `fldilpa7qfgWZwxH6` | Master Owners | Master Owner currently holding the master; see §6 for naming note |
| [DON'T DELETE] Original Release in Recordings | `fld1Mh5OoA23r4nGm` | Recordings | Auto-generated reverse side of Recordings.Original Release — do not write |
| Chevy Showroom Dist Mgmt | `fldbLdqXtUapQ8JBh` | Chevy Showroom Dist Mgmt | Distribution records for this release |
| APM Dist Mgmt | `fldI26ZqCc65BoOrm` | APM Dist Mgmt | Distribution records for this release |
| Legal Docs | `fldQdqUgXLYutGCKD` | Legal Docs | Agreements covering this release |
| PROGRESS REPORT | `fldwzhPADkBeZeAhk` | PROGRESS REPORT | Progress tracking entries for this release |

---

### Recordings (`tblESvQQmOBbEXAH0`)

| Field | field_id | → Table | Notes |
|-------|----------|---------|-------|
| All Releases | `fld57hhrA0PBM88o6` | Releases | Reverse side of Releases.Recordings |
| Original Release | `fldV2X7dziu3HDfw8` | Releases | "The first Release that the Recording was featured on" |
| Compositions | `fldEAl8K8Sn0gvC98` | Compositions | Primary composition(s) for this recording |
| Compositions 2 | `fld3gjnOrMPcFZalU` | Compositions | Overflow slot |
| Compositions 3 | `fldn4r74Eub5FushA` | Compositions | Overflow slot |
| Primary Artist | `fld9vMhhhV6aAZPZP` | Artists | Primary credited act |
| Featured Artist | `fldr6WmY3lmlfnTrb` | Artists | Featured credited act |
| Master Owner 1 | `fldMKw9veaxGqmWJy` | Master Owners | Primary master rights holder |
| Master Owner 2 | `fldtEeYpvscGJUiCf` | Master Owners | Second ownership slot |
| Master Owner 3 | `fldEw8iScPnOFWTx0` | Master Owners | Third ownership slot |
| REGISTRATION PROJECT (SOUNDEXCHANGE) 3 | `fldvX8g1YQ40aEtW4` | REGISTRATION PROJECT (SOUNDEXCHANGE) | SoundExchange registration record for this recording |
| REGISTRATION PROJECT (PRO +MLC) | `fldEUVTZBGYl5tb0v` | REGISTRATION PROJECT (PRO +MLC) | PRO/MLC registration — reverse side of Reg.PRO.Matched Recording on MLC |
| APM Dist Mgmt | `flddt6bS2GN56LUQY` | APM Dist Mgmt | APM distribution records |
| Chevy Showroom Dist Mgmt | `flddAZaL7CL5QwgH1` | Chevy Showroom Dist Mgmt | Chevy Showroom distribution records |
| Legal Docs | `fldVZMnGqosAZKLjf` | Legal Docs | Agreements covering this recording |

---

### Compositions (`tblomWINKPjfgAVpo`)

#### Aggregate / roll-up links (safe to read; written via individual slots below)

| Field | field_id | → Table | Notes |
|-------|----------|---------|-------|
| Recordings | `fldVjjMa9H9Zpx9p0` | Recordings | "Recordings of the composition" |
| Recordings 2 | `fldxWNmJpXpvsObEg` | Recordings | Overflow slot |
| Recordings 3 | `fldYObdWITjl5fAAO` | Recordings | Overflow slot |
| Releases | `fldJj9yZLZEdu8qS8` | Releases | "Releases with a recording of the composition" |
| Releases 2 | `fldQlJmvFWq4ipS17` | Releases | Overflow slot |
| Releases 3 | `fldF908RO6LCB39D5` | Releases | Overflow slot |
| All Songwriters | `fldRfWFbfjTZXzfKP` | Songwriters | Union of all Songwriter 1–9 slots |
| All Original Publishers | `fldkIOo7kToJaT5zm` | Publishers | Union of all Original Pub slots |
| All Admin Publishers | `fld58IACBmYnW9DJu` | Publishers | Union of all Admin Pub slots |
| All Sub-Publishers | `fldMf59kc6MdOns1n` | Publishers | Union of all Sub-Pub slots |
| REGISTRATION PROJECT | `fldN5elY1M8qIXXZ4` | REGISTRATION PROJECT (PRO +MLC) | Reverse side of Reg.PRO.Compositions |
| Legal Docs | `fldh0MvKdlr37yU6N` | Legal Docs | Agreements covering this composition |

#### Per-songwriter ownership slots

Each co-writer gets a numbered slot (1–9). Each slot can have up to 4 publisher positions (Original Pub 1–4, Admin Pub 1–4, Sub-Pub 1). This is AirTable's way of encoding a per-songwriter ownership split.

| Slot | Songwriter field_id | Orig Pub 1 | Admin Pub 1 | Sub-Pub 1 |
|------|---------------------|------------|-------------|-----------|
| SW 1 | `fldLhXZcoaevUSLlA` | `fldcx8y9D1KbIfCCj` | `fldeNG9WWWEeKzHpN` | `fldMi4ctlHPOaPFMD` |
| SW 2 | `fldeivT63AcOXMinA` | `fld4085JeJSnRKbhA` | `fld2pifFJ2sg6UMRo` | `fld9zTSYx2pv31dxT` |
| SW 3 | `fldpQwAEw0mATtMW4` | `fldVAiZ0RFyEih9HO` | `fldiKRkycbb71x06O` | `fld8ssi2tFWvUy7WO` |
| SW 4 | `fldfi9zF7k7eyzN3E` | `fldqbaFomnWoWwRwi` | `fldqXGTiRaLiF4ZKx` | — |
| SW 5 | `fld94WOrOzwY3ZZr4` | `fldwZSHeismDTtoRm` | `fldTBUGYFJFk2GA0k` | — |
| SW 6 | `fldspvCZJR5LI2KMM` | `fldGo6i2jCDh3VWYM` | `fldupwtvdkBPnmeUv` | — |
| SW 7 | `fldd3R26JG9uqgw9P` | `fldVFyqtVZKZFDxUc` | `fldsCeVEfrGptKpJc` | — |
| SW 8 | `fldCtxeKcFoop5kpv` | `fldg4VsKIA2ABmEY7` | `fld4Q0oVqasrLgOPZ` | — |
| SW 9 | `fld3prOTF7TdS4cdj` | `fldPr6m9Tnf83vlJ0` | `fldM8ji8hdvlOs2qX` | — |

Each songwriter slot also has Orig Pub 2–4 and Admin Pub 2–4 fields for cases where a writer has multiple publishers in the chain (original + admin + sub). For the full field_id list see the Metadata API output.

---

### Songwriters (`tbl2KLh2RIrS5AmSX`)

| Field | field_id | → Table | Notes |
|-------|----------|---------|-------|
| Compositions | `fldEoEyYlIjaKwrkq` | Compositions | Reverse side of Compositions.All Songwriters |
| Compositions 2–8 | `fld0bWrdHt8Z8ONQz`–`fld06Logrgm1PYtJO` | Compositions | Auto-generated reverses of Songwriter 1–8 slots on Compositions |
| Compositions 7 copy | `fldKl1LiSp8T5mJIT` | Compositions | Reverse of Composer.Songwriter 8 slot (legacy name) |
| Compositions 7 copy copy | `fldSdlzArrF30VgBR` | Compositions | Reverse of Composer.Songwriter 9 slot (legacy name) |
| Published by | `fld5mmxZv286NzYCs` | Publishers | "Publishers that have published work by the Songwriter" |
| Legal Docs | `fldwccASH977BT3le` | Legal Docs | Agreements involving this songwriter |

---

### Publishers (`tbl6TNKQRPfY3hXZ2`)

#### Meaningful links

| Field | field_id | → Table | Notes |
|-------|----------|---------|-------|
| Original Pub. Compositions | `fldun7E4qgE0odL9Q` | Compositions | Reverse of Compositions.All Original Publishers |
| Admin Pub. Compositions | `fldpqaDDnpqZhO1Wf` | Compositions | Reverse of Compositions.All Admin Publishers |
| Compositions | `fldlrC144iV4zNWG2` | Compositions | Reverse of Compositions.All Sub-Publishers |
| Songwriters | `fldP7iqjXfkQMvTdS` | Songwriters | Reverse of Songwriters.Published by |
| In Care Of | `fldPx8Rrlljp0Uw94` | Publishers (self) | "This Publisher is being administered and/or sub-published by ________" |
| Administered Pubs | `fldMTRizR1S5wOPbx` | Publishers (self) | "This Publisher acts as an Admin Publisher for _____________" |
| Legal Docs | `fldFFEnrBSdCtHfvZ` | Legal Docs | Agreements involving this publisher |

#### Overflow / [DON'T DELETE] Compositions fields (all → Compositions)

These are auto-generated reverse sides of the per-songwriter publisher slots on the Compositions table. There are approximately 35 of them with names like `Compositions 2`, `Compositions 2 copy copy copy...`, `[DON'T DELETE] Songwriter 1 Admin Pub. 1`, etc. None should be written to directly — they are read-only roll-ups on the Publishers side. The meaningful write path is always via the Compositions table's `Songwriter N Original/Admin Pub M` fields.

---

### Artists (`tbla7zxpHm76x0Aj9`)

| Field | field_id | → Table | Notes |
|-------|----------|---------|-------|
| Primary Recordings | `fld9Eyowsg94qVrJe` | Recordings | Recordings where this act is the primary artist |
| Featured Recordings | `flddCYswYDG3kkOY8` | Recordings | Recordings where this act is a featured artist |
| Primary Releases | `fldMZrQCVME3cIBnE` | Releases | "Releases where the Artist is the Primary Artist" |
| Featured Releases | `fldXrX9pcvBTDf7YF` | Releases | "Releases that Artist is featured on" |
| Legal Docs | `fldnpu57KRbN8DIAg` | Legal Docs | Agreements involving this artist |

---

### Master Owners (`tblqfRCyEWjlfTMBd`)

| Field | field_id | → Table | Notes |
|-------|----------|---------|-------|
| Related labels | `fldocX256KHFPNvak` | Master Owners (self) | "If you're viewing a Parent Type master owner, then these are their Subdivision labels. If you're viewing a Subdivision Type, this is their Parent label" |
| Owned Recordings | `fldxyKSwINUjwCSfK` | Recordings | Recordings where this entity is Master Owner 1 |
| Original releases | `fldBpxKhX21ESiiuE` | Releases | "Were responsible for the original release of these Releases"; inverse of Releases.Current release label (see §6) |
| Releases | `fldWAKqc4GPb7uesN` | Releases | Inverse of Releases.Original release label (see §6) |
| [DON'T DELETE] Master Owner 2 in Recordings | `fld3eWa7SYrEN2HkL` | Recordings | Auto-generated reverse of Recordings.Master Owner 2 — do not write |
| [DON'T DELETE] Master Owner 3 in Recordings | `fld1Iq5MydRBkOktY` | Recordings | Auto-generated reverse of Recordings.Master Owner 3 — do not write |
| Legal Docs | `fldZxv4TMJuPZNWPH` | Legal Docs | Agreements involving this master owner |

---

### Legal Docs (`tbl0JjCNEaGmFGAkx`)

A cross-cutting table — a single legal document record can link to any combination of entities across both rights sides.

| Field | field_id | → Table | Notes |
|-------|----------|---------|-------|
| Master Owner | `fldXUjQvuEbtzF2y6` | Master Owners | "Master Owners involved in this legal document." |
| Artists | `fld589CVNN3Dz4LIo` | Artists | "Artists involved in this legal document." |
| Linked Compositions | `fldD2pmUU5QiXFHSx` | Compositions | "Compositions involved in this legal document." |
| Publisher(s) | `fldE9rUE0HpFuoxGX` | Publishers | "Publishers involved in this legal document." |
| Songwriter(s) | `fld1qPXmNU8VlgWOj` | Songwriters | "Songwriters involved in this legal document." |
| Recordings | `fldPBENvLLuCsdN7g` | Recordings | "Recordings involved in this legal document." |
| Releases | `fldoyrjPJv0VJzsns` | Releases | "Releases involved in this legal document." |
| Related Legal Docs | `fldTIZRdifmWsei2p` | Legal Docs (self) | Self-referential link for related/parent agreements |
| From field: Related Legal Docs | `flddf50UzWyJzJA7G` | Legal Docs (self) | Auto-generated reverse side of Related Legal Docs — do not write |

---

### REGISTRATION PROJECT (PRO +MLC) (`tbl7FGL9AZlKaqOwm`)

Tracks composition-side registrations with Performing Rights Organizations and the Mechanical Licensing Collective.

| Field | field_id | → Table | Notes |
|-------|----------|---------|-------|
| Compositions | `fldHiMGgWMpTNCQmV` | Compositions | The composition being registered |
| Matched Recording on MLC | `fldTTsqgKn6xtbFKy` | Recordings | "Matched Recording on MLC" — the specific recording the MLC matched during registration |

---

### REGISTRATION PROJECT (SOUNDEXCHANGE) (`tbliX5cAVK47tYsL8`)

Tracks recording-side registrations with SoundExchange (digital performance royalties).

| Field | field_id | → Table | Notes |
|-------|----------|---------|-------|
| Recordings | `fld2j5Wejenu7sbM4` | Recordings | The recording being registered with SoundExchange |

---

### APM Dist Mgmt (`tbllGX2Hxg3SGhJMa`)

Distribution management records for the APM channel.

| Field | field_id | → Table | Notes |
|-------|----------|---------|-------|
| From Release | `fldJNJzhWluDYWDTS` | Releases | "This is the release(s) that the recording is from. NOTE: This release may/may not be the same as the CD ID that recording is packaged in by APM. We're using release to help us verify metadata like 'Primary Artist' etc." |
| Recording | `fldHwS1bgXbIMxljd` | Recordings | The specific recording in this distribution record |

---

### Chevy Showroom Dist Mgmt (`tblRqFtQrPCNB1fwT`)

Distribution management records for the Chevy Showroom channel.

| Field | field_id | → Table | Notes |
|-------|----------|---------|-------|
| Release | `fld8ZRGggXaSZ6WPr` | Releases | The release being distributed |
| Recordings | `fldu3zfcd8SW7QJwG` | Recordings | The recording in this distribution record |

---

### PROGRESS REPORT (`tblPBXgEXtDH6TaRR`)

Progress tracking entries on the recording side.

| Field | field_id | → Table | Notes |
|-------|----------|---------|-------|
| Releases | `fldYG5yQVaoJrH8LE` | Releases | Releases tracked in this report |

---

## 4. Tables Not Covered Here

These tables exist in the base but are excluded from this reference:

| Table | Reason |
|-------|--------|
| Dot Records Data | External data import; not part of the active catalog workflow |
| Resources | Internal reference/links table; no catalog entity links |
| SCRATCH | Working scratch space; not canonical data |
| artists_copy | Duplicate of Artists; excluded from `load_tables()` in md_parser.py |

---

## 5. Self-Referential Tables

Three tables link to themselves:

**Publishers → Publishers**
- `In Care Of` (`fldPx8Rrlljp0Uw94`): "This Publisher is being administered and/or sub-published by ________" — points to the parent/admin publisher above this one in the publishing chain.
- `Administered Pubs` (`fldMTRizR1S5wOPbx`): "This Publisher acts as an Admin Publisher for _____________" — points to the child publishers this publisher administers.

These two are separate, independent fields (neither is the auto-generated reverse of the other — confirmed by both having empty `inverseLinkFieldId`). They model a directed graph of publisher relationships.

**Master Owners → Master Owners**
- `Related labels` (`fldocX256KHFPNvak`): "If you're viewing a Parent Type master owner, then these are their Subdivision labels. If you're viewing a Subdivision Type, this is their Parent label" — models parent/imprint relationships between entities. Also an independent self-referential field (no auto-generated reverse).

**Legal Docs → Legal Docs**
- `Related Legal Docs` (`fldTIZRdifmWsei2p`) / `From field: Related Legal Docs` (`flddf50UzWyJzJA7G`): Bidirectional link between related agreements. Unlike the Publisher/Master Owner self-refs, this one does have an auto-generated reverse side (`flddf50UzWyJzJA7G`) — do not write to the reverse.

---

## 6. Key Design Notes

### Release → Compositions denormalization

The canonical data path is `Release → Recordings → Compositions`. However, the Releases table also has direct `Compositions`, `Compositions 2`, and `Compositions 3` fields. These appear to be a convenience denormalization to enable quick lookups without traversing through Recordings. When writing new data, always populate via `Recordings → Compositions`; the Releases.Compositions fields should stay in sync automatically through AirTable's bidirectional links.

### Releases label field naming quirk

The field naming on Releases vs. Master Owners is counterintuitive:

| Releases field | → Master Owners field | API description |
|---|---|---|
| `Original release label` | → `Releases` (no description) | The master owner who is tracked generically |
| `Current release label` | → `Original releases` | "Were responsible for the original release" |

The `Master Owners.Original releases` description ("Were responsible for the original release of these Releases") is the inverse of `Releases.Current release label`, not `Original release label`. This naming inversion appears to be a historical artifact — trust the field_id pairs above, not the field names, when writing code.

### Per-songwriter publisher slots on Compositions

AirTable has no native join table. The Compositions table replicates a proper ownership-split join table by having explicit per-songwriter × per-publisher fields (up to Songwriter 9 × Pub 4). Each slot independently captures one publisher's role for one co-writer. The aggregate fields (`All Original Publishers`, `All Admin Publishers`, `All Sub-Publishers`, `All Songwriters`) are roll-ups of these individual slots.

### Publisher overflow fields

The Publishers table accumulates ~35 link fields back to Compositions, most with names like `Compositions 2 copy copy copy...`. These are the auto-generated reverse sides of all the per-songwriter publisher slot fields on the Compositions table. They all point to the same Compositions table and are read-only from the Publishers side. None should be written to directly.

### [DON'T DELETE] fields

Any field prefixed `[DON'T DELETE]` is an auto-generated reverse-side link. AirTable requires them to exist to maintain bidirectional link integrity. They should never be written to — always write to the primary side of the link.
