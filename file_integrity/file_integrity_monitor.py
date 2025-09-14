#!/usr/bin/env python

from pathlib import Path
import hashlib
import json
import logging
import argparse
import sys

logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(message)s")


def scan_dir(base_dir, output_file="hashes.json"):
    base = Path(base_dir)
    if not base.exists():
        logging.error("Base directory does not exist: %s", base_dir)
        sys.exit(2)

    files = {}

    for path in base.rglob("*"):
        if path.is_file():
            digest = _sha256_of_file_(path)
            rel_path = path.relative_to(base)
            files[str(rel_path)] = digest

    result = {"base": str(base.resolve()), "files": files}

    # Print to screen
    print(json.dumps(result, indent=2))

    # Save to JSON file
    with open(output_file, "w") as f:
        json.dump(result, f, indent=2)

    logging.info(f"Hashes saved to {output_file}")
    return result


def _sha256_of_file_(path, chunk_size=8192):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(chunk_size), b""):
            h.update(chunk)
        return h.hexdigest()


def main():
    # 👇 argparse magic
    parser = argparse.ArgumentParser(
        description=("Simple file integrity monitor (SHA256 hashes)")
    )
    parser.add_argument("base_dir", help="Directory to scan")
    parser.add_argument(
        "-o", "--output", default="hashes.json", help="Output JSON file"
    )
    args = parser.parse_args()

    scan_dir(args.base_dir, args.output)


if __name__ == "__main__":
    main()
