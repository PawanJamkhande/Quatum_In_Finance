def compare_results(baseline, automated):
    improvement = {}

    improvement["solution_quality"] = (
        (automated["solution_quality"] - baseline["solution_quality"])
        / baseline["solution_quality"]
    ) * 100

    improvement["runtime"] = (
        (baseline["runtime"] - automated["runtime"])
        / baseline["runtime"]
    ) * 100

    return improvement
