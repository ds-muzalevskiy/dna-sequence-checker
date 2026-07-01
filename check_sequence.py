#!/usr/bin/env python3
import shutil
import subprocess
import sys
import time

DEFAULT_FASTQ_BZ2 = "/Users/muzalevs/Downloads/S_1_EKDL230002110-1A_HNVTNDSX5_L4_1.fastq.bz2"
FASTQ_BZ2 = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_FASTQ_BZ2
K = 31

if shutil.which("lbzip2"):
    DECOMP_CMD = ["lbzip2", "-dc", "-n", "12", FASTQ_BZ2]
elif shutil.which("pbzip2"):
    DECOMP_CMD = ["pbzip2", "-dc", FASTQ_BZ2]
else:
    DECOMP_CMD = ["bzcat", FASTQ_BZ2]

TARGET = (
    "ctggaagggctaattcactcccaacgaagacaagatatccttgatctgtggatctaccacacacaaggctacttccctgattggcagaactacacaccagggccagggatcagatatccactgacctttggatggtgctacaagctagtaccagttgagcaagagaaggtagaagaagccaatgaaggagagaacacccgcttgttacaccctgtgagcctgcatgggatggatgacccggagagagaagtattagagtggaggtttgacagccgcctagcatttcatcacatggcccgagagctgcatccggactgtactgggtctctctggttagaccagatctgagcctgggagctctctggctaactagggaacccactgcttaagcctcaataaagcttgccttgagtgcttcaagtagtgtgtgcccgtctgttgtgtgactctggtaactagagatccctcagacccttttagtcagtgtggaaaatctctagcagtggcgcccgaacagggacttgaaagcgaaagggaaaccagaggagctctctcgacgcaggactcggcttgctgaagcgcgcacggcaagaggcgaggggcggcgactggtgagtacgccaaaaattttgactagcggaggctagaaggagagagatgggtgcgagagcgtcagtattaagcgggggagaattagatcgcgatgggaaaaaattcggttaaggccagggggaaagaaaaaatataaattaaaacatatagtatgggcaagcagggagctagaacgattcgcagttaatcctggcctgttagaaacatcagaaggctgtagacaaatactgggacagctacaaccatcccttcagacaggatcagaagaacttagatcattatataatacagtagcaaccctctattgtgtgcatcaaaggatagagataaaagacaccaaggaagctttagacaagatagaggaagagcaaaacaaaagtaagaccaccgcacagcaagcggccggccgcgctgatcttcagacctggaggaggagatatgagggacaattggagaagtgaattatataaatataaagtagtaaaaattgaaccattaggagtagcacccaccaaggcaaagagaagagtggtgcagagagaaaaaagagcagtgggaataggagctttgttccttgggttcttgggagcagcaggaagcactatgggcgcagcgtcaatgacgctgacggtacaggccagacaattattgtctggtatagtgcagcagcagaacaatttgctgagggctattgaggcgcaacagcatctgttgcaactcacagtctggggcatcaagcagctccaggcaagaatcctggctgtggaaagatacctaaaggatcaacagctcctggggatttggggttgctctggaaaactcatttgcaccactgctgtgccttggaatgctagttggagtaataaatctctggaacagatttggaatcacacgacctggatggagtgggacagagaaattaacaattacacaagcttaatacactccttaattgaagaatcgcaaaaccagcaagaaaagaatgaacaagaattattggaattagataaatgggcaagtttgtggaattggtttaacataacaaattggctgtggtatataaaattattcataatgatagtaggaggcttggtaggtttaagaatagtttttgctgtactttctatagtgaatagagttaggcagggatattcaccattatcgtttcagacccacctcccaaccccgaggggacccgacaggcccgaaggaatagaagaagaaggtggagagagagacagagacagatccattcgattagtgaacggatcggcactgcgtgcgccaattctgcagacaaatggcagtattcatccacaattttaaaagaaaaggggggattggggggtacagtgcaggggaaagaatagtagacataatagcaacagacatacaaactaaagaattacaaaaacaaattacaaaaattcaaaattttcgggtttattacagggacagcagagatccagtttggttagtaccgggcccgctctagtcgaggtcgacggtatcgataagctcgcttcacgagattccagcaggtcgagggacctaataacttcgtatagcatacattatacgaagttatattaagggttccaagcttaagcggccgcggatcccgccaccatggtgagcaagggcgaggagctgttcaccggggtggtgcccatcctggtcgagctggacggcgacgtaaacggccacaagttcagcgtgtccggcgagggcgagggcgatgccacctacggcaagctgaccctgaagttcatctgcaccaccggcaagctgcccgtgccctggcccaccctcgtgaccaccctgacctacggcgtgcagtgcttcagccgctaccccgaccacatgaagcagcacgacttcttcaagtccgccatgcccgaaggctacgtccaggagcgcaccatcttcttcaaggacgacggcaactacaagacccgcgccgaggtgaagttcgagggcgacaccctggtgaaccgcatcgagctgaagggcatcgacttcaaggaggacggcaacatcctggggcacaagctggagtacaactacaacagccacaacgtctatatcatggccgacaagcagaagaacggcatcaaggtgaacttcaagatccgccacaacatcgaggacggcagcgtgcagctcgccgaccactaccagcagaacacccccatcggcgacggccccgtgctgctgcccgacaaccactacctgagcacccagtccgccctgagcaaagaccccaacgagaagcgcgatcacatggtcctgctggagttcgtgaccgccgccgggatcactctcggcatggacgagctgtacaagtaagaattcgtcgagggacctaataacttcgtatagcatacattatacgaagttatacatgtttaagggttccggttccactaggtacaattcgatatcaagcttatcgataatcaacctctggattacaaaatttgtgaaagattgactggtattcttaactatgttgctccttttacgctatgtggatacgctgctttaatgcctttgtatcatgctattgcttcccgtatggctttcattttctcctccttgtataaatcctggttgctgtctctttatgaggagttgtggcccgttgtcaggcaacgtggcgtggtgtgcactgtgtttgctgacgcaacccccactggttggggcattgccaccacctgtcagctcctttccgggactttcgctttccccctccctattgccacggcggaactcatcgccgcctgccttgcccgctgctggacaggggctcggctgttgggcactgacaattccgtggtgttgtcggggaaatcatcgtcctttccttggctgctcgcctgtgttgccacctggattctgcgcgggacgtccttctgctacgtcccttcggccctcaatccagcggaccttccttcccgcggcctgctgccggctctgcggcctcttccgcgtcttcgccttcgccctcagacgagtcggatctccctttgggccgcctccccgcatcgataccgtcgacctcgatcgagacctagaaaaacatggagcaatcacaagtagcaatacagcagctaccaatgctgattgtgcctggctagaagcacaagaggaggaggaggtgggttttccagtcacacctcaggtacctttaagaccaatgacttacaaggcagctgtagatcttagccactttttaaaagaaaaggggggactggaagggctaattcactcccaacgaagacaagatatccttgatctgtggatctaccacacacaaggctacttccctgattggcagaactacacaccagggccagggatcagatatccactgacctttggatggtgctacaagctagtaccagttgagcaagagaaggtagaagaagccaatgaaggagagaacacccgcttgttacaccctgtgagcctgcatgggatggatgacccggagagagaagtattagagtggaggtttgacagccgcctagcatttcatcacatggcccgagagctgcatccggactgtactgggtctctctggttagaccagatctgagcctgggagctctctggctaactagggaacccactgcttaagcctcaataaagcttgccttgagtgcttcaagtagtgtgtgcccgtctgttgtgtgactctggtaactagagatccctcagacccttttagtcagtgtggaaaatctctagcag"
).upper()

