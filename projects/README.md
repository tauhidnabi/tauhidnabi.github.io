# projects (served at tauhidnabi.github.io/projects)

- `docs/index.html` — public list of all projects → tauhidnabi.github.io/projects/
- `docs/signalsense/` — password-protected Signal Sense site → tauhidnabi.github.io/projects/signalsense/
  - first analysis → tauhidnabi.github.io/projects/signalsense/warbler-dt-analysis-v1.1/
- `src/signalsense/` — readable sources (keep the repo private)

## Update Signal Sense
1. Edit `src/signalsense/index.html` (About, Analyses, Meeting Minutes, Timeline).
2. Add a report as `src/signalsense/analyses/<slug>.html` and a card for it under Analyses.
3. Rebuild: `python3 build.py <password>` (needs `pip install cryptography`), then commit and push.

## Reviewer log
Name + page are posted to a Google Sheet after a correct password (`reviewer_log_apps_script.gs`).
Set the web-app URL in `docs/signalsense/assets/config.js`; no rebuild needed.

## GitHub Pages
Repo name `projects` under `tauhidnabi`. Settings > Pages > Deploy from a branch > `main` / `docs`.
