# Scholarly source feasibility — P0–P1 only

**Decision: PROVISIONAL_PENDING_REVIEW.** The seed-20261123 pilot produced 24 provisionally usable focal cases (17 outcome disputes, 7 interpretive alternatives), from 32 attempted occurrences representing 30 candidate source families after two documented merges. All attempts now have **ai_independent_double** readings, with scope disagreements preserved. No knowledgeable human has reviewed them. Initial named-assignment agreement among jointly eligible original attempts is **22/22**; eligibility agreement is **28/30**. Across all 32 attempts, preserved first-round eligibility agreement is **29/32**, and named-assignment agreement is **23/23**. After the recorded first-reader RS32 context extension these become **30/32** and **24/24**. Missing assignments are excluded from agreement denominators. The 20-of-30 yield and 90% conditional AI-assignment workflow criteria are provisionally met, but certified disjoint grouping and knowledgeable-human review remain pending. These are workflow criteria, not evidence of correctness.

The original planning branch `origin/research/metric-attribution-plan-20261123`, its RESEARCH_PLAN, NEXT_AGENT_PROMPT, and SOURCE_SNAPSHOT were consulted. Earlier P0–P1 boundaries, indexes, published IDs, confirmation plans and source corpora are preserved. Work was prepared on `codex/individual-decision-pilot-20261124`, based on `2c6d3466328752c220a9b1fc05c3c308553dab47`; the enclosing handoff records the final deliverable commit. Older plan references to a private repository are stale; no visibility change was made here.

## Reverified inventory

| Pair | Source locations | Bavli | Yerushalmi |
|---|---:|---:|---:|
| Rav–Shmuel | 512 | 423 | 89 |
| Abaye–Rava | 498 | 498 | 0 |
| Rabbi Yohanan–Resh Lakish | 563 | 338 | 225 |
| Rabbah–Rav Yosef | 101 | 101 | 0 |

These are 1,674 locations across pair inventories, not independent human observations, verified questions, or unique disputes. Hashes are in `scholar/source_manifest.json`. Rav–Shmuel and Abaye–Rava Git blobs exactly match the prior planning snapshot (`073a702c7ab59b2ed8e37fc4f42852be4a567dfb` and `cce41259b9b8aa064451eb0ef49ce76e41fd41b2`). The other two indexes were re-read and hashed without running historical builders.

## Draw, context, and failures

The sampling frame used conservative connected components of shared indexed context references across all four inventories. Within each of three tractate-defined strata, component hashes were sorted, shuffled using Python `random.Random(20261123)` in declared stratum order, and the first ten were selected. Focal occurrences use minimum `(work, json_index)`, independently of attribution. The exact pools and procedure are saved in `scholar/pilot_selection.json`.

The strata are tractate proxies: civil/property (three Bavas), Shabbat/festival (specified Moed tractates), and prayer/blessing (Berakhot). Reading exposed aggadic and dietary passages within these tractates; the report does **not** misrepresent them as purely legal or prayer cases. Retaining them avoids content-dependent replacement.

Two later links reduced the first 30 components to 28 candidate families:

- Bava Batra 152a:1 and 152b:4 explicitly refer to the same deathbed-gift discussion and alternate transmission (RS09/RS10).
- Pesachim 101a:7–9 repeats the named three-dispute bundle from Shabbat 22a:5–6, exposing answer-bearing material across RS11/RS13 even though the focal questions differ.

The next shuffled civil and festival candidates were appended as RS31/RS32, preserving the original attempts. Thus 32 attempted occurrences cover 30 current candidate families. These family counts remain provisional: semantic parallels outside the indexed context graph require further review. No test split is claimed.

Original local `merged.json` source files were available. Exact raw spans, normalized reading text, references, array indices, edition metadata and file SHA256 are retained. Context extraction covers 1,682 segments from eight tractates, usually three complete amudim per occurrence; Eruvin 49b was extended through 51a and Eruvin 42b back through 41b. Extraction itself is not a claim every unrelated segment was read. The AI read the focal discussion and relevant continuation recorded in the evidence notes. Source sufficiency is scoped to the displayed focal question under the merged edition, not manuscript-critical certification of the whole sugya.

Eight occurrence-level exclusions/pending records affect seven candidate families, one of which has another usable focal case:

| Reason | Occurrences | References/notes |
|---|---:|---|
| Anonymous named assignment unresolved | 3 | Bava Batra 91a:4; Berakhot 61a:7; Berakhot 10b:15 |
| Transaction/version scope pending | 2 | Bava Batra 152a:1 and 152b:4, one family; מיפה את כחו and the Pumbedita report need a tighter transaction schema |
| Duplicate answer-bearing family plus atomic-scope concern | 1 | Shabbat 22a:5 grouped with the usable Pesachim 100b:5 family; direct/intermediate flame scope not forced into a clean label |
| Alternative derivation of shared norm | 1 | Berakhot 14a:11–14 |
| Explicit reconciliation | 1 | Berakhot 38a:8–13: thick versus thin שתיתא, ולא פליגי |

The six-family remainder is the three anonymous families, the shared-norm derivation, the reconciled case, and the pending gift family. The Shabbat/Pesachim merged family **does** have a usable focal case. Thus 30 candidate families minus 24 usable focal families = 6 pending/excluded families. Every excluded occurrence remains in `attempted_families.jsonl` and `evidence_records.jsonl`.

Key qualifications were preserved rather than erased: the tannaitic inversion at Bava Batra 65a:1; the rejected general majority/proximity explanation at 24a:10–11; the eight-amot/reachability conditions at Eruvin 50b; the two after-matzah versions at Pesachim 120a; the challenged Rav transmission at Berakhot 25a; Rav Asi as a distinct third speaker at Bava Batra 62b; and the unresolved Rav-versus-Rav קשיא at Shabbat 56a. Attributions denote explicit positions in this version, not final practical rulings or harmonized scholar-wide beliefs.

## Views and review status

`scholar/evidence_records.jsonl` holds source-linked evidence, named assignments, qualifications, and Hebrew paraphrase provenance. `prediction_inputs.jsonl` contains only a hashed case identifier, neutral Hebrew question/conditions, and two content-hashed alternative texts. Alternatives are sorted by their content hashes, not by named scholar. Source addresses, transmission chains, named amoraim, labels, and commentary-derived explanations are absent from that view. This prevents obvious field leakage; literary recognizability and memorization remain possible and require independent checking before modeling.

The first saved AI decisions remain in `initial_reviews_round1.jsonl`. The same reader then resolved RS32's initially missing boundary by reading Eruvin 41b:6–8; `initial_reviews.jsonl` contains that later state. This self-correction is **not** an independent review. A separate AI reader subsequently read source evidence before seeing those judgments, froze `second_review.jsonl` (SHA256 `df45928a843dfe445d469eac184ae1569bfd02047467fa482affbc803e3de7cf`), then compared its independently authored paraphrases and checked the neutral inputs. See `INDEPENDENT_REVIEW.md` for the precise scope. Agreement is semantic matching of named positions, not string identity or source correctness. No withheld confirmation material was scored.

`review_disagreements.jsonl` preserves RS10's conditional-interpretation versus pending-transaction judgment, RS21's interpretive versus shared-norm exclusion, and RS32's original boundary failure. RS10 stays pending and RS21 stays excluded under the current scope; these are adjudicated decisions, not invented consensus. The second reader also found a missing condition in RS14. After reading Eruvin 7a:4–5 and 12–15, the first reader corrected the neutral view to specify public thoroughfares at both ends, distinguish legal rule from public-instruction variants, and require a door capable of closing (6b:9). The substantive Rav/Shmuel assignment did not change. `prediction_inputs_pre_second_review.jsonl` preserves the earlier neutral views. Unresolved anonymous attributions and version issues remain unassigned; RS22 retains its contested-transmission qualification.

## Person–case overlap graph

`person_case_overlap_graph.json`, `occurrence_family_map.jsonl`, `family_relationships.jsonl`, and `cross_inventory_overlap.jsonl` provide an inventory-level graph. There are 1,276 initial context components; 161 shared-reference cross-inventory edges connect 67 distinct occurrence pairs. These counts are mechanical and precede the two manual pilot links saved separately. The graph's scholar labels come from pair inventories; they are not individually certified case responses.

Eight principal scholar identities are not a large sample of independent people. Context overlap creates candidate bridges among the pair banks, but incidental nearby discussion is not a shared comparable question. A mechanically connected graph therefore does not identify a common psychological or halachic scale. Conversely, disconnected pair banks could not identify that scale either. No silence or unmentioned scholar is treated as a negative answer. Before any simulation, annotate genuinely shared questions and corresponding alternatives, including agreements and single-scholar statements sampled independently of disputes.

## Verification and endpoint

Run the three commands in `scholar/README.md`. The verifier passed: 32 unique attempt IDs, 30 current family IDs, 24 distinct usable focal families, valid complete paired assignments, exact matching raw source spans and array-derived references, source hashes, neutral-view fields and obvious name/address masking. These checks establish engineering integrity, not scholarly truth. Original report UI was not modified or regenerated.

Resources: no downloads, no paid calls, no model fitting, embeddings, scholar simulation, or confirmation scoring. Source preparation and checking use standard-library Python and local files; no human-review claim or model-performance estimate is made.

The justified next task is knowledgeable-human source review and parallel-family adjudication of these 30 candidate families, concentrating on the six unusable families, transaction/version ambiguity, and documented cross-case parallels. The independent AI neutral-view check is complete with the recorded RS14 repair; it does not rule out memorized source recognition. Preserve initial decisions and disagreements. Only then reconsider benchmark construction; scholarly training and earlier confirmation scoring remain outside this completed preparation cycle.
