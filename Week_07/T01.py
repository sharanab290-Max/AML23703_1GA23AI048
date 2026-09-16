def constant_one_deutsch():
    circuit = QuantumCircuit(2, 1)

    # Prepare |0>|1> and transform both qubits to the required states
    circuit.x(1)
    circuit.h(0)
    circuit.h(1)

    # Oracle: f(x) = 1, so the target is flipped for every x
    circuit.x(1)
    # Interference and readout
    circuit.h(0)
    circuit.measure(0, 0)
    return circuit
qc_easy = constant_one_deutsch()

print("=== EXERCISE 1: CONSTANT FUNCTION f(x)=1 ===")
print(qc_easy.draw(output="text"))

counts = sim.run(qc_easy, shots=256).result().get_counts()
print("Counts:", counts
print("Detected type:", "Constant" if set(counts) == {"0"} else "Balanced")
