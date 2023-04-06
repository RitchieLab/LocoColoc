run_eqt <- function(gwas_df, eqtl_df, genes_df, trait, gene, tissue = "all", gbuild="hg19",
                    sigpvalue_eQTL = 0.05, sigpvalue_GWAS = 5e-8, ld_df = TRUE, 
                    congruence = FALSE, leadSNP = TRUE, R2min = 0.2) {
    source("./eQTpLot/R/eQTpLot.R")

    GWAS.df <- get(load(gwas_df))
    eQTL.df <- get(load(eqtl_df))

    if (ld_df != TRUE) {
        ld_df <- get(load(ld_df))
    }

    if (!missing(genes_df)) {
        Genes.df <- get(load(genes_df))

        eQTpLot(GWAS.df=GWAS.df, eQTL.df=eQTL.df, Genes.df=Genes.df, LD.df=ld_df, 
            gene=gene, trait=trait, sigpvalue_GWAS=sigpvalue_GWAS, sigpvalue_eQTL= sigpvalue_eQTL,
            tissue=tissue, congruence=congruence, R2min=R2min, leadSNP=leadSNP, gbuild=gbuild)
    } else {
        eQTpLot(GWAS.df=GWAS.df, eQTL.df=eQTL.df, LD.df=ld_df, 
            gene=gene, trait=trait, sigpvalue_GWAS=sigpvalue_GWAS, sigpvalue_eQTL=sigpvalue_eQTL,
            tissue=tissue, congruence=congruence, R2min=R2min, leadSNP=leadSNP, gbuild=gbuild)
    }
}