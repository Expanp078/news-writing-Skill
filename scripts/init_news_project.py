#!/usr/bin/env python3
"""Create an empty alpha1.1 news-writing project without overwriting files."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Initialize a news-writing alpha1.1 project")
    p.add_argument("path", type=Path, help="new project directory")
    p.add_argument("--task-id", required=True, help="stable task identifier")
    p.add_argument("--genre", default="", help="optional requested genre")
    p.add_argument("--medium", default="", help="optional medium")
    p.add_argument("--audience", default="", help="optional audience")
    return p.parse_args()


def quote(value: str) -> str:
    return "'" + value.replace("'", "''") + "'"


def main() -> int:
    args = parse_args()
    root = args.path.expanduser().resolve()
    if root.exists() and any(root.iterdir()):
        raise SystemExit(f"refusing to overwrite non-empty directory: {root}")
    root.mkdir(parents=True, exist_ok=True)
    for name in ("drafts", "reviews", "revisions", "state", "final"):
        (root / name).mkdir()
    now = datetime.now(timezone.utc).isoformat()
    (root / "00-input-manifest.yaml").write_text(
        "\n".join(
            [
                f"task_id: {quote(args.task_id)}",
                "skill_version: 'alpha1.1'",
                f"created_at: {quote(now)}",
                f"requested_genre: {quote(args.genre)}",
                f"medium: {quote(args.medium)}",
                f"audience: {quote(args.audience)}",
                "material_cutoff: ''",
                "product_state: unknown",
                "event_time: ''",
                "source_publication_time: ''",
                "update_trigger: ''",
                "source_files: []",
                "source_urls: []",
                "constraints: []",
                "unknowns: []",
                "route_hypotheses: []",
                "risk_flags: []",
                "",
            ]
        ),
        encoding="utf-8",
    )
    (root / "state" / "progress.yaml").write_text(
        "\n".join(
            [
                f"task_id: {quote(args.task_id)}",
                "skill_version: 'alpha1.1'",
                "state: intake",
                "rounds_completed: 0",
                "minimum_rounds: 3",
                "convergence: pending",
                f"last_update: {quote(now)}",
                "unresolved: []",
                "",
            ]
        ),
        encoding="utf-8",
    )
    (root / "state" / "resource-load-log.yaml").write_text("loads: []\n", encoding="utf-8")
    (root / "state" / "input-hashes.yaml").write_text("files: []\n", encoding="utf-8")
    (root / "state" / "material-precheck.md").write_text(
        "# 材料预检\n\n"
        "- task_id: " + args.task_id + "\n"
        "- 先由主写作者补充材料边界、来源层级、材料截点、产品状态和风险。\n",
        encoding="utf-8",
    )
    print(root)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
