import csv

def save_orfs_to_csv(orfs, filename="orf_results.csv"):

    with open(filename, "w", newline="") as csvfile:

        writer = csv.writer(csvfile)

        writer.writerow([
            "ORF_ID",
            "Start",
            "End",
            "Length",
            "DNA_Sequence",
            "Protein"
        ])

        for idx, orf in enumerate(orfs, start=1):

            writer.writerow([
                idx,
                orf["start"],
                orf["end"],
                orf["length"],
                orf["sequence"],
                orf["protein"]
            ])

    print(f"Results saved to {filename}")