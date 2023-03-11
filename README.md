# Manual inspection of CHS gene models
CHS gene structure prediction analysis

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




