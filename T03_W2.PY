from qiskit import QuantumCircuit 
from qiskit.quantum_info import Statevector 
import numpy as np 

qc = QuantumCircuit(2) 
qc.h([0, 1]) 

state = Statevector.from_instruction(qc) 

prob = np.abs(state.data) ** 2 

print("Statevector:", state.data) 
print("Probabilities:", prob) 
print("Total Probability =", prob.sum()) 
if np.isclose(prob.sum(), 1): 
    print("Normalized") 
    else: 
    print("Not Normalized") 