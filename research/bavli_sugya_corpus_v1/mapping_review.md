# Independent bounded daf/reference mapping review

**PASS: 11 amudim, 215 numbered Hebrew segments, zero normalized mismatches.** Separate AI source-reading audit; no human or Gemini review. Original named Wikisource Talmud Bavli files and schemas were read directly. Each amud was then requested from the live Sefaria API by its explicit reference and selected Hebrew version, and every segment was compared in order. This is stronger than reusing the local arithmetic alone; it is not independent textual-witness certification.

| Explicit ref | Local page index | Numbered segment span | API mismatches |
|---|---:|---|---:|
| Berakhot 2a | 2 | Berakhot 2a:1–Berakhot 2a:14 | 0 |
| Berakhot 2b | 3 | Berakhot 2b:1–Berakhot 2b:19 | 0 |
| Berakhot 3a | 4 | Berakhot 3a:1–Berakhot 3a:15 | 0 |
| Berakhot 3b | 5 | Berakhot 3b:1–Berakhot 3b:32 | 0 |
| Berakhot 4a | 6 | Berakhot 4a:1–Berakhot 4a:19 | 0 |
| Berakhot 4b | 7 | Berakhot 4b:1–Berakhot 4b:28 | 0 |
| Berakhot 5a | 8 | Berakhot 5a:1–Berakhot 5a:24 | 0 |
| Bava Metzia 21a | 40 | Bava Metzia 21a:1–Bava Metzia 21a:19 | 0 |
| Bava Metzia 21b | 41 | Bava Metzia 21b:1–Bava Metzia 21b:17 | 0 |
| Bava Metzia 22a | 42 | Bava Metzia 22a:1–Bava Metzia 22a:12 | 0 |
| Bava Metzia 22b | 43 | Bava Metzia 22b:1–Bava Metzia 22b:16 | 0 |

Schemas specify `addressTypes=[Talmud,Integer]`, `sectionNames=[Daf,Line]`, depth2. Both arrays begin with two empty placeholders. Preserve those placeholders: i=2 is2a, not3a. Within an amud, segment numbering is one-based. `Line` is an export segment, not a printed Vilna line. Exact per-segment mappings, hashes, endpoint URLs and response hashes are in [mapping_review.json](mapping_review.json).

Two independently addressed Wikisource pages corroborate page-level anchors: [Berakhot2a](https://he.wikisource.org/w/index.php?title=ברכות_ב_א&oldid=3006896) and [BavaMetzia21a](https://he.wikisource.org/wiki/בבא_מציעא_כא_א). The latter starts with the previous chapter’s receipt discussion; אלו מציאות starts at21a:7, and the page ends איתמר at21a:19, continued on21b. Wikisource does not separately certify Sefaria segment numbering and marks the BavaMetzia page not proofread. No anchor mismatch was observed.

License fields in both named local versions and the live Hebrew API are CC-BY-SA, without a numeric version. The [Wikisource footer](https://he.wikisource.org/wiki/ברכות_ב_א) states CC BY-SA4.0 with possible additional terms. Preserve named-version attribution and do not silently treat the unspecified local metadata as a distinct fully resolved license version. The API also returned an English edition with different CC-BY-NC terms; no English text is included in this audit.

Independence limits: the live service and local export share the Wikisource/Sefaria lineage. Checks establish addressed transcription consistency, not manuscript accuracy, semantic boundaries, or scholarly validity. No primary semantic annotations were read. No full corpus or API response copies were written. Future exact reruns may differ in volatile API metadata; normalized Hebrew comparison is the substantive check.
