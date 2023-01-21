#This sh config file was copied over from /project/ritchie21/personal/wbone/ColocQuiaL_test/ColocQuiaL_test_config_files

#this bash config file allows you to set the paths to all the dependency file you need to run the qtl colocalizer pipeline
#this config file is required for running the colocalizer pipeline on multiple loci at a time

#path to the directory where the ColocQuiaL code is saved locally
#colocquial_dir="/project/ritchie21/personal/wbone/ColocQuiaL_test/coloc_refactor_git/ColocQuiaL"
colocquial_dir="/home/nimay512/repos/LocoColoc/ColocQuiaL"

#provide the path to plink refernce files to be used for plink commands
plink_bfile="/project/ritchie21/personal/wbone/ColocQuiaL_test/LD_reference_files/All_chr_merged_1KG"
#provide the path to the plink ped files for the list of individuals you wish to use in your LD reference panel
plink_keep="/project/ritchie21/personal/wbone/ColocQuiaL_test/LD_reference_files/EUR.final.plink"

bsub_queue="epistasis_normal"