# Data analysis associated to the program bb84_qkd.py

# Importing standard Qiskit libraries and configuring account
from qiskit import QuantumCircuit, execute, Aer, IBMQ
from qiskit.compiler import transpile, assemble
from qiskit.tools.jupyter import *
from qiskit.visualization import plot_bloch_multivector, plot_histogram
from qiskit.extensions import Initialize
from math import sqrt, pi
import numpy as np
import matplotlib.pyplot as plt
from random import *


# DEFINITIONS

def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., height + 1, '%f' % height + " %", ha='center', va='bottom')	
        
        # '%f' % height + " %" means that I am substituting ''height + " %"'' 
        # in the string which is passed as argument of the function 
        # (height is passed as a float (--> '%f'), ''%'' as a string character)


# ---------------------------------- MAIN PROGRAM ------------------------------------------

print("\nDATA ANALYSIS associated to the program ''bb84_qkd.py''")

# Reading of the data file

data_file = open("bb84_data.txt", "r")
content = data_file.read()	# It reads the data file and stores all the characters in a list called ''content''

number_of_characters = len(content)

alice_bits = []
alice_basis = []
bob_basis = []
bob_measures = []

for i in range(0, number_of_characters, 8):	# where range(start, stop, step)

    alice_bits.append(content[i])	# content[i] = i-th element of the first column
    alice_basis.append(content[i+2])	# content[i+2] = i-th element of the second column
    bob_basis.append(content[i+4])	# content[1+4] = i-th element of the third column   
    bob_measures.append(content[i+6])	# content[1+6] = i-th element of the fourth column   
                                       # ---> that's because we have to ignore \n and \t characters 
    
data_file.close()

# Let's do a little safety test; all the strings must have the same length, and contain only the symbols 0 or 1

if len(alice_bits) != len(alice_basis) or len(alice_basis) != len(bob_basis) or len(bob_basis) != len(bob_measures):
    print("\nAttention! The bit strings have not the same length!!\n")
    exit()
else:
    print("\nBit strings length:", len(alice_bits))   
    
for i in range(len(alice_basis)):
    if (alice_bits[i] != "0" and alice_bits[i] != "1") or (alice_basis[i] != "0" and alice_basis[i] != "1") \
    or (bob_basis[i] != "0" and bob_basis[i] != "1") or (bob_measures[i] != "0" and bob_measures[i] != "1"):
    
        print("\nAttention! The strings contain values which are different from ''0'' or ''1''!!!\n")
        exit()
 
# Alice and Bob publish their basis' strings and compare them: then they select only the measures which had been operated WITH THE SAME CHOICE OF BASIS

strings_length = len(alice_basis)

correlated_bits = []		# We are defining 3 new lists: the first (correlated_bits) will contain 
                               # the original Alice's bits associated with the elements of the second list;
                               
correlated_basis = []		# the second (correlated_basis) will contain the value of the bits
                               # associated with the same choice of basis, 
                               
correlated_measurements = []	# and the third (correlated_measurements) will contain the relative measurements 

# NOTICE: same_basis_measure represents the KEY which is now in common between Alice and Bob!

for i in range(strings_length):
    if alice_basis[i] == bob_basis[i]:
        correlated_bits.append(alice_bits[i])
        correlated_basis.append(bob_basis[i])
        correlated_measurements.append(bob_measures[i])

"""
print(correlated_bits)
print(correlated_basis)
print(correlated_measurements)
"""

# --------------------------------------------------------- STATISTICS      
  
# 1. The probability of having chosen the same basis

correlated_bits_number = len(correlated_measurements)

corr_prob = correlated_bits_number/strings_length
uncorr_prob = 1 - correlated_bits_number/strings_length

print("\n------------------------------------------------------------------------------------------------------------------") 
print("\n1. Correlation between Alice's and Bob's bases")
print("\n------------------------------------------------------------------------------------------------------------------") 
print("\nTotal number of qubits: ", strings_length)
print("\nNumber of qubits which have been encoded and measured with:")
print("a) the same basis:", correlated_bits_number)
print("b) different bases:", strings_length - correlated_bits_number)
print("\nProbability of having chosen the same basis: ", corr_prob*100, "%")
print("Probability of having chosen a different basis: ", uncorr_prob*100, "%")

fig, ax = plt.subplots(figsize=(8, 6))  # Create the figure
ax.set_title("Probability of having measured the qubits in the same basis (or not)")
ax.set_ylabel("Probability (%)")
rectangle1 = ax.bar([0,1], height=[corr_prob*100, uncorr_prob*100], tick_label=["Same basis", "Different basis"], \
             color=["c", (1, 0.5, 0)]) # (1, 0.5, 0) is the RGB code for color orange
plt.axis([None, None , 0, 110])

autolabel(rectangle1)

# 2. Evaluating Hacking Eve's presence ---> Alice and Bob publish the first half of the measures' results

identical_results = 0	# Counters: they count how many times the measurements 
                       # of the ''same basis qubits'' are identical to the original Alice's bits,
