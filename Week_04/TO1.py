Create a 2-qubit circuit
qc = QuantumCircuit(2, 2)
# Put control qubit q0 into |1>
qc.x(0)
# Apply CNOT: q0 = control, q1 = target
qc.cx(0, 1)
# Measure both qubits
qc.measure([0, 1], [0, 1])
# Display circuit
print(qc)
# Run simulation
simulator = AerSimulator()
result = simulator.run(qc, shots=1024).result()
# Get measurement results
counts = result.get_counts()
print("Measurement results:", counts)
# Verify target flipped
if counts == {'11': 1024}:
    print("Verified: target qubit flipped from 0 to 1.")
else:
    print("Unexpected result:", counts)
