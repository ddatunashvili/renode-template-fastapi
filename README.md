# FastAPI on Renode

A small FastAPI service that already follows every Renode rule:

- `app.py` runs uvicorn on `0.0.0.0` on `SERVER_PORT`, the one port the server
  is given. It is the file the Python egg runs by default.
- Dependencies are in `requirements.txt`, which the server installs before
  every start.
- `.python-version` pins **Python 3.12**, which the Python egg offers.

Endpoints: `GET /`, `GET /health`, and the generated docs at `/docs`.

## Deploy on Renode

1. Create your own repository from this template (**Use this template** on GitHub, or **Start from a template** on the panel's GitHub tab).
2. Order a server that runs it: an **App Runtimes → Python** plan, with **Python 3.12** picked under *Runtime version*.
3. On the server's **GitHub** tab, connect GitHub and pick the new repository and its `main` branch, then **Deploy**.
4. Upload a filled-in `.env` through the **Files** tab if you need any settings.
5. Start the server. The console shows the install, then the app.

## Run it locally

```bash
python -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
python app.py      # http://localhost:8000/docs
```
