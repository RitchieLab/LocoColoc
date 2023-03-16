run_eqt <- function(gwas_df, eqtl_df, genes_df, ld_df = TRUE, gene, trait,
                    sigpvalue_GWAS = 5e-8, sigpvalue_eQTL = 0.05,
                    tissue = "all", range = 200, NESeQTLRange = c(NA,NA), 
                    congruence = FALSE, R2min = 0.2, LDmin = 10, leadSNP = TRUE,
                    LDcolor = "color", ylima = NA, ylimd = NA, xlimd = NA,
                    genometrackheight = 2, gbuild = "hg19",
                    res = 300, wi = "wi", CollapseMethod = "min",
                    getplot = TRUE, saveplot = TRUE,
                    GeneList = FALSE, TissueList = FALSE) {
    source("./eQTpLot/R/eQTpLot.R")

    GWAS.df <- get(load(gwas_df))
    eQTL.df <- get(load(eqtl_df))

    if (ld_df != TRUE) {
        ld_df <- get(load(ld_df))
    }

    if (!missing(genes_df)) {
        Genes.df <- get(load(genes_df))

        eQTpLot(GWAS.df=GWAS.df, eQTL.df=eQTL.df, Genes.df=Genes.df, LD.df=ld_df, 
            gene=gene, trait=trait,sigpvalue_GWAS=sigpvalue_GWAS, sigpvalue_eQTL= sigpvalue_eQTL,
            tissue=tissue, range=range, NESeQTLRange=NESeQTLRange, 
            congruence=congruence, R2min=R2min, LDmin=LDmin, leadSNP=leadSNP,
            LDcolor=LDcolor, ylima=ylima, ylimd=ylimd, xlimd=xlimd,
            genometrackheight=genometrackheight, gbuild=gbuild,
            res=res, wi=wi, CollapseMethod=CollapseMethod,
            getplot=getplot, saveplot=saveplot,
            GeneList=GeneList, TissueList=TissueList)
    } else {
        eQTpLot(GWAS.df=GWAS.df, eQTL.df=eQTL.df, LD.df=ld_df, 
            gene=gene, trait=trait,sigpvalue_GWAS=sigpvalue_GWAS, sigpvalue_eQTL=sigpvalue_eQTL,
            tissue=tissue, range=range, NESeQTLRange=NESeQTLRange, 
            congruence=congruence, R2min=R2min, LDmin=LDmin, leadSNP=leadSNP,
            LDcolor=LDcolor, ylima=ylima, ylimd=ylimd, xlimd=xlimd,
            genometrackheight=genometrackheight, gbuild=gbuild,
            res=res, wi=wi, CollapseMethod=CollapseMethod,
            getplot=getplot, saveplot=saveplot,
            GeneList=GeneList, TissueList=TissueList)
    }
}