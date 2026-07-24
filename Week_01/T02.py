from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

qc = QuantumCircuit(3, 3)

qc.h([0, 1, 2])

qc.measure([0, 1, 2], [0, 1, 2])

print(qc.draw())

simulator = AerSimulator()

job = simulator.run(qc, shots=1024)
result = job.result()

counts = result.get_counts()

print("Measurement Counts:")
print(counts)

plot_histogram(counts)
plt.show()

print("\nExperimental Probabilities:")
for state in sorted(counts):
    print(f"{state}: {counts[state]/1024:.3f}")

print("\nTheoretical Probability for each state = 1/8 = 0.125")