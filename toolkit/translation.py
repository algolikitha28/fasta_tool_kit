from Bio.Seq import Seq

def translate_sequence(sequence):

    trimmed_length = len(sequence) - (len(sequence) % 3)

    trimmed_sequence = sequence[:trimmed_length]

    dna = Seq(trimmed_sequence)

    protein = dna.translate()

    return str(protein)