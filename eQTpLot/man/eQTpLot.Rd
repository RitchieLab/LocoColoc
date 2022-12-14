% Generated by roxygen2: do not edit by hand
% Please edit documentation in R/eQTpLot.R
\name{eQTpLot}
\alias{eQTpLot}
\title{An eQTpLot function}
\usage{
eQTpLot(
  GWAS.df,
  eQTL.df,
  Genes.df,
  LD.df = TRUE,
  gene,
  trait,
  sigpvalue_GWAS = 5e-08,
  sigpvalue_eQTL = 0.05,
  tissue = "all",
  range = 200,
  NESeQTLRange = c(NA, NA),
  congruence = FALSE,
  R2min = 0.2,
  LDmin = 10,
  leadSNP = TRUE,
  LDcolor = "color",
  ylima = NA,
  ylimd = NA,
  xlimd = NA,
  genometrackheight = 2,
  gbuild = "hg19",
  res = 300,
  wi = "wi",
  CollapseMethod = "min",
  getplot = TRUE,
  saveplot = TRUE,
  GeneList = FALSE,
  TissueList = FALSE
)
}
\arguments{
\item{GWAS.df}{Dataframe, one row per SNP, as one might obtain from a PLINK association analysis, with columns :
CHR          Chromosome for SNP (X coded numerically as 23)
BP           Chromosomal position for each SNP, in base pairs
SNP          Variant ID (such ws dbSNP ID "rs...". Note: Must be the same naming scheme as  used in the eQTL.df to ensure proper matching)
P            P value for the SNP from GWAS analysis
BETA         Beta for SNP from GWAS analysis
PHE          (Optional) Name of the phenotype for which the GWAS was run. This column is optional, and is useful if your GWAS.df contains data for multiple phenotypes,
such as one might obtain from a PheWAS). The "trait" parameter is subsequently used to filter in the GWAS.df entries for only this phenotype.
If GWAS.df does not contain a "PHE" column, eQTpLot will assume all the supplied GWAS data is for the phenotype specified by the "trait" parameter}

\item{eQTL.df}{Dataframe, one row per SNP, as one might obtain from the GTEx Portal, with columns:
SNP.Id       Variant ID (such ws dbSNP ID "rs...". Note: Must be the same naming scheme as used in the GWAS.df to ensure proper matching)
Gene.Symbol  Gene symbol/name to which the eQTL expression data refers (Note: gene symbol/name must match entries in Genes.df to ensure proper matching)
P.value      pvalue for the SNP from eQTL analysis (such as one might download from the GTEx Portal)
NES          NES (normalized effect size) for the SNP from eQTL analysis
(Per GTEx: defined as the slope of the linear regression, and is computed as the effect of the alternative allele (ALT) relative to the reference allele (REF) in the human genome reference
(i.e., the eQTL effect allele is the ALT allele). NES are computed in a normalized space where magnitude has no direct biological interpretation.)
Tissue       Tissue type to which the eQTL pvalue/beta refer
(Note: eQTL.df can contain multiple tissue types. Specifying the tissue type to be analyzed will filter only for eQTL entires for this tissue type.
Alternatively, setting tissue type to "all" (the default setting) will automatically pick the smallest eQTL pvalue for each SNP across all tissues for a PanTissue analysis)
N            (Optional) The number of samples used to calculate the p-value and NES for the eQTL data. This value is used if performing a MultiTissue or PanTissue analysis with the option eQTL.Collapse.Method set to "meta"}

\item{Genes.df}{Dataframe, one row per gene, with the following columns
(Note: eQTpLot automatically loads a default Genes.df database containing information for both genomic builds hg19 and hg38,
but you may wish to specify our own Genes.df dataframe if your gene of interest is not included in the default dataframe, or if your eQTL data uses a different gene naming scheme
(for example, Gencode ID instead of gene symbol)):
Gene         Gene symbol/name for which the Coordinate data (below) refers to
(Note: gene symbol/name must match entries in eQTL.df to ensure proper matching)
CHR          Chromosome the gene is on (X coded numerically as 23)
Start        Chromosomal coordinate of start position (in basepairs) to use for gene (Note: this should be the smaller of the two values between Start and Stop)
Stop         Chromosomal coordinate of end position (in basepairs) to use for gene (Note: this should be the larger of the two values between Start and Stop)
Build        The genome build (either hg19 or hg38) for the location data -
the default Genes.df dataframe contains entries for both genome builds for each gene, and the script will select the appropriate entry based on the specified gbuild (default is hg19)).}

