def evaluate_oracle(gate, bits, n):
    circuit = QuantumCircuit(2 * n, n)
    for index, value in enumerate(bits):
        if value == "1":
            circuit.x(index)

    circuit.append(gate, range(2 * n))
    circuit.measure(range(n, 2 * n), range(n))
    result = backend.run(circuit, shots=1).result()
    measured = next(iter(result.get_counts()))
    return measured[::-1]

s = "011"
n = len(s)
oracle = make_simon_oracle(s)

value_zero = evaluate_oracle(oracle, "0" * n, n)
value_secret = evaluate_oracle(oracle, s, n)

print("f(000) =", value_zero)
print("f(011) =", value_secret)
print("Collision verified:", value_zero == value_secret)