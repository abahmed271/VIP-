# VIP Ukraine Infrastructure Damage Research

Exploratory computer-vision research on damage to buildings and infrastructure in Ukraine.

## Research question
How well do building-damage classifiers trained on natural disasters transfer to war-related damage in Ukraine?

## Two starting datasets
- [Ukraine Damage Assessment](https://huggingface.co/datasets/KOlegaBB/damage_assessment_ukraine): Ukraine-focused pre/post satellite imagery, masks and damage annotations. License is not specified; verify permission before any redistribution or model use.
- [xBD / xView2](https://xview2.org/dataset): annotated pre/post satellite imagery of natural-disaster damage, with registration and noncommercial-use terms.

## Research milestones
1. Audit a locally downloaded Ukraine sample and a licensed xBD subset; inspect labels, class balance, and missing images.
2. Define consistent labels and geography-aware train/test splits, avoiding leakage across nearby images.
3. Compare a basic damage/no-damage baseline with a fine-tuned pretrained classifier; report precision, recall, macro-F1 and error cases.

## Local setup (Mac/Linux)
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python scripts/download_ukraine.py --sample
python scripts/audit_ukraine.py
```

To inspect xBD, obtain an authorized copy via its official site, extract labels under `data/xbd/`, then run `python scripts/audit_xbd.py`.

The sample audit does **not** represent all Ukrainian buildings. No ML model has been trained by this repository yet.

**Data policy:** raw satellite imagery and generated local reports stay outside GitHub; verify all licenses and research permissions before reuse. See [RESEARCH_PLAN.md](RESEARCH_PLAN.md) for papers and next steps.
