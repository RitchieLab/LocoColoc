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