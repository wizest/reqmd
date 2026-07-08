#!/usr/bin/env python3
"""Run the standard ReqMd repair pipeline."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


def run_step(script: Path, root: Path) -> int:
    print(f"== {script.name} ==")
    result = subprocess.run([sys.executable, str(script), str(root)], check=False)
    return result.returncode


def main() -> int:
    parser = argparse.ArgumentParser(description="Run ReqMd index update, link repair, and validation")
    parser.add_argument("root", nargs="?", default=".", help="Requirement root to repair and validate")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    script_dir = Path(__file__).resolve().parent

    for name in ["update_index.py", "repair_index_links.py"]:
        code = run_step(script_dir / name, root)
        if code != 0:
            return code

    return run_step(script_dir / "validate_reqmd.py", root)


if __name__ == "__main__":
    raise SystemExit(main())
