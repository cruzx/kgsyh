#!/usr/bin/env python3
from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description="Append one kgsyh learning note.")
    parser.add_argument("--task", required=True)
    parser.add_argument("--reaction", required=True)
    parser.add_argument("--effective", required=True)
    parser.add_argument("--ineffective", required=True)
    parser.add_argument("--rule", required=True)
    parser.add_argument("--promote", default="否")
    parser.add_argument("--file", default=None)
    args = parser.parse_args()

    root = Path(__file__).resolve().parent.parent
    log_path = Path(args.file) if args.file else root / "learning" / "SESSION_LOG.md"
    today = date.today().isoformat()

    entry = (
        f"\n## {today}\n\n"
        f"- 任务：{args.task}\n"
        f"- 用户反应：{args.reaction}\n"
        f"- 有效做法：{args.effective}\n"
        f"- 无效做法：{args.ineffective}\n"
        f"- 可复用规则：{args.rule}\n"
        f"- 是否升级到 PROFILE：{args.promote}\n"
    )

    if not log_path.exists():
        log_path.write_text("# 会话沉淀\n\n按时间倒序追加，保留最近最有价值的记录。\n", encoding="utf-8")

    original = log_path.read_text(encoding="utf-8")
    marker = "---\n"
    insert_at = original.find(marker)
    if insert_at != -1:
        insert_at += len(marker)
        updated = original[:insert_at] + entry + original[insert_at:]
    else:
        updated = original.rstrip() + "\n" + entry

    log_path.write_text(updated, encoding="utf-8")
    print(log_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
