# Research plan

## Why start with buildings?

Our broader VIP goal is to explore how infrastructure damage assessment could support resilient reconstruction in Ukraine, potentially across housing, energy, transportation, and water systems. **Building damage classification is a first proof of concept, not the entire research goal.**

- **Available labeled data:** The Ukraine Damage Assessment and xBD datasets provide before/after imagery with building damage annotations, so we can evaluate an actual model rather than guessing whether it works.
- **Existing research to build on:** Papers such as the Mariupol CNN study provide methods and limitations that can guide an initial experiment.
- **Manageable technical scope:** Buildings let us practice the complete workflow: downloading authorized data, verifying image/label quality, preparing splits, training a baseline, and evaluating its mistakes.
- **Transferable engineering workflow:** We can reuse or adapt preprocessing, model-evaluation code, and geographic reporting methods for other infrastructure classes. The trained building model itself **will not automatically recognize** bridges, roads, power facilities, or water infrastructure.

**Connection to reconstruction:** A validated damage-detection workflow could eventually help screen assets for follow-up inspection or summarize damage geographically. Supporting reconstruction priorities would require additional data about asset importance, dependencies, engineering condition, and local needs; imagery alone cannot establish those priorities.

**Proposed expansion (subject to Dr. Hughes's guidance):** (1) test a building-damage proof of concept; (2) assess available labels for roads, bridges, and energy/water facilities; (3) investigate how damage estimates could connect to infrastructure-system recovery analysis.

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
