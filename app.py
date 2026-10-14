"""A small FastAPI service.

The Python egg runs the file named on the Startup tab, which is `app.py` by
default, after installing requirements.txt. Running uvicorn from here, rather
than from a command line, keeps the bind address and port in the code.
"""
import os

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI

# A .env uploaded through the panel's Files tab, if there is one.
load_dotenv()

app = FastAPI(title=os.environ.get("APP_NAME", "renode-fastapi"))


@app.get("/")
def root() -> dict:
    return {"message": "Hello from Renode"}


@app.get("/health")
def health() -> dict:
    return {"ok": True}


if __name__ == "__main__":
    # The panel sets SERVER_PORT to this server's port. It is the only port
    # reachable from outside, and 0.0.0.0 is the only address that is.
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("SERVER_PORT", os.environ.get("PORT", "8000"))))
