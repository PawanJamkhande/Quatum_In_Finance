import time
from preprocessing.data_loader import load_data
from preprocessing.normalize import normalize_data
from preprocessing.feature_extractor import extract_features

from encoding.encoding_selector import select_encoding
from workflows.workflow_selector import select_workflow
from workflows.classical_sa import classical_solver
from workflows.qaoa_quantum import qaoa_quantum_solver
from workflows.hybrid import hybrid_solver

from evaluation.metrics import evaluate
from evaluation.logger import log_result

# Load & preprocess
returns, cov, constraints = load_data()
returns, cov = normalize_data(returns, cov)
features = extract_features(returns, cov, constraints)

# Encoding selection
encoding_name, Q = select_encoding(features, returns, cov, constraints)

# Workflow selection
workflow = select_workflow(features)

# Execute solver
start = time.time()

if workflow == "CLASSICAL":
    x, energy = classical_solver(Q)
elif workflow == "QAOA":
    x, energy = qaoa_quantum_solver(Q)
else:
    x, energy = hybrid_solver(Q)

# Evaluation
metrics = evaluate(start, energy)

# Logging
result = {
    "encoding": encoding_name,
    "workflow": workflow,
    "energy": float(metrics["energy"]),
    "runtime": metrics["runtime"]
}

log_result(result)

print("Done:", result)
