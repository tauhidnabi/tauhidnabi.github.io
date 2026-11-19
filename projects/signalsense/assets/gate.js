(function(){
  const P = JSON.parse(document.getElementById("payload").textContent);
  const PAGE = document.body.dataset.page || location.pathname;
  const b64 = s => Uint8Array.from(atob(s), c => c.charCodeAt(0));
  const store = {
    get(k){ try{ return sessionStorage.getItem(k) }catch(_){ return null } },
    set(k,v){ try{ sessionStorage.setItem(k,v) }catch(_){} }
  };
  async function decrypt(pw){
    const base = await crypto.subtle.importKey("raw", new TextEncoder().encode(pw), "PBKDF2", false, ["deriveKey"]);
    const key = await crypto.subtle.deriveKey({name:"PBKDF2", salt:b64(P.s), iterations:P.n, hash:"SHA-256"}, base, {name:"AES-GCM", length:256}, false, ["decrypt"]);
    return new TextDecoder().decode(await crypto.subtle.decrypt({name:"AES-GCM", iv:b64(P.i)}, key, b64(P.c)));
  }
  async function log(name){
    const url = window.SS_LOG_URL; const flag = "ss_logged:" + PAGE;
    if (!url || store.get(flag)) return;
    try{
      await fetch(url, {method:"POST", mode:"no-cors", headers:{"Content-Type":"text/plain"},
        body: JSON.stringify({name, page: PAGE})});
      store.set(flag, "1");
    }catch(_){}
  }
  function show(html){ document.open(); document.write(html); document.close(); }
  async function unlock(name, pw){
    const html = await decrypt(pw);
    store.set("ss_name", name); store.set("ss_pw", pw);
    await log(name); show(html);
  }
  const f = document.getElementById("f"), msg = document.getElementById("msg"), go = document.getElementById("go");
  const savedName = store.get("ss_name"), savedPw = store.get("ss_pw");
  if (savedName && savedPw){
    unlock(savedName, savedPw).catch(() => { f.classList.remove("hidden"); document.getElementById("foot")?.classList.remove("hidden"); });
  } else { f.classList.remove("hidden"); document.getElementById("foot")?.classList.remove("hidden"); }
  if (savedName) document.getElementById("name").value = savedName;
  f.addEventListener("submit", async e => {
    e.preventDefault();
    const name = document.getElementById("name").value.trim(), pw = document.getElementById("pw").value;
    if (!name){ msg.textContent = "Please enter your name."; return; }
    go.disabled = true; go.textContent = "Opening…"; msg.textContent = "";
    try { await unlock(name, pw); }
    catch(_){ msg.textContent = "Incorrect password."; go.disabled = false; go.textContent = "Enter"; }
  });
})();
