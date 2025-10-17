
# NURI Piknik v5 — Render Ready

## Deploy
- Render → New Web Service → **Upload .zip**
- Build Command: `pip install -r requirements.txt`
- Start Command: (boş bırakabilirsiniz — Procfile var) veya:  
  `python -m gunicorn -k eventlet -w 1 -b 0.0.0.0:$PORT app.server:app`

## Env Vars (opsiyonel)
- SECRET_KEY, MAX_USERS=50

## Local
python -m venv .venv && .venv\Scripts\activate
pip install -r requirements.txt
python app/server.py
