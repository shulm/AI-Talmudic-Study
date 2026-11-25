"""Cumulative per-sugya JSONL export, compact index, and self-contained Hebrew RTL reader for Berakhot.

Strictly separates display HTML stripping from untouched raw Wikisource text and preserves CC-BY-SA attribution.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import pipeline as p


ATTRIBUTION_NOTICE = {
    "edition": "Wikisource Talmud Bavli",
    "version_source": "https://he.wikisource.org/wiki/תלמוד_בבלי",
    "license": "CC-BY-SA",
    "attribution": "Wikisource contributors and Sefaria export (pinned local snapshot; bounded processed range only, not a full corpus copy).",
    "display_note": "display_text removes HTML tags for reading only; raw_text preserves exact source bytes.",
}


def build_berakhot_exports(base_dir: Path) -> dict[str, Any]:
    segments = {s["id"]: s for s in p.rows(base_dir / "data/segments.jsonl")}
    sugyot = p.rows(base_dir / "data/sugyot.jsonl")
    scholars = {s["id"]: s for s in p.rows(base_dir / "data/scholars.jsonl")}
    statements = p.rows(base_dir / "data/statements.jsonl")
    questions = p.rows(base_dir / "data/questions.jsonl")
    reviews = p.rows(base_dir / "data/review_queue.jsonl")

    ber_primary = [
        g for g in sugyot if g["tractate"] == "Berakhot" and g["level"] == "primary"
    ]
    ber_primary.sort(key=lambda g: segments[g["segment_ids"][0]]["source_index"])
    ber_subs = [
        g for g in sugyot if g["tractate"] == "Berakhot" and g["level"] == "sub_sugya"
    ]

    stmts_by_sugya: dict[str, list[dict[str, Any]]] = {}
    for st in statements:
        stmts_by_sugya.setdefault(st["sugya_id"], []).append(st)

    qs_by_sugya: dict[str, list[dict[str, Any]]] = {}
    for q in questions:
        qs_by_sugya.setdefault(q["sugya_id"], []).append(q)

    export_rows: list[dict[str, Any]] = []
    compact_index_rows: list[dict[str, Any]] = []

    for order_num, g in enumerate(ber_primary, 1):
        gid = g["id"]
        g_segs = [segments[sid] for sid in g["segment_ids"]]
        seg_id_set = set(g["segment_ids"])
        g_stmts = stmts_by_sugya.get(gid, [])
        g_qs = qs_by_sugya.get(gid, [])
        g_subs = [sub for sub in ber_subs if sub["parent_id"] == gid]

        # Derive short Hebrew summary: use v1.1.0 summary_he if present, else pilot main question + first claim summaries
        if "summary_he" in g:
            summary_he = g["summary_he"]
        else:
            q_txt = g_qs[0]["question_he"] if g_qs else ""
            top_claims = [
                st["summary_he"]
                for st in g_stmts
                if not st["authoring_key"].startswith("unit_")
            ][:3]
            summary_he = (q_txt + (" — " + "؛ ".join(top_claims) if top_claims else "")).strip(" —")

        # Linked names: combine v1.1.0 name_mentions and v1.0.0 statement scholar links
        linked_names: list[dict[str, Any]] = []
        seen_name_keys: set[tuple[str, str]] = set()
        for nm in g.get("name_mentions", []):
            k = (nm["name_he"], nm["role"])
            if k not in seen_name_keys:
                seen_name_keys.add(k)
                linked_names.append(
                    {
                        "scholar_id": nm["scholar_id"],
                        "name_he": nm["name_he"],
                        "role": nm["role"],
                        "attribution_status": nm["attribution_status"],
                        "transmitters_he": [scholars[tid]["name_he"] for tid in nm["transmitter_ids"]],
                        "candidates_he": [scholars[cid]["name_he"] for cid in nm["candidate_ids"]],
                        "ref": nm["evidence"][0]["ref"],
                    }
                )
        for st in g_stmts:
            if st["attributed_authority_id"]:
                nm_he = scholars[st["attributed_authority_id"]]["name_he"]
                role = "quoted_authority" if st["transmitter_ids"] else "attributed_authority"
                k = (nm_he, role)
                if k not in seen_name_keys:
                    seen_name_keys.add(k)
                    linked_names.append(
                        {
                            "scholar_id": st["attributed_authority_id"],
                            "name_he": nm_he,
                            "role": role,
                            "attribution_status": st["attribution_status"],
                            "transmitters_he": [scholars[tid]["name_he"] for tid in st["transmitter_ids"]],
                            "candidates_he": [],
                            "ref": st["evidence"][0]["ref"],
                        }
                    )
            for tid in st["transmitter_ids"]:
                t_he = scholars[tid]["name_he"]
                k = (t_he, "transmitter")
                if k not in seen_name_keys:
                    seen_name_keys.add(k)
                    linked_names.append(
                        {
                            "scholar_id": tid,
                            "name_he": t_he,
                            "role": "transmitter",
                            "attribution_status": "transmitted",
                            "transmitters_he": [],
                            "candidates_he": [],
                            "ref": st["evidence"][0]["ref"],
                        }
                    )
            if st["speaker_candidates"]:
                c_names = [scholars[cid]["name_he"] for cid in st["speaker_candidates"]]
                label = " / ".join(c_names)
                k = (label, "unresolved_candidate_group")
                if k not in seen_name_keys:
                    seen_name_keys.add(k)
                    linked_names.append(
                        {
                            "scholar_id": None,
                            "name_he": label,
                            "role": "unresolved_candidate_group",
                            "attribution_status": "unresolved_alternatives",
                            "transmitters_he": [],
                            "candidates_he": c_names,
                            "ref": st["evidence"][0]["ref"],
                        }
                    )

        # Unresolved review items touching this sugya or its statements/segments (excluding generic per-segment extraction markers in summary count, while listing non-trivial items + count of deferred segment extractions)
        stmt_ids = {st["id"] for st in g_stmts}
        sugya_reviews = [
            r
            for r in reviews
            if r["status"] == "open"
            and (
                gid in r["target_ids"]
                or bool(stmt_ids & set(r["target_ids"]))
                or (
                    r["issue_type"] != "semantic_extraction_pending"
                    and bool(seg_id_set & set(r["target_ids"]))
                )
            )
        ]
        deferred_seg_count = sum(
            1
            for r in reviews
            if r["status"] == "open"
            and r["issue_type"] == "semantic_extraction_pending"
            and bool(seg_id_set & set(r["target_ids"]))
        )

        daf_list: list[str] = []
        for s in g_segs:
            daf = s["ref"].split()[1].split(":")[0]
            if daf not in daf_list:
                daf_list.append(daf)

        exp_rec = {
            "order_in_tractate": order_num,
            "id": gid,
            "authoring_key": g["authoring_key"],
            "schema_version": g["schema_version"],
            "tractate": "Berakhot",
            "tractate_he": "ברכות",
            "start_ref": g["start_ref"],
            "end_ref": g["end_ref"],
            "dafs": daf_list,
            "crosses_amud": len(daf_list) > 1,
            "title_he": g["title_he"],
            "summary_he": summary_he,
            "summary_origin": "editorial_paraphrase",
            "boundary_status": g["boundary_status"],
            "pending_continuation": g.get(
                "pending_continuation",
                {
                    "is_open": g["boundary_status"] != "provisional",
                    "direction": "right" if g["boundary_status"] == "open_right" else "none",
                    "next_unprocessed_ref": None,
                    "context_preview_refs": [],
                    "note_he": None,
                },
            ),
            "construction_status": g.get("construction_status", "pilot_segmented"),
            "extraction_status": g.get("extraction_status", g["annotation_completeness"]),
            "span_review_status": g.get("span_review_status", "pilot_reviewed_partial_blind"),
            "review_status": "ai_provisional",
            "ml_eligible": False,
            "conditions_he": g.get("conditions", []),
            "uncertainty_notes_he": g.get("uncertainty_notes_he", []),
            "sub_sugyot": [
                {
                    "id": sub["id"],
                    "authoring_key": sub["authoring_key"],
                    "start_ref": sub["start_ref"],
                    "end_ref": sub["end_ref"],
                    "title_he": sub["title_he"],
                    "summary_he": sub.get("summary_he", ""),
                }
                for sub in g_subs
            ],
            "segments": [
                {
                    "id": s["id"],
                    "ref": s["ref"],
                    "short_ref": s["ref"].replace("Berakhot ", ""),
                    "raw_text": s["text"],
                    "display_text": p.plain(s["text"]).strip(),
                    "text_sha256": s["text_sha256"],
                }
                for s in g_segs
            ],
            "linked_names": linked_names,
            "unresolved_items": [
                {
                    "id": r["id"],
                    "issue_type": r["issue_type"],
                    "description_he": r["description_he"],
                }
                for r in sugya_reviews
            ],
            "deferred_atomic_extraction_segments": deferred_seg_count,
            "source_attribution": ATTRIBUTION_NOTICE,
        }
        export_rows.append(exp_rec)
        compact_index_rows.append(
            {
                "order": order_num,
                "id": gid,
                "key": g["authoring_key"],
                "start_ref": g["start_ref"],
                "end_ref": g["end_ref"],
                "dafs": daf_list,
                "segment_count": len(g_segs),
                "title_he": g["title_he"],
                "boundary_status": g["boundary_status"],
                "construction_status": exp_rec["construction_status"],
                "extraction_status": exp_rec["extraction_status"],
                "span_review_status": exp_rec["span_review_status"],
                "linked_names_count": len(linked_names),
                "unresolved_items_count": len(sugya_reviews),
            }
        )

    exports_dir = base_dir / "exports"
    exports_dir.mkdir(parents=True, exist_ok=True)
    p.jsonl(exports_dir / "berakhot_sugyot_cumulative.jsonl", export_rows)

    closed_units = [r for r in export_rows if r["boundary_status"] == "provisional"]
    open_units = [r for r in export_rows if r["boundary_status"] != "provisional"]
    total_ber_segs = sum(len(r["segments"]) for r in export_rows)

    index_doc = {
        "schema_version": "1.1.0",
        "tractate": "Berakhot",
        "tractate_he": "ברכות",
        "source_attribution": ATTRIBUTION_NOTICE,
        "provisional_notice": "All segmentation and editorial fields are AI-provisional and ML-ineligible (ml_eligible=false). Not a completed masechet.",
        "coverage": {
            "total_tractate_segments_in_edition": 2749,
            "processed_segments": total_ber_segs,
            "processed_daf_range": "2a-6a",
            "primary_sugyot_count": len(export_rows),
            "last_closed_ref": closed_units[-1]["end_ref"] if closed_units else None,
            "open_tails": [
                {
                    "id": u["id"],
                    "key": u["authoring_key"],
                    "start_ref": u["start_ref"],
                    "end_ref": u["end_ref"],
                    "next_unprocessed_ref": u["pending_continuation"].get("next_unprocessed_ref"),
                }
                for u in open_units
            ],
            "next_unprocessed_ref": "Berakhot 6b:1",
        },
        "sugyot": compact_index_rows,
    }
    p.write(exports_dir / "berakhot_index.json", index_doc)

    html_str = _render_rtl_reader_html(index_doc, export_rows)
    (exports_dir / "berakhot_sugya_reader.html").write_text(html_str, encoding="utf-8", newline="\n")
    return {
        "sugyot_exported": len(export_rows),
        "segments_exported": total_ber_segs,
        "last_closed_ref": index_doc["coverage"]["last_closed_ref"],
        "next_unprocessed_ref": index_doc["coverage"]["next_unprocessed_ref"],
    }


def _render_rtl_reader_html(index_doc: dict[str, Any], export_rows: list[dict[str, Any]]) -> str:
    payload_json = json.dumps(
        {"index": index_doc, "sugyot": export_rows}, ensure_ascii=False
    ).replace("</", "<\\/")

    return f"""<!DOCTYPE html>
<html lang="he" dir="rtl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>קורא סוגיות — מסכת ברכות (ב ע״א – ו ע״א) | מאגר זמני v1.1</title>
<style>
  :root {{
    --bg: #f7f5f0;
    --panel: #ffffff;
    --ink: #1e242b;
    --muted: #5a6572;
    --accent: #1d4e89;
    --accent-soft: #e8f0fa;
    --warn-bg: #fff8e6;
    --warn-border: #e0a800;
    --border: #dcd7cc;
  }}
  * {{ box-sizing: border-box; }}
  body {{
    margin: 0;
    font-family: "David Libre", "Frank Ruhl Libre", "SBL Hebrew", "Times New Roman", serif;
    background: var(--bg);
    color: var(--ink);
    line-height: 1.65;
  }}
  header {{
    background: #162638;
    color: #f8f9fa;
    padding: 14px 22px;
    border-bottom: 3px solid #c99a2e;
  }}
  header h1 {{ margin: 0 0 4px 0; font-size: 1.35rem; }}
  .meta-bar {{
    font-family: system-ui, -apple-system, sans-serif;
    font-size: 0.84rem;
    color: #d5dde6;
    display: flex;
    flex-wrap: wrap;
    gap: 14px;
  }}
  .badge-warn {{
    background: #5c4300;
    color: #ffe8a1;
    padding: 2px 8px;
    border-radius: 4px;
    font-weight: 600;
  }}
  .layout {{
    display: grid;
    grid-template-columns: 350px 1fr;
    min-height: calc(100vh - 84px);
  }}
  aside {{
    background: var(--panel);
    border-left: 1px solid var(--border);
    display: flex;
    flex-direction: column;
    max-height: calc(100vh - 84px);
    position: sticky;
    top: 0;
  }}
  .controls {{
    padding: 12px;
    border-bottom: 1px solid var(--border);
    font-family: system-ui, -apple-system, sans-serif;
    display: flex;
    flex-direction: column;
    gap: 8px;
  }}
  .controls input, .controls select {{
    width: 100%;
    padding: 7px 10px;
    border: 1px solid var(--border);
    border-radius: 6px;
    font-size: 0.9rem;
    direction: rtl;
  }}
  .sugya-list {{
    overflow-y: auto;
    flex: 1;
    padding: 8px;
  }}
  .sugya-item {{
    padding: 9px 11px;
    border-radius: 6px;
    cursor: pointer;
    border: 1px solid transparent;
    margin-bottom: 5px;
  }}
  .sugya-item:hover {{ background: #f2efe8; }}
  .sugya-item.active {{
    background: var(--accent-soft);
    border-color: var(--accent);
  }}
  .sugya-item-top {{
    font-family: system-ui, -apple-system, sans-serif;
    font-size: 0.78rem;
    color: var(--muted);
    display: flex;
    justify-content: space-between;
  }}
  .sugya-item-title {{ font-weight: 700; font-size: 1rem; }}
  .open-pill {{
    background: var(--warn-bg);
    border: 1px solid var(--warn-border);
    color: #7a5600;
    font-size: 0.72rem;
    padding: 0 6px;
    border-radius: 4px;
  }}
  main {{
    padding: 22px 30px;
    max-width: 980px;
  }}
  .card {{
    background: var(--panel);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 20px 24px;
    margin-bottom: 18px;
  }}
  .toolbar {{
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    justify-content: space-between;
    align-items: center;
    font-family: system-ui, -apple-system, sans-serif;
    margin-bottom: 12px;
  }}
  button {{
    font-family: system-ui, -apple-system, sans-serif;
    font-size: 0.85rem;
    padding: 6px 12px;
    border-radius: 6px;
    border: 1px solid var(--border);
    background: #fff;
    cursor: pointer;
  }}
  button.primary {{
    background: var(--accent);
    color: #fff;
    border-color: var(--accent);
  }}
  .sugya-text {{
    font-size: 1.28rem;
    line-height: 1.95;
    text-align: justify;
    padding: 14px 18px;
    background: #fcfbf8;
    border-right: 4px solid var(--accent);
    border-radius: 4px;
  }}
  .seg-ref {{
    font-family: system-ui, -apple-system, sans-serif;
    font-size: 0.74rem;
    color: var(--accent);
    background: var(--accent-soft);
    padding: 1px 6px;
    border-radius: 4px;
    margin: 0 4px;
    vertical-align: middle;
    direction: ltr;
    display: inline-block;
  }}
  .raw-pre {{
    white-space: pre-wrap;
    font-family: "Courier New", monospace;
    font-size: 0.95rem;
    background: #f4f4f4;
    padding: 12px;
    border-radius: 6px;
  }}
  .chips {{ display: flex; flex-wrap: wrap; gap: 6px; margin-top: 8px; }}
  .chip {{
    font-family: system-ui, -apple-system, sans-serif;
    font-size: 0.8rem;
    background: #eef2f6;
    border: 1px solid #cfd8e3;
    padding: 3px 9px;
    border-radius: 14px;
  }}
  .chip.unresolved {{ background: var(--warn-bg); border-color: var(--warn-border); }}
  .section-label {{
    font-family: system-ui, -apple-system, sans-serif;
    font-size: 0.85rem;
    font-weight: 700;
    color: var(--muted);
    margin: 14px 0 6px 0;
  }}
  .review-box {{
    font-family: system-ui, -apple-system, sans-serif;
    font-size: 0.86rem;
    background: var(--warn-bg);
    border: 1px solid var(--warn-border);
    border-radius: 6px;
    padding: 8px 12px;
    margin-top: 6px;
  }}
  footer {{
    font-family: system-ui, -apple-system, sans-serif;
    font-size: 0.78rem;
    color: var(--muted);
    margin-top: 16px;
  }}
  @media (max-width: 860px) {{
    .layout {{ grid-template-columns: 1fr; }}
    aside {{ max-height: 340px; position: static; }}
  }}
</style>
</head>
<body>
<header>
  <h1>מסכת ברכות — קורא סוגיות רציף (ב ע״א – ו ע״א)</h1>
  <div class="meta-bar" id="headerMeta"></div>
</header>
<div class="layout">
  <aside>
    <div class="controls">
      <input type="search" id="searchInput" placeholder="חיפוש בלשון הגמרא, כותרת, תקציר או שם חכם...">
      <div style="display:flex; gap:6px;">
        <select id="dafFilter"><option value="all">כל הדפים (2a–6a)</option></select>
        <select id="statusFilter">
          <option value="all">כל הסוגיות</option>
          <option value="open">זנב פתוח (open_right)</option>
          <option value="continuation">בלוק המשך (5b–6a)</option>
        </select>
      </div>
      <div id="countSummary" style="font-size:0.8rem; color:var(--muted);"></div>
    </div>
    <div class="sugya-list" id="sugyaList"></div>
  </aside>
  <main>
    <div id="detailPane"></div>
  </main>
</div>

<script id="corpusPayload" type="application/json">{payload_json}</script>
<script>
const DATA = JSON.parse(document.getElementById('corpusPayload').textContent);
const SUGYOT = DATA.sugyot;
const INDEX = DATA.index;

function stripNikud(s) {{
  return (s || '').replace(/[\\u0591-\\u05C7]/g, '').replace(/["״׳']/g, '');
}}

let state = {{
  selectedId: SUGYOT.length ? SUGYOT[0].id : null,
  query: '',
  daf: 'all',
  status: 'all',
  showRaw: false
}};

function initFilters() {{
  const cov = INDEX.coverage;
  document.getElementById('headerMeta').innerHTML =
    `<span class="badge-warn">זמני בלבד · ml_eligible=false</span>` +
    `<span>כיסוי: ${{cov.processed_segments}} / ${{cov.total_tractate_segments_in_edition}} קטעים (${{cov.processed_daf_range}})</span>` +
    `<span>סוגיות ראשיות: ${{cov.primary_sugyot_count}}</span>` +
    `<span>סגור אחרון: ${{cov.last_closed_ref}}</span>` +
    `<span>הבא בתור: ${{cov.next_unprocessed_ref}}</span>` +
    `<span>מקור: Wikisource Talmud Bavli (CC-BY-SA)</span>`;

  const dafs = new Set();
  SUGYOT.forEach(s => s.dafs.forEach(d => dafs.add(d)));
  const dafSel = document.getElementById('dafFilter');
  Array.from(dafs).forEach(d => {{
    const opt = document.createElement('option');
    opt.value = d;
    opt.textContent = 'דף ' + d;
    dafSel.appendChild(opt);
  }});
}}

function matchesSugya(s, qNorm, daf, status) {{
  if (daf !== 'all' && !s.dafs.includes(daf)) return false;
  if (status === 'open' && s.boundary_status === 'provisional') return false;
  if (status === 'continuation' && s.schema_version !== '1.1.0') return false;
  if (!qNorm) return true;
  const hay = stripNikud([
    s.authoring_key,
    s.title_he,
    s.summary_he,
    s.start_ref,
    s.end_ref,
    ...s.segments.map(x => x.display_text),
    ...s.linked_names.map(n => n.name_he)
  ].join(' '));
  return hay.includes(qNorm);
}}

function formatPlainTextExport(s) {{
  const lines = [
    `סוגיה ${{s.authoring_key}} (${{s.id}}) — ${{s.title_he}}`,
    `טווח: ${{s.start_ref}} – ${{s.end_ref}} | מצב גבול: ${{s.boundary_status}} | מעמד: זמני (ml_eligible=false)`,
    `תקציר עריכה: ${{s.summary_he}}`,
    `מקור ורישיון: ${{s.source_attribution.edition}} (${{s.source_attribution.license}}) — ${{s.source_attribution.version_source}}`,
    `--- נוסח המקור (תצוגה נקייה מתגיות HTML; הנוסח הגולמי שמור ב-JSON) ---`,
    ...s.segments.map(seg => `[${{seg.ref}}] ${{seg.display_text}}`),
  ];
  if (s.linked_names.length) {{
    lines.push(`--- שמות ותפקידים מזוהים ---`);
    s.linked_names.forEach(n => lines.push(`- ${{n.name_he}} (${{n.role}}, ${{n.ref}})`));
  }}
  if (s.unresolved_items.length) {{
    lines.push(`--- פריטי ביקורת פתוחים ---`);
    s.unresolved_items.forEach(r => lines.push(`- [${{r.issue_type}}] ${{r.description_he}}`));
  }}
  return lines.join('\\n');
}}

function downloadBlob(filename, content, mime) {{
  const blob = new Blob([content], {{ type: mime }});
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = filename;
  document.body.appendChild(a);
  a.click();
  a.remove();
  URL.revokeObjectURL(url);
}}

function render() {{
  const qNorm = stripNikud(state.query.trim());
  const filtered = SUGYOT.filter(s => matchesSugya(s, qNorm, state.daf, state.status));
  document.getElementById('countSummary').textContent =
    `מוצגות ${{filtered.length}} מתוך ${{SUGYOT.length}} סוגיות`;

  if (filtered.length && !filtered.some(s => s.id === state.selectedId)) {{
    state.selectedId = filtered[0].id;
  }}

  const listEl = document.getElementById('sugyaList');
  listEl.innerHTML = '';
  filtered.forEach(s => {{
    const div = document.createElement('div');
    div.className = 'sugya-item' + (s.id === state.selectedId ? ' active' : '');
    const openBadge = s.boundary_status !== 'provisional' ? `<span class="open-pill">${{s.boundary_status}}</span>` : '';
    div.innerHTML =
      `<div class="sugya-item-top"><span>${{s.authoring_key}} · ${{s.start_ref.replace('Berakhot ','')}}–${{s.end_ref.replace('Berakhot ','')}}</span>${{openBadge}}</div>` +
      `<div class="sugya-item-title">${{s.title_he}}</div>`;
    div.onclick = () => {{ state.selectedId = s.id; render(); }};
    listEl.appendChild(div);
  }});

  const pane = document.getElementById('detailPane');
  const cur = filtered.find(s => s.id === state.selectedId);
  if (!cur) {{
    pane.innerHTML = '<div class="card">לא נמצאו סוגיות מתאימות לחיפוש.</div>';
    return;
  }}

  const roleLabels = {{
    attributed_authority: 'בעל המימרא',
    quoted_authority: 'מקור מצוטט',
    transmitter: 'מוסר',
    speaker: 'דובר',
    unresolved_candidate_group: 'ייחוס לא מוכרע (חד אמר / חילופי גירסה)',
    interlocutor: 'משתתף בדו-שיח'
  }};

  const textHtml = state.showRaw
    ? `<div class="raw-pre">${{cur.segments.map(seg => `[${{seg.ref}}] ${{seg.raw_text.replace(/&/g,'&amp;').replace(/</g,'&lt;')}}`).join('\\n')}}</div>`
    : `<div class="sugya-text">${{cur.segments.map(seg => `<span class="seg-ref">${{seg.short_ref}}</span><span>${{seg.display_text}}</span>`).join(' ')}}</div>`;

  const namesHtml = cur.linked_names.length
    ? `<div class="chips">${{cur.linked_names.map(n => {{
        const cls = n.attribution_status === 'unresolved_alternatives' ? 'chip unresolved' : 'chip';
        const via = n.transmitters_he && n.transmitters_he.length ? ` (מפי ${{n.transmitters_he.join(' ← ')}})` : '';
        return `<span class="${{cls}}"><strong${{}}> ${{n.name_he}}</strong> · ${{roleLabels[n.role] || n.role}}${{via}} [${{n.ref.replace('Berakhot ','')}}]</span>`;
      }}).join('')}}</div>`
    : `<div style="font-size:0.9rem;color:var(--muted);">סוגיה סתמאית / ללא שמות חכמים מפורשים בחילוץ הנוכחי.</div>`;

  const subsHtml = cur.sub_sugyot.length
    ? `<div class="section-label">תתי-סוגיות מובחנות ברצף</div>` +
      cur.sub_sugyot.map(sub => `<div class="chip">${{sub.authoring_key}}: ${{sub.title_he}} (${{sub.start_ref.replace('Berakhot ','')}}–${{sub.end_ref.replace('Berakhot ','')}})</div>`).join(' ')
    : '';

  const revHtml = cur.unresolved_items.map(r =>
    `<div class="review-box"><strong>${{r.issue_type}}:</strong> ${{r.description_he}}</div>`
  ).join('');

  const pendingNote = cur.pending_continuation && cur.pending_continuation.is_open
    ? `<div class="review-box"><strong>המשך פתוח מעבר לגבול הבלוק (${{cur.boundary_status}}):</strong> ${{cur.pending_continuation.note_he || ''}} (הקטע הבא: ${{cur.pending_continuation.next_unprocessed_ref || ''}})</div>`
    : '';

  pane.innerHTML = `
    <div class="card">
      <div class="toolbar">
        <div>
          <span style="font-weight:700; color:var(--accent);">${{cur.authoring_key}}</span> ·
          <span>${{cur.start_ref}} – ${{cur.end_ref}}</span> ·
          <span style="color:var(--muted); font-size:0.82rem;">ID: ${{cur.id}}</span>
        </div>
        <div style="display:flex; gap:6px; flex-wrap:wrap;">
          <button id="btnToggleRaw">${{state.showRaw ? 'תצוגת קריאה נקייה' : 'הצג נוסח גולמי (Raw Markup)'}}</button>
          <button id="btnExportTxt">ייצוא סוגיה ל-TXT</button>
          <button class="primary" id="btnExportJson">ייצוא סוגיה ל-JSON</button>
        </div>
      </div>
      <h2 style="margin:4px 0 8px 0;">${{cur.title_he}}</h2>
      <p style="margin:0 0 14px 0; color:#2e3842;"><strong>תקציר עריכה (פרפרזה):</strong> ${{cur.summary_he}}</p>
      <div style="font-family:system-ui,sans-serif; font-size:0.79rem; color:var(--muted); margin-bottom:12px;">
        בנייה: <code>${{cur.construction_status}}</code> ·
        חילוץ: <code>${{cur.extraction_status}}</code> ·
        ביקורת: <code>${{cur.span_review_status}}</code> ·
        קטעים הממתינים לפירוק אטומי: <code>${{cur.deferred_atomic_extraction_segments}}</code>
      </div>
      ${{pendingNote}}
      ${{textHtml}}
      ${{subsHtml}}
      <div class="section-label">חכמים, מוסרים ותפקידים במקור</div>
      ${{namesHtml}}
      <div class="section-label">פריטי ביקורת ואי-ודאות פתוחים (${{cur.unresolved_items.length}})</div>
      ${{revHtml}}
      <footer>
        מקור הטקסט: ${{cur.source_attribution.edition}} (${{cur.source_attribution.license}}) · תצוגת הקריאה מסירה תגיות HTML בלבד ואינה משנה את נוסח המקור החתום ב-SHA256.
      </footer>
    </div>
  `;

  document.getElementById('btnToggleRaw').onclick = () => {{ state.showRaw = !state.showRaw; render(); }};
  document.getElementById('btnExportJson').onclick = () => {{
    downloadBlob(`berakhot_${{cur.authoring_key}}_${{cur.id}}.json`, JSON.stringify(cur, null, 2) + '\\n', 'application/json;charset=utf-8');
  }};
  document.getElementById('btnExportTxt').onclick = () => {{
    downloadBlob(`berakhot_${{cur.authoring_key}}_${{cur.id}}.txt`, formatPlainTextExport(cur) + '\\n', 'text/plain;charset=utf-8');
  }};
}}

document.getElementById('searchInput').oninput = e => {{ state.query = e.target.value; render(); }};
document.getElementById('dafFilter').onchange = e => {{ state.daf = e.target.value; render(); }};
document.getElementById('statusFilter').onchange = e => {{ state.status = e.target.value; render(); }};

initFilters();
render();
</script>
</body>
</html>
"""
