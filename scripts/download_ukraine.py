from huggingface_hub import snapshot_download
from pathlib import Path
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--sample", action="store_true")
args = parser.parse_args()

patterns = ["classification/kamianka_data/fold_0/**", "README.md"] if args.sample else ["classification/**", "README.md"]

path = snapshot_download(
    repo_id="KOlegaBB/damage_assessment_ukraine",
    repo_type="dataset",
    allow_patterns=patterns,
    local_dir=str(Path("data/ukraine"))
)
print("Dataset stored in:", path)
