from workflows.classical_sa import classical_solver
from workflows.qaoa_quantum import qaoa_quantum_solver

def hybrid_solver(Q):
    # Step 1: Classical pre-optimization
    x_classical, _ = classical_solver(Q, steps=500)

    # Step 2: Quantum refinement (simulated)
    x_quantum, energy = qaoa_quantum_solver(Q)

    return x_quantum, energy
