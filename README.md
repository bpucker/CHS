# Manual inspection of CHS gene models

This repository contains scripts that were developed for the investigation of suspicious _CHS_ gene models. Multiple copies of the CHS domain within the same protein were suggested by the database entries. In addition to the scripts, detailed instructions are shared how to investigate gene models.


## How to analyze suspicious gene models that might be an annotation artifact?

1) Identification homologs in many closely related species: BLAST is an efficient tool for the identification of sequences with similarity that indicates homology. [collect_best_BLAST_hits.py](https://github.com/bpucker/ApiaceaeFNS1) is a Python script that can be used to collect the best BLAST hits for a given FASTA file with sequences. This script requires a local installation of [BLAST](https://blast.ncbi.nlm.nih.gov/Blast.cgi?CMD=Web&PAGE_TYPE=BlastDocs&DOC_TYPE=Download). [DIAMOND](https://github.com/bbuchfink/diamond) is an alternative to BLAST that delivers the same output, but runs much faster at the expense of a substantially increased memory consumption.
2) 





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




