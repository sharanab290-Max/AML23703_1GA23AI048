from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
 
def measure_x_basis(state_type: str):
    qc = QuantumCircuit(1, 1)
    # Step 1: Prepare target state
    if state_type == "+":
        qc.h(0)  # Prepares |+> state
    elif state_type == "-":
        qc.x(0)
        qc.h(0)  # Prepares |-> state
    # Step 2: Basis change (H transforms X-basis into Z-basis)
    qc.h(0)
    # Step 3: Measure
    qc.measure(0, 0)
    simulator = AerSimulator()
    counts = simulator.run(qc, shots=1024).result().get_counts()
    return qc, counts
 
print("=== MEDIUM: X-BASIS MEASUREMENTS ===")
# Test |+> state
qc_plus, counts_plus = measure_x_basis("+")
print("1. Circuit for |+> in X-Basis:")
print(qc_plus.draw(output="text"))
print("Counts for |+> state (Expect only '0'):", counts_plus)
 
# Test |-> state
qc_minus, counts_minus = measure_x_basis("-")
print("\n2. Circuit for |-> in X-Basis:")
print(qc_minus.draw(output="text"))
print("Counts for |-> state (Expect only '1'):", counts_minus)

