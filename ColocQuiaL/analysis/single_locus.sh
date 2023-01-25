#!/bin/bash
# Runs colocquial.R on a single locus

module load R/3.6.3
module load plink/1.90Beta4.5
module load htslib 
module load tabix
module load liftover

colocquial_dir=$1
cp $colocquial_dir/colocquial.R ./

Rscript colocquial.R
