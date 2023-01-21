import json

config = './cql_config.JSON'
cql_dir = './ColocQuiaL'
analysis_dir = '{}/analysis'.format(cql_dir)

f = open(config)
args = json.load(f)

setup_args = args['setup_config']
qtl_args = args['qtl_config']

setup_config_sh_keys = ['colocquial_dir', 'plink_bfile', 'plink_keep', 'bsub_queue']

setup_config_r_keys = ['plink_bfile', 'plink_keep', 'hash_table_dir', 'eQTL_tissue_table', 
                    'sQTL_tissue_table', 'eQTL_sig_qtl_tabix_dir', 'eQTL_sig_geneID_col',
                    'eQTL_all_qtl_tabix_dir', 'eQTL_all_header', 'eQTL_all_geneID',
                    'eQTL_all_chrom', 'eQTL_all_chromEnd', 'eQTL_all_pvalue',
                    'sQTL_sig_qtl_tabix_dir', 'sQTL_sig_geneID_col', 'sQTL_all_qtl_tabix_dir',
                    'sQTL_all_header', 'sQTL_all_geneID', 'sQTL_all_chrom', 'sQTL_all_chromEnd',
                    'sQTL_all_pvalue', 'sQTL_all_intron_chr', 'sQTL_all_intron_bp_first', 
                    'sQTL_all_intron_bp_end', 'sQTL_all_intron_clu', 'liftOver_chain', 'recomb_rate_data']

qtl_config_sh_keys = ['trait', 'traitFilePath', 'trait_A1col', 'trait_A2col', 
                    'trait_SNPcol', 'trait_CHRcol', 'trait_BPcol', 'trait_Pcol',
                    'trait_Ncol', 'trait_MAFcol', 'traitType', 'traitProp', 'leadSNPsFilePath',
                    'build', 'qtlType', 'window', 'clumpP1', 'clumpKB', 'clumpR2',
                    'setup_config_sh', 'setup_config_R']

qtl_config_r_keys = ['trait', 'traitFilePath', 'trait_A1col', 'trait_A2col', 
                    'trait_SNPcol', 'trait_CHRcol', 'trait_BPcol', 'trait_Pcol',
                    'trait_Ncol', 'trait_MAFcol', 'traitType', 'traitProp',
                    'build', 'qtlType', 'clumpP1', 'clumpKB', 'clumpR2',
                    'lead_SNP', 'setup_config_R']

arr = setup_args['eQTL_all_header']


with open('{}/setup_config.sh'.format(cql_dir), 'w') as setup_sh:
    for key in setup_config_sh_keys:
        setup_sh.write('{}=\"{}\"\n'.format(key, setup_args[key]))

setup_sh.close()

with open('{}/setup_config.R'.format(cql_dir), 'w') as setup_r:
    for key in setup_config_r_keys:

        if isinstance(setup_args[key], list):
            arr = setup_args[key]
            vector_string = 'c('
            for i in range(len(arr)):
                if i < len(arr) - 1:
                    vector_string += '\"{}\",'.format(arr[i])
                else:
                    vector_string += '\"{}\")'.format(arr[i])
            val = vector_string
        elif isinstance(setup_args[key], int) or isinstance(setup_args[key], float):
            val = '{}'.format(setup_args[key])
        else:
            val = '\"{}\"'.format(setup_args[key])
        
        setup_r.write('{} = {}\n'.format(key, val))
        
setup_r.close()

with open('{}/qtl_config.sh'.format(analysis_dir), 'w') as qtl_sh:
    for key in qtl_config_sh_keys:
        if isinstance(qtl_args[key], int) or isinstance(qtl_args[key], float):
            val = '{}'.format(qtl_args[key])
        else:
            val = '\"{}\"'.format(qtl_args[key])

        qtl_sh.write('{}={}\n'.format(key, val))
        
qtl_sh.close()

with open('{}/QTL_config.R'.format(analysis_dir), 'w') as qtl_r:
    for key in qtl_config_r_keys:
        
        if isinstance(qtl_args[key], int) or isinstance(qtl_args[key], float):
            val = '{}'.format(qtl_args[key])
        else:
            val = '\"{}\"'.format(qtl_args[key])

        qtl_r.write('{} = {}\n'.format(key, val))
    
    qtl_r.write('chrom = CHROMOSOME\n')
    qtl_r.write('colocStart = STARTBP\n')
    qtl_r.write('colocStart = STOPBP\n')

qtl_r.close()

