3 qubits and 3 classical bits
qc = QuantumCircuit(3, 3)
# Create GHZ state
qc.h(0)
qc.cx(0, 1)
qc.cx(0, 2)
# Measure all qubits
qc.measure([0, 1, 2], [0, 1, 2])
# Run measurements
simulator = AerSimulator()
result = simulator.run(qc, shots=1024).result()
counts = result.get_counts()
print(qc)
print(counts)
# Verify perfect three-way correlation
assert set(counts.keys()).issubset({"000", "111"})
assert counts.get("000", 0) + counts.get("111", 0) == 1024
print("Verified: only 000 and 111 occur.")
