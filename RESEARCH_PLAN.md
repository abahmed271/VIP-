# Research plan

## Milestone 1: Dataset inventory
- Inspect Ukraine classification imagery and CSV labels with a small authorized download.
- Obtain an authorized xBD subset and audit its post-disaster JSON labels.
- Summarize class balance, missing files, locations and license limitations.
- **Deliverable:** scripts and local plots, plus shareable aggregate findings if permitted.

## Milestone 2: Comparable evaluation data
- Confirm how xBD and Ukraine damage labels align before combining them.
- Begin with damaged vs undamaged if four-class labels cannot be matched reliably.
- Keep geographic locations or events separated between training and evaluation.
- **Deliverable:** split manifest, label mapping, evaluation protocol.

## Milestone 3: Baseline experiment
- Compare a majority-class baseline with a simple pretrained image classifier.
- Evaluate on held-out Ukraine locations; report precision, recall, macro-F1, confusion matrix.
- Document limitations, including class imbalance, image quality and domain shift.
- **Deliverable:** reproducible training script and honest measured results.

## Related research
- [xBD (2019)](https://arxiv.org/abs/1911.09296): annotated building damage from satellite imagery.
- [Transfer learning for damage assessment (2022)](https://doi.org/10.3390/rs14112532): cross-disaster generalization.
- [Mariupol conflict-zone CNN study (2024)](https://arxiv.org/abs/2410.04802): domain adaptation to war damage.
- [Ukraine radar damage mapping (2025)](https://doi.org/10.1038/s43247-025-02183-7): larger-area SAR-based estimates.
- [BRIGHT multimodal dataset (2025)](https://doi.org/10.5194/essd-17-6217-2025): optical/radar comparisons.
- [Dataset author's training examples](https://github.com/KOlegaBB/damage-eval-sat-images): reference notebooks, not our own results.

Raw image files should not be committed; permissions for training and sharing must be checked.
