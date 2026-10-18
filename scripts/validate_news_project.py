#!/usr/bin/env python3
"""Validate alpha1.0 project structure and iteration gates, not article quality."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Validate a news-writing alpha1.0 project")
    p.add_argument("path", type=Path)
    return p.parse_args()


def require(path: Path, errors: list[str]) -> None:
    if not path.is_file():
        errors.append(f"missing file: {path.relative_to(path.parents[1]) if len(path.parents) > 1 else path}")


def main() -> int:
    root = parse_args().path.expanduser().resolve()
    errors: list[str] = []
    if not root.is_dir():
        print(f"invalid project directory: {root}")
        return 2
    require(root / "00-input-manifest.yaml", errors)
    require(root / "state" / "material-precheck.md", errors)
    require(root / "01-analysis-report.md", errors)
    require(root / "02-prewriting-plan.md", errors)
    for name in ("drafts", "reviews", "revisions", "state", "final"):
        if not (root / name).is_dir():
            errors.append(f"missing directory: {name}")
    drafts = sorted((root / "drafts").glob("draft-v*.md")) if (root / "drafts").is_dir() else []
    reviews = sorted((root / "reviews").glob("review-r*.md")) if (root / "reviews").is_dir() else []
    revisions = sorted((root / "revisions").glob("revision-log-r*.md")) if (root / "revisions").is_dir() else []
    if not drafts:
        errors.append("no draft found")
    if len(reviews) < 3:
        errors.append(f"at least 3 independent reviews required; found {len(reviews)}")
    if len(revisions) < 3:
        errors.append(f"at least 3 revision logs required; found {len(revisions)}")
    final = root / "final" / "final.md"
    progress = root / "state" / "progress.yaml"
    if progress.is_file():
        text = progress.read_text(encoding="utf-8")
        if "state: final" in text and not final.is_file():
            errors.append("state says final but final/final.md is missing")
        if "convergence: no_material_change" in text and len(reviews) < 3:
            errors.append("convergence declared before minimum review rounds")
    if final.is_file():
        last_reviews = reviews[-1].read_text(encoding="utf-8") if reviews else ""
        if "no_material_change" not in last_reviews:
            errors.append("final exists but latest review does not declare no_material_change")
        explicit_clear = (
            "unresolved_p0_p1: 0" in last_reviews
            or ("P0/P1" in last_reviews and ("无未处理" in last_reviews or "没有发现未处理" in last_reviews or "no unresolved" in last_reviews.lower()))
        )
        if not explicit_clear:
            errors.append("final exists but latest review lacks an explicit no-unresolved-P0/P1 statement")
        final_text = final.read_text(encoding="utf-8")
        for marker in ("主写作者", "检查智能体", "revision-log", "draft-v", "正式发布前仍需回核"):
            if marker in final_text:
                errors.append(f"final contains internal workflow marker: {marker}")
        if "权威媒体优秀新闻稿学习" in final_text:
            errors.append("final references forbidden legacy knowledge directory")
    for log in revisions:
        round_match = re.search(r"r(\d+)", log.name)
        if round_match:
            n = round_match.group(1)
            log_text = log.read_text(encoding="utf-8")
            if not (re.search(rf"R{n}-\d+", log_text) or "finding_id" in log_text or "decision:" in log_text):
                errors.append(f"revision log lacks finding decisions: {log.name}")
    for state_file in (root / "state" / "resource-load-log.yaml", root / "00-input-manifest.yaml"):
        state_text = state_file.read_text(encoding="utf-8") if state_file.is_file() else ""
        if state_file.is_file() and any("path:" in line and "权威媒体优秀新闻稿学习" in line for line in state_text.splitlines()):
            errors.append(f"forbidden legacy directory appears in {state_file.name}")
    for review in reviews:
        text = review.read_text(encoding="utf-8")
        if not re.search(r"(reviewer|round|加载|独立|convergence_judgment|收敛)", text, re.I):
            errors.append(f"review lacks reviewer/round/independence metadata: {review.name}")
    if errors:
        print("INVALID")
        for e in errors:
            print(f"- {e}")
        return 1
    print(f"VALID drafts={len(drafts)} reviews={len(reviews)} revisions={len(revisions)} final={final.is_file()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
