def deutsch_solver(truth_table):
    if len(truth_table) != 2 or any(bit not in "01" for bit in truth_table):
        raise ValueError("truth_table must contain exactly two binary values")
    
    f0, f1 = map(int, truth_table)
    qc = QuantumCircuit(2, 1)

    # |0>|1> -> |+>|->
    qc.x(1)
    qc.h(0)
    qc.h(1)

    # Encode f(0)
    if f0:

        qc.x(1)

    # Encode the difference f(0) XOR f(1)

    if f0 ^ f1:
        qc.cx(0, 1)
    qc.h(0)
    qc.measure(0, 0)
    return qc

truth_tables = ["00", "11", "01", "10"]

for table in truth_tables:
    circuit = deutsch_solver(table)
    result = sim.run(circuit, shots=128).result().get_counts()
    bit = next(iter(result))
    kind = "Constant" if bit == "0" else "Balanced"
    print(f"Truth table {table} -> measurement {bit} -> {kind}")