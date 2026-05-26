def reverse_complement(sequence):

    complement = {
        "A": "T",
        "T": "A",
        "G": "C",
        "C": "G"
    }

    reverse_seq = sequence[::-1]

    rev_comp = ""

    for base in reverse_seq:
        rev_comp += complement.get(base, base)

    return rev_comp