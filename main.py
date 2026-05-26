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

    print("ID:", record["id"])
    print("Sequence:", seq)

    print("GC Content:", calculate_gc(seq))

    print("Reverse Complement:")
    print(reverse_complement(seq))

    print("Protein Translation:")
    print(translate_sequence(seq))

    print("Motif Positions:")
    print(find_motif(seq, "ATG"))

    print("-" * 40)

    print("ORFs Found:")

    orfs = find_orfs(seq)

    for idx, orf in enumerate(orfs, start=1):

        print(f"ORF {idx}")
        print("Start:", orf["start"])
        print("End:", orf["end"])
        print("Length:", orf["length"])
        print("Sequence:", orf["sequence"])
        print()

    print("-" * 40)