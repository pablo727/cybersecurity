from pathlib import Path
import hashlib
import json
import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(message)s")


def scan_dir(base_dir, output_file="hashes.json"):

    files = {}

    for path in Path(base_dir).rglob("*"):
        if path.is_file():
            digest = _sha256_of_file_(path)
            rel_path = path.relative_to(base_dir)
            files[str(rel_path)] = digest

    result = {"base": str(base_dir), "files": files}

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
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            h.update(chunk)
        return h.hexdigest()


# Example usage:
# scan_dir("/home/pablo/Desktop/cybersecurity/ssh_lab")
