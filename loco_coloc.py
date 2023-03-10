import sys
import argparse

from glc import run_glc
from cql import run_cql
from eqt import run_eqt

def get_args(argv):
    parser = argparse.ArgumentParser(description="Loco Coloc")
    parser.add_argument("-f", "--file", help="Path to config file.")
    parser.add_argument("-qt", "--eqt", action=argparse.BooleanOptionalAction, help="Optional arg to include to run eQTpLot.")

    group = parser.add_mutually_exclusive_group()
    group.add_argument('-glc', '--gene-level-coloc', action='store_true')
    group.add_argument('-cql','--colocquial', action='store_true')

    return parser.parse_args(argv)


if __name__ == "__main__":    
    args = get_args(sys.argv[1:])
    
    if not args.file:
        print('Must include path to config file.')
        exit(1)

    if args.gene_level_coloc:
        run_glc(args)
    elif args.colocquial:
        run_cql(args)
    
    if args.eqt is True:
        run_eqt(args)

#python loco_coloc.py -glc ./GLC -f ./GLC/example_input.JSON