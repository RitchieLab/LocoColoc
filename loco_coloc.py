import sys
import argparse
import os
import subprocess

def init_glc_argparse(argv):
    parser = argparse.ArgumentParser(description="Gene Level Statistical Colocalization")
    parser.add_argument("-hz", "--harmonization", required=True, help="Full path to harmonization file to run. Read GLC ReadMe for default harmonization script.")
     
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-f","--file", help="Full path input for file input for running gene level coloc. Mutually exclusive with -i." )
    group.add_argument("-i", "--input",help="Manual input for running gene level coloc. Mutually exclusive with -f." )

    return parser.parse_args(argv)


def gene_level_coloc(args):

    pri
    if not args.harmonization and not args.file:
        print("Must include path to both harmonization and input file.")
        return

    def run_harmonization(harmonization_file):
        print('Running harmonization with {}...'.format(harmonization_file))
        subprocess.run(['bash', harmonization_file])

    def run_example():
        print('running example')

    harmonization = args.harmonization
    f = args.file




def get_args(argv):
    parser = argparse.ArgumentParser(description="Loco Coloc")
    parser.add_argument("-qt", "--eqtplot", action=argparse.BooleanOptionalAction, help="Optional arg to include to use eQTpLot")
    parser.add_argument("-hz", "--harmonization", help="Path to harmonization file to run")
    parser.add_argument("-f", "--file", help="Path to input file")

    g = parser.add_mutually_exclusive_group()
    g.add_argument("-glc", "--gene-level-coloc", help="Run Gene Level Statistical Colocalization")
    g.add_argument("-cql", "--colocquial", help="Run ColocQuiaL")

    return parser.parse_args(argv)


if __name__ == "__main__":

    args = get_args(sys.argv[1:])
    
    if args.gene_level_coloc is not None:
        gene_level_coloc(args)
    elif args.colocquial is not None:
        #colocquial()
        pass
    
    if args.eqtplot is True:
        #eqtplot()
        pass

#/Users/nimay/Desktop/examples_glc/harmonized_gwas/run_Harmonization