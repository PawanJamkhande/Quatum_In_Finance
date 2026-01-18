import csv

def generate_csv_summary(baseline, automated, improvement):
    with open("summary_table.csv", "w", newline="") as f:
        writer = csv.writer(f)

        writer.writerow(["Metric", "Default", "Automated", "Improvement"])

        writer.writerow([
            "Solution Quality",
            round(baseline["solution_quality"], 3),
            round(automated["solution_quality"], 3),
            f"{round(improvement['solution_quality'], 2)}%"
        ])

        writer.writerow([
            "Runtime (s)",
            round(baseline["runtime"], 3),
            round(automated["runtime"], 3),
            f"{round(improvement['runtime'], 2)}%"
        ])

        writer.writerow([
            "Manual Tuning",
            "High",
            "None",
            "100% saved"
        ])
