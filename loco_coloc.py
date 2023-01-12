import sys
import argparse
import os
import subprocess
import json

def yes_no_input(prompt):
    while True:
        ans = input(prompt).casefold()
        if ans == 'y':
            return True
        elif ans == 'n':
            return False


def init_glc_argparse(argv):
    parser = argparse.ArgumentParser(description="Gene Level Statistical Colocalization")
    parser.add_argument("-hz", "--harmonization",help="Full path to harmonization file to run. Read GLC ReadMe for default harmonization script.")
     
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-f","--file", help="Full path input for file input for running gene level coloc. Mutually exclusive with -i." )
    group.add_argument("-i", "--input",help="Manual input for running gene level coloc. Mutually exclusive with -f." )

    return parser.parse_args(argv)


def skip_hz():
    print("Skipping harmonization...")


def run_harmonization(harmonization_file):
        i = harmonization_file.rfind('/')
        harm_path = harmonization_file[:i]

        print('Running harmonization with {}...'.format(harmonization_file))
        subprocess.run(['bash', harmonization_file, harm_path])


def run_glc(glc_folder, glc_args):
    args_arr = ['Rscript', '{}/run_gene_level_coloc.R'.format(glc_folder)]

    for k, v in glc_args.items():
        if v:
            args_arr.append("--{}={}".format(k, v))

    subprocess.run(args_arr)


def gene_level_coloc(args):
    if not args.file:
        print("Must include path to input file.")
        return

    # Handle Harmonization
    if args.harmonization is None:
        skip_hz()
    else:
        i = args.harmonization.rfind('/')
        harm_path = args.harmonization[:i]

        override = False
        if os.path.exists('{}/GLGC_LDL_GWAS_harmonized.txt.gz'.format(harm_path)):
            override = yes_no_input("Harmonized output txt.gz file exists. Re-run harmonization and override existing file? (y/n)")
            
        if override:
            os.remove('{}/GLGC_LDL_GWAS_harmonized.txt.gz'.format(harm_path))
            run_harmonization(args.harmonization)
        else:
            skip_hz()

    # Run Coloc
    f = open(args.file)
    coloc_args = json.load(f)
    run_glc(args.gene_level_coloc, coloc_args)


def get_args(argv):
    parser = argparse.ArgumentParser(description="Loco Coloc")
    parser.add_argument("-qt", "--eqtplot", action=argparse.BooleanOptionalAction, help="Optional arg to include to use eQTpLot")
    parser.add_argument("-hz", "--harmonization", help="Path to harmonization file to run")
    parser.add_argument("-f", "--file", help="Path to input file")

    g = parser.add_mutually_exclusive_group()
    g.add_argument("-glc", "--gene-level-coloc", help="Path to folder containing run_gene_level_coloc.R")
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

#python loco_coloc.py -glc ./GLC -f ./GLC/example_input.JSON