from pathlib import Path
from collections import Counter
import json
import pandas as pd
import matplotlib.pyplot as plt

root = Path("data/xbd")
out = Path("reports")
out.mkdir(exist_ok=True)

files = [p for p in root.rglob("*.json") if "post_disaster" in p.name]
if not files:
    raise SystemExit("No xBD post-disaster JSON labels found under data/xbd/.")

counts = Counter()
unreadable = 0
for path in files:
    try:
        payload = json.loads(path.read_text())
    except (ValueError, UnicodeDecodeError):
        unreadable += 1
        continue
    for feature in payload.get("features", {}).get("xy", []):
        label = feature.get("properties", {}).get("subtype", "unknown")
        counts[str(label)] += 1

df = pd.DataFrame(sorted(counts.items()), columns=["damage_label", "building_count"])
df.to_csv(out / "xbd_damage_counts.csv", index=False)
ax = df.plot(kind="bar", x="damage_label", y="building_count", legend=False, rot=25, title="xBD damage labels")
ax.set_ylabel("Buildings")
plt.tight_layout()
plt.savefig(out / "xbd_damage_labels.png", dpi=150)
plt.close()
print("JSON files parsed:", len(files) - unreadable)
print("Unreadable JSON files:", unreadable)
print(df.to_string(index=False))
