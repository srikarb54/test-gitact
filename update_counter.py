from datetime import datetime, timezone
from pathlib import Path
import re

FILE = Path("counter.txt")

value = 0
if FILE.exists():
    text = FILE.read_text()
    m = re.search(r"value=(\d+)", text)
    if m:
        value = int(m.group(1))

value += 1
now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

FILE.write_text(f"value={value}\nlast_updated={now}\n")