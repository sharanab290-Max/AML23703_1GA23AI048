from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
 
# 1. Create a single-qubit Hadamard superposition circuit
qc_easy = QuantumCircuit(1, 1)
qc_easy.h(0)
qc_easy.measure(0, 0)
 
simulator = AerSimulator()
shots_list = [100, 1000, 10000]
 
print("=== EASY: MEASUREMENT SHOT CONVERGENCE ===")
print("Circuit Layout:")
print(qc_easy.draw(output="text"))
print("\nShot Count | Counts (0, 1) | P(0) Measured | Error from 0.5")
print("-" * 55)
 
for shots in shots_list:
    result = simulator.run(qc_easy, shots=shots).result()
    counts = result.get_counts()
    count_0 = counts.get("0", 0)
    count_1 = counts.get("1", 0)
    p_0 = count_0 / shots
    error = abs(p_0 - 0.5)
    print(
        f"{shots:<10} | {f'0:{count_0}, 1:{count_1}':<13} | {p_0:<13.4f} | {error:<12.4f}"
    )

