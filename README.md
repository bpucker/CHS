# Manual inspection of _CHS_ gene models

This repository contains scripts that were developed for the investigation of suspicious _CHS_ gene models. Multiple copies of the CHS domain within the same protein were suggested by the database entries. In addition to the scripts, detailed instructions are shared how to investigate gene models.


## How to analyze suspicious gene models that might be an annotation artifact?

1) Identification homologs in many closely related species: BLAST is an efficient tool for the identification of sequences with similarity that indicates homology. [collect_best_BLAST_hits.py](https://github.com/bpucker/ApiaceaeFNS1) is a Python3 script that can be used to collect the best BLAST hits for a given FASTA file with sequences. This script requires a local installation of [BLAST](https://blast.ncbi.nlm.nih.gov/Blast.cgi?CMD=Web&PAGE_TYPE=BlastDocs&DOC_TYPE=Download). [DIAMOND](https://github.com/bbuchfink/diamond) is an alternative to BLAST that delivers the same output, but runs much faster at the expense of a substantially increased memory consumption. It is also possible to perform this analysis online on the NCBI [BLAST website](https://blast.ncbi.nlm.nih.gov/Blast.cgi). All hits should be downloaded as FASTA file.
2) Global alignment of all collected sequences: [MAFFT](https://mafft.cbrc.jp/alignment/software/), [MUSCLE](https://www.drive5.com/muscle/), or [CLUSTAL](http://www.clustal.org/clustal2/) can be used to align all collected sequences. The alignment tools are available for local analysis and on the EBI website. An inspection of the alignment can already help to identify likely artifacts. If the sequence in question is not supported by any other sequence, it is likely an artifact. The other explanaition would be striking biological event during evolution.
3) Retrieving RNA-seq datasets: The [Sequence Read Archive (SRA)](https://www.ncbi.nlm.nih.gov/sra) offers a huge amount of RNA-seq datasets that can be retrieved via [fastq-dump](https://github.com/ncbi/sra-tools) (part of the SRA toolkit). The installation of fastq-dump requires a proper configuration of temporary and output folders. [This instruction](https://akiomiyao.github.io/ped/sratoolkit/index.html) worked well in our hands.
4) RNA-seq read mapping: Proper split read aligners are important for the correct placement of RNA-seq reads across exon-intron borders. [STAR](https://github.com/alexdobin/STAR) or [HISAT2](http://daehwankimlab.github.io/hisat2/) are recommended for this task. Please see the respective documentations for details.
5) Extraction of region of interest: [Samtools](http://www.htslib.org/) allows the extraction of a certain region of interest from a read mapping (BAM file): ``` samtools view input.bam "ChrX:13-37" > output.bam ```.
6) Inspection of RNA-seq read mapping: [Integrative Genomics Viewer (IGV)])(https://software.broadinstitute.org/software/igv/) is a freely available tool that allows inspection of read mappings. Please see the respetive documentation for additional details.
7) Conversion of BAM into COV file: [construct_RNA_seq_coverage_file.py](https://github.com/bpucker/ncss2018/blob/master/construct_RNA_seq_coverage_file.py) is a python3 script that converts a BAM file into a COV file. This coverage file is a table listing the number of reads that map to each position in the reference. It is possible to generate a coverage file based on the original BAM file or based on an extracted region.
8) Visualization of RNA-seq coverage: The coverage_plotter.py (see below) can generate a figure based on the given coverage file. It is also possible to supply a GFF3 file to display the positions of annoated exons below the coverage plot. See the description below for details.




## BAM collection

```
Usage:
  python3 collect_bams.py --in <DIR> --out <DIR>
  
  --in   STR   BAM input folder
  --out  STR   BAM output file
```

`--in` specifies a BAM file containing folder.

`--out` specifies a BAM file output folder.


## Genomic region selection from BAM

```
Usage:
  python3 extract_bam_region.py --in <FILE> --out <FILE> --seq <STR> --start <INT> --end <INT>
  
  --in      STR   BAM input folder
  --out     STR   BAM output file
  --seq     STR   Sequence name
  --start   INT   Region start
  --end     INT   Region end
```

`--in` specifies a BAM file containing folder.

`--out` specifies a BAM file output folder.

`--seq` specifies the name of the sequence (chromosome) of interest.

`--start` specifies a start position of the genomic region.

`--end` specifies an end position of the genomic region.


## Coverage plotting
```
Usage:
  python3 coverage_plotter.py --cov <FILE> --out <DIR> --seq <STR> --start <INT> --end <INT>
  
  --cov     STR   Coverage input file
  --out     STR   Output folder
  --seq     STR   Sequence name
  --start   INT   Region start
  --end     INT   Region end
```

`--in` specifies a coverage file resulting from an RNA-seq read mapping.

`--out` specifies an output folder.

`--seq` specifies a sequence of interest (e.g. contig/scaffold/pseudochromosome).

`--start` specifies a start position on the sequence of interest.

`--end` specifies an end position on the sequence of interest.





## References

This repository.


