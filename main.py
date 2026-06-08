import argparse

from toolkit.parser import read_fasta
from toolkit.gc_content import calculate_gc
from toolkit.reverse_complement import reverse_complement
from toolkit.translation import translate_sequence
from toolkit.motif_finder import find_motif
from toolkit.orf_finder import find_orfs
from toolkit.export_csv import save_orfs_to_csv


# ----------------------------
# Command Line Arguments
# ----------------------------

parser = argparse.ArgumentParser(
    description="FASTA Toolkit for sequence analysis"
)

parser.add_argument(
    "fasta_file",
    help="Path to FASTA file"
)

parser.add_argument(
    "--gc",
    action="store_true",
    help="Calculate GC content"
)

parser.add_argument(
    "--reverse",
    action="store_true",
    help="Generate reverse complement"
)

parser.add_argument(
    "--translate",
    action="store_true",
    help="Translate DNA sequence"
)

parser.add_argument(
    "--motif",
    help="Find motif in sequence"
)

parser.add_argument(
    "--orf",
    action="store_true",
    help="Find ORFs"
)

args = parser.parse_args()

# Require at least one analysis option
if not any([
    args.gc,
    args.reverse,
    args.translate,
    args.motif,
    args.orf
]):
    parser.error(
        "Please specify at least one option: "
        "--gc, --reverse, --translate, --motif, or --orf"
    )

# ----------------------------
# Read FASTA File
# ----------------------------

records = read_fasta(args.fasta_file)

# ----------------------------
# Process Records
# ----------------------------

for record in records:

    seq = record["sequence"]

    print("=" * 50)
    print("ID:", record["id"])
    print("Sequence:", seq)
    print("=" * 50)

    # GC Content
    if args.gc:
        print("\nGC Content:")
        print(f"{calculate_gc(seq)} %")

    # Reverse Complement
    if args.reverse:
        print("\nReverse Complement:")
        print(reverse_complement(seq))

    # Translation
    if args.translate:
        print("\nProtein Translation:")
        print(translate_sequence(seq))

    # Motif Finder
    if args.motif:

        print(f"\nMotif Positions ({args.motif}):")

        motifs = find_motif(seq, args.motif)

        if motifs:
            print(motifs)
        else:
            print("Motif not found")

    # ORF Finder
    if args.orf:

        print("\nORFs Found:")

        orfs = find_orfs(seq)

        if not orfs:
            print("No ORFs found")

        else:

            filename = f"{record['id']}_orf_results.csv"
            save_orfs_to_csv(orfs, filename)

            for idx, orf in enumerate(orfs, start=1):

                print(f"\nORF {idx}")
                print("Start:", orf["start"])
                print("End:", orf["end"])
                print("Length:", orf["length"])
                print("DNA:", orf["sequence"])
                print("Protein:", orf["protein"])

            longest_orf = max(
                orfs,
                key=lambda x: x["length"]
            )

            print("\nLongest ORF")
            print("Length:", longest_orf["length"])
            print("DNA:", longest_orf["sequence"])
            print("Protein:", longest_orf["protein"])

    print("\n" + "=" * 50)