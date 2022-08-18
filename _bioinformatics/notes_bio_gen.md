[>>>BACK TO HOME PAGE<<<](https://liu-xnd.github.io)

Notes of Bioinfo & Genomics

# Chapter 1: Introduction

## Learning objectives:
- 定义术语 bioinformatics;
- explain the scope of bioinformatics;
- explain why 珠蛋白/球蛋白/血红蛋白 globins are a useful example to illustrate this discipline;
- describe web-based versus command-line approaches to bioinformatics.

---

**Bioinformatics** represents a new field at the interface of the ongoing revolutions in **molecular biology** and **computers**.

## Definition of Bioinformatics

>利用电脑数据库和算法来分析蛋白质, 基因和全套构成基因组有机体的DNA.

*Russ Altman (1998) and Altman and Dugan (2003)* offer 2 definitions of bioinformatics.

- The 1st involves **information flow** following the central dogma of molecular biology 
```
DNA->RNA->蛋白质->细胞表现型(phenotype).
```
Central dogma of genomics:
```
基因组(genome)->转录组(transcriptome)->蛋白质组(proteome)->细胞表现型(cellular phenotype).
```

- The 2nd definition involves information flow that is transferred based on scientific methods. This second definition includes problems such as designing, validating, and sharing software; storing and sharing data; performing reproducible research workflows; and interpreting experiments.

**The goal of genomics** is 确定和分析有机体(基因组)的整套DNA序列. The DNA encodes genes can be expressed as ribonucleic acid (RNA) transcripts and then, in many cases, further translated into protein. **Functional genomics** describes the use of genome‐wide assays to study **gene and protein function**.

## Bioinformatics: The big picture

生信和基因组学的三个角度.

1. 细胞 Cell (Central dogma);

**The essential nature of bioinformatics**: biological questions can be approached from levels ranging from **single genes and proteins** to **cellular pathways and networks** or even **whole‐genomic responses**. Our goals are to understand how to study both individual genes and proteins and collections of thousands of genes/proteins.

2. 器官 Organisms;

Each organism changes across different stages of development and across different regions of the body.

3. 生命树 The tree of life.

## Bioinformatic software

### Web-based

We will focus on the main publicly accessible databases that serve as **repositories for DNA and protein data**. These include:

1. the National Center for Biotechnology Information (**NCBI**), which hosts GenBank and other resources; 
2. the European Bioinformatics Institute (EBI); 
3. **Ensembl**, which includes a genome browser and resources to study dozens of genomes; and 
4. the University of California at Santa Cruz (UCSC) Genome bioinformatics site, including a web browser and table browser for a variety of species.

### Command-line software

1. Linux OS.
2. Programming languages: Perl, Python, R.
3. Bash.

---
### Reproducible Research in Bioinformatics

Our work must be cumulative, progressive.

- A workflow should be well documented.
- Well organize files.
- Data should be available to others.
- Metadata.
- Databases should be documented.
- Software should be documented.

---
Review: Learning Objectives
- 定义术语生物信息学;
- 解释生信学的尺度;
- explain why globins are a useful example to illustrate this discipline;
- describe web-based versus command-line approaches to bioinformatics.

# Chapter 2: Access to Sequence Data and Related Information.

## Learning objectives
- define the types of molecular databases;
- define **授权数 accession numbers** and the significance of **参照列-索引 RefSeq identifiers**;
- describe the main genome browsers and use them to study features of a genomic region; and 
- use resources to study information about both individual genes (or proteins) and large sets of genes/proteins.

## Access to Information: Accession numbers to label and Identify sequences

用授权数来标记和索引序列.

The problem we will address now is how to extract information about your gene or protein of interest from databases.

An essential feature of DNA  and protein sequence records is that they are tagged with accession numbers. **An accession number** is a string of about 4–12 numbers and/ or alphabetic characters that are associated with a molecular sequence record (some are much longer).

Different resources have different formats.

When we compare beta globin sequence derived from mRNA and from genomic DNA we may expect them to match perfectly (or nearly so) but, as we will see, there are often discrepancies (Chapter 10).

### The Reference Sequence (RefSeq) Project

The goal is to provide the best representative sequence for each normal transcript produced by a gene and for each normal protein product.

RefSeq entries have **不同的状态等级 different status levels** (predicted, provisional, and reviewed), but in each case the RefSeq entry is intended to unify the sequence records. You can recognize a RefSeq accession by its format, such as NP_000509 (P stands for beta globin protein) or NM_006744 (for beta globin mRNA). The corresponding **X** P_12345 and **X** M_12345 formats imply that the sequences **are not based on experimental evidence**.

## 在NCBI通过基因资源获取信息

数据库的新型特点是愈发互相连接, 提供一系列DNA, RNA, 蛋白质的其他网站和算法的链接. NCBI的基因资源(原称Entrez Gene, 更早称LocusLink)作为主要传送门尤其有用.

>Genetic Loci/Locus, 基因座/基因位点, 是基因在染色体上的位置.

Entrez Gene是人为的数据库, 为各基因座提供详细说明信息.

>NCBI: [National Center for Biotechnology Information](https://www.ncbi.nlm.nih.gov/)

## 在NCBI通过命令行 Command-Line 获取数据

许多生信软件包为了命令行使用而设计.

(推荐Linux系统) Linux有许多优点, 特别是为了操作生信数据集和软件程序.

- 免费,
- 被广泛发展, 可提供类似Windows/Mac OS 的熟悉环境,
- 可定制, 灵活,
- 可处理大型数据集,
- MS Excel 限制行数, 自动改变行名和数字. Unix中的表格只被磁盘空间限制.

>你可以在Microsoft Windows上通过Secure Shell (SSH) client, 例如PuTTY, 来得到一个Linux机器.
>PuTTY是开源免费的终端仿真器(terminal emulator).

*这里我自己配置了WSL2:Kali:Kex环境.*

>安装EDirect:
>perl -MNet::FTP -e \ '$ftp = new Net::FTP("ftp.ncbi.nlm.nih.gov", Passive => 1); $ftp->login; $ftp->binary; $ftp->get("/entrez/entrezdirect/edirect.zip");'

### 例子1
搜索PubMed文章, 作者J. Pevsner, 包含术语GNAQ, 将结果保存为summary形式, 发送到屏幕, 然后保存到文件`example1.out`中.

## 获取信息: Genome Browsers 基因组浏览器

### Genome Builds 基因组框架
使用UCSC, Ensembl, 或者其他基因组浏览器, 对任何研究的器官(有机体)都有对应的基因组框架Genome Build. 一个基因组框架是一个集合, 其中有DNA序列, 按在染色体上的顺序排列.

一个build包括注释, 例如基因的起点, 终点, 外显子, 重复DNA元素, 和其它特征.

# ⋇ Chapter 3: Pairwise Sequence Alignment 成对序列比对

>一个被接受的蛋白质点突变是一个氨基酸被其他氨基酸代替, 被自然选择接受. 为了被接受, 新的氨基酸通常有与旧的相似的功能: 对于两个频繁互相变化的氨基酸, 化学上, 物理上的相似性可以被发现.    --Margaret Dayhoff

## Learning objectives

- 定义homology **同源** (orthologs **直系同源**, paralogs **旁系同源**);
- 解释PAM (accepted point mutation 接受的点突变) 矩阵怎么来的;
- 对比PAM, BLOSUM 得分矩阵;
- 定义dynamic programming (动态规划) and 解释 global and local pairwise alignments are performed;
- perform pairwise alignment of protein or DNA sequences at the NCBI website.

## Introduction

关于基因/蛋白质的一个基础的问题是它是否与其他基因/蛋白质有关. 序列层级上的相关性表明了它们是**同源的 homologous**, 它们可能有共同功能. 通过分析DNA/蛋白质序列, 可能找到被一组分子共享的motifs or domains.

>**Motif** 是一种在某个组中被所有成员共享的模式, 我姑且翻译为**公式/模式**, 但大多数情况下还是不翻译.
>**Domain** 是**蛋白质结构域**, 是蛋白质中不同的功能/结构单位. Domains 可能在不同的生物学语境中存在, 相似的domains可能有不同的官能.

随着许多有机体的基因组测序的完成, 找出蛋白质如何内部和有机体间**相互联系**的任务对于理解生命来说变得愈发根本.

### Protein alignment: 通常比DNA alignment更有信息量.

Given the choice of aligning a DNA sequence or the sequence of the protein it encodes, it is often more informative to compare protein sequence.

- 某些基因突变不改变蛋白质合成.
- Protein alignment 能确定同源序列, 而DNA alignment 不能. *(Pearson, 1996)*

### 定义: Homology, Similarity, Identity.

两个序列是同源的, 若它们有共同的进化祖先.

Homology没有程度, 只有是或不是. Similarity, identity 有程度; 同源的序列未必有统计学显著的相似性/相同性. In general, three‐dimensional **structures** diverge much more **slowly** than **amino acid sequence** identity between two proteins (Chothia and Lesk, 1986).

- Orthologs: Share same ancestry; (Ortho- = exact)
- Paralogs: Arose by Gene duplication. (Para- = in parallel)

Two DNA (or protein) sequences are **defined as homologous** based on achieving **significant alignment scores**.

Conduct Pairwise Alignment (through BLASTP, (for BLAST Protein)):
1. choose the program BLASTP, check "Align two or more sequences";
2. Enter the seq or their accession numbers. Here we use the seq of human beta globin in the FASTA format, and for myoglobin we use the accession number.
3. Select optional parameters;
4. Click "align".


*local* pairwise alignment: only a subset of the two proteins is aligned. Otherwise is called *global*.

这个pairwise alignment 的另一个方面是, 有些比对残留(residues)相似(similar)但不相同(identical). 这些是**conservative substitutions** (保守替代). 

>If the amount of sequence identity is sufficient, then the two sequences are probably homologous. It is never correct to say that two proteins share a certain percent homology, because they are either homologous or not.

Ultimately, the strongest evidence to determine whether two proteins are homologous comes from structural studies in combination with evolutionary analyses.

### Gaps

P-A 对于确认进化中的突变十分有用. 最常见的突变有: *substitutions*, *insertions*, and *deletions*. (替代, 插入, 删除) 插入和删除在比对中被称为沟(**gaps**).

在经典的得分算法中有两种沟的惩罚, 称为仿射沟损失 (**affine gap costs**). One is a score $−a$ for creating a gap. A second penalty is $–b$ for each residue that a gap extends. *If a gap extends for k residues it is assigned a penalty of −(a + bk). For a gap of length 1, the score is −(a + b).*

### Pairwise alignment, Homology, and Evolution of Life.

>Human, horse, chicken: Share homologous myoglobins.

The study of homologous protein seqs by pairwise alignment involves an investigation of the evolutionary history of that protein.

(一种研究方法是化石法.)

## Scoring Matrices

*Margaret Dayhoff (1966, 1978).*

### Dayhoff Model step 1/7: Accepted Point Mutations (PAM)

>Their approach was to catalog hundreds of proteins and compare the sequences of closely related proteins in many families. They considered the question of which specific amino acid substitutions are observed to occur when two homologous protein sequences are aligned.
>他们对几百个蛋白质分类, 比较许多家族中紧密相关的蛋白质序列. 他们考虑这个问题: 哪些substitutions可以被观察到, 当两个同源蛋白质序列比对时.

他们定义accepted point mutation (**PAM**)作为**自然选择接受的**氨基酸替代.

一个**被自然选择接受的氨基酸替代**发生在: (1) 基因突变从而编码**不同氨基酸**; 以及(2) 整个物种接受了那个变化作为**主流蛋白质形式**.

>例如, conservative replacements such as serine for threonine would be most readily accepted.

统计可得PAM矩阵, 元素(i,j)指示i,j间的PAM频率.

### Dayhoff Model step 2/7: Frequency of Amino Acids.

>To model the prob that aligned amino acid in a protein changes to another, we need to know the freqs of occurrence of each amino acid.

### Dayhoff Model step 3/7: Relative Mutability of Amino Acids. (相对突变性)

Dayhoff计算了氨基酸的相对突变性. (设某个氨基酸, 如Ala, 的相对突变性为100.) 氨基酸的**相对突变性**是说在**较短**的时间内 (因为考虑的蛋白质之间紧密联系, 易转化) 每个氨基酸**改变的可能性**. (类似于化学"*活化能*"). 计算方式: 氨基酸$i$突变的频数/总频数$f_i$.

>Why are some amino acids more mutable than others? 进化的角度看: The less mutable residues probably have important structural or functional roles in proteins, such that the consequence of replacing them with any other residue could be harmful to the organism.

>基因/结构的角度看: The substitutions that occur in proteins can also be understood with reference to the genetic code. (It can be seen that) common amino acid substitutions tend to require only a single‐nucleotide change. (但是有些结构上编码易突变不稳定的氨基酸, 实际相对突变性弱, 这是不被自然选择容忍所导致的.)

### Dayhoff Model step 4/7: Mutation Probability Matrix for the Evolutionary Distance of 1 PAM. (1PAM进化距离的突变概率矩阵)

Dayhoff 生成了**Mutation prob matrix** $M$ (PAM1-matrix). 元素$M_{ij}$ 表示在一个给定的*进化区间*内, 氨基酸j被i替代的概率. In the case of Figure 3.9 the interval is **one PAM**, which is defined as the unit of evolutionary divergence in which **1% of the amino acids have been changed** between the two protein sequences. (即, 1PAM进化距离=1%氨基酸改变的时间/"进化距离". 注意这里单位是氨基酸改变(amino acid divergence)的百分率, 不是"年".)

### Dayhoff Model step 5/7: PAM250 and other PAM Matrices

PAM1阵是基于紧密联系的蛋白质序列, 有平均1%的变化. 为了确保多对比对是合法的, 一个家族内的蛋白质至少有85%相同性(identical). 我们通常对探索远小于99%氨基酸相同性的蛋白质感兴趣. PAM100, PAM250被产生来研究遥远联系(几乎不联系)的蛋白质.

PAM250不是在100长度的序列中发生250次突变, 而是PAM1自身矩阵相乘250次 (PAM1也不一定只发生一次突变. 可以近似认为1PAM是一种时间单位, 但对不同的蛋白质序列它对应不同的时间). 试想PAM$\infty$, (从而氨基酸在某有限时间内100%转变为任何特定氨基酸, 从而任意两个氨基酸在无限长时间内转变为给定氨基酸的概率相同.) 则被转变概率即为各氨基酸的总体背景概率. 

对于PAM250,

$$
\text{PAM250} = \text{PAM1} ^ {250}.
$$

这是用于BLAST数据库搜索的其中一个最常见的矩阵. 这个矩阵实际上对应一个20%氨基酸相同性进化距离, 因此一般应用在有20%相同性的序列之间.

(我自注: 实际应用时, 研究两个序列A,B是否同源 (已知二者有20%identity), 先比对A和A', 其中A'是A的1PAM演化结果, 得到PAM1(A), 然后研究A,B的PAM250(AB), 然后比对PAM1(A)自乘250次是否近似等于PAM250(AB), 这样来推断A,B的同源性.)

### Dayhoff Model step 6/7: 从突变概率矩阵到相关性可能性矩阵 (Relatedness Odds Matrix)

$$
R_{ij} = \frac{M_{ij}}{f_i};
$$

其中$M_{ij}$是j变为i的概率, $f_i$是i出现的自然概率/背景概率. 这个比值作为元素构成ROM.

$R_{ij}=1$意味着j to i的替换突变几乎和by chance一样可以被预期(A'=B). 大于1意味着j to i氨基酸突变比总体by chance更频繁. (直观理解为: A演化到A', 对于给定位点A(j), B中对应位点生成i的频率小于A中j到i的突变.) 小于1意味着B中的i主要是环境生成的而不是A的j突变而来的.

>Prob of an authentic alignment = $\frac{P(aligned|authentic)}{P(aligned|random)}$.

### Dayhoff Model step 7/7: Log-Odds scoring matrix

$$s_{ij}=10\times log_{10}(\frac{M_{ij}}{f_i})$$
