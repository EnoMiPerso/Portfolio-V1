#!/usr/bin/env python3
"""Move flat assets/ into subfolders (<100 files each) for easier manual GitHub uploads."""
from __future__ import annotations

import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"


def pick_subdir(name: str) -> str | None:
    if name.startswith("fms-") or name.startswith("file-mgmt-") or name == "file-management-system-hero.png":
        return "fms"
    if name.startswith("th-") or name.startswith("transformation-hub"):
        return "transformation-hub"
    if name.startswith("smart-inputs-"):
        return "smart-inputs"
    if name.startswith("ai-annotations"):
        return "ai-annotations"
    if name.startswith("studio-framework"):
        return "studio"
    if name.startswith("rpg-") or name == "group-displacement.png":
        return "rpg"
    if (
        name.startswith("admin-")
        or name.startswith("hi-fi-")
        or name.startswith("ia-")
        or name.startswith("def-ideation-")
        or name.startswith("research-")
        or name == "content-management.png"
    ):
        return "platform"
    return None


def move_files() -> None:
    for p in list(ASSETS.iterdir()):
        if not p.is_file() or p.name.startswith("."):
            continue
        sub = pick_subdir(p.name)
        if not sub:
            raise SystemExit(f"No subdir rule for: {p.name}")
        dest_dir = ASSETS / sub
        dest_dir.mkdir(parents=True, exist_ok=True)
        dest = dest_dir / p.name
        if dest.exists():
            raise SystemExit(f"Collision: {dest}")
        shutil.move(str(p), str(dest))
    # Root should only contain subdirs (no stray files)
    stray = [p.name for p in ASSETS.iterdir() if p.is_file()]
    if stray:
        raise SystemExit(f"Unclassified files remain: {stray}")


REPLACEMENTS: list[tuple[str, str]] = [
    ("assets/file-mgmt-", "assets/fms/file-mgmt-"),
    ("assets/file-management-system-hero.png", "assets/fms/file-management-system-hero.png"),
    ("assets/fms-", "assets/fms/fms-"),
    ("assets/th-", "assets/transformation-hub/th-"),
    ("assets/transformation-hub-hero.png", "assets/transformation-hub/transformation-hub-hero.png"),
    ("assets/transformation-hub.png", "assets/transformation-hub/transformation-hub.png"),
    ("assets/transformation-hub-product-demo.mp4", "assets/transformation-hub/transformation-hub-product-demo.mp4"),
    ("assets/smart-inputs-", "assets/smart-inputs/smart-inputs-"),
    ("assets/ai-annotations-", "assets/ai-annotations/ai-annotations-"),
    ("assets/ai-annotations.png", "assets/ai-annotations/ai-annotations.png"),
    ("assets/studio-framework-", "assets/studio/studio-framework-"),
    ("assets/studio-framework.png", "assets/studio/studio-framework.png"),
    ("assets/rpg-", "assets/rpg/rpg-"),
    ("assets/group-displacement.png", "assets/rpg/group-displacement.png"),
    ("assets/admin-", "assets/platform/admin-"),
    ("assets/hi-fi-", "assets/platform/hi-fi-"),
    ("assets/ia-", "assets/platform/ia-"),
    ("assets/def-ideation-", "assets/platform/def-ideation-"),
    ("assets/research-benchmark-", "assets/platform/research-benchmark-"),
    ("assets/content-management.png", "assets/platform/content-management.png"),
]


def patch_text_files() -> None:
    exts = {".html", ".md", ".txt"}
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in exts:
            continue
        if "scripts" in path.parts and path.name == "reorganize-assets.py":
            continue
        text = path.read_text(encoding="utf-8")
        orig = text
        for old, new in REPLACEMENTS:
            text = text.replace(old, new)
        if text != orig:
            path.write_text(text, encoding="utf-8")
            print("patched", path.relative_to(ROOT))


def main() -> None:
    move_files()
    patch_text_files()
    print("Done. Folder counts:")
    for d in sorted(ASSETS.iterdir()):
        if d.is_dir():
            n = sum(1 for _ in d.iterdir())
            print(f"  {d.name}: {n}")


if __name__ == "__main__":
    main()
