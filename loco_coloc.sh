#!/bin/bash
# Script to handle running workflow of either ColocQuiaL, eQTpLot, or Gene-level statistical colocization

package=$(echo "$1" | tr '[:upper:]' '[:lower:]')

if [ "$package" = "colocquial" ]; then
    echo "ColocQuiaL workflow selected"
elif [ "$package" = "eqtplot" ]; then
    echo "eQTpLot workflow selected"
elif [ "$package" = "gene_level_coloc" ]; then
    echo "Gene Level Coloc workflow selected"
else 
    echo "Please ensure you use the correct package named when running."
fi