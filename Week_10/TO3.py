# (a) X error on every transmission
display(superdense("10", channel="x").draw("mpl", fold=-1))
rows = []
for bits in ENCODING:
    counts = send(superdense(bits, channel="x"))
    rows.append({"Sent": bits, "Received": max(counts, key=counts.get),
                 "Counts": counts, "Success (%)": 100 * counts.get(bits, 0) / SHOTS})
display(pd.DataFrame(rows))
 
# (b) Random bit-flip channel with probability p
p = 0.15
flip_noise = NoiseModel()
flip_noise.add_quantum_error(pauli_error([("X", p), ("I", 1 - p)]), ["id"], [0])
noisy_backend = AerSimulator(noise_model=flip_noise, seed_simulator=SEED)
 
rows = []
for i, bits in enumerate(ENCODING):
    counts = send(superdense(bits, channel="id"), sim=noisy_backend, seed=SEED + i)
    flipped = bits[0] + str(1 - int(bits[1]))
    rows.append({"Sent": bits, "Correct": counts.get(bits, 0),
                 "2nd bit flipped": counts.get(flipped, 0),
                 "Other": SHOTS - counts.get(bits, 0) - counts.get(flipped, 0),
                 "Success (%)": round(100 * counts.get(bits, 0) / SHOTS, 2)})
ex3b = pd.DataFrame(rows)
display(ex3b)
print(f"Bit-flip probability p = {p}, expected success = {1 - p:.0%}, "
      f"mean observed = {ex3b['Success (%)'].mean():.2f}%")

