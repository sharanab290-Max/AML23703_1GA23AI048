import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit.quantum_info import Statevector
from qiskit_aer import AerSimulator
 
# Ideal state check (no measurement)
qc_state = QuantumCircuit(2)
qc_state.h(0)
qc_state.cx(0, 1)
print("=== EASY: PHI+ BELL STATE ===")
print("Ideal statevector:", np.round(Statevector.from_instruction(qc_state).data, 3))
 
qc_phi_plus = QuantumCircuit(2, 2)
qc_phi_plus.h(0)
qc_phi_plus.cx(0, 1)
qc_phi_plus.measure([0, 1], [0, 1])
 
print("Circuit Diagram:")
print(qc_phi_plus.draw(output="text"))
print()
 
simulator = AerSimulator()
counts = simulator.run(transpile(qc_phi_plus, simulator), shots=1024).result().get_counts()
print("Measurement Results (1024 shots):", counts)
print("Anti-correlated outcomes ('01','10'):", counts.get("01", 0) + counts.get("10", 0))
