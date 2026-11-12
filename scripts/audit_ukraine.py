from pathlib import Path
import json
import pandas as pd
import matplotlib.pyplot as plt

root = Path("data/ukraine/classification")
out = Path("reports")
out.mkdir(exist_ok=True)

files = sorted(root.glob("*_data/fold_*/fold_*.csv"))
if not files:
    raise SystemExit("No Ukraine CSV files. Run python scripts/download_ukraine.py --sample first.")

rows = []
missing = []
for csv_path in files:
    frame = pd.read_csv(csv_path, dtype=str)
    required = {"pre_image", "post_image", "mask_image", "damage"}
    if not required.issubset(frame.columns):
        raise SystemExit(f"Missing columns in {csv_path}: {required - set(frame.columns)}")
    location = csv_path.parent.parent.name.replace("_data", "")
    for _, item in frame.iterrows():
        pre = str(item["pre_image"])
        post = str(item["post_image"])
        mask = str(item["mask_image"])
        fold = str(item.get("fold", csv_path.parent.name.replace("fold_", "")))
        target_dir = csv_path.parent.parent / f"fold_{fold}"
        if not target_dir.is_dir():
            continue
        rows.append({"location": location, "pre": pre, "post": post, "mask": mask, "damage": str(item["damage"])})
        for folder, filename in [("pre", pre), ("post", post), ("mask", mask)]:
            if not (target_dir / folder / filename).exists():
                missing.append(str(target_dir / folder / filename))

if not rows:
    raise SystemExit("CSV files were found, but no matching rows were found.")

df = pd.DataFrame(rows)
fields = ["location", "pre", "post", "mask"]
conflicts = df.groupby(fields, dropna=False)["damage"].nunique()
unique = df.drop_duplicates(subset=fields)
summary = {
    "csv_files": len(files),
    "csv_rows_including_repeats": len(df),
    "unique_building_records": len(unique),
    "different_labels_on_same_record": int((conflicts > 1).sum()),
    "missing_referenced_file_paths": len(set(missing)),
    "counts_by_location": {str(k): int(v) for k, v in unique["location"].value_counts().items()},
    "counts_by_label": {str(k): int(v) for k, v in unique["damage"].value_counts().items()}
}
(out / "ukraine_audit.json").write_text(json.dumps(summary, indent=2))
unique.to_csv(out / "ukraine_records.csv", index=False)
ax = unique["damage"].value_counts().sort_index().plot(kind="bar", rot=20, title="Ukraine damage labels")
ax.set_ylabel("Unique building instances")
plt.tight_layout()
plt.savefig(out / "ukraine_damage_labels.png", dpi=150)
plt.close()
print(json.dumps(summary, indent=2))