different_results = 0	# and how many times they are not.

for i in range(int(correlated_bits_number/2)):
    if correlated_bits[i] == correlated_measurements[i]:
        identical_results += 1
    else:
        different_results += 1
                
prob_identical = identical_results / int(correlated_bits_number/2)
prob_different = different_results / int(correlated_bits_number/2)

rate = different_results / identical_results

print("\n------------------------------------------------------------------------------------------------------------------") 
print("\n2. Let's consider the qubits which have been encoded and measured with the same basis,")
print("and, from these, let's select the first half of the corresponding Alice's original bits")
print("and the corresponding results of Bob's measurements.")
print("\n------------------------------------------------------------------------------------------------------------------") 
print("\nNumber of bits which have been taken into account: ", int(correlated_bits_number/2))
print("\nNumber of Bob's measurements which are:") 
print("a) identical to the original Alice's bits: ", identical_results) 
print("b) different from the original Alice's bits: ", different_results) 
print("\nProbability of obtaining measurements which are:")
print("a) Identical to the original Alice's bits: ", prob_identical*100, "%")
print("b) Different from the original Alice's bits: ", prob_different*100, "%")

print("\nRatio between different and identical results:\n(Different results) / (Identical results) =", rate)

print("\nExample: considering the ''same-basis'' bits, let's see the first 20:")
print("Alice's first 20 original bits:", correlated_bits[0:19])
print("Bob's first 20 measurements:   ", correlated_measurements[0:19])


fig, ax = plt.subplots(figsize=(8, 6))  # Create the figure
ax.set_title("Probability of obtaining Bob's measurements identical\nto Alice's original bits (considering ''same-basis'' bits)")
ax.set_ylabel("Probability (%)")
rectangle2 = ax.bar([0,1], height=[prob_identical*100, prob_different*100], tick_label=["Identical", "Different"], color=["b", "r"]) 
plt.axis([None, None , 0, 110])

autolabel(rectangle2)



# 3. Bob's statistics, relative to the first half of the ''same-basis'' bits

basis_0_results_0_ide = 0	# Counts how many ''0'' Bob measured in the ''0'' basis
basis_0_results_1_ide = 0	# Counts how many ''1'' Bob measured in the ''0'' basis
basis_1_results_0_ide = 0	# Counts how many ''0'' Bob measured in the ''1'' basis
basis_1_results_1_ide = 0	# Counts how many ''0'' Bob measured in the ''1'' basis	
                               # ---> Measurements which are identical to the original Alice's bits

basis_0_results_0_diff = 0	# Counts how many ''0'' Bob measured in the ''0'' basis
basis_0_results_1_diff = 0	# Counts how many ''1'' Bob measured in the ''0'' basis
basis_1_results_0_diff = 0	# Counts how many ''0'' Bob measured in the ''1'' basis
basis_1_results_1_diff = 0	# Counts how many ''0'' Bob measured in the ''1'' basis	
                               # ---> Measurements which are different from the original Alice's bits

for i in range(int(correlated_bits_number/2)):  # NOTICE: we consider only the CORRELATED bits (the others must be thrown away)

    if correlated_bits[i] == correlated_measurements[i]:
       if correlated_basis[i] == "0":
           if correlated_measurements[i] == "0":
               basis_0_results_0_ide += 1
           if correlated_measurements[i] == "1":
               basis_0_results_1_ide += 1
       if correlated_basis[i] == "1":
           if correlated_measurements[i] == "0":
               basis_1_results_0_ide += 1
           if correlated_measurements[i] == "1":
               basis_1_results_1_ide += 1
    else:
       if correlated_basis[i] == "0":
           if correlated_measurements[i] == "0":
               basis_0_results_0_diff += 1
           if correlated_measurements[i] == "1":
               basis_0_results_1_diff += 1
       if correlated_basis[i] == "1":
           if correlated_measurements[i] == "0":
               basis_1_results_0_diff += 1
           if correlated_measurements[i] == "1":
               basis_1_results_1_diff += 1
           
prob_0_basis_0_ide = basis_0_results_0_ide / int(correlated_bits_number/2)	
prob_1_basis_0_ide = basis_0_results_1_ide / int(correlated_bits_number/2)		
prob_0_basis_1_ide = basis_1_results_0_ide / int(correlated_bits_number/2)		
prob_1_basis_1_ide = basis_1_results_1_ide / int(correlated_bits_number/2)	

prob_0_basis_0_diff = basis_0_results_0_diff / int(correlated_bits_number/2)		
prob_1_basis_0_diff = basis_0_results_1_diff / int(correlated_bits_number/2)		
prob_0_basis_1_diff = basis_1_results_0_diff / int(correlated_bits_number/2)		
prob_1_basis_1_diff = basis_1_results_1_diff / int(correlated_bits_number/2)		
  
