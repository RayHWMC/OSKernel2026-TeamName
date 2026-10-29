"""Verify the recorded upstream snapshots using only the Python standard library."""
import hashlib
import json
from pathlib import Path
import sys


def main():
    root = Path(__file__).resolve().parents[1]
    manifest_path = root / "tests/upstream/imports.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    failures = []
    recorded = set()
    total_bytes = 0
    for source in manifest["sources"]:
        for item in source["files"]:
            relative = item["path"]
            path = root / relative
            if relative in recorded:
                failures.append(f"Duplicate manifest path: {relative}")
                continue
            recorded.add(relative)
            if path.is_symlink() or not path.resolve().is_relative_to(root):
                failures.append(f"Unsafe import path: {relative}")
                continue
            if not path.is_file():
                failures.append(f"Missing import: {relative}")
                continue
            content = path.read_bytes()
            total_bytes += len(content)
            if len(content) != item["bytes"] or hashlib.sha256(content).hexdigest() != item["sha256"]:
                failures.append(f"Changed import: {relative}")
    for directory in (root / "tests/upstream", root / "tools/environment/reference"):
        for path in directory.rglob("*"):
            if path.is_file() and path != manifest_path:
                relative = path.relative_to(root).as_posix()
                if relative not in recorded:
                    failures.append(f"Unrecorded import file: {relative}")
    if failures:
        print("\n".join(failures), file=sys.stderr)
        return 1
    print(f"Verified {len(recorded)} imported files ({total_bytes} bytes) across {len(manifest['sources'])} sources.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