\item{LD.df}{Optional dataframe of SNP linkage data, one row per SNP pair, with columns as one might obtain from a PLINK linkage analysis using the PLINK --r2 option:
(If no LD.df is supplied, eQTpLot will plot data without LD information)
BP_A         Basepair position of the first SNP in the LD pair
SNP_A        Variant name of the first SNP in the LD pair (Not: only SNPs that also appear in the GWAS.df SNP column will be used for LD analysis)
BP_B         Basepair position of the second SNP in the LD pair
SNP_B        Variant name of the second SNP in the LD pair (Note: only SNPs that also appear in the GWAS.df SNP column will be used for LD analysis)
R2           Squared correlation measure of linkage between the two SNPs in the pair}

\item{gene}{name/symbol of gene to analyze, in quotes}

\item{trait}{name of GWAS phenotype to analyze, in quotes. If all the data in GWAS.df is for a single phenotype and no PHE column is present, this parameter will be used as the name for the analyzed phenotype.
If GWAS.df contains information on multiple phenotypes, as specified in the optional GWAS.df PHE column, this parameter will be used to filter in GWAS.df entries for only this phenotype.}

\item{sigpvalue_GWAS}{GWAS pvalue significance threshold to use (this value will be used for a horizontal line in plot A, and to define GWAS significant/non-significant SNPs for plot C)}

\item{tissue}{tissue type, in quotes, for eQTL data to use (from eQTL.df, default setting is "all" for Pan-Tissue analysis)}

\item{range}{range, in kB, to extend analysis window on either side of gene boundry. Default is 200 kb}

\item{NESeQTLRange}{the maximum and minimum limits in the format c(min,max), to display for the NES value in eQTL.df.
The default setting will adjust the size limits automatically for your data, whereas specifying the limits
can keep them consistent between plots.}

\item{congruence}{if set to TRUE, variants with congruent and incongruent effects will be plottes separately. Default is FALSE.}

\item{R2min}{R^2 values less than this value in the the LD.df (is supplied) will not be displayed. Default is 0.1}

\item{LDmin}{for the LDheatmap panel, only variants that are in LD (with R^2 > R2min) with at least this many other variants will be displayed. The default is 10}

\item{leadSNP}{if LD.df data is included, this parameter is used to specify the lead SNP to use for plotting LD information in the P-P plots. The SNP ID must be present in both the GWAS.df and LD.df dataframes.}

\item{LDcolor}{the default color scheme for the LDheatmap is in the viridis color palate. This option can be set to "black" to plot the LDheatmap in grayscale}

\item{ylima}{used to manually adjust the y axis limit in plot A, if needed}

\item{ylimd}{used to manually adjust the y axis limit for the P-P plot, if needed}

\item{xlimd}{used to manually adjust the x axis limit for the P-P plot, if needed}

\item{genometrackheight}{used to set the height of the genome track panel (B), with default setting of 2.
Gene-dense regions may require more plotting space, whereas gene-poor regions may look better with less plotting space.}

\item{gbuild}{the genome build to use, in quotes, for fetching genomic information for panel B.
Default is "hg19" but can specify "hg38" if needed. This build should match the genome build used for "CHR" and "BP" in the GWAS.df}

\item{res}{resolution of the output plot image (default is 300 dpi)}

\item{wi}{the width of the output plot image (the height is calculated from this to maintain the correct aspect ratio)}

\item{CollapseMethod}{the method used to collapse eQTL p-values and NES across tissues, if a MultiTissue or PanTissue analysis is used.
Default is "min" (which selects the p-value and NES from the tissue with the smallest p-value for each variant).
"median" and "mean" can be specified instead, which will take the median or mean of the p-value and NES for each variant, across all specified tissues
"meta" can be specified instead, which will perform a simple weighted meta-analysis (Stouffer et al., 1949) of the p-values across the specified tissues.
NOTE: If "meta" is specified, eQTL.df must include a column with header "N" indicating the number of samples used to derive the given eQTL pvalue.
NOTE: If "meta" is specified, the Normalized Effect Size witll not be computed, and all variants will be displayed as the same size.}

\item{getplot}{default is TRUE. If set to false, script will not dsiplay the generated plot in the viewer}

\item{saveplot}{default is TRUE, script will save the generated plot in the working diretory with the name
"gene.trait.tissue.eQTL.png" using the supplied variables}

\item{GeneList}{used to obtain the Pearson correlation between eQTL and GWAS p-values for a given tissue across a user-supplied list of genes. Default is FALSE.}

\item{TissueList}{used to obtain the Pearson correlation between eQTL and GWAS p-values for a given gene across a user-supplied list of tissues. Default is FALSE.}

\item{sigpvalue_eQTLeQTL}{pvalue significance threshold to use (eQTL data with a pvalue larger than this threshold will be excluded from the analysis)}
}
\description{
This function creates an eQTpLot composite
}
\examples{
Saves to current directory
eQTpLot(Genes.df = Genes.df.example, GWAS.df = GWAS.df.example,
        eQTL.df = eQTL.df.example, gene = "ACTN3", trait = "LDL",
        getplot=FALSE)
eQTpLot()
}
