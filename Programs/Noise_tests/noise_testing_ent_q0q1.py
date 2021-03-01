# Noise testing program - ibmq_5_yorktown - Entangled qubits: q0 and q1

# Importing standard Qiskit libraries and configuring account
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, execute, Aer, IBMQ
from qiskit.compiler import transpile, assemble
from qiskit.tools.jupyter import *
from qiskit.visualization import plot_bloch_multivector, plot_histogram
from qiskit.extensions import Initialize
from math import sqrt, pi
import numpy as np
import matplotlib.pyplot as plt
from random import *
		
# Loading your IBM Q account(s)

provider = IBMQ.load_account() 

   
# ---------------------------------- MAIN PROGRAM ------------------------------------------

print("\n\n-------------------------------------------------------------")
print("Backend: ibmq_5_yorktown")

number_of_circuits = 100
n_qubits = 2
n_cbits = n_qubits

n_test = input("\nInsert the number of the test: ")

# Number of different results:
diff_total = 0

results_string = []

#backend = provider.get_backend("ibmq_vigo")

print("\n-------------------------------------------------------------")
print("\nTest number", n_test)
print("\nTest execution launched...\n")

print("Number of circuits: ", number_of_circuits)
print("\nNumber of qubits per circuit: ", n_qubits)
print("\n")
print("------------------------------------------------")


for i in range(number_of_circuits):

    qc = QuantumCircuit(n_qubits,n_cbits)
    
    qc.h(0)
    qc.cx(0,1)
    
    for k in range(n_qubits):
        qc.measure(k,k)
        
    #qc.draw("mpl")
    
    backend = provider.get_backend("ibmq_5_yorktown")
    job = execute(qc, backend, shots=1, memory=True)
    result = job.result()
    list_of_results = result.get_memory()
        
    # Exporting the results in a text file:
    data_file = open("ent_noise_tests_raw_data.txt", "a")
    
    separated_results = list(map(int, str(list_of_results[0])))      # Permette di dividere l'elemento 0 della stringa
                                                                     # dei risultati nei singoli numeri. Ad esempio,
                                                                     # 10011 viene mappato in [1, 0, 0, 1, 1] (notare che map() richiede
                                                                     # sempre di essere usato in list() oppure set())
  
    """  
    print("str", str(list_of_results[0]))
    print("map", map(int, str(list_of_results[0])))
    print("list", list(map(int, str(list_of_results[0]))))
    """
    
    for j in range(n_qubits):
        data_file.write(str(separated_results[j]))
        data_file.write("\t")
    
    data_file.write("\n")
    
    print(i, "-th circuit executed:")
    print("Results:", list_of_results)
    print("------------------------------------------------")
   
data_file.close()


data_file = open("ent_noise_tests_raw_data.txt", "r")

lines = data_file.readlines()

# Lists of a specific qubit's results:
qubit0 = []
qubit1 = []
qubit2 = []
qubit3 = []
qubit4 = []

# Counts:
count_same = 0
count_diff = 0

for x in lines:
    qubit0.append(x.split()[0])    # split() permette di considerare le diverse colonne (non legge gli spazi)
    qubit1.append(x.split()[1])
    #qubit2.append(x.split()[2])
    #qubit3.append(x.split()[3])
    #qubit4.append(x.split()[4])

for i in range(len(qubit0)):                 # Confronto i risultati dei due qubit entangled: in 
                                             # linea di principio, dovrebbero essere gli stessi. Conto quanti sono
                                             # i risultati identici e quanti quelli diversi.
    if qubit0[i] == qubit1[i]:
        count_same = count_same + 1
    else:
        count_diff = count_diff + 1

print("\nSame results:", count_same)    
print("Different results:", count_diff)

data_file = open("ent_noise_tests.txt", "a")

n_qubits_total = number_of_circuits*n_qubits

data_file.write("-------------------------------------------------------------------------------")
data_file.write("ibmq_5_yorktown")
data_file.write("\nTEST NUMBER ")
data_file.write(str(n_test))
data_file.write("\n\n")
data_file.write("Entangled qubits: q0 q1")
data_file.write("\n")
data_file.write("Number of circuits: ")
data_file.write(str(number_of_circuits))
data_file.write("\n")
data_file.write("Number of qubits per circuit: ")
data_file.write(str(n_qubits))
data_file.write("\n")
data_file.write("Total number of qubits: ")
data_file.write(str(n_qubits_total))
data_file.write("\n")
data_file.write("Results per qubit: ")
data_file.write(str(len(qubit0)))
data_file.write("\n")
data_file.write("Same results count: ")
data_file.write(str(count_same))
data_file.write("\n")
data_file.write("Different results count: ")
data_file.write(str(count_diff))
data_file.write("\n")
    
data_file.close()

plt.show()


