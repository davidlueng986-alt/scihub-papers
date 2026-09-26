#!/usr/bin/env python3
"""Download and verify the exact Shetaya et al. 2019 Mendeley dataset archive."""

from __future__ import annotations

import hashlib
import io
import sys
import urllib.request
import zipfile
from pathlib import Path

URL = "https://data.mendeley.com/public-files/datasets/xw2kr7ykhd/files/13b5d059-1556-4563-8154-f1c510f4e7f5/file_downloaded"
EXPECTED_SHA256 = "e04adc7856ef0f607fd92805648725412850d5ef3c522da4a26b15bf4c39af60"
OUT = Path("data/raw/shetaya_2019/DATA FILES.zip")
EXTRACT_DIR = Path("data/raw/shetaya_2019/extracted")


def main() -> int:
    print(f"Downloading {URL}")
    with urllib.request.urlopen(URL) as response:
        payload = response.read()

    digest = hashlib.sha256(payload).hexdigest()
    if digest != EXPECTED_SHA256:
        print(f"SHA256 mismatch: {digest}", file=sys.stderr)
        return 1

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_bytes(payload)
    print(f"Verified SHA256: {digest}")
    print(f"Wrote {OUT} ({len(payload):,} bytes)")

    EXTRACT_DIR.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(io.BytesIO(payload)) as zf:
        zf.extractall(EXTRACT_DIR)
    print(f"Extracted to {EXTRACT_DIR}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
