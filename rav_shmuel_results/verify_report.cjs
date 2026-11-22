const fs=require('fs'),vm=require('vm'),path=require('path');
const html=fs.readFileSync(path.join('rav_shmuel_results','מחלוקות_רב_ושמואל.html'),'utf8');
const data=html.match(/<script id="data" type="application\/json">([\s\S]*?)<\/script>/)[1];
const scripts=[...html.matchAll(/<script(?: [^>]*)?>([\s\S]*?)<\/script>/g)];
const elements=new Map();
function get(id){if(!elements.has(id))elements.set(id,{value:'',innerHTML:'',textContent:id==='data'?data:'',addEventListener(){}});return elements.get(id)}
const context={document:{getElementById:get,querySelector:s=>get(s.slice(1))},console};
vm.createContext(context);vm.runInContext(scripts.at(-1)[1],context);
if(!get('results').innerHTML.includes('<article>'))throw Error('No results rendered');
get('q').value='שמוטת גף';vm.runInContext('render(true)',context);
if(!get('results').innerHTML.includes('Chullin'))throw Error('Hebrew search failed');
get('q').value='';get('branch').value='Yerushalmi';vm.runInContext('render(true)',context);
if(!get('count').textContent.startsWith('89 '))throw Error('Branch filter failed');
console.log('Rendering logic, Hebrew search, and Yerushalmi filter passed.');
