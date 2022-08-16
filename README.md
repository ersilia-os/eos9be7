# Frechet Chemnet Distance
## Model identifiers
- Slug: chemnet-distance
- Ersilia ID: eos9be7
- Tags: generative, distance, similarity

# Model description
- Input: A pair of SMILES lists. Ideally, one list represents training data and the other list represents a generated 
- Output: Frechet ChemNet Distance (FCD) score. This metric incorporates biological and chemical properties to compare generative model outputs to training data. A lower FCD means that generated molecules are similar to those in the training set. 
- Model type: N/A
- Training set: The distance is based on ChemNet, a model trained on approximately 500,000 molecules to predict 6000 assays in ChEMBL, ZINC, and PubChem. Further training details may be found in [this paper](https://pubs.rsc.org/en/content/articlelanding/2018/sc/c8sc00148k).
- Mode of training: Pretrained

# Source code
Preuer, K., Renz, P., Unterthiner, T., Hochreiter, S. & Klambauer, G. Fréchet ChemNet Distance: A Metric for Generative Models for Molecules in Drug Discovery. J. Chem. Inf. Model. 58, 1736–1741 (2018).

- Code: https://github.com/bioinf-jku/FCD
- Checkpoints: N/A

# License
The GPL-v3 license applies to all parts of the repository that are not externally maintained libraries. This repository uses the externally maintained library "fcd," located at [/model/framework](/model/framework) and licensed under a [LGPL-3.0 license](/model/framework/README.md)


# History 
- The model was downloaded on 8/11/2022.
- The model was incorporated on 8/16/2022.

# About us
The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission or [volunteer](https://www.ersilia.io/volunteer) with us!
