def calculate_gc(sequence):

    g = sequence.count("G")
    c = sequence.count("C")

    gc_percent = ((g + c) / len(sequence)) * 100

    return round(gc_percent, 2)