import sys
import argparse
import os
import subprocess

GENE_LEVEL_COLOC_ARGS = {

}

BASE = os.getcwd()

def gene_level_coloc(argv):

    def run_harmonization(harmonization_file):
        print('Running harmonization with {}...'.format(harmonization_file))
        subprocess.run(['bash', harmonization_file])

    def run_example():
        print('running example')

    path = BASE + "/Gene-level-statistical-colocalization/"
    parser = argparse.ArgumentParser(description="Gene Level Statistical Colocalization")
    parser.add_argument("-z", "--harmonization", required=False, help="Optional full path to harmonization file to run. If left empty, default harmonization script will be run.")

    group = parser.add_mutually_exclusive_group()
    group.add_argument("-f","--file", help="Full path input for file input for running gene level coloc. Mutually exclusive with -i." )
    group.add_argument("-i", "--input",help="Manual input for running gene level coloc. Mutually exclusive with -f." )
    args = parser.parse_args(argv)

    if args.harmonization == None:
        harmonization = path + 'examples/harmonized_gwas/default_run_harmonization'
    else:
        harmonization = args.harmonization

    if args.file == None and args.input == None:
        run_harmonization(harmonization)
        run_example()
    elif args.file == None:
        print(args.input)
    elif args.input == None:
        print(args.file)
    else:
        pass

    print()





if __name__ == "__main__":
    package = sys.argv[1].lower()
    if package == "-h" or package == "--help":
        print("Usage: loco_coloc.py <package>. Case insensitive")
        print("Packages available: Gene_Level_Coloc/GLC, ColocQuiaL/CQL, eQTpLoT/EQT.")
        print("Use loco_coloc.py <package> -h/--help for help running individual tools.")
    elif package == "gene_level_coloc" or package == "glc":
        gene_level_coloc(sys.argv[2:])
    elif package == "eqtplot" or package == "eqt":
        pass
    elif package == "colocquial" or package == "cql":
        pass
    else:
        print("Please use with -h/--help for usage.")

