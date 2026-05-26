def find_motif(sequence, motif):

    positions = []

    for i in range(len(sequence) - len(motif) + 1):

        if sequence[i:i+len(motif)] == motif:
            positions.append(i)

    return positions