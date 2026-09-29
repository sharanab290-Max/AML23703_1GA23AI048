from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
 
def build_dj_circuit(n: int, oracle_type: str, value: int = 1):
    qc = QuantumCircuit(n + 1, n)
    qc.x(n)
    for i in range(n + 1):
        qc.h(i)
    qc.barrier()
    if oracle_type == "constant":
        if value == 1:
            qc.x(n)                 # f(x) = 1 ; f(x) = 0 needs no gate
    elif oracle_type == "balanced":
        for i in range(n):          # f(x) = x0 XOR ... XOR x(n-1)
            qc.cx(i, n)
    else:
        raise ValueError("Invalid oracle type")
    qc.barrier()
    for i in range(n):
        qc.h(i)
    qc.measure(range(n), range(n))
    return qc
 
print("=== HARD: GENERALIZED DEUTSCH-JOZSA (n = 2 to 5) ===")
simulator = AerSimulator()
for n_bits in range(2, 6):
    for o_type, val in [("constant", 0), ("constant", 1), ("balanced", None)]:
        qc = build_dj_circuit(n_bits, o_type, val if val is not None else 1)
        counts = simulator.run(transpile(qc, simulator), shots=500).result().get_counts()
        measured = max(counts, key=counts.get)
        assert len(counts) == 1, "outcome should be deterministic"
        cls = "Constant" if measured == "0" * n_bits else "Balanced"
        label = o_type if val is None else f"{o_type} f={val}"
        print(f"n = {n_bits} | Case: {label:<12} | Measured: {measured:<6} | Result: {cls}")
    print("-" * 65)
