from qiskit import QuantumCircuit 
from qiskit.quantum_info import Statevector 
from qiskit.visualization import plot_bloch_multivector 
import matplotlib.pyplot as plt 

qc = QuantumCircuit(1) 
qc.h(0) 
qc.z(0) 

state = Statevector.from_instruction(qc) 

print(qc.draw()) 
plot_bloch_multivector(state) 
plt.show() 