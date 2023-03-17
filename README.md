# LocoColoc is a consolidation of three R packages: ColocQuiaL, eQTplot, and Gene-level-statistical-colocalization (GLC).

## Setting up & Using LocoColoc:
It is recommended to first read the individual READMEs for each of the packages above, which can be found in their respectively named folders under LocoColoc. This README only provides information on usage of the loco_coloc script and its arguments.

Below is a list of the parameters of running loco_coloc.py:
* -*h* Show the help menu.
* -*glc* Run with this flag to run gene-level-colocalization. Code for this package can be found in /GLC. Mutually exclusive with ColocQuiaL flag
* -*cql* Run with this flag to run ColocQuiaL. Code for this package can be found in /ColocQuiaL. Mutually exclusive with ColocQuiaL flag.
* -*f* Required path to JSON input file containing params for packages to be run. Template available as config.JSON.
* -*eqt*/--*eqtplot* Use either of these optional flags to run eQTpLot. Code for this package can be found in /eQTpLot.
* --*no*-eqtplot* Use this flag to not run eQTpLot. Can also be omitted as default is to not run eQTpLot. Mutually exclussive with -*eqt*/--*eqtplot*.

## Example for Running Gene-Level-Coloc

## Example for Running ColocQuiaL

## Example for eQTpLot