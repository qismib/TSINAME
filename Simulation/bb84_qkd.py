# Implementation of the QKD BB84 protocol

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
		

# DEFINITIONS

# Implementation of the measurement in the {|+>, |->} basis: HZH = X

def x_measure (quantumcircuit, qubit, cbit):	
    quantumcircuit.h(qubit)
    quantumcircuit.measure(qubit, cbit)
    quantumcircuit.h(qubit)
    return quantumcircuit
    
# Implementation of a function which builds up a single qubit circuit based on Alice's strings
 
def encoding_circuit_builder (alice_bits, alice_basis, nth_qubit):   

    i = nth_qubit	# the n-th bit which Alice wants to encode
    
    encoding_circuit = QuantumCircuit(1,1)
        
    if alice_bits[i] == 0 and alice_basis[i] == 0: 
        # Alice chooses {|0>, |1>} basis
        pass # Apply I (nothing happens)
        
    if alice_bits[i] == 1 and alice_basis[i] == 0: 
        # Alice chooses {|0>, |1>} basis
        encoding_circuit.x(0) # Apply X-Gate (flip |0> to |1>)
       
    if alice_bits[i] == 0 and alice_basis[i] == 1: 
        # Alice chooses {|+>, |->} basis
        encoding_circuit.h(0) # Apply H-Gate (change |0> to |+>)
       
    if alice_bits[i] == 1 and alice_basis[i] == 1: 
        # Alice chooses {|+>, |->} basis
        encoding_circuit.x(0)
        encoding_circuit.h(0) # Apply X-Gate and H-Gate (so |0> goes in |->) 
            
    encoding_circuit.barrier()
           
    return encoding_circuit


# Implementation of the function with which Bob measures Alice's qubit
      
def circuit_measure (encoding_circuit, bob_basis, bob_measures, nth_qubit):	
    
    i = nth_qubit	# the n-th qubit sent by Alice
    
    if bob_basis[i] == 0: # Bob chooses {|0>, |1>} basis
        # Measurement with the default {|0>, |1>} basis
        encoding_circuit.measure(0,0) 
            
        #encoding_circuit.draw("mpl")

# Now we run the circuit ONLY ONE TIME, 
# and memorize the result in the bob_measures list.

        backend = Aer.get_backend("qasm_simulator")
        job = execute(encoding_circuit, backend, shots=1, memory=True)
        result = job.result()
        list_of_results = result.get_memory()
        bob_measures.append(list_of_results[0])
        
    if bob_basis[i] == 1: # Bob chooses {|+>, |->} basis
        # Measurement with the {|+>, |->} basis
        x_measure(encoding_circuit, 0, 0)
            
        #encoding_circuit.draw("mpl")

# Now we run the circuit ONLY ONE TIME, 
# and memorize the result in the bob_measures list.

        backend = Aer.get_backend("qasm_simulator")
        job = execute(encoding_circuit, backend, shots=1, memory=True)
        result = job.result()
        list_of_results = result.get_memory()
        bob_measures.append(list_of_results[0])

            
def eve_hacking_measures (hacker_activated, encoding_circuit, eve_measures, nth_qubit):

    if hacker_activated == True:
    
# Eve measures the n-th qubit sent by Alice. After that, Eve sends it to Bob:

        i = nth_qubit	# the n-th qubit sent by Alice
   
        if eve_basis[i] == 0: # Eve chooses {|0>, |1>} basis
           # Measurement with the default {|0>, |1>} basis
            encoding_circuit.measure(0,0) # 

            backend = Aer.get_backend("qasm_simulator")
            job = execute(encoding_circuit, backend, shots=1, memory=True)
            result = job.result()
            list_of_results = result.get_memory()
            eve_measures.append(list_of_results[0])
        
        if eve_basis[i] == 1: # Eve chooses {|+>, |->} basis
            # Measurement with the {|+>, |->} basis
            x_measure(encoding_circuit, 0, 0) 

            backend = Aer.get_backend("qasm_simulator")
            job = execute(encoding_circuit, backend, shots=1, memory=True)
            result = job.result()
            list_of_results = result.get_memory()
            eve_measures.append(list_of_results[0])

        return encoding_circuit

    else: 
        pass


def eve_hacking_entangle (hacker_activated, encoding_circuit):

    if hacker_activated == True:
    
# Eve ENTANGLES the n-th qubit sent by Alice with a |0> state qubit. 
# After that, Eve sends the entangled qubit to Bob:
   
        eve_q = QuantumRegister(1, "eve_qubit")
        encoding_circuit.add_register(eve_q)
        
        encoding_circuit.cx(0, eve_q[0])
        encoding_circuit.barrier()
    
       #encoding_circuit.draw("mpl")
    
    return encoding_circuit
    
def eve_entangled_measurement (hacker_activated, encoding_circuit, eve_measures):

    if hacker_activated == True:
    
# Eve measures all her entangled qubits in the {|0>, |1>} basis:
        
        eve_c = ClassicalRegister(1, "eve_cbit")
        encoding_circuit.add_register(eve_c)
        
        encoding_circuit.barrier()

        encoding_circuit.measure(1,1)
        
       #encoding_circuit.draw("mpl")
    
        backend = Aer.get_backend("qasm_simulator")
        job = execute(encoding_circuit, backend, shots=1, memory=True)
        result = job.result()
        list_of_results = result.get_memory()
        eve_measures.append(list_of_results[0])
   
   
   
   
# ---------------------------------- MAIN PROGRAM ------------------------------------------

# Number of bits (and then qubits) that Alice is going to use:
number_of_qubits = 10000 

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


# For each classical bit which Alice wants to encode and transmit to Bob, they proceed as it follows:

bob_measures = []
eve_measures = []

for n in range(number_of_qubits):

# Alice codes the n-th bit of her initial string as a qubit and sends it to Bob
    qubit = encoding_circuit_builder(alice_bits, alice_basis, n)
    
# Bob measures the qubit with his own basis: but what if Eve is hacking the message?
    eve_hacking_measures (hacker_activated1, qubit, eve_measures, n)
    eve_hacking_entangle (hacker_activated2, qubit)
    circuit_measure (qubit, bob_basis, bob_measures, n)
    eve_entangled_measurement (hacker_activated2, qubit, eve_measures)
    
# Let's see the results of the measurements!

print("\nBob's measurements (first 20 measurements):\n")
print(bob_measures[0:19])

if hacker_activated1 == True or hacker_activated2 == True:
    print("\nEve's measurements (first 20 measurements):\n")
    print(eve_measures[0:19])
    
# Now we export the results in a text file:

data_file = open("bb84_data.txt", "w")

for i in range(number_of_qubits):  
    data_file.write(str(alice_bits[i]))
    data_file.write("\t") 
    data_file.write(str(alice_basis[i]))
    data_file.write("\t")
    data_file.write(str(bob_basis[i]))
    data_file.write("\t")
    data_file.write(str(bob_measures[i]))
    data_file.write("\n")
    
data_file.close()

plt.show()


