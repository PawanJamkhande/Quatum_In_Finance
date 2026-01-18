import time

# ---------- Imports ----------
from preprocessing.data_loader import load_data
from preprocessing.normalize import normalize_data
from preprocessing.feature_extractor import extract_features
from preprocessing.asset_generator import generate_asset_returns
from preprocessing.covariance_generator import generate_covariance

from encoding.encoding_selector import select_encoding
from workflows.workflow_selector import select_workflow
from workflows.classical_sa import classical_solver
from workflows.hybrid import hybrid_solver
from workflows.qaoa_quantum import qaoa_quantum_solver

from evaluation.baseline_runner import run_baseline
from evaluation.comparator import compare_results

# ---------- Data Loading ----------
returns, constraints = load_data()
returns, _ = normalize_data(returns, returns)

num_assets = len(returns)
asset_returns = generate_asset_returns(num_assets)
cov = generate_covariance(asset_returns)

features = extract_features(returns, cov, constraints)

# ---------- Encoding Selection ----------
encoding_name, Q = select_encoding(features, returns, cov, constraints)

# ---------- BASELINE RUN ----------
baseline_metrics = run_baseline(Q)

# ---------- WORKFLOW SELECTION ----------
workflow = select_workflow(features)

# ---------- AUTOMATED RUN ----------
start = time.time()

if workflow == "CLASSICAL":
    x, energy = classical_solver(Q)
elif workflow == "QAOA":
    x, energy = qaoa_quantum_solver(Q)
else:
    x, energy = hybrid_solver(Q)

auto_runtime = time.time() - start

scaled_energy = energy / len(Q)
auto_solution_quality = 1 / (1 + abs(scaled_energy))



automated_metrics = {
    "energy": energy,
    "runtime": auto_runtime,
    "solution_quality": auto_solution_quality
}

# ---------- COMPARISON ----------
improvement = compare_results(baseline_metrics, automated_metrics)

# ---------- FINAL REPORT GENERATION ----------
from evaluation.report_generator import generate_json_report
from evaluation.csv_generator import generate_csv_summary

json_report = generate_json_report(
    encoding=encoding_name,
    solver=workflow,
    automated=automated_metrics,
    baseline=baseline_metrics,
    improvement=improvement
)

generate_csv_summary(
    baseline_metrics,
    automated_metrics,
    improvement
)

print("Final JSON Report Generated:")
print(json_report)
print("CSV Summary Table Generated")
