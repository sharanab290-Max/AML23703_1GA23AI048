def balanced_not_oracle():
    circuit = QuantumCircuit(2, 1)
    # Prepare input |+> and ancilla |->
    circuit.x(1)
    circuit.h(0)
    circuit.h(1)

    # Oracle for f(x) = NOT x
    circuit.x(0)
    circuit.cx(0, 1)
    circuit.x(0)
    circuit.h(0)
    circuit.measure(0, 0)
    return circuit

qc_medium = balanced_not_oracle()
print("=== EXERCISE 2: BALANCED FUNCTION f(x)=NOT x ===")
print(qc_medium.draw(output="text"))

counts = sim.run(qc_medium, shots=384).result().get_counts()
print("Counts:", counts)
print("Detected type:", "Balanced" if set(counts) == {"1"} else "Constant")