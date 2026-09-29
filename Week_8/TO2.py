from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
 
n = 3
qc_medium = QuantumCircuit(n + 1, n)
qc_medium.x(n)
for i in range(n + 1):
    qc_medium.h(i)
qc_medium.barrier()
 
# Balanced parity oracle f(x) = x0 XOR x1 XOR x2 (CNOT from each input to ancilla)
for i in range(n):
    qc_medium.cx(i, n)
qc_medium.barrier()
 
for i in range(n):
    qc_medium.h(i)
qc_medium.measure(range(n), range(n))
 
print("=== MEDIUM: 3-BIT BALANCED PARITY ORACLE ===")
print("Circuit Diagram:")
print(qc_medium.draw(output="text"))
print()
 
simulator = AerSimulator()
counts_med = simulator.run(transpile(qc_medium, simulator), shots=1024).result().get_counts()
print("Measurement Results (1024 shots):", counts_med)
print("Probability of '000':", counts_med.get("0" * n, 0) / 1024)
print("Inferred Classification:",
      "Constant" if "0" * n in counts_med else "Balanced (Non-zero result)")
