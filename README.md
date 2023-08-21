# FCD: Fréchet ChemNet Distance to evaluate generative models

The Fréchet ChemNet distance is a metric to evaluate generative models. It unifies, in a single score, whether the generated molecules are valid according to chemical and biological properties as well as their diversity from the training set. The score measures the Fréchet Inception Distance between molecules represented by ChemNet, a deep neural network trained to predict biological and chemical properties of small molecules. 

## Identifiers

* EOS model ID: `eos9be7`
* Slug: `chemnet-distance`

## Characteristics

* Input: `Compound`
* Input Shape: `Pair of Lists`
* Task: `Similarity`
* Output: `Distance`
* Output Type: `Float`
* Output Shape: `Single`
* Interpretation: Frechet ChemNet Distance (FCD). Higher FCD indicates higher difference to the training set

## References

* [Publication](https://pubs.acs.org/doi/10.1021/acs.jcim.8b00234)
* [Source Code](https://github.com/bioinf-jku/FCD)
* Ersilia contributor: [brosular](https://github.com/brosular)

## Ersilia model URLs
* [GitHub](https://github.com/ersilia-os/eos9be7)
* [AWS S3](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos9be7.zip)
* [DockerHub](https://hub.docker.com/r/ersiliaos/eos9be7) (AMD64, ARM64)

## Citation

If you use this model, please cite the [original authors](https://pubs.acs.org/doi/10.1021/acs.jcim.8b00234) of the model and the [Ersilia Model Hub](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff).

## License

This package is licensed under a GPL-3.0 license. The model contained within this package is licensed under a LGPL-3.0 license.

Notice: Ersilia grants access to these models 'as is' provided by the original authors, please refer to the original code repository and/or publication if you use the model in your research.

## About Us

The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission!