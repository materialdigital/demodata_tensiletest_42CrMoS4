# pmd_referenceproject

This repository contains data from a joint project between Fraunhofer IWM, Freiburg and IWT, Bremen. The provided python scripts generate a structured dataset using the [PMDco v2.0.7](https://github.com/materialdigital/core-ontology) and [TTO v2.0.1](https://github.com/materialdigital/application-ontologies). The resulting ABox is published to [github-pages](https://matttjung.github.io/pmd_referenceproject/) as .ttl and .rdf alongside all references file resources.

## About the described scientific data
The scientific task in the project was to analyse the relation between grain size and yield strength (Hall-Petch-Relation) on 42CrMoS4. The image below gives an overview over the experimental steps. The raw material was aquired as rod and machined to blanks. These blanks were heat treated (quenched and tempered) in five batches with different austenitisation temperatures each ({850 °C, 925 °C, 1000 °C, 1075 °C, 1150 °C}). The specimens were then shipped from the first project partner (IWT) to the second project partner (IWM), where tensile test specimens as well as metallographic specimens were machined and tested or examined, respectively.

![alt text](project_flowchart.drawio.png)

## About the generated A-Box
Using a highly customized and rudimentary pipeline consisting of the python scripts in this repo, a RDF representation of the scientific data acquired during the research process is generated. The representation uses the [PMDco v2.0.7](https://github.com/materialdigital/core-ontology) and the [TTO v2.0.1](https://github.com/materialdigital/application-ontologies). The metallography section (gray boxes in the image) is not part of the RDF dataset as there is currently no application level ontology known to the authors, that is applicable. The resulting ABox is published to [github-pages](https://materialdigital.github.io/demodata_tensiletest_42CrMoS4/) as .ttl and .rdf and dereferenceable in its namespace [https://w3id.org/pmd/demodata/tensiletest_42CrMoS4/](https://w3id.org/pmd/demodata/tensiletest_42CrMoS4/) alongside all references file resources.

**The repo is currently WIP**