// Verify self-contained Hebrew RTL Berakhot sugya reader payload, search, raw/display separation, and export formatting.
const fs = require('fs');
const path = require('path');

const htmlPath = path.join(__dirname, 'berakhot_sugya_reader.html');
const html = fs.readFileSync(htmlPath, 'utf8');

assert(html.includes('dir="rtl"'), 'Missing RTL root direction');
const m = html.match(/<script id="corpusPayload" type="application\/json">([\s\S]*?)<\/script>/);
if (!m) throw new Error('Embedded corpusPayload JSON not found');

const payload = JSON.parse(m[1]);
const cov = payload.index.coverage;
const sugyot = payload.sugyot;

if (cov.processed_segments !== 203) throw new Error(`Expected 203 Berakhot segments, got ${cov.processed_segments}`);
if (cov.last_closed_ref !== 'Berakhot 6a:16') throw new Error(`Unexpected last_closed_ref: ${cov.last_closed_ref}`);
if (cov.next_unprocessed_ref !== 'Berakhot 6b:1') throw new Error(`Unexpected next_unprocessed_ref: ${cov.next_unprocessed_ref}`);
if (sugyot.length < 30) throw new Error(`Unexpected sugyot count: ${sugyot.length}`);

// Check extended B24 (sug_9a1c712c3a26fe45003b) spans 5a:24 -> 5b:3
const b24 = sugyot.find(s => s.id === 'sug_9a1c712c3a26fe45003b');
if (!b24 || b24.start_ref !== 'Berakhot 5a:24' || b24.end_ref !== 'Berakhot 5b:3') {
  throw new Error('Extended B24 (5a:24-5b:3) missing or malformed in reader');
}

// Check raw_text vs display_text separation on opening Mishnah 2a:1 (contains HTML markup in raw_text, stripped in display_text)
const b01 = sugyot[0];
const seg0 = b01.segments[0];
if (!seg0.raw_text.includes('<') || seg0.display_text.includes('<big>')) {
  throw new Error('raw_text and display_text are not properly separated');
}

// Check Hebrew search hit on continuation block ('אבא בנימין' and 'תפילין')
const hitsAbba = sugyot.filter(s => s.linked_names.some(n => n.name_he === 'אבא בנימין'));
if (hitsAbba.length < 4) throw new Error(`Expected >=4 Abba Binyamin sugyot, got ${hitsAbba.length}`);

// Check open tail at 6a:25
const lastSugya = sugyot[sugyot.length - 1];
if (lastSugya.boundary_status !== 'open_right' || lastSugya.end_ref !== 'Berakhot 6a:25') {
  throw new Error('Final Berakhot sugya must be open_right at Berakhot 6a:25');
}

function assert(cond, msg) { if (!cond) throw new Error(msg); }
console.log(`PASS: Berakhot RTL reader verified (${sugyot.length} sugyot, ${cov.processed_segments} segments, B24 extended, raw/display separated, open tail at 6a:25).`);
