# dna-sequence-checker

Check whether a target DNA sequence (e.g. a lentiviral / plasmid construct) is
present in a bzip2-compressed FASTQ file, using a **k-mer** strategy fed by a
**parallel bzip2 decompressor**.

## How it works

The target is thousands of bp long while Illumina reads are ~150 bp, so no single
read spans the whole construct. `check_sequence.py`:

1. Chops the target into overlapping **k-mers** (`K = 31`) and reduces each to its
   **canonical** form (the lexicographically smaller of the k-mer and its reverse
   complement), so a read from either strand matches the same key.
2. Streams reads by piping the `.fastq.bz2` through a **parallel decompressor** —
   it auto-selects `lbzip2 -dc -n 12`, then `pbzip2 -dc`, then `bzcat`. 
3. Reads only the sequence line of each FASTQ record and slides a k-window across
   it, recording which target k-mers were observed.
4. **Stops early** as soon as every target k-mer has been found.

### Reported metrics

- **k-mer coverage** — how many of the target's unique k-mers were observed
  (`found / total`, as a percentage). 
- **Longest contiguous covered region** — the longest run of consecutive target
  positions whose k-mers were all seen, expressed in bp (`run + K - 1`). 

### Outcomes

| k-mer coverage | Verdict             |
| --- |---------------------|
| ≥ 95% | PRESENT             |
| ≥ 50% | PARTIALLY present   |
| > 5%  | Weak/partial signal |
| ≤ 5%  | NOT present         |

## Usage

```bash
# Pass the FASTQ.bz2 path explicitly:
python3 check_sequence.py /path/to/S_1_EKDL230002110-1A_HNVTNDSX5_L4_1.fastq.bz2

# Or run with no argument to use the built-in DEFAULT_FASTQ_BZ2 path:
python3 check_sequence.py
```

## Configuration

Settings are edited directly at the top of `check_sequence.py`:

| Constant | Default | Meaning |
| --- | --- | --- |
| `DEFAULT_FASTQ_BZ2` | `~/Downloads/S_1_...fastq.bz2` | file used when no CLI arg is passed |
| `K` | 31 | k-mer length |
| `TARGET` | built-in construct | the sequence to search for |

The number of decompression threads is set in the `lbzip2` command (`-n 12`) —
adjust it to match your CPU.

## Requirements

- For best speed, install a parallel bzip2 decompressor:

  ```bash
  brew install lbzip2      # or: brew install pbzip2
  ```

  If neither is available the script falls back to the standard `bzcat`.

## Example output

```
Decompressor: lbzip2
Target length: 4368 bp
Unique target 31-mers to find: 4319
Streaming reads from: /path/to/reads.fastq.bz2

     4,000,000 reads | coverage 4319/4319 (100.0%) | ... | ...k reads/s

All target k-mers found — stopping early.

===================== RESULT =====================
Reads scanned:        4,000,000
Time:                 ...s
Target k-mers found:  4319/4319 (100.0%)
Longest contiguous covered region: ~4368 bp
Verdict: PRESENT — the sequence is well represented in the reads.
==================================================
```
