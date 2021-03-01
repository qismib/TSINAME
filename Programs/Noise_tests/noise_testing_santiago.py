# Noise testing program - ibmq_santiago

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
print("Backend: ibmq_santiago")

number_of_circuits = 20
n_qubits = 5
n_cbits = n_qubits

n_test = input("\nInsert the number of the test: ")

# Number of results which are different from '1':
diff_total = 0

results_string = []



print("\n-------------------------------------------------------------")
print("\nTest number", n_test)
print("\nTest execution launched...\n")

print("Number of circuits: ", number_of_circuits)
print("\nNumber of qubits per circuit: ", n_qubits)
print("\n")
print("------------------------------------------------")


for i in range(number_of_circuits):

    qc = QuantumCircuit(n_qubits,n_cbits)
    for k in range(n_qubits):
        qc.x(k)
        qc.h(k)
        
        #X-measure:
        qc.h(k)
        qc.measure(k,k)
        #qc.h(k)
        
    #qc.draw("mpl")
    
    backend = provider.get_backend("ibmq_santiago")
    job = execute(qc, backend, shots=1, memory=True)
    result = job.result()
    list_of_results = result.get_memory()
    
    results_string.append(list_of_results[0])
 
    
    print(i, "-th circuit executed:")
    print("Results:", list_of_results)
    print("------------------------------------------------")
   


# Exporting the results in a text file:

data_file = open("santiago_noise_testing_data.txt", "a")

for i in range(number_of_circuits):  
    data_file.write(str(results_string[i]))
    
data_file.write("\n")
    
data_file.close()

# Analysis

final_string = []
n_qubits_total = number_of_circuits*n_qubits

for i in range(number_of_circuits):
    final_string = final_string + list(map(int, str(results_string[i])))

for i in range(n_qubits_total):
    if final_string[i] != 1:
        diff_total = diff_total + 1

        
print("\nNumber of results which are different from ''1'':", diff_total)
print("over a total number of qubits equal to", n_qubits_total, "= (number of circuits x number of qubit per circuit)")

prob_diff = diff_total/(n_qubits_total)*100

print("\nProbability =", prob_diff, "%")

data_file = open("santiago_noise_tests.txt", "a")

data_file.write("-------------------------------------------------------------------------------")
data_file.write("\nTEST NUMBER ")
data_file.write(str(n_test))
data_file.write("\n\n")
data_file.write("Number of circuits: ")
data_file.write(str(number_of_circuits))
data_file.write("\n")
data_file.write("Number of qubits per circuit: ")
data_file.write(str(n_qubits))
data_file.write("\n")
data_file.write("Total number of qubits: ")
data_file.write(str(n_qubits_total))
data_file.write("\n")
data_file.write("Number of results which are different from ''1'': ")
data_file.write(str(diff_total))
data_file.write("\n")
data_file.write("Probability: ")
data_file.write(str(prob_diff))
data_file.write(" %\n\n")


    
data_file.close()

plt.show()


