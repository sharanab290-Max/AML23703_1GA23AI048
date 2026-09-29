import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit.quantum_info import Statevector
from qiskit_aer import AerSimulator
 
def generate_bell_circuit(bell_type, measure=True):
    qc = QuantumCircuit(2, 2)
    # Pauli-X gates must act BEFORE H and CNOT (a Z on |0> would do nothing)
    if bell_type in ("Phi-", "Psi-"):
        qc.x(0)
    if bell_type in ("Psi+", "Psi-"):
        qc.x(1)
    qc.h(0)
    qc.cx(0, 1)
    if measure:
        qc.measure([0, 1], [0, 1])
    return qc
 
r = 1 / np.sqrt(2)
targets = {                       # Qiskit index = q1 q0
    "Phi+": [r, 0, 0, r], "Phi-": [r, 0, 0, -r],
    "Psi+": [0, r, r, 0], "Psi-": [0, r, -r, 0],
}
simulator = AerSimulator()
bell_states = ["Phi+", "Phi-", "Psi+", "Psi-"]
 
print("=== MEDIUM: ALL FOUR BELL STATES ===")
print("Part A: computational-basis measurement (1024 shots)")
for name in bell_states:
    circuit = generate_bell_circuit(name)
    counts = simulator.run(transpile(circuit, simulator), shots=1024).result().get_counts()
    print(f"State: {name:<5} | Measured Counts: {dict(sorted(counts.items()))}")
 
print("\nPart B: fidelity of prepared state with the ideal Bell state")
for name in bell_states:
    sv = Statevector.from_instruction(generate_bell_circuit(name, measure=False))
    fid = abs(np.vdot(targets[name], sv.data)) ** 2
    print(f"State: {name:<5} | Fidelity: {fid:.3f}")
 
print("\nPart C: Bell-basis measurement (CNOT, H, then measure) separates all four")
for name in bell_states:
    qc = generate_bell_circuit(name, measure=False)
    qc.cx(0, 1)
    qc.h(0)
    qc.measure([0, 1], [0, 1])
    counts = simulator.run(transpile(qc, simulator), shots=1024).result().get_counts()
    print(f"State: {name:<5} | Measured Counts: {counts}")
