
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
 
n = 3
simulator = AerSimulator()
 
def constant_dj(n, value):
    qc = QuantumCircuit(n + 1, n)
    qc.x(n)                       # ancilla to |1>
    for i in range(n + 1):
        qc.h(i)                   # inputs -> |+>, ancilla -> |->
    qc.barrier()
    if value == 1:
        qc.x(n)                   # f(x) = 1 : flip ancilla unconditionally
    # f(x) = 0 : identity, no gates
    qc.barrier()
    for i in range(n):
        qc.h(i)
    qc.measure(range(n), range(n))
    return qc
 
for v in (1, 0):
    qc = constant_dj(n, v)
    if v == 1:
        print("=== EASY: 3-BIT CONSTANT ORACLE ===")
        print("Circuit Diagram (f(x) = 1):")
        print(qc.draw(output="text"))
        print()
    counts = simulator.run(transpile(qc, simulator), shots=1024).result().get_counts()
    print(f"f(x) = {v} | Measurement Results (1024 shots): {counts}")
    result = max(counts, key=counts.get)
    print("Inferred Classification:", "Constant (All Zeros)" if result == "0" * n else "Balanced")

