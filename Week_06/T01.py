def make_simon_oracle(secret: str):
    n = len(secret)
    circuit = QuantumCircuit(2 * n, name="SimonOracle")

    # Start with y = x
    for q in range(n):

        circuit.cx(q, n + q)
    # Add the XOR mask using the first set bit as the control

    control = next((pos for pos, bit in enumerate(secret) if bit == "1"), None)

    if control is not None:
        for pos, bit in enumerate(secret):
            if bit == "1":
                circuit.cx(control, n + pos)

    return circuit.to_gate(label="Simon Oracle")

secret = "011"
oracle = make_simon_oracle(secret)
print(oracle.definition.draw(output="text"))
