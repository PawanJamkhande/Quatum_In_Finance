from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit import transpile
import numpy as np

def qaoa_quantum_solver(Q):
    "Q is a cost matrics (n*n) see in covariance.csv currently we are making the covariance matrics but in future we can automate the covariance matrics as well"

    n = Q.shape[0]
    "Here we are taking two 'n' for qubits and classical bits"
    qc = QuantumCircuit(n, n)

    # this is Superposition state applying hadamard gate to every qubit for making an equal superposition state for all
    for i in range(n):
        qc.h(i)

    # Here, gamma scales how strongly each qubit “feels” its cost term (Q[i,i]): qc.rz(gamma * Q[i, i], i). A larger gamma applies more phase for the same cost value, changing the interference pattern and thus the output bitstring probabilities
    # rz is the rotation by z axis
    gamma = 0.8 # this 0.8 is demonstrative value not tuned value 0.8 is the optimized value to minimize the objectives in QAOA
    for i in range(n):
        qc.rz(gamma * Q[i, i], i)

    
    beta = 0.6
    for i in range(n):
        qc.rx(2 * beta, i)

    # measuring every qubit to its corresponding classical bit
    qc.measure(range(n), range(n))

    backend = Aer.get_backend("aer_simulator") #this chooses or you can say build a state vector of given input
    qc = transpile(qc, backend) # it matches the circuits with that state vector.
    "here we are using aer simulator to simulate the quantum circuit and get the measurement results"
    
    result = backend.run(qc, shots=1024).result()
    counts = result.get_counts() #gives a dictionary with bitstrings as keys and their counts as values (histogram basicallly)
    "here we are getting the counts of measurement results from the simulator running 1024 shots"
    
    # pick the most frequent bitstring
    best = max(counts, key=counts.get)
    x = np.array([int(bit) for bit in best[::-1]])
    "here we are converting the most frequent bitstring into a numpy array of integers"
    "these bits represent the solution to the optimization problem"
    
    energy = x @ Q @ x #computing quadratic costs of choosen bitstring
    "this computes the energy (or cost) of the chosen bitstring solution"
    return x, energy #returns the choosen bitstring and its cost
    