def find_orfs(sequence):

    start_codon = "ATG"
    stop_codons = ["TAA", "TAG", "TGA"]

    orfs = []

    seq_length = len(sequence)

    for i in range(seq_length - 2):

        codon = sequence[i:i+3]

        if codon == start_codon:

            for j in range(i + 3, seq_length - 2, 3):

                stop_codon = sequence[j:j+3]

                if stop_codon in stop_codons:

                    orf = sequence[i:j+3]

                    orfs.append({
                        "start": i,
                        "end": j + 3,
                        "sequence": orf,
                        "length": len(orf)
                    })

                    break

    return orfs