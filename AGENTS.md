# Instructions for AI agents

- Read `AGENT_HANDOFF.md` before continuing research.
- The user's main interests are Talmudic and halachic commentary and preparing Hebrew chaburot, discussions, conclusions, and lessons.
- Preserve accurate quotations, speaker attribution, and references. Clearly separate source text from your explanations and inferences.
- Do not equate a nearby occurrence of רב and שמואל with a dispute. Exclude other amoraim such as רב אסי and רב יהודה when the intended speaker is Rav himself.
- In חד אמר / וחד אמר passages, do not assign views by name order. Check whether the continuation identifies the speakers.
- Read the continuation for איפוך, תסתיים, לא פליגי, alternative versions, retractions, and rejected assumptions.
- Keep parallel source occurrences, but distinguish occurrence counts from unique-topic counts.
- Treat raw candidates as unverified. The current selected index has only first-pass excerpt review, not full-sugya verification.
- Never modify the user's source corpora in place. Put derived data and corrections in this project.
- Do not commit credentials, environment files, cache directories, or full corpus copies.
- Preserve this repository's private visibility unless the user explicitly requests a change.
- Validate changes to the generated report with `node rav_shmuel_results/verify_report.cjs`. This checks UI logic only, not scholarly accuracy.
