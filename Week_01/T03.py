from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer


# Oracle
def deutsch_oracle(oracle_type="constant0"):
    qc = QuantumCircuit(2, name="Uf")

    if oracle_type == "constant1":
        qc.x(1)
    elif oracle_type == "balanced":
        qc.cx(0, 1)

    return qc.to_gate()


# Deutsch Algorithm
def deutsch(oracle_type):
    qc = QuantumCircuit(2, 1)

    # Prepare |1> in ancilla
    qc.x(1)

    # Apply Hadamard gates
    qc.h([0, 1])

    # Apply Oracle
    qc.append(deutsch_oracle(oracle_type), [0, 1])

    # Apply Hadamard to first qubit
    qc.h(0)

    # Measure first qubit
    qc.measure(0, 0)

    # Run on Aer simulator
    simulator = Aer.get_backend("aer_simulator")
    compiled_circuit = transpile(qc, simulator)

    job = simulator.run(compiled_circuit, shots=1024)
    result = job.result()
    counts = result.get_counts()

    print(f"{oracle_type}: {counts}")

    if "0" in counts:
        print("Function is CONSTANT\n")
    else:
        print("Function is BALANCED\n")


# Run the algorithm
deutsch("constant0")
deutsch("constant1")
deutsch("balanced")