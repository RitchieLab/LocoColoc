import json
import os
import copy
import glob
import time

import numpy as np
import pandas as pd
import rpy2.robjects as ro

def parse_cg_output(outfolder):
    param_arr = []

    for file in os.scandir(outfolder):
        if file.path.endswith('_colocProbs.txt'):
            df = pd.read_csv(file.path, sep="\t" ,usecols=['Gene', 'Tissue', 'GWAS.Lead.SNP'])
            df.rename(columns={'Gene': 'gene', 'Tissue': 'tissue', 'GWAS.Lead.SNP': 'leadSNP'}, inplace=True)
            data = df.to_dict(orient='records')
            param_arr = np.concatenate((param_arr, data))

    return param_arr


def parse_cql_output(outfolder):

    res = []
    while len(res) == 0:
        print('Waiting for ColocQuiaL to finish running...')
        time.sleep(30)
        res = glob.glob(outfolder + '*condPP4.txt')
    
    param_arr = []
    
    for file in res:
        df = pd.read_csv(file, sep="\t", usecols=['SNP', 'Gene', 'GeneID-Tissue'])
        df.rename(columns={'Gene': 'gene', 'GeneID-Tissue': 'tissue', 'SNP': 'leadSNP'}, inplace=True)
        df['tissue'] = df['tissue'].str.split('_', n=1, expand=True)[1]

        data = df.to_dict(orient='records')    
        param_arr = np.concatenate((param_arr, data))  

    return param_arr 


def run_eqt(args):
    config = json.load(open(args.file))

    if args.colo_gene:
        gene_tissue_pairs = parse_cg_output(config['cg']['params']['output_folder'])
    else:
        outfolder = config['cql']['setup_config']['colocquial_dir'] + '/analysis/'
        gene_tissue_pairs = parse_cql_output(outfolder)

    input = config['eqt']
    base_args = {**input['required']}

    for k, v in (input['required']).items():
        if k[-2:] == "df":
            base_args[k] = v
        
    for k, v in (input['optional']).items():
        if v != "":
                base_args[k] = v

    r = ro.r
    r('''source('./eQTpLot/R/eqt_wrapper.R')''')

    for gtp in gene_tissue_pairs:
        arg_dict = copy.deepcopy(base_args)
        arg_dict.update(gtp)

        run_eqt = ro.globalenv['run_eqt']
        run_eqt(**arg_dict)