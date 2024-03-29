#' eQTL data
#'
#' A dataset containing eQTL data
#' 
#' @docType data
#'
#' @usage data(eQTL.df.example)
#'
#' @format Dataframe, one row per SNP, with 5 columns
#' \describe{
#'   \item{SNP.Id}{Variant ID (such as dbSNP ID "rs..."). Data type: character
#'                 Note: naming scheme must be the same as what is used in the GWAS.df to ensure proper matching.}
#'   \item{Gene.Symbol}{Gene symbol to which the eQTL expression data refers. Data type: character 
#'                      Note: gene symbol must match entries in Genes.df to ensure proper matching.}
#'   \item{P.value}{P-value for the SNP from eQTL analysis. Data type: numeric}
#'   \item{NES}{Normalized effect size for the SNP from eQTL analysis. Data type: numeric 
#'              Note: Per GTEx, this is defined as the slope of the linear regression, and is computed 
#'              as the effect of the alternative allele relative to the reference allele in 
#'              the human genome reference.}
#'   \item{Tissue}{Tissue type to which the eQTL p-value/NES refer. Data type: character
#'                 Note: eQTL.df can contain multiple tissue types.}
#' }
#'
"eQTL.df.example"