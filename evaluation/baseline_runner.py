import time
from workflows.classical_sa import classical_solver

def run_baseline(Q):
    """
    Baseline = fixed encoding + classical solver
    """
    start = time.time()
    x, energy = classical_solver(Q)
    runtime = time.time() - start

    scaled_energy = energy / len(Q)
    solution_quality = 1 / (1 + abs(scaled_energy))

    return {
        "energy": energy,
        "runtime": runtime,
        "solution_quality": solution_quality
    }
