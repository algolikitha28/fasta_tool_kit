from toolkit.parser import read_fasta
from toolkit.gc_content import calculate_gc
from toolkit.reverse_complement import reverse_complement
from toolkit.translation import translate_sequence
from toolkit.motif_finder import find_motif
from toolkit.orf_finder import find_orfs

file_path = "data/sample.fasta"

records = read_fasta(file_path)

for record in records:

    seq = record["sequence"]

    print("=" * 50)
    print("ID:", record["id"])
    print("Sequence:", seq)
    print("=" * 50)

    # GC Content
    print("\nGC Content:")
    print(calculate_gc(seq), "%")

    # Reverse Complement
    print("\nReverse Complement:")
    print(reverse_complement(seq))

    # Translation
    print("\nProtein Translation:")
    print(translate_sequence(seq))

    # Motif Finder
    print("\nMotif Positions (ATG):")
    motifs = find_motif(seq, "ATG")

    if motifs:
        print(motifs)
    else:
        print("Motif not found")

    # ORF Finder
    print("\nORFs Found:")

    orfs = find_orfs(seq)

    if not orfs:
        print("No ORFs found")
    else:
        for idx, orf in enumerate(orfs, start=1):

            print(f"\nORF {idx}")
            print("Start:", orf["start"])
            print("End:", orf["end"])
            print("Length:", orf["length"])
            print("Sequence:", orf["sequence"])
            print("Protein:", orf["protein"])

    print("\n" + "=" * 50)