# LocoColoc is a consolidation of three R packages: ColocQuiaL, eQTplot, and Gene-level-statistical-colocalization (GLC).

## Setting up & Using LocoColoc:
It is recommended to first read the individual READMEs for each of the packages above, which can be found in their respectively named folders under LocoColoc. This README only provides information on usage of the loco_coloc script and its arguments.

Below is a list of the parameters of running loco_coloc.py:
* -*h* Show the help menu.
* -*glc* Path to folder containing run_gene_level_coloc.R (./GLC). Mutually exclusive with ColocQuiaL flag
* -*cql* In progress. Mutually exclusive with ColocQuiaL flag.
* -*f* Path to JSON input file containing params. GLC example and template found in ./GLC. In progress for cql

## Gene-Level-Coloc Example Input & Template Files
In the GLC folder, there are two JSON files: one example_input file, and one blank input template file. All paths for file/folder variables in these JSON files should be specified relative to the LocoColoc folder where the script is. 