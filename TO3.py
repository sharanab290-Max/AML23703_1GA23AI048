from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
 
qc_bell = QuantumCircuit(2)
qc_bell.h(0)
qc_bell.cx(0, 1)
 
print("=== HARD: PARTIAL MEASUREMENT ON BELL STATE ===")
print("Circuit Diagram:")
print(qc_bell.draw(output="text"))
print()
 
state_initial = Statevector.from_instruction(qc_bell)
print("Initial Joint Statevector:", state_initial.data)
 
outcome, post_meas_state = state_initial.measure([0])
print(f"\nMeasured Qubit 0 Outcome: {outcome}")
print("Collapsed Post-Measurement Statevector:", post_meas_state.data)

