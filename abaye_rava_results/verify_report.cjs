// UI checks only; these do not establish scholarly accuracy or completeness.
const fs=require('fs'),vm=require('vm'),path=require('path'),assert=require('assert');
const html=fs.readFileSync(path.join(__dirname,'מחלוקות_אביי_ורבא.html'),'utf8');
const data=html.match(/<script id="data" type="application\/json">([\s\S]*?)<\/script>/)[1];
const D=JSON.parse(data);
assert(!html.includes('</option value='));
for(const v of ['Bavli','Yerushalmi','dispute','reconciled'])assert(html.includes('<option value="'+v+'">'));
const scripts=[...html.matchAll(/<script(?: [^>]*)?>([\s\S]*?)<\/script>/g)];
const elements=new Map();
function get(id){if(!elements.has(id))elements.set(id,{value:'',innerHTML:'',textContent:id==='data'?data:'',addEventListener(){}});return elements.get(id)}
const context={document:{getElementById:get,querySelector:s=>get(s.slice(1))},console};
vm.createContext(context);vm.runInContext(scripts.at(-1)[1],context);
assert.equal((get('results').innerHTML.match(/<article>/g)||[]).length,25);
get('q').value='יאוש שלא מדעת';vm.runInContext('render(true)',context);
assert(get('results').innerHTML.includes('Bava Metzia 21b'));
get('q').value='';get('branch').value='Yerushalmi';vm.runInContext('render(true)',context);
assert(get('count').textContent.startsWith('0 '));assert.equal(get('results').innerHTML,'');
get('branch').value='';get('work').value='Niddah';vm.runInContext('render(true)',context);
assert(get('results').innerHTML.includes('Niddah'));assert(!get('results').innerHTML.includes('Chullin'));
get('work').value='';get('all').onclick();
assert.equal((get('results').innerHTML.match(/<article>/g)||[]).length,D.entries.length);
console.log('PASS: initial render, Hebrew multiword search, empty branch, tractate filter, and show-all.');