print("\n------------------------------------------------------------------------------------------------------------------")        
print("\n3. Bob's statistics - only ''correlated bits'' (also called ''same-basis'' bits) will be taken into account")
print("\n------------------------------------------------------------------------------------------------------------------")      
print("\nResults which are identical to the original Alice's bits:")
print("\nMeasurements in the ''0'' basis {|0>, |1>}:\n''0'' occurred", basis_0_results_0_ide, "times with prob. =", prob_0_basis_0_ide*100, "%", \
    "\n''1'' occurred", basis_0_results_1_ide, "times with prob. =", prob_1_basis_0_ide*100, "%")
print("\nMeasurements in the ''1'' basis {|+>, |->}:\n''0'' occurred", basis_1_results_0_ide, "times with prob. =", prob_0_basis_1_ide*100, "%", \
    "\n''1'' occurred", basis_1_results_1_ide, "times with prob. =", prob_1_basis_1_ide*100, "%")
    
print("\nResults which are different from the original Alice's bits:")
print("\nMeasurements in the ''0'' basis {|0>, |1>}:\n''0'' occurred", basis_0_results_0_diff, "times with prob. =", prob_0_basis_0_diff*100, "%", \
    "\n''1'' occurred", basis_0_results_1_diff, "times with prob. =", prob_1_basis_0_diff*100, "%")
print("\nMeasurements in the ''1'' basis {|+>, |->}:\n''0'' occurred", basis_1_results_0_diff, "times with prob. =", prob_0_basis_1_diff*100, "%", \
    "\n''1'' occurred", basis_1_results_1_diff, "times with prob. =", prob_1_basis_1_diff*100, "%")


fig, ax = plt.subplots(figsize=(8, 6))
ax.set_title("Probability of the results of Bob's measurements in the {|0>, |1>} basis\n(''correlated bits'' only)\n- Results which are identical / different from original Alice's bits")
ax.set_ylabel("Probability (%)")
rectangle3 = ax.bar([0,1,2,3], height=[prob_0_basis_0_ide*100, prob_1_basis_0_ide*100, prob_0_basis_0_diff*100, prob_1_basis_0_diff*100], \
    tick_label=["0\nIdentical", "1\nIdentical", "0\nDifferent", "1\nDifferent"], color=["g", "g", "m", "m"]) 
plt.axis([None, None , 0, 110])

autolabel(rectangle3)

fig, ax = plt.subplots(figsize=(8, 6))
ax.set_title("Probability of the results of Bob's measurements in the {|+>, |->} basis\n(''correlated bits'' only)\n- Results which are identical / different from original Alice's bits")
ax.set_ylabel("Probability (%)")
rectangle4 = ax.bar([0,1,2,3], height=[prob_0_basis_1_ide*100, prob_1_basis_1_ide*100, prob_0_basis_1_diff*100, prob_1_basis_1_diff*100], \
    tick_label=["0\nIdentical", "1\nIdentical", "0\nDifferent", "1\nDifferent"], color=["g", "g", "m", "m"]) 
plt.axis([None, None , 0, 110])

autolabel(rectangle4)




# 4. Evaluating Eve's presence ---> Comparison with the threshold

threshold = 0		# We have to set a threshold in order to evaluate Eve's presence.

print("\n------------------------------------------------------------------------------------------------------------------")       
print("\n4. In order to evaluate hacker Eve's presence, let's compare the probability of obtaining different values of bits")
print("with the threshold probability we have established before.")
print("\n------------------------------------------------------------------------------------------------------------------")       
print("\nThe established threshold is: ", threshold, "%\n")

if prob_different > threshold:
    print(prob_different*100, "%  > ", threshold, "%")
    print("\n----> There might be a hacker's attack: the channel must be changed!")
    print("\nEve's meddling causes different results in Bob's measurements, in percentage:\n")
    print(prob_different*100, "% of the ''same-basis'' bits")
    print("2 x", 100*different_results/strings_length, "% =", 2*100*different_results/strings_length,  "% of the initial", strings_length, "bits extracted by Alice")
    print("\n(Notice: I multiplied by 2 because we had divided the strings by 2 to share the first half of Bob's results)")

else:
    print(prob_different*100, "%  <= ", threshold, "%")
    print("\n----> It seems that no attacks have been attempted. The channel may be considered safe.")
    print("\n------------------------------------------------------------------------------------------------------------------")      
    print("\n5. Obtaining the key")
    print("\n------------------------------------------------------------------------------------------------------------------") 
    print("\nThe key is the second half of Alice's original bits, as well as the second half of the results")
    print("of Bob's measurements (Notice: only the ''SAME-BASIS'' bits!):")
    print("\n(Alice's original bits)  ", correlated_bits[int(correlated_bits_number/2):int(correlated_bits_number/2)+19], "...")
    print("(Bob's measurements)     ", correlated_measurements[int(correlated_bits_number/2):int(correlated_bits_number/2)+19], "...")
    print("\nActual number of bits which build up the key: ", int(correlated_bits_number/2))
    print("which are", 100*int(correlated_bits_number/2)/strings_length, "% of the initial", strings_length, "bits extracted by Alice")


plt.show()
 



