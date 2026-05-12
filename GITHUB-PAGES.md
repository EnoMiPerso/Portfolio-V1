# Publish this site on GitHub Pages

Target repo: **[EnoMiPerso/Portfolio-V1](https://github.com/EnoMiPerso/Portfolio-V1)** (`https://github.com/EnoMiPerso/Portfolio-V1.git`)

Your HTML uses **relative** paths (`work.html`, `fms/...`, `platform/...`, etc.), which is correct for a project site at:

`https://<username>.github.io/Portfolio-V1/`

---

## 1. Put the full site in the repository

From your local project folder (the one that contains `index.html`, `work.html`, the seven media folders at **root**, and the `work-project-*.html` files), either:

**Option A — Git (recommended)**  
```bash
cd /path/to/Sky\ Parallax   # or your clone of Portfolio-V1
git remote add origin https://github.com/EnoMiPerso/Portfolio-V1.git   # skip if already set
git add -A
git status    # confirm fms/, platform/, work-project-*.html, .nojekyll are included
git commit -m "Deploy static portfolio for GitHub Pages"
git push -u origin main
```

**Option B — Manual upload on GitHub**  
GitHub’s web UI only accepts **about 100 files per upload**, so the repo splits media into subfolders (each stays under that limit). Each folder lives at the **repository root** next to `index.html` (there is **no** `assets/` parent):

| Folder at repo root | Role |
|---------------------|------|
| `fms/` | File management case study (56 files) |
| `transformation-hub/` | Transformation Hub + `th-*` slides (45) |
| `smart-inputs/` | Smart inputs & variables (41) |
| `ai-annotations/` | AI annotations (31) |
| `studio/` | Studio framework (23) |
| `platform/` | Admin / hi-fi / IA / research / def-ideation (27) |
| `rpg/` | Group displacement / RPG (13) |

Upload in **separate commits**, e.g. one commit per folder: **Add file → Upload files** → select every file inside `fms/` (under 100), commit. Repeat for `transformation-hub/`, `smart-inputs/`, `ai-annotations/`, `studio/`, `platform/`, and `rpg/`. Then upload all **`.html`** files, **`.nojekyll`**, and optional meta files (`README.md`, this file, `MANIFEST-PAGES-DEPLOY.txt`).

**Option B2 — Still too many clicks**  
Use **Git push** or **GitHub Desktop** once; there is no per-file cap.

A full list of paths is in **`MANIFEST-PAGES-DEPLOY.txt`** (regenerate with `find` if you add files).

---

## 1c — Delete everything on GitHub and re-upload manually (safe layout)

Yes, you can wipe the repo and start clean. Use this **exact** shape so images and videos work:

1. **Repository root** contains: the **10** `.html` files, **`.nojekyll`**, and the **seven** media folders **`fms/`**, **`transformation-hub/`**, **`smart-inputs/`**, **`ai-annotations/`**, **`studio/`**, **`platform/`**, **`rpg/`** (plus optional docs like `README.md`). Do **not** nest those seven inside another folder named `assets` — paths in HTML expect them at root.
2. **Upload order (web UI, fewer than 100 files per commit):**  
   - At repo root, upload all files for **`fms/`** → commit.  
   - Repeat for: `transformation-hub/`, `smart-inputs/`, `ai-annotations/`, `studio/`, `platform/`, `rpg/`.  
   - Then upload **root** files: all `.html` + `.nojekyll` in one batch.
3. **Checklist file:** open **`REPO-FILE-LAYOUT.txt`** in this project for the same tree in plain text while you upload.

After a wipe, **`git push`** from your Mac is still the least error-prone method (one command, correct tree guaranteed).

---

## 2. Turn on GitHub Pages

1. Repo → **Settings** → **Pages** (left sidebar).  
2. **Build and deployment** → Source: **Deploy from a branch**.  
3. Branch: **`main`**, folder: **`/` (root)** → Save.

After a minute or two, the site is served from the URL shown on that settings page (usually `https://enomiperso.github.io/Portfolio-V1/`).

---

## 3. Why `.nojekyll` is in the repo

GitHub Pages can run **Jekyll** on pushes. An empty **`.nojekyll`** file at the **repository root** disables Jekyll so static files (including images and videos in the media folders) are copied as-is. Keep this file in the root next to `index.html`.

---

## 4. Optional checks

- **Transformation Hub video:** `work.html` references `transformation-hub/transformation-hub-product-demo.mp4`. That file must exist on the branch Pages deploys, or remove the `videos` entry until it is added.  
- **Deep links:** `work-project-transformation-hub.html` (and siblings) are full pages with `data-default-project`; open them as  
  `https://<username>.github.io/Portfolio-V1/work-project-transformation-hub.html`  
  after deploy.

---

## 5. Custom domain (later)

In **Pages** settings, add your domain and follow GitHub’s DNS instructions. No code change is required if you keep paths relative to the site root.
