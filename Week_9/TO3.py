from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
 
def bell_x_basis(bell_type):
    qc = QuantumCircuit(2, 2)
    if bell_type in ("Phi-", "Psi-"):
        qc.x(0)
    if bell_type in ("Psi+", "Psi-"):
        qc.x(1)
    qc.h(0)
    qc.cx(0, 1)
    qc.barrier()
    qc.h(0)                      # rotate X basis -> Z basis
    qc.h(1)
    qc.measure([0, 1], [0, 1])
    return qc
 
simulator = AerSimulator()
print("=== HARD: MEASURING BELL PAIR IN HADAMARD BASIS ===")
print("Circuit Diagram (Phi+):")
print(bell_x_basis("Phi+").draw(output="text"))
print()
 
for name in ["Phi+", "Phi-", "Psi+", "Psi-"]:
    counts = simulator.run(transpile(bell_x_basis(name), simulator), shots=1024).result().get_counts()
    same = counts.get("00", 0) + counts.get("11", 0)
    kind = "correlated" if same == 1024 else "anti-correlated" if same == 0 else "mixed"
    print(f"X-basis | {name:<5} | Counts: {dict(sorted(counts.items()))} | {kind}")

