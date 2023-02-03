# CHS
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
  python3 extract_bam_region.py --in <DIR> --out <DIR> --seq <STR> --start <INT> --end <INT>
  
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


## References




