#Copied over from /project/ritchie21/personal/wbone/ColocQuiaL_test/ColocQuiaL_test_config_files

#this R config file allows you to set the paths to all the dependency file you need to run the qtl colocalizer pipeline
# this config file is required for running the colocalizer pipeline on one locus

#provide the path to plink refernce files to be used for plink commands
plink_bfile = "/project/ritchie21/personal/wbone/ColocQuiaL_test/LD_reference_files/All_chr_merged_1KG"
#provide the path to the plink ped files for the list of individuals you wish to use in your LD reference panel
plink_keep = "/project/ritchie21/personal/wbone/ColocQuiaL_test/LD_reference_files/EUR.final.plink"

#provide path to GRCh37 to GRCh38 variant hash table directory
hash_table_dir = "/project/ritchie21/personal/wbone/ColocQuiaL_test/ftp.ncbi.nih.gov/snp/organisms/human_9606_b151_GRCh38p7/BED/"

#provide path to eqtl tissue table
eQTL_tissue_table = "/project/ritchie21/personal/wbone/ColocQuiaL_test/ColocQuiaL_test_config_files/GTEx_v8_Tissue_Summary_with_filenames.csv"
#provide path to sqtl tissue table
sQTL_tissue_table = ""

#provide path to significant eqtl data tabix directory NOTE: don't include last slash
eQTL_sig_qtl_tabix_dir = "/project/ritchie21/personal/wbone/ColocQuiaL_test/GTEx_eqtl_sigpairs_tabix"
#column number of column in significant eqtl files that contains geneID
eQTL_sig_geneID_col = 7 

#provide path to the all eqtl data tabix directory
eQTL_all_qtl_tabix_dir = "/project/ritchie21/personal/wbone/ColocQuiaL_test/GTEx_eqtl_allpairs_tabix/"
#provide the header to the eqtl data
eQTL_all_header = c("chrom_b38", "chromStart_b38", "chromEnd_b38", "eGeneID", "A1_eqtl", "A2_eqtl", "build", "tss_distance", "ma_samples", "ma_count", "maf", "pvalue_eQTL", "slope", "slope_se")
#name of column in header representing geneID
eQTL_all_geneID = "eGeneID" 
#name of column in header representing chromosome
eQTL_all_chrom = "chrom_b38"
#name of column in header representing end coordinate 
eQTL_all_chromEnd = "chromEnd_b38"
#name of column in header representing p-value
eQTL_all_pvalue = "pvalue_eQTL"

#provide path to significant sqtl data tabix directory NOTE: don't include last slash
sQTL_sig_qtl_tabix_dir = ""
#column number of column in significant sqtl files that contains geneID
sQTL_sig_geneID_col = ""

#provide path to the all sqtl data tabix directory
sQTL_all_qtl_tabix_dir = ""
#provide the header to the sqtl data
sQTL_all_header =  ""#c("")
#name of column in header representing geneID
sQTL_all_geneID = "" 
#name of column in header representing chromosome
sQTL_all_chrom = ""
#name of column in header representing end coordinate 
sQTL_all_chromEnd = ""
#name of column in header representing p-value
sQTL_all_pvalue = ""
#intron information
sQTL_all_intron_chr = "" 
sQTL_all_intron_bp_first = ""
sQTL_all_intron_bp_end = ""
sQTL_all_intron_clu = ""


#path to GRCh37 to GRCh38 liftOver chain file
liftOver_chain = "/appl/liftOver-20180423/chains/hg19ToHg38.over.chain"
#path to recombination rate directory (expected to b 1K genmoe chromosome recombination rate files or in the same format as these files: http://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/working/20130507_omni_recombination_rates/
recomb_rate_data="/project/ritchie21/personal/wbone/ColocQuiaL_test/recomb_data_dir/CEU/CEU"