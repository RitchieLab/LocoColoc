# eQTpLot

## Visualization of Colocalization Between eQTL and GWAS Data
eQTpLot is an intuitive and user-friendly R package developed for the visualization of colocalization between eQTL and GWAS data. eQTpLot takes as input standard GWAS and eQTL summary statistics, and optional pairwise LD information, to generate a series of plots visualizing colocalization, correlation, and enrichment between eQTL and GWAS signals for a given gene-trait pair. With eQTpLot, investigators can easily generate a series of customizable plots clearly illustrating, for a given gene-trait pair: 

<ol>
<li>colocalization between GWAS and eQTL signals</li> 
<li>correlation between GWAS and eQTL p-values</li>
<li>enrichment of eQTLs among trait-significant variants</li>
<li>the LD landscape of the locus in question</li>
<li>the relationship between the direction of effect of eQTL signals and the direction of effect of colocalizing GWAS peaks</li> 
</ol>

These clear and comprehensive plots provide a unique view of eQTL-GWAS colocalization, allowing for a more complete understanding of the interaction between gene expression and trait associations. eQTpLot was developed in R version `4.0.0` and depends on a number of packages for various aspects of its implementation 

`c("biomaRt", "dplyr", "GenomicRanges", "ggnewscale", "ggplot2", "ggplotify", "ggpubr", "gridExtra", "Gviz", "LDheatmap", "patchwork")`

<p>&nbsp;</p>
<p>&nbsp;</p>

## Table of Contents
  - [Installation](#installation)
  - [Input files](#input-files)
      - [GWAS.df](#gwasdf)
      - [eQTL.df](#eqtldf)
      - [Genes.df](#genesdf)
      - [LD.df](#lddf)
  - [Function arguments](#function-arguments)
  - [Notes on Analysis](#notes-on-analysis)
      - [Congruence/Incongruence](#congruence-incongruence)
      - [PanTissue and MultiTissue Analysis](#pantissue-and-multitissue-analysis)
  - [Generation of Each Panel](#generation-of-each-panel)
      - [Generation of the main eQTL-GWAS Colocalization Plot](#generation-of-the-main-eqtl-gwas-colocalization-plot)
      - [Generation of the eQTL Enrichment Plot](#generation-of-the-eqtl-enrichment-plot)
      - [Generation of P-P Correlation Plots](#generation-of-p-p-correlation-plots)
  - [Use Examples](#use-examples)
    + Example 1 – comparing eQTpLots for two genes within a linkage peak
      - [Figure 1](#figure-1)
      - [Figure 2](#figure-2)
    + Example 2 –The `TissueList` function and adding LD information to eQTpLot
      - [Figure 3](#figure-3)
    + Example 3 – Separating Congruous from Incongruous Variants]
      - [Figure 4](#figure-4)

<p>&nbsp;</p>
<p>&nbsp;</p>

## Installation

eQTpLot can be install using `devtools`, either directly from GitHub,

`devtools::install_github("RitchieLab/eQTpLot")`

or by downloading the repository to your computer, unzipping, and installing the `eQTpLot` folder.

`devtools::install("eQTpLot")`

*Note: For issues installing dependencies, try running the following code prior to installation.

`Sys.setenv(R_REMOTES_NO_ERRORS_FROM_WARNINGS=TRUE)`

<p>&nbsp;</p>
<p>&nbsp;</p>

## Input files
At a minimum, eQTpLot requires two input data frames: 

<ol>
<li>GWAS summary statistics (compatible with PLINK --linear/logistic output format https://www.cog-genomics.org/plink/1.9/formats#assoc_linear) </li>
<li>eQTL summary statistics, ex. downloaded directly from the GTEx portal https://gtexportal.org/home/</li> 
</ol>


Two optional data frames may also be supplied:

<ol>
<li>pairwise linkage disequilibrium (LD) data for the analyzed variants</li>
<li>gene coordinates</li> 
</ol>

The formatting parameters of all both required and both optional input files are summarized below.

#### GWAS.df
`GWAS.df` is a data frame of GWAS summary data with one row per SNP, ex. PLINK `.assoc.linear, .assoc.logistic` format, containing the following columns:

**Column**|**Description**
-----|:-----
  `CHR`|Chromosome for SNP (sex chromosomes coded numerically). Data type: integer
  `POS`|Chromosomal position for each SNP, in base pairs. Data type: integer
  `SNP`|Variant ID (such as dbSNP ID "rs...". *Note: Must be the same naming scheme as used in `eQTL.df` to ensure proper matching).* Data type: character  
  `P`|p-value for the SNP from GWAS analysis. Data type: numeric 
  `BETA`|beta for the SNP from GWAS analysis. Data type: numeric 
  `PHE`|*OPTIONAL* Name of the phenotype for which the GWAS data refers, useful if your `GWAS.df` contains data for multiple phenotypes, i.e. PheWAS. If not provided, eQTpLot will assume the GWAS data is for a single phenotype, specified with the `trait` argument. Data type: character 

```
> data(GWAS.df.example)
> head(GWAS.df.example)
  CHR       BP             SNP       P       BETA        PHE
1  11 66078129       rs1625595 0.06646 -7.925e-05 Creatinine
2  11 66078252     rs565374903 0.17350 -1.915e-02 Creatinine
3  11 66078296     rs750544051 0.03073 -4.299e-02 Creatinine
4  11 66078347 11:66078347_C_G 0.64030 -9.298e-03 Creatinine
5  11 66078368     rs541384459 0.93890  5.763e-04 Creatinine
6  11 66078385     rs138591375 0.34690  1.647e-03 Creatinine
```

<p>&nbsp;</p>

#### eQTL.df
`eQTL.df` is a data frame of eQTL data, one row per SNP, ex. downloaded directly from the GTEx Portal in .csv format, containing the following columns:

**Column**|**Description**
-----|:-----
  `SNP.Id`|Variant ID *Note: naming scheme must be the same as what is used in the `GWAS.df` to ensure proper matching.* Data type: character
  `Gene.Symbol`|Gene symbol to which the eQTL expression data refers *Note: gene symbol must match entries in `Genes.df` to ensure proper matching.* Data type: character
  `P.value`|P-value for the SNP from eQTL analysis Data type: numeric  
  `NES`|Normalized effect size for the SNP from eQTL analysis (Per GTEx, defined as the slope of the linear regression, and is computed as the effect of the alternative allele relative to the reference allele in the human genome reference. Data type: numeric 
  `Tissue`|Tissue type to which the eQTL p-value/NES refer *Note: eQTL.df can contain multiple tissue types.* Data type: character
  `N`|*OPTIONAL* Number of samples used to calculate the p-value and NES for the eQTL data, used if performing a MultiTissue or PanTissue analysis with the option CollapseMethod set to "meta" for a simple sample size weighted meta-analysis. Data type: character

```
> data(eQTL.df.example)
> head(eQTL.df.example)
  Gene.Symbol      SNP.Id   P.Value       NES               Tissue
1       PELI3 rs138677235 0.0377103 -0.139874 Adipose_Subcutaneous
2       PELI3 rs111472085 0.0131649  0.257579 Adipose_Subcutaneous
3       PELI3  rs75325358 0.0442168 -0.147111 Adipose_Subcutaneous
4       PELI3 rs113298476 0.0442168 -0.147111 Adipose_Subcutaneous
5       PELI3  rs73490435 0.0134318  0.256645 Adipose_Subcutaneous
6       PELI3 rs112219657 0.0387010  0.214056 Adipose_Subcutaneous
```
  
<p>&nbsp;</p>

#### Genes.df
`Genes.df` is an optional data frame, one row per gene, which should contain the following columns: 

*Note: eQTpLot automatically loads a default `Genes.df` containing information for most protein-coding genes for genome builds hg19 and hg38, but you may wish to specify our own `Genes.df` data frame if your gene of interest is not included in the default data frame, or if your eQTL data uses a different gene naming scheme (for example, Gencode ID instead of gene symbol)*

**Column**|**Description**
-----|:-----
`Gene`|Gene symbol/name for which the Coordinate data refers to *Note: gene symbol/name must match entries in `eQTL.df` to ensure proper matching.* Data type: character
`CHR`|Chromosome the gene is on *Note: do not include a "car" prefix, and sex chromosomes should be coded numerically.* Data type: integer
`Start`|Chromosomal coordinate of start position (in basepairs) to use for gene *Note: this should be the smaller of the two values between `Start` and `Stop`.* Data type: integer
`Stop`|Chromosomal coordinate of end position (in basepairs) to use for gene *Note: this should be the larger of the two values between `Start` and `Stop`.* Data type: integer  
`Build`|The genome build for the coordinate data -- the default `Genes.df` dataframe contains entries for both genome builds for each gene, and the script will select the appropriate entry based on the specified `gbuild` (default is `"hg19"`)). Data type: character, `c("hg19", "hg38")`

```
> data(Genes.df.example)
> head(Genes.df.example)
  CHR    Start     Stop    Gene Build
1  19 58858171 58864865    A1BG  hg19
2  10 52559168 52645435    A1CF  hg19
3  12  9220303  9268825     A2M  hg19
4  12  8975067  9039798   A2ML1  hg19
5   1 33772366 33786699 A3GALT2  hg19
6  22 43088117 43117307  A4GALT  hg19
```

<p>&nbsp;</p>

#### LD.df
`LD.df` is an optional data frame of SNP linkage data, one row per SNP pair, compatible with PLINK .ld (--r/--r2) file format https://www.cog-genomics.org/plink/1.9/formats#ld

*Note: If no `LD.df` is supplied, eQTpLot will plot data without LD information*

**Column**|**Description**
-----|:-----
`BP_A`|Base pair position of the first variant in the LD pair. Data type: integer	
`SNP_A`|Variant ID of the first variant in the LD pair. Data type: character	
`BP_B`|Base pair position of the second variant in the LD pair. Data type:integer
`SNP_B`|Variant ID of the second variant in the LD pair. Data type: character
`R2`|Squared correlation measure of linkage between the two variants. Data type: numeric

```
> data(LD.df.example)
> head(LD.df.example)
  CHR_A     BP_A     SNP_A CHR_B     BP_B            SNP_B       R2
1    11 66078129 rs1625595    11 66079275 11:66079275_GA_G 0.299550
2    11 66078129 rs1625595    11 66079361       rs33981819 0.686453
3    11 66078129 rs1625595    11 66079786         rs490972 0.991748
4    11 66078129 rs1625595    11 66079787         rs565972 0.991756
5    11 66078129 rs1625595    11 66079818       rs61891388 0.706614
6    11 66078129 rs1625595    11 66080770        rs7924580 0.309860
```

*Note: variants in SNP_A and SNP_B must also appear in the `GWAS.df` SNP column to be used for LD analysis.*

<p>&nbsp;</p>
<p>&nbsp;</p>
   

## Function arguments

**Required Arguments**

Argument|Description
-----|-----
`eQTL.df`|a data frame of eQTL summary statistic data, as defined above
`GWAS.df`|a data frame of GWAS summary statistic data, as defined above
`gbuild`|**Default: “hg19”**. The genome build to use for fetching genomic information for the genome track (panel B). This build should match the genome build used for chromosomal positions in `GWAS.df`. Currently compatibile with hg19 and hg38.
`gene`| gene name or symbol *Note: gene name must match an entry in `Genes.df` for the specified gbuild*
`sigpvalue_eQTL`|**Default: 0.05**. Significance threshold for eQTL data (variants with eQTL p-value > `sigpvalue_eQTL` are excluded from analysis)
`sigpvalue_GWAS`|**Default: 5e-8**. Significance threshold for GWAS data (corresponds to the horizontal line in plot A and GWAS significance thresholds for the eQTL enrichment plot). 
`tissue`|**Default: “all”**. Single tissue or list of tissue names to filter `eQTL.df` by. If this parameter is set to “all”, eQTpLot will pick the smallest eQTL p-value for each SNP across all tissues for a PanTissue analysis (described in more detail below). *Note: the tissue name must match at least one entry in the `eQTL.df` `Tissue` column*
`trait`|name of the GWAS phenotype to analyze. If no `PHE` column is present in `GWAS.df`, this argument will be used as the name for the analyzed phenotype. If `GWAS.df` contains multiple phenotypes in the `PHE` column, this parameter will be used to filter in `GWAS.df` for only this phenotype.

<p>&nbsp;</p>

**Optional Arguments**

Argument|Description
-----|-----
`Genes.df`|A data frame of gene coordinates, as defined above
`LD.df`|A data frame of pairwise linkage data, as defined above
`congruence`|**Default: FALSE**. If TRUE, variants with congruent and incongruent effects will be plotted separately, as described below. 
`genometrackheight`|**Default: 2**. Relative height of the genome track panel (B). Gene-dense regions may require more plotting space, whereas gene-sparse regions may look better with less plotting space.
`getplot`|**Default: TRUE**. Displays the generated plot in the viewport.
`LDcolor`|**Default: “color”**. Determines the color palette used in the LDheatmap panel if `LD.df` is supplied. Options are `c("color", "black")` for viridis and grayscales, respectively. 
`LDmin`|**Default: 10**. Only variants in LD, i.e. R<sup>2</sup> > `R2min`, with at least this many other variants will be plotted in the LDheatmap panel if `LD.df` is supplied. This parameter can be used to thin the number of variants being plotted in the LDheatmap. *Warning: setting `LDmin` and/or `R2min` too low when dealing with high density data may cause performance issues; eQTpLot will give a warning if attempting to plot > 1,000 SNPs*
`leadSNP`|Name of the lead SNP to use for plotting LD information in the P-P plots, if `LD.df` is supplied. The name of the variant must be present in both `GWAS.df` and `LD.df`.
`NESeQTLRange`| a list of maximum and minimum limits `c(min,max)`, to display for the `NES` value in `eQTL.df`. The default setting will adjust the size scale automatically to fit the displayed data, whereas specifying the limits will keep them consistent between plots.
`R2min`|Only used if `LD.df` is supplied. **Default: 0.1**. The threshold for R<sup>2</sup> to use when selecting LD data from `LD.df`. Variant pairs with R<sup>2</sup> < `R2min` will not be included in the analysis. *Warning: setting `LDmin` and/or `R2min` too low when dealing with high density data may cause performance issues; eQTpLot will give a warning if attempting to plot > 1,000 SNPs*
`range`|**Default: 200**. The range, in kB, to extend the analysis window on either side of the gene of interest, as defined by the `Start` and `Stop` points for the specified `gene` in `Genes.df`.
`res`|**Default: 300**. The resolution, in dpi, for the output plot image 
`saveplot`|**Default: TRUE**. Saves the generated plot in the working directory with the name "`gene`.`trait`.`tissue`.Congreunce_Info.LD_Info.eQTpLot.png", using the provided arguments
`wi`|**Default: 12 if `LD.df` is not supplied, 14 if `LD.df` is supplied**. The width of the output plot image, in inches. The height of the plot is calculated from this argument as well to maintain the appropriate aspect ratio.
`xlimd`|sets the x-axis upper limit for the P-P plot
`ylima`|sets the y-axis upper limit in plot A
`ylimd`|sets the y-axis upper limit for the P-P plot
`CollapsMethod`|**Default: “min”**. the method used to collapse eQTL p-values and NES across tissues if a MultiTissue or PanTissue analysis is specified. If set to "min”, the p-value and NES from the tissue with the smallest p-value for each variant will be selected. If set to "median" or "mean" the median or mean p-value and NES for each variant, across all specified tissues, will be selected. If set to “meta” eQTpLot will perform a simple sample-size-weighted meta-analysis of the p-values across all specified tissues. If "meta" is specified, `eQTL.df` should include a column with header "N" indicating the number of samples used to derive the given eQTL data. If no column N is present, eQTpLot will give the user the option to complete a meta-analysis assuming equal sample sizes for all tissues, which may lead to inaccurate results. Additionally. if "meta" is specified, no meta-analyzed NES will be computed and all variants will be displayed as the same size in the main eQTpLot figure.
`Gene.List`| **Default: FALSE**. If set to TRUE, outputs the Pearson correlation between eQTL and GWAS p-values for a given tissue across a user-supplied list of genes, ordered by significance. No plots will be generated. If the user sets the parameter tissue to “all,” or to a list of tissues, eQTpLot will collapse the eQTL data for these tissues by variant, using the method specified by the parameter `CollapseMethod`. This may be a useful parameter to obtain a very simple bird’s-eye view of the genes at a locus whose expression is most closely correlated to a relevant GWAS signal for a given trait.
`Tissue.List`|**Default: FALSE**. If TRUE, this parameter will output the Pearson correlation between eQTL and GWAS p-values for a given gene across a user-supplied list of tissues, ordered by significance. No plots will be generated. If the user sets the parameter tissue to “all,” eQTpLot will consider each tissue included in `eQTL.df`. This may be a useful parameter to obtain a very simple bird’s-eye view of the tissues in which a given gene’s expression is most closely tied to a relevant GWAS signal for a given trait.




<p>&nbsp;</p>
<p>&nbsp;</p>

## Notes on Analysis

In its simplest implementation, eQTplot takes as input two data frames, one of GWAS summary data and the other of eQTL summary data, with the user specifying the name of the gene to be analyzed, the GWAS trait to be analyzed (useful if the GWAS data contains information on multiple associations, as one might obtain from a Phenome-wide Association Study (PheWAS)), and the tissue type to use for the eQTL analysis. Using these inputs, eQTpLot generates a series of plots intuitively illustrating the colocalization of GWAS and eQTL signals in chromosomal space, and the enrichment of and correlation between the candidate gene eQTLs and trait-significant variants. Additional parameters and data can be supplied, such as pairwise variant LD information, allowing for an even more comprehensive visualization of the interaction between eQTL and GWAS data within a given genomic locus.


#### Congruence/Incongruence
One major implementation feature of eQTpLot is the option to divide eQTL/GWAS variants into two groups based on their directions of effect. If the argument `congruence` is set to TRUE, all variants are divided into two groups: congruous, or those with the same direction of effect on gene expression and the GWAS trait (e.g., a variant that is associated with increased expression of the candidate gene and an increase in the GWAS trait), and incongruous, or those with opposite directions of effect on gene expression and the GWAS trait (e.g., a variant that is associated with increased expression of the candidate gene but a decrease in the GWAS trait). The division between congruous and incongruous variants provides a more nuanced view of the relationship between gene expression level and GWAS associations – a variant associated with increased expression of a candidate gene and an increase in a given GWAS trait would seem to be operating through different mechanisms that a variant that is similarly associated with increased expression of the same candidate gene, but a decrease in the same GWAS trait. eQTpLot intuitively visualizes these differences as described below. This distinction also serves to illuminate important underlying biologic difference between different gene-trait pairs, discriminating between genes that appear to suppress a particular phenotype and those that appear to promote it.

#### PanTissue and MultiTissue Analysis
In some instances, it may be of interest to visualize a variant’s effect on candidate gene expression across multiple tissue types, or even across all tissues. Such analyses can be accomplished by setting the argument `tissue` to a list of tissues contained within `eQTL.df` *(e.g. c(“Adipose_Subcutaneous”, “Adipose_Visceral”))* for a MultiTissue analysis, or by setting the argument `tissue` to “all” for a PanTissue analysis. In a PanTissue analysis, eQTL data across all tissues contained in `eQTL.df` will be collapsed, by variant, into a single pan-tissue eQTL; a similar approach is used in a MultiTissue analysis, but in this case eQTL data will be collapsed, by variant, across only the specified tissues. The method by which eQTpLot collapses eQTL data can be specified with the argument `CollapseMethod`, which accepts as input one of four options – “min,” “median,” “mean,” or “meta.” By setting `CollapseMethod` to “min” (the default), for each variant the tissue with the smallest eQTL p-value will be selected, such that each variant’s most significant eQTL effect, agnostic of tissue, can be visualized. Setting the parameter to “median” or “mean” will visualize the median or mean p-value and NES value for each SNP across all specified tissues. Lastly, setting `CollapseMethod` to “meta” will perform a simple sample-size-weighted meta-analysis *(i.e. a weighted Z-test)* for each variant across all specified tissues, visualizing the resultant p-value for each variant. It should be noted that this meta-analysis method requires a sample size for each eQTL entry in `eQTL.df`, which should be supplied in an optional column “N.” If sample size numbers are not readily available *(as may be the case if directly downloading cis-eQTL data from the GTEx portal)*, eQTpLot gives the user the option to presume that all eQTL data is derived from identical sample sizes across all tissues – this approach may of course yield inaccurate estimates of a variant’s effect in meta-analysis, but may be useful to the user.



<p>&nbsp;</p>
<p>&nbsp;</p>

## Generation of Each Panel

#### Generation of the main eQTL-GWAS Colocalization Plot
To generate the main eQTL-GWAS Colocalization Plot (Figures 1A, 2A, 3A, 4A), a locus of interest (LOI) is defined to include the target gene’s chromosomal coordinates (as listed in `Genes.df`, for the indicated `gbuild`, for the user-specified `gene`), along with a range of flanking genome (specified with the argument `range`, with a default value of 200 kilobases on either side of the gene). GWAS summary statistics from `GWAS.df` are filtered to include only variants that fall within the LOI. The variants are then plotted in chromosomal space along the horizontal axis, with the inverse log of the p-value of association with the specified GWAS trait (P<sub>GWAS</sub>) plotted along the vertical axis, as one would plot a standard GWAS Manhattan plot. The GWAS significance threshold, `sigpvalue_GWAS` (default value 5e-8), is depicted with a red horizontal line.

Within this plot, variants that lack eQTL data for the target gene in `eQTL.df` (or for which the eQTL p-value (P<sub>eQTL</sub>) does not meet the specified significance threshold, `sigpvalue_eQTL` (default value 0.05)) are plotted as grey squares. On the other hand, variants that act as eQTLs for the target gene (withP<sub>eQTL</sub> < `sigpvalue_eQTL`) are plotted as colored triangles, with a color gradient corresponding to the inverse magnitude ofP<sub>eQTL</sub>. As noted above, an analysis can be specified to differentiate between variants with congruous versus incongruous effects on the GWAS trait and candidate gene expression levels – if this is the case, variants with congruous effects will be plotted using a blue color scale, while variants with incongruous effects will be plotted using a red color scale (as seen in Figure 4A).The size of each triangle corresponds to the eQTL normalized effect size (NES) for each variant, while the directionality of each triangle is set to correspond to the direction of effect for the variant on the GWAS trait. 

A depiction of the genomic positions of all genes within the LOI is generated below the plot using the package Gviz (Figures 1B, 2B, 3B, 4B). If LD data is supplied, in the form of `LD.df`, a third panel illustrating the LD landscape of eQTL variants within the LOI is generated using the package LDheatmap (Figure 3C, 4C). To generate this panel, `LD.df` is filtered to contain only eQTL variants that appear in the plotted LOI, and to include only variant pairs that are in LD with each other with R<sup>2</sup> > `R2min` (default value of 0.1). This dataset is further filtered to include only variants that are in LD (with R<sup>2</sup> > `R2min`) with at least a certain number of other variants (user-defined with the argument `LDmin`, default value of 10). These filtering steps are useful in paring down the number of variants to be plotted in the LDheatmap, keeping the most informative variants and reducing the time needed to generate the eQTpLot. A heatmap illustrating the pairwise linkage disequilibrium of the final filtered variant set is subsequently generated below the main eQTL-GWAS Colocalization Plot, with a fill scale corresponding to R<sup>2</sup> for each variant pair. The location of each variant in chromosomal space is indicated at the top of the heatmap, using the same chromosomal coordinates as displayed in panels A and B.  

#### Generation of the eQTL Enrichment Plot
For variants within the LOI with P<sub>GWAS</sub> less than the specified GWAS significance threshold, `sigpvalue_GWAS`, the proportion that are also eQTLs for the gene of interest (with P<sub>eQTL</sub> < `sigpvalue_eQTL`) are calculated and plotted, and the same is done for variants withP<sub>GWAS</sub> > `sigpvalue_GWAS`, (Figure 1C, 2C, 3D, 4D). Enrichment of candidate gene eQTLs among GWAS-significant variants is determined by Fisher’s exact test. If an analysis differentiating between congruous and incongruous variants is specified, these are considered separately in the analysis (as seen in figure 4D).

#### Generation of P-P Correlation Plots
To visualize correlation between P<sub>GWAS</sub> and P<sub>eQTL</sub>, each variant within the LOI is plotted withP<sub>eQTL</sub> along the horizontal axis, and P<sub>GWAS</sub> along the vertical axis. Correlation between the two probabilities is visualized by plotting a best-fit linear regression over the points. The Pearson correlation coefficient and p-value of correlation are computed and displayed on the plot as well (Figure 1D, 2D). If an analysis differentiating between congruous and incongruous variants is specified, separate plots are made for each set of variants and superimposed over each other as a single plot, with linear regression lines/Pearson coefficients displayed for both sets.

If LD data is supplied in the form of `LD.df`, a similar plot is generated, but the fill color of each point is set to correspond to the LD R<sup>2</sup> value for each variant with a specified lead variant, plotted as a green diamond (Figure 3E). This lead variant can be user-specified with the argument `leadSNP` or is otherwise automatically defined as the upper-right-most variant in the P-P plot. This same lead variant is also labelled in the main eQTpLot panel A (Figure 3A). In the case where LD data is provided and an analysis differentiating between congruous and incongruous variants is specified, two separate plots are generated: one for congruous and one for incongruous variants (Figure 4E-F). In each plot, the fill color of each point is set to correspond to the LD R<sup>2</sup> value for each variant with the lead variant for that specific plot (again defined as the upper-right most variant of the P-P plot), with both the congruous and incongruous lead variants labelled in the main eQTpLot panel A (Figure 4A).

<p>&nbsp;</p>
<p>&nbsp;</p>

## Use Examples

### Example 1 – comparing eQTpLots for two genes within a linkage peak
In this example, a GWAS study of LDL cholesterol levels has identified a significant association with a genomic locus at chr11:66,196,265-66,338,300 (build hg19), which contains a number of plausible candidate genes, including the genes *BBS1* and *ACTN3*. 

Using the `GeneList` function of eQTpLot, the user supplies both the *BBS1* and *ACTN3* genes to eQTpLot, along with all required input data, to obtain a crude estimation of which gene’s eQTL data most closely correlates with the GWAS signal observed at this locus. 

Calling eQTpLot as follows generates Pearson correlation statistics between P<sub>GWAS</sub> and P<sub>eQTL </sub> for both genes and the LDL trait, using a PanTissue approach and collapsing by method “min” as described above.

```
> eQTpLot(GWAS.df = GWAS.df.example, eQTL.df = eQTL.df.example, gene = c("BBS1", "ACTN3"), 
          gbuild = "hg19",  trait = "LDL", tissue =  "all", CollapseMethod = "min", 
          GeneList = T)       
[1] "Checking input data..."
[1] "PHE column found in GWAS.df. Analyzing data for phenotype LDL"
[1] "PanTissue eQTL analysis, collapsing by method  min  will be completed across all tissues in eQTL.df"
[1] "For genes:"
[1] "'BBS1', 'ACTN3'"
[1] "eQTL analysis for gene BBS1: Pearson correlation: 0.823, p-value: 1.62e-127"
[2] "eQTL analysis for gene ACTN3: Pearson correlation: 0.245, p-value: 1.52e-07"
[1] "Complete"

```


Demonstrating that there is significantly stronger correlation between the GWAS signal at this locus and eQTLs for the gene *BBS1*, compared to the gene *ACTN3*. To visualize these differences, starting with the gene *BBS1*, eQTpLot can be called as follows:

 ```
 eQTpLot(GWAS.df = GWAS.df.example, eQTL.df = eQTL.df.example, gene = "BBS1", 
         gbuild = "hg19",  trait = "LDL", tissue =  "all", CollapseMethod = "min")
```

This command will analyze the GWAS data in `GWAS.df.example` within a default 200kb range surrounding the *BBS1* gene, using the preloaded `Genes.df` to define the genomic boundaries of *BBS1* based on genome build hg19. eQTL data from `eQTL.df.example` will be filtered to contain only data pertaining to *BBS1*. Since `tissue` is set to “all”, eQTpLot will perform a PanTissue analysis, as described above. 

This generates the following plot:

#### Figure 1
![](man/figures/Figure1.jpeg)<!-- -->

Figure 1 illustrates clear evidence of colocalization between the LDL-significant locus and *BBS1* eQTLs. In Figure 1A, it is easy to see that all variants significantly associated with LDL cholesterol (those plotted above the horizontal red line) are also very significantly associated with *BBS1* expression levels, as indicated by their coloration in bright orange. Figure 1C shows that there is a significant enrichment (p = 9.5e-46 by Fisher’s exact test) for *BBS1* eQTLs among GWAS-significant variants (as shown on the plot). Lastly, Figure 1D illustrates strong evidence for correlation between P<sub>GWAS</sub> and P<sub>eQTL</sub> for the analyzed variants, with a Pearson correlation coefficient of 0.823 and a p-value of correlation of 1.62e-127 (as displayed on the plot). Taken together, this analysis provides strong evidence for colocalization between variants associated with LDL cholesterol levels, and variants associated with *BBS1* expression levels. 

To investigate the possibility that the LDL association signal might also be acting through modulation of the expression of other genes at this locus, the same analysis can be performed, substituting the gene *ACTN3* for the gene *BBS1*, as in the following command:

```
eQTpLot(GWAS.df = GWAS.df.example, eQTL.df = eQTL.df.example, gene = "ACTN3", 
        gbuild = "hg19",  trait = "LDL", tissue =  "all", CollapseMethod = "min")
```

This generates the following plot:

#### Figure 2
![](man/figures/Figure2.jpeg)<!-- -->

Unlike the previous example for *BBS1*, Figure 2 shows very poor evidence for colocalization between *ACTN3* eQTLs and LDL cholesterol-significant variants. Although there is significant enrichment for *ACTN3* eQTLs among GWAS-significant variants (Figure 2B), there is poor evidence for correlation between P<sub>GWAS</sub> and P<sub>eQTL</sub> (Figure 2D), and it is intuitively clear in Figure 2A that the eQTL and GWAS signals do not colocalize (the brightest colored points, with the strongest association with *ACTN3* expression, are not among the variants most significantly associated with LDL cholesterol levels).

<p>&nbsp;</p>

### Example 2 –The `TissueList` function and adding LD information to eQTpLot
The plots generated in Example 1 illustrated colocalization between *BBS1* eQTLs and the GWAS peak for LDL cholesterol on chromosome 11, using a PanTissue analysis approach. The user may next wish to investigate if there are specific tissues in which *BBS1* expression is most clearly correlated with the LDL GWAS peak. Using the `TissueList` function of eQTpLot, we can se the Pearson correlation statistics between P<sub>GWAS</sub> and P<sub>eQTL</sub> for *BBS1* and the LDL trait across each tissue contained within `eQTL.df` ranked by degree of correlation:

```
> eQTpLot(GWAS.df = GWAS.df.example, eQTL.df = eQTL.df.example, gene ="BBS1", 
        gbuild = "hg19",  trait = "LDL", tissue =  "all", TissueList = T)
[1] "For gene:"
[1] "BBS1"
[1] "eQTL analysis for tissue Cells_Cultured_fibroblasts: Pearson correlation: 0.902, p-value: 1.12e-65"           
[2] "eQTL analysis for tissue Whole_Blood: Pearson correlation: 0.85, p-value: 1.64e-55"                           
[3] "eQTL analysis for tissue Brain_Frontal_Cortex_BA9: Pearson correlation: 0.84, p-value: 1.02e-51"              
[4] "eQTL analysis for tissue Brain_Nucleus_accumbens_basal_ganglia: Pearson correlation: 0.841, p-value: 1.74e-48"
[5] "eQTL analysis for tissue Brain_Cortex: Pearson correlation: 0.818, p-value: 2.44e-43"                         
# Truncated #                    
[48] "eQTL analysis for tissue Nerve_Tibial: Pearson correlation: -0.007, p-value: 9.56e-01"                        
[1] "Complete"
```
    
This output demonstrates a strong correlation between LDL cholesterol levels and *BBS1* expression levels in a number of tissues. To further explore these associations, the user can specifically run eQTpLot on data from a single tissue, for example "Whole_Blood", while also supplying LD data to eQTpLot using the argument `LD.df`:

```
eQTpLot(GWAS.df = GWAS.df.example, eQTL.df = eQTL.df.example, gene = "BBS1", 
        gbuild = "hg19", trait = "LDL", tissue =  "Whole_Blood", 
        LD.df =LD.df.example, R2min = 0.25, LDmin = 100)
```

Here the argument `LD.df` refers to a data frame containing a list of pairwise LD correlation measurements between all the variants within the LOI, as one might obtain from a PLINK linkage disequilibrium analysis using the --r2 option. `R2min=0.25` such that `LD.df` is filtered to drop variant LD pairs with R<sup>2</sup> < 0.25, and `LDmin=100`, such that only variants in LD with >= 100 other variants will be plotted in the LD heatmap. 

This generates the following plot:

#### Figure 3
![](man/figures/Figure3.jpeg)<!-- -->

Figure 3 is different than Figure 1 (the same eQTpLot analysis carried out without LD information supplied) in two important ways. First, a heat map of the LD landscape for all *BBS1* eQTL variants in the tissue "Whole_Blood" within the LOI is shown in Figure 3C; this heatmap makes it clear that a number of GWAS-significant variants are in strong LD with each other. Second, the P-P plot, Figure 3E, now includes LD information for all plotted variants; a lead variant, rs3741360, has been defined (by default the upper-right most variant on the P-P plot), and all other variants are plotted with a color scale corresponding to their squared coefficient of linkage correlation with rs3741360. rs3741360 is also labeled in Figure 3A for reference. Although colocalization of the BBS1 eQTL and LDL GWAS signal spans the entire association peak, most but not all of the GWAS-significant variants are in strong LD with each other. This implies that there are at least two distinct LD blocks at the *BBS1* locus with strong evidence of colocalization between the *BBS1* eQTL and LDL GWAS signals.

<p>&nbsp;</p>

### Example 3 – Separating Congruous from Incongruous Variants
In addition to including LD data in our eQTpLot analysis, we can also include information on the directions of effect of each variant, with respect to the GWAS trait and *BBS1* expression levels. This is accomplished by setting `congruence=TRUE`:

```
eQTpLot(GWAS.df = GWAS.df.example, eQTL.df = eQTL.df.example, gene = "BBS1", 
        gbuild = "hg19",  trait = "LDL", tissue =  "Whole_Blood", LD.df = LD.df.example, 
        R2min = 0.25, LDmin = 100, congruence = TRUE)
```

This generates the following plot:

#### Figure 4
![](man/figures/Figure4.jpeg)<!-- -->

Figure 4 divides all *BBS1* eQTL variants in "Whole_Blood" into two groups: congruent – those associated with either an increase in both *BBS1* expression levels and LDL levels, or a decrease in both – and incongruent – those with opposite directions of effect on *BBS1* expression levels and LDL levels. In carrying out such an analysis, it becomes clear that it is specifically variants with congruent directions of effect on *BBS1* levels and LDL cholesterol levels that are driving the signal colocalization; that is, variants associated with decreases in *BBS1* expression strongly colocalize with variants associated with decreases in LDL cholesterol.

<p>&nbsp;</p>

Multiple additional modifications to the plots can be specified, as noted above.
