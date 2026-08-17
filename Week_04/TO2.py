Create a 2-qubit circuit with 2 classical bits
qc = QuantumCircuit(2, 2)
# Create the Bell state (|00> + |11>) / sqrt(2)
qc.h(0)
qc.cx(0, 1)
# Measure both qubits
qc.measure([0, 1], [0, 1])
# Run 1024 shots
simulator = AerSimulator()
result = simulator.run(qc, shots=1024).result()
counts = result.get_counts()
print(qc)
print(counts)
# Verify that only 00 and 11 occurred
assert set(counts.keys()).issubset({"00", "11"})
assert counts.get("00", 0) + counts.get("11", 0) == 1024
print("Verified: outcomes are only 00 and 11.")
