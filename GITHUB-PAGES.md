# Publish this site on GitHub Pages

Target repo: **[EnoMiPerso/Portfolio-V1](https://github.com/EnoMiPerso/Portfolio-V1)** (`https://github.com/EnoMiPerso/Portfolio-V1.git`)

Your HTML uses **relative** paths (`work.html`, `assets/...`), which is correct for a project site at:

`https://<username>.github.io/Portfolio-V1/`

---

## 1. Put the full site in the repository

From your local project folder (the one that contains `index.html`, `work.html`, `assets/`, and the `work-project-*.html` files), either:

**Option A — Git (recommended)**  
```bash
cd /path/to/Sky\ Parallax   # or your clone of Portfolio-V1
git remote add origin https://github.com/EnoMiPerso/Portfolio-V1.git   # skip if already set
git add -A
git status    # confirm assets/, work-project-*.html, .nojekyll are included
git commit -m "Deploy static portfolio for GitHub Pages"
git push -u origin main
```

**Option B — Manual upload on GitHub**  
1. Open the repo → **Add file** → **Upload files**.  
2. Drag in **everything** at once: all `.html` files, the whole **`assets/`** folder (all images and `.mp4` files), **`.nojekyll`**, and optionally `.gitignore`, `README.md`, this file, `MANIFEST-PAGES-DEPLOY.txt`.  
3. Missing **`assets/`** is the most common reason images or video break on Pages.

A full list of paths to include is in **`MANIFEST-PAGES-DEPLOY.txt`** (regenerate with `find` if you add files).

---

## 2. Turn on GitHub Pages

1. Repo → **Settings** → **Pages** (left sidebar).  
2. **Build and deployment** → Source: **Deploy from a branch**.  
3. Branch: **`main`**, folder: **`/` (root)** → Save.

After a minute or two, the site is served from the URL shown on that settings page (usually `https://enomiperso.github.io/Portfolio-V1/`).

---

## 3. Why `.nojekyll` is in the repo

GitHub Pages can run **Jekyll** on pushes. An empty **`.nojekyll`** file at the **repository root** disables Jekyll so static files (including everything under `assets/`) are copied as-is. Keep this file in the root next to `index.html`.

---

## 4. Optional checks

- **Transformation Hub video:** `work.html` references `assets/th-transformation-hub-product-motion.mp4`. That file must exist in `assets/` on the branch Pages deploys, or remove the `videos` entry for that project until the file is added.  
- **Deep links:** `work-project-transformation-hub.html` (and siblings) are full pages with `data-default-project`; open them as  
  `https://<username>.github.io/Portfolio-V1/work-project-transformation-hub.html`  
  after deploy.

---

## 5. Custom domain (later)

In **Pages** settings, add your domain and follow GitHub’s DNS instructions. No code change is required if you keep paths relative to the site root.
