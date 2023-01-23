import json
import os
import subprocess

def yes_no_input(prompt):
    while True:
        ans = input(prompt).casefold()
        if ans == 'y':
            return True
        elif ans == 'n':
            return False


def run_harmonization(harmonization_file):
        i = harmonization_file.rfind('/')
        harm_path = harmonization_file[:i]

        print('Running harmonization with {}...'.format(harmonization_file))
        subprocess.run(['bash', harmonization_file, harm_path])


def run_glc(args):
    config = open(args.file)
    input = json.load(config)['glc']

    hz = input['setup']['harmonization_file']
    if hz:
        i = hz.rfind('/')
        harm_path = hz[:i]

        override = False
        if os.path.exists('{}/GLGC_LDL_GWAS_harmonized.txt.gz'.format(harm_path)):
            override = yes_no_input("Harmonized output txt.gz file exists. Re-run harmonization and override existing file? (y/n)")
            
        if override:
            os.remove('{}/GLGC_LDL_GWAS_harmonized.txt.gz'.format(harm_path))
            run_harmonization(hz)
        else:
            print('Skipping harmonization...')


    cmd = ['Rscript', '{}/run_gene_level_coloc.R'.format(input['setup']['glc_dir'])]

    for k, v in input['params'].items():
        if v:
            cmd.append("--{}={}".format(k, v))

    subprocess.run(cmd)