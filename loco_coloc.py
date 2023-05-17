import sys
import argparse

from cg import run_cg
from cql import run_cql
from eqt import run_eqt

def get_args(argv):
    print('Parsing arguments...')
    parser = argparse.ArgumentParser(description="Loco Coloc")
    parser.add_argument("-f", "--file", help="Path to config file.")
    parser.add_argument("-eqt", "--eqtplot", action=argparse.BooleanOptionalAction, help="Optional arg to include to run eQTpLot.")

    group = parser.add_mutually_exclusive_group()
    group.add_argument('-cg', '--colo-gene', action='store_true')
    group.add_argument('-cql','--colocquial', action='store_true')

    return parser.parse_args(argv)


if __name__ == "__main__":    
    args = get_args(sys.argv[1:])
    
    if not args.file:
        print('Must include path to config file.')
        exit(1)

    if args.colo_gene:
        print('Running ColoGene...')
        run_cg(args)
    elif args.colocquial:
        print('Running ColocQuiaL...')
        run_cql(args)
    
    if args.eqtplot is True:
        print('Running eQTpLot...')
        run_eqt(args)