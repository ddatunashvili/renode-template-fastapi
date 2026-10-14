# FastAPI on Renode

A FastAPI service. The server runs `app.py`, which starts uvicorn.

Your own notes go here, above or below the Renode block. The panel only ever rewrites the text between the two markers.

<!-- renode:start -->
<!-- Maintained by the Renode panel. Everything between these markers is replaced when the server's settings change; write your own notes outside them. -->
## Renode server

This repository started from a Renode starter template. When it is deployed to a Renode server with "Keep AI context in the repository" switched on, the panel replaces this block with that server's own details and adds `.renode/server.md`.

- Listen on `0.0.0.0` on the port in the `SERVER_PORT` environment variable. No other port is reachable from outside.
- The entry file is `app.py` (the Startup tab names it) and it starts uvicorn itself. Keep it, or change the Startup tab with it.
- Dependencies go in `requirements.txt`; `pyproject.toml` alone is not installed.
- Only `/home/container` persists. No root, no apt, no systemd, no Docker.
- Never commit secrets. They go in a `.env` uploaded through the panel's Files tab, or in Startup variables, and are read from the environment.
- After pushing, restart the server from the panel to run the new commit, or switch on "Restart the server when someone pushes" on the GitHub tab.
- Fix the code, not the startup command or the Docker image.
<!-- renode:end -->
