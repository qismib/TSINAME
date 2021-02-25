# Implementation of the QKD BB84 protocol - Experiment on a real device: ibmq_yorktown

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


# DEFINITIONS

# Implementation of the measurement in the {|+>, |->} basis: HZH = X

def x_measure (quantumcircuit, qubit, cbit):	
    quantumcircuit.h(qubit)
    quantumcircuit.measure(qubit, cbit)

    return quantumcircuit
  
# Notice: in x_measure (Bob's measurements), we DO NOT apply the final H-Gate.
#         We apply H-Gate only in the function x_measure_eve (Eve's measurement).
#         That's because in the experiment we MUST END THE CIRCUIT WITH A MEASUREMENT
#         (not with a gate).
    
def x_measure_eve (quantumcircuit, qubit, cbit):	
    quantumcircuit.h(qubit)
    quantumcircuit.measure(qubit, cbit)
    quantumcircuit.h(qubit)
    return quantumcircuit
    
# Implementation of a function which builds up a single qubit circuit based on Alice's strings
 
def encoding_circuit_builder (alice_bits, alice_basis, nth_circuit):   

    i = nth_circuit	# the n-th circuit which contains 5 qubits
    
    encoding_circuit = QuantumCircuit(5,5)
    
    for k in range(5):
        
        if alice_bits[5*i+k] == 0 and alice_basis[5*i+k] == 0: 
            # Alice chooses {|0>, |1>} basis
            pass # Apply I (nothing happens)
        
        if alice_bits[5*i+k] == 1 and alice_basis[5*i+k] == 0: 
            # Alice chooses {|0>, |1>} basis
            encoding_circuit.x(k) # Apply X-Gate (flip |0> to |1>)
       
        if alice_bits[5*i+k] == 0 and alice_basis[5*i+k] == 1: 
            # Alice chooses {|+>, |->} basis
            encoding_circuit.h(k) # Apply H-Gate (change |0> to |+>)
       
        if alice_bits[5*i+k] == 1 and alice_basis[5*i+k] == 1: 
            # Alice chooses {|+>, |->} basis
            encoding_circuit.x(k)
            encoding_circuit.h(k) # Apply X-Gate and H-Gate (so |0> goes in |->) 
            
    encoding_circuit.barrier()
           
    return encoding_circuit


# Implementation of the function with which Bob measures Alice's qubit
      
def circuit_measure (backend_name, encoding_circuit, bob_basis, nth_circuit):	
  
    i = nth_circuit
    
    list_of_results = []
    inverted_list = []
    
    definitive_results = []
    
    for k in range(5):

        if bob_basis[5*i + k] == 0: # Bob chooses {|0>, |1>} basis
            # Measurement with the default {|0>, |1>} basis
            encoding_circuit.measure(k,k)
                    
        if bob_basis[5*i + k] == 1: # Bob chooses {|+>, |->} basis
            # Measurement with the {|+>, |->} basis
            x_measure(encoding_circuit, k, k)
     
    backend = provider.get_backend(backend_name)
    job = execute(encoding_circuit, backend, shots=1, memory=True)
    result = job.result()
    list_of_results = result.get_memory()
            
    list_of_results = list(map(int, str(list_of_results[0]))) 
    # But these results are ordered backwards!
    # Their order must be inverted!
    
    for k in range(5):
        inverted_list.append(list_of_results[4-k])
  
    
    # Scenario 1-2:
    definitive_results = inverted_list
    """
    
    # Scenario 3:   
    
    # We have to consider ONLY qubits q3, which has been entangled with q4  
    definitive_results.append(inverted_list[3])
    """
    """
    encoding_circuit.draw("mpl")
    print("\nlist_of_results:", list_of_results)
    print("inverted_list:", inverted_list)
    print("definitive_results:", definitive_results)
    """
    
    return definitive_results       


            
def eve_hacking_measures (hacker_activated, encoding_circuit, alice_basis, nth_circuit):

    if hacker_activated == True:
    
# Eve measures each qubit sent by Alice. After that, Eve sends it to Bob:

        i = nth_circuit
   
        for k in range(5):
   
            if eve_basis[5*i+k] == 0: # Eve chooses {|0>, |1>} basis
               # Measurement with the default {|0>, |1>} basis
                if alice_basis[5*i+k] == 0:
                    encoding_circuit.z(k) # --> ''right'' choice --> the state remains the same
                if alice_basis[5*i+k] == 1:
                    encoding_circuit.h(k) # --> ''wrong'' choice --> change basis
        
            if eve_basis[5*i+k] == 1: # Eve chooses {|+>, |->} basis
                # Measurement with the {|+>, |->} basis
                if alice_basis[5*i+k] == 1:
                    encoding_circuit.x(k) # --> ''right'' choice --> the state remains the same
                if alice_basis[5*i+k] == 0:
                    encoding_circuit.h(k) # --> ''wrong'' choice --> change basis

        encoding_circuit.barrier()

        return encoding_circuit

    else: 
        pass


def eve_hacking_entangle (hacker_activated, encoding_circuit):

    if hacker_activated == True:
    
# Eve ENTANGLES qubits q0 and q3 sent by Alice with |0> state qubits (q2 and q4). 
# After that, Eve sends the entangled qubit to Bob:

        encoding_circuit.cx(3, 4)
        encoding_circuit.barrier()
    
       #encoding_circuit.draw("mpl")
    
    return encoding_circuit
   
   
   
# ---------------------------------- MAIN PROGRAM ------------------------------------------

# Number of qubits that Alice is going to use:

number_of_circuits = 2
number_of_qubits = 5 * number_of_circuits

# Backend:

backend_name = "ibmq_5_yorktown"

# Alice generates n random bits (some of these bits will form the key)

alice_bits = []
for i in range (number_of_qubits):
    alice_bits.append(randint(0,1))

print("\nAlice's bits (first 20 bits):\n", alice_bits[0:19])

# Alice randomly chooses the bases in which she is going to measure

alice_basis = []
for i in range (number_of_qubits):
    alice_basis.append(randint(0,1))
print("\nAlice's basis (first 20 bits):\n", alice_basis[0:19])

# Bob also randomly chooses the bases in which he is going to measure

bob_basis = []
for i in range (number_of_qubits):
    bob_basis.append(randint(0,1))
print("\nBob's basis (first 20 bits):\n", bob_basis[0:19])

print("\nChoose an option [digit 1, 2 or 3]:\n\n1. Transmission without hacker's attack" \
    "\n2. Transmission with a measurement-based hacker's attack" \
    "\n3. Transmission with an Entanglement-based hacker's attack\n")
scelta = input()

if scelta == "1":
    hacker_activated1 = False
    hacker_activated2 = False
if scelta == "2":
    hacker_activated1 = True
    hacker_activated2 = False
if scelta == "3":
    hacker_activated1 = False
    hacker_activated2 = True
if scelta != "1" and scelta != "2" and scelta != "3":
    print("\nTry again (digit only 1, 2 or 3)")   
    
# Eve randomly chooses the bases in which she is going to measure (like Bob)
if hacker_activated1 == True:
    eve_basis = []
    for i in range (number_of_qubits):
        eve_basis.append(randint(0,1))
    print("\nEve's basis (first 20 bits):\n", eve_basis[0:19]) 

print("-----------------------------------------------------------------------")

print("\nThe experiment has been launched!\n")
print("Backend:", backend_name)
print("Number of circuits:", number_of_circuits)
print("Number of qubits per circuit:", 5)
print("Total number of qubits:", number_of_qubits)

print("\n\n-----------------------------------------------------------------------") 

# For each classical bit which Alice wants to encode and transmit to Bob, they proceed as it follows:

bob_measures = []

for n in range(number_of_circuits):

# Alice codes the (5*n+k)-th bit of her initial string as a qubit.
# Then she builds up the n-th circuit with 5 of these qubits, and sends it to Bob
    circuit = encoding_circuit_builder(alice_bits, alice_basis, n)
    
# Bob measures the qubit with his own basis: but what if Eve is hacking the message?
    eve_hacking_measures (hacker_activated1, circuit, alice_basis, n)
    eve_hacking_entangle (hacker_activated2, circuit)
    new_results = circuit_measure (backend_name, circuit, bob_basis, n)
    bob_measures = bob_measures + new_results

    counter = 0 # Little check, in order to be sure that the datas have been saved

# For each job, we immediately register the result in the data file:
    data_file = open("bb84_yorktown_scenario1_data.txt", "a")


# Scenario 1-2:
    
    for k in range(5):
        data_file.write(str(alice_bits[5*n+k]))
        data_file.write("\t") 
        data_file.write(str(alice_basis[5*n+k]))
        data_file.write("\t")
        data_file.write(str(bob_basis[5*n+k]))
        data_file.write("\t")
        data_file.write(str(bob_measures[5*n+k]))
        data_file.write("\n")
        counter = counter + 1
    """

# Scenario 3: again, we must consider only qubit q3

    data_file.write(str(alice_bits[5*n+3]))
    data_file.write("\t") 
    data_file.write(str(alice_basis[5*n+3]))
    data_file.write("\t")
    data_file.write(str(bob_basis[5*n+3]))
    data_file.write("\t")
    data_file.write(str(bob_measures[n]))    # Because we have only 1 result per circuit        
    data_file.write("\n")        
    counter = counter + 1
    """         
    data_file.close()
    
    print(n, "-th job")
    print("Results:", new_results)
    if scelta == 1 or scelta == 2:
        if counter == 5:
            print("Datas have been correctly saved")
        else:
            print("DATA WERE NOT CORRECTLY SAVED!!")
            
    if scelta == 3:
        if counter == 1:
            print("Datas have been correctly saved")
        else:
            print("DATA WERE NOT CORRECTLY SAVED!!")
        
    print("-----------------------------------------------------------------------")
    

# Let's see the first 20 results of the measurements!

print("\nBob's measurements (first 20 measurements):\n")
print(bob_measures[0:19])

print("\nThe experiment ended with success!")

plt.show()