_COMP = str.maketrans("ACGT", "TGCA")


def revcomp(s: str) -> str:
    return s.translate(_COMP)[::-1]


def canonical(kmer: str) -> str:
    rc = revcomp(kmer)
    return kmer if kmer <= rc else rc


def build_target_kmers(seq: str, k: int):
    """Return list of canonical k-mers per position and the set of unique ones."""
    per_pos = []
    for i in range(len(seq) - k + 1):
        kmer = seq[i:i + k]
        if "N" in kmer:
            per_pos.append(None)
            continue
        per_pos.append(canonical(kmer))
    unique = {km for km in per_pos if km is not None}
    return per_pos, unique


def main():
    per_pos, target_canon = build_target_kmers(TARGET, K)
    total = len(target_canon)

    both_strands = set()
    canon_of = {}
    for ck in target_canon:
        rc = revcomp(ck)
        both_strands.add(ck)
        both_strands.add(rc)
        canon_of[ck] = ck
        canon_of[rc] = ck

    found = set()
    print(f"Decompressor: {' '.join(DECOMP_CMD[:1])}")
    print(f"Target length: {len(TARGET)} bp")
    print(f"Unique target {K}-mers to find: {total}")
    print(f"Streaming reads from: {FASTQ_BZ2}\n")

    proc = subprocess.Popen(
        DECOMP_CMD,
        stdout=subprocess.PIPE,
        bufsize=1024 * 1024 * 8,
    )

    start = time.time()
    n_reads = 0
    line_idx = 0
    KK = K
    bs = both_strands
    try:
        for raw in proc.stdout:
            line_idx += 1
            if line_idx & 3 != 2:
                continue
            n_reads += 1
            seq = raw[:-1].decode("ascii", "replace")
            L = len(seq)
            for i in range(L - KK + 1):
                kmer = seq[i:i + KK]
                if kmer in bs:
                    found.add(canon_of[kmer])

            if n_reads % 4_000_000 == 0:
                elapsed = time.time() - start
                pct = 100.0 * len(found) / total
                rate = n_reads / elapsed / 1000
                print(f"  {n_reads:>12,} reads | coverage {len(found)}/{total} "
                      f"({pct:5.1f}%) | {elapsed:6.0f}s | {rate:.0f}k reads/s")
                sys.stdout.flush()

            if len(found) == total:
                print("\nAll target k-mers found — stopping early.")
                break
    finally:
        proc.stdout.close()
        proc.terminate()

    elapsed = time.time() - start
    pct = 100.0 * len(found) / total
    print("\n===================== RESULT =====================")
    print(f"Reads scanned:        {n_reads:,}")
    print(f"Time:                 {elapsed:.0f}s")
    print(f"Target k-mers found:  {len(found)}/{total} ({pct:.1f}%)")

    best = cur = 0
    for km in per_pos:
        if km is not None and km in found:
            cur += 1
            best = max(best, cur)
        else:
            cur = 0
    covered_bp = best + K - 1 if best else 0

    if pct >= 95:
        verdict = "PRESENT — the sequence is well represented in the reads."
    elif pct >= 50:
        verdict = "PARTIALLY present — a substantial portion is covered."
    elif pct > 5:
        verdict = "Weak/partial signal — only a small portion is covered."
    else:
        verdict = "NOT present — essentially no coverage of this sequence."
    print(f"Longest contiguous covered region: ~{covered_bp} bp")
    print(f"Verdict: {verdict}")
    print("==================================================")



if __name__ == "__main__":
    main()

