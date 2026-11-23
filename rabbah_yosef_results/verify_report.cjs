// UI behavior only; does not certify scholarly accuracy.
const fs=require('fs'),vm=require('vm'),path=require('path'),assert=require('assert');
const html=fs.readFileSync(path.join(__dirname,'מחלוקות_רבה_ורב_יוסף.html'),'utf8');
const data=html.match(/<script id="data" type="application\/json">([\s\S]*?)<\/script>/)[1],D=JSON.parse(data);
assert(!html.includes('</option value='));
for(const v of ['Bavli','Yerushalmi','dispute','reconciled'])assert(html.includes('<option value="'+v+'">'));
const scripts=[...html.matchAll(/<script(?: [^>]*)?>([\s\S]*?)<\/script>/g)],elements=new Map();
function get(id){if(!elements.has(id))elements.set(id,{value:'',innerHTML:'',textContent:id==='data'?data:'',addEventListener(){}});return elements.get(id)}
const context={document:{getElementById:get,querySelector:s=>get(s.slice(1))},console};
vm.createContext(context);vm.runInContext(scripts.at(-1)[1],context);
assert.equal((get('results').innerHTML.match(/<article>/g)||[]).length,25);
get('q').value='כופין';vm.runInContext('render(true)',context);
assert(get('results').innerHTML.includes('Bava Batra 12b'));
get('q').value='';get('branch').value='Yerushalmi';vm.runInContext('render(true)',context);
assert(get('count').textContent.startsWith((D.metadata.branch_counts.Yerushalmi||0)+' '));
get('branch').value='';get('work').value='Shabbat';vm.runInContext('render(true)',context);
assert(get('results').innerHTML.includes('Shabbat'));assert(!get('results').innerHTML.includes('Chullin'));
get('work').value='';get('status').value='reconciled';vm.runInContext('render(true)',context);
assert(get('count').textContent.startsWith(D.entries.filter(e=>e.status==='reconciled').length+' '));
get('status').value='';get('all').onclick();
assert.equal((get('results').innerHTML.match(/<article>/g)||[]).length,D.entries.length);
console.log('PASS: pagination, Hebrew search, both branches, tractate and status filters, show-all.');
