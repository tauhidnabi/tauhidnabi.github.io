"""Build the password-protected site into docs/.

Each page in src/ is encrypted (AES-256-GCM, key from PBKDF2-SHA256) and wrapped in a
name + password gate. Run:  python3 build.py PASSWORD
Pages: src/signalsense/index.html -> docs/signalsense/index.html;
       src/signalsense/analyses/<slug>.html -> docs/signalsense/<slug>/index.html
"""
import sys, os, glob, json, base64, html
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

PW = sys.argv[1]; ITER = 600_000; ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = f"{ROOT}/src/signalsense"; OUT = f"{ROOT}/docs/signalsense"
b = lambda x: base64.b64encode(x).decode()

def encrypt(data: bytes):
    salt, iv = os.urandom(16), os.urandom(12)
    key = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=ITER).derive(PW.encode())
    return {"s": b(salt), "i": b(iv), "c": b(AESGCM(key).encrypt(iv, data, None)), "n": ITER}

# Subtitle shown on each report's sign-in card
TITLES = {"warbler-dt-analysis-v1.1": "Warbler drive-test analysis · app v1.1"}

BACK = ('<div style="font-family:-apple-system,Helvetica,Arial,sans-serif;font-size:13px;'
        'padding:8px 18px;background:#f4f5f7;border-bottom:1px solid #e4e7ec">'
        '<a href="../#analyses" style="color:#4b2fd6;text-decoration:none">&larr; Signal Sense · Analyses</a></div>')

def gate(title, subtitle, page_id, payload, prefix):
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow">
<title>{html.escape(title)}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Space+Grotesk:wght@500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{prefix}assets/gate.css"></head>
<body data-page="{html.escape(page_id)}">
<form id="f" class="hidden" autocomplete="on">
<div class="head"><div class="bars" aria-hidden="true"><span></span><span></span><span></span><span></span></div>
<h1>Signal Sense</h1><p>{html.escape(subtitle)}</p></div>
<div class="field"><label for="name">Your name</label><input id="name" type="text" required maxlength="100" autocomplete="name"></div>
<div class="field"><label for="pw">Password</label><input id="pw" type="password" required autocomplete="current-password"></div>
<button id="go" type="submit">Enter</button><div id="msg" role="alert"></div></form>
<p class="foot hidden" id="foot">Tauhid Nabi · Virginia Tech · <a href="https://tauhidnabi.github.io/projects/">All projects</a></p>
<script id="payload" type="application/json">{json.dumps(payload)}</script>
<script src="{prefix}assets/config.js"></script><script src="{prefix}assets/gate.js"></script></body></html>"""

def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True); open(path, "w").write(text); print("built", os.path.relpath(path, ROOT))

hub = open(f"{SRC}/index.html", "rb").read()
write(f"{OUT}/index.html", gate("Signal Sense", "Project site for reviewers and collaborators", "home", encrypt(hub), ""))
for src in sorted(glob.glob(f"{SRC}/analyses/*.html")):
    slug = os.path.splitext(os.path.basename(src))[0]
    doc = open(src, encoding="utf-8").read()
    i = doc.find(">", doc.lower().find("<body")) + 1 if "<body" in doc.lower() else 0
    doc = doc[:i] + BACK + doc[i:]
    write(f"{OUT}/{slug}/index.html", gate("Signal Sense · " + slug, TITLES.get(slug, slug), slug, encrypt(doc.encode()), "../"))
