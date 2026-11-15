// Minimal in-memory stand-in for the artifact runtime, for local testing only.
(function(){
  const docs = new Map(); const subs = [];
  const collOf = p => p.split("/").slice(0,-1).join("/");
  function notify(coll){ for (const s of subs) if (s.coll===coll) s.fire(); }
  function snapDoc(path){ const d=docs.get(path); return {id:path.split("/").pop(), exists:!!d, data:()=>d&&JSON.parse(JSON.stringify(d)), metadata:{fromCache:false,hasPendingWrites:false}}; }
  function merge(a,b){ for(const k in b){ if(b[k]&&typeof b[k]==="object"&&!Array.isArray(b[k])&&a[k]&&typeof a[k]==="object") merge(a[k],b[k]); else a[k]=b[k]; } return a; }
  const db = {
    doc(path){ return { path,
      async get(){ return snapDoc(path); },
      async set(d){ docs.set(path, JSON.parse(JSON.stringify(d))); notify(collOf(path)); },
      async update(d){ if(!docs.has(path)) throw {code:"invalid_argument",message:"missing"}; merge(docs.get(path), JSON.parse(JSON.stringify(d))); notify(collOf(path)); },
      async delete(){ docs.delete(path); notify(collOf(path)); } }; },
    collection(coll){ return { onSnapshot(next){ const s={coll, fire(){ const ds=[...docs.keys()].filter(k=>collOf(k)===coll).sort().map(snapDoc); next({docs:ds,size:ds.length,empty:!ds.length,docChanges:()=>[],metadata:{fromCache:false,hasPendingWrites:false}}); }}; subs.push(s); setTimeout(()=>s.fire(),50); return ()=>{}; } }; }
  };
  window.__fakedocs = docs;
  window.claude = { use: async n => n==="db" ? db : n==="downloads" ? { save: async ({filename,data}) => { window.__saved = {filename, size: data.size||data.length}; return {status:"saved"}; } } : null };
})();
