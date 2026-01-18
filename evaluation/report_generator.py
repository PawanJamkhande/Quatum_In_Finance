import json

def generate_json_report(
    encoding,
    solver,
    automated,
    baseline,
    improvement
):
    report = {
        "selected_encoding": encoding,
        "selected_solver": solver,
        "solution_quality": round(automated["solution_quality"], 3),
        "runtime_sec": round(automated["runtime"], 3),
        "baseline_improvement": round(improvement["solution_quality"], 2)
    }

    with open("final_report.json", "w") as f:
        json.dump(report, f, indent=4)

    return report
