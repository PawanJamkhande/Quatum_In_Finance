Automated Hybrid Quantum–Classical Portfolio Optimization Framework

This project implements an automated hybrid quantum–classical optimization framework for portfolio optimization problems.
The system converts a financial portfolio optimization problem into a QUBO (Quadratic Unconstrained Binary Optimization) formulation and automatically selects:

The appropriate encoding strategy

The appropriate solver workflow (Classical / Hybrid / Quantum)

The quantum component is implemented using QAOA (Quantum Approximate Optimization Algorithm) executed on a quantum simulator, integrated within a classical automation pipeline.

The goal of the project is not to prove quantum supremacy, but to demonstrate how quantum solvers can be orchestrated automatically within a larger decision-making framework.

###_Key Features_

- Automated QUBO encoding selection
- Automated solver workflow selection
- Classical, Quantum (QAOA), and Hybrid solvers
- Simulator-based quantum execution using Qiskit
- Automated covariance matrix generation
- Baseline vs automated performance comparison
- Structured JSON and CSV result generation
- Modular, extensible architecture

###_Problem Statement_

Portfolio optimization involves selecting a subset of assets that maximizes expected return while minimizing risk under given constraints.
Such problems are NP-hard and can be naturally expressed as QUBO problems, which are compatible with quantum and quantum-inspired solvers.

However, practical use of quantum optimization requires manual decisions regarding encoding strategies and solver selection.
This project automates those decisions.

###_System Architecture_

The system is organized into three conceptual layers:

1) Decision Layer (Automation)

Encoding Selector

Workflow Selector (Classical / Hybrid / Quantum)

2) Execution Layer

Classical Simulated Annealing Solver

Quantum QAOA Solver (Simulator-based)

Hybrid Solver (Classical + Quantum)

3) Evaluation Layer

Baseline vs automated comparison

Performance metrics computation

JSON and CSV report generation

###_Project Structure_
autoqubo/
│
├── data/
│   ├── returns.csv
│   └── constraints.json
│
├── preprocessing/
│   ├── data_loader.py
│   ├── normalize.py
│   ├── feature_extractor.py
│   ├── asset_generator.py
│   └── covariance_generator.py
│
├── encoding/
│   ├── encoding_selector.py
│   └── penalty.py
│
├── workflows/
│   ├── classical_sa.py
│   ├── qaoa_quantum.py
│   └── hybrid.py
│
├── evaluation/
│   ├── baseline_runner.py
│   ├── comparator.py
│   ├── report_generator.py
│   ├── csv_generator.py
│   ├── metrics.py
│   └── logger.py
│
├── main.py
├── requirements.txt
└── README.md

Installation & Setup (Run on Any Device)
###_Prerequisites_

Python 3.9 or above

pip installed

Internet access (for installing dependencies)

Step 1: Clone the Repository
git clone <your-repository-url>
cd autoqubo

Step 2: Create Virtual Environment (Recommended)
python -m venv venv


- Activate it:

macOS / Linux

source venv/bin/activate


- Windows

venv\Scripts\activate

🔹 Step 3: Install Dependencies
pip install -r requirements.txt

###_Dependencies Used_

Add this to requirements.txt:

numpy
qiskit
qiskit-aer


(Standard libraries like json, csv, time are included with Python.)

###_How to Run the Project_

From the project root directory:

python main.py

###_Output Files Generated_

After execution, the following files are automatically generated:

File	Description
final_report.json	Structured output matching report’s expected output
summary_table.csv	Baseline vs automated comparison table
qubo_matrix.csv	Generated QUBO matrix
results.csv	Execution logs

- Example JSON Output
{
    "selected_encoding": "Penalty-Based",
    "selected_solver": "Hybrid",
    "solution_quality": 0.72,
    "runtime_sec": 0.14,
    "baseline_improvement": 18.4
}

###_Quantum Computing Component_

Uses QAOA (Quantum Approximate Optimization Algorithm)

1) Implemented with:

- Qubits
- Hadamard gates
- Rotation gates
- Measurement
- Executed on Qiskit Aer Simulator
- No real quantum hardware is required

###_Performance Evaluation_

- The system compares:

1) Baseline: Fixed classical solver, no automation

2) Automated: Encoding + workflow selection with hybrid/quantum solvers

3) Metrics used:
- Normalized solution quality
- Runtime
- Relative improvement percentage
- Due to stochastic solvers, results may vary across runs.

###_Limitations_

- Simulator-based execution only
- Rule-based automation (no trained ML models)
- Synthetic asset data
- No claim of quantum advantage

###_Future Scope_

- Learning-based encoding and workflow selection
- Integration with real financial market data
- Execution on real quantum hardware
- Advanced hybrid feedback mechanisms

###_Academic Disclaimer_

- This project is designed as an undergraduate-level research prototype to demonstrate:
- Hybrid quantum–classical architectures
- Automation around quantum optimization
- Honest benchmarking and evaluation
- It does not claim superiority over classical optimization.

###_Author_

WaveOPS
Bachelor of Engineering (CSE)
Final Year Project – Hybrid Quantum–Classical Systems