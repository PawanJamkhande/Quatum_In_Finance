import csv
import os

def log_result(result):
    file_exists = os.path.isfile("results.csv")

    with open("results.csv", "a", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=result.keys()
        )

        if not file_exists:
            writer.writeheader()

        writer.writerow(result)
