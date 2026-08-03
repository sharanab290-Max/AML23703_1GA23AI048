from qiskit import QuantumCircuit 
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_vector 
import matplotlib.pyplot as plt 
qc = QuantumCircuit(1) 
qc.y(0) 
state = Statevector.from_instruction(qc) 
print("Statevector:", state.data) 
print(qc.draw()) 


plot_bloch_vector([0, 0, -1], title="Y Gate on |0>") 
plt.show() 
