# TSINAME

### BB84 - Three Scenarios Implementation - No Attack, Measurement-based attack, Entanglement-based attack

## Overview


*Quantum cryptography* falls into the scope of computer data security, and this thesis project is
focused on it. In particular, the **BB84 protocol** is studied in the thesis. Proposed by **C. H. Bennett**
and **G. Brassard** in **1984**, it is the *first protocol devised to allow the exchange of cryptographic keys*
*through the use of Quantum Computing*.
This protocol consists of the **transmission of qubits** which have been initially prepared in four
possible different physical states, related to the vector states which are described by two bases which
are orthonormal to each other. For example, considering a qubit obtained by the *polarization of a*
*photon*, one of these two bases can be given by the two states vertical polarization and horizontal
polarization of the photon; then, the basis which is orthonormal to that basis could be a couple of
states with a transverse or intermediate polarization. An *operator* is associated to each basis, whose
states are *eigenstates of that operator*. For example, the states of the first basis are eigenstates of the
generic operator *A*, while the states of the second are eigenstates of the generic operator *B*.
The choice to prepare a qubit in a certain state is carried out in a random way, with a uniform prob-
ability associated to each of the four possible states. The qubits are then sent to a recipient, who
executes on each qubit a measurement of the operator *A* or of the operator *B*, by operating the choice
of the operator to use randomly.
In order to carry out these choices, **three random bit strings are extracted**. One of them will be the
string of the bits which will be encoded (namely the bits which will make up the criptographic key);
a string will be needed by the sender to choose the eigentates basis with which he will prepare the
qubit related to a certain encoded bit, while the other string will be needed by the recipient to choose
the operator with which he will measure the qubit. Each measurement returns a result, which can
correspond to the two possible values of a bit: **0 or 1**.
At the end of the transmission, the sender and the recipient **publish the strings related to the choice**
**of the eigenstates basis and of the measurement’s operator. Also, the sender publishes the first half of**
**the encoded bits, and the recipient publishes the first half of his results**.
Then, an analysis of the firs half of the collected data is carried out, comparing the measurement’s results 
of the recipient with the encoded bits of the sender. They count how many times the recipient
obtains the same value of the respective bit encoded by the sender, in the only case in which the sender
would have prepared the qubit in an eigenstate of the operator chosen by the recipient in order to do
the measurement. In this case, the encoded bit and the corresponding result bit are called *correlated*
*bits*.
The a posteriori analysis of the results allows to verify the safety of the transmission and to obtain
a cryptographic key, shared only by the sender and by the recipient. In case of ideal transmission
(without noise), indeed, the measurements’ results should be always equal to the related encoded bits:
so **the presence of different results would signify that the key has been intercepted by a hacker**, and
then the protocol must be interrupted.

The thesis discusses the theory behind the protocol and, basing on simple considerations about the
probabilities which came into play, the theoretical results expected from the a posteriori data analysis
are computed. The intervention of a possibile hacker is introduced throughout the implementation of
**two possible types of attack**: one based on a **direct measurement of the qubits**, and the other based
on the **creation of entangled states** with the transmitted qubits. Thanks to the analysis of the data
which have been collected by the recipient, it is proven that neither of these two attacks can succeed,
and that the protocol is **completely safe from any intrusion attempts** performed by an external agent
of this type. Each hacking attempt, indeed, causes the change of the state of some of the transmitted
qubits; as an observable consequence, after the data analysis, the **percentage of different results** is
equal to the **25% of the correlated bits**.
The protocol is implemented by writing a Python program which exploits *Qiskit*, an open-source
framework developed by **IBM**, which allows to write code for Quantum Computing.
Then a **simulation** of the code is carried out, in order to prove the correct functioning and to verify
the accuracy of the results expected from the data analysis. Finally, the **experiment on real quantum**
**computers** is executed. **Preliminary tests** are launched to determine a good choice of the devices which
have been made available by IBM, and to choose the optimal configuration of the quantum circuit
related to each execution. These tests shows the trend of the error on the measurements, varying the
number of qubits in parallel in each circuit, in relation to the different considered devices. Once the
device’s choice has been made, the experiment and the data analysis of the results are performed,
taking into account the noise introduced by the device. That noise is identified with the percentage
of different results in case of hacker’s absence (namely, in the case in which, if the device was ideal,
this percentage would be 0%).

As expected, *in case of hacker’s attack there is an increase of the different results’ percentage, which*
*exceeds the noise threshold in hacker’s absence*; in particular, the percentage of correlated bits which
are different is approximately equal to 25% plus the percentage associated with the noise.

## Characters


* Alice: she is the **sender**. She wants to share with Bob a cryptographic key.
* Bob: he is the **recipient**. He receives the qubits sent by Alice.
* Eve: she is the **hacker**. She wants to stole the cryptograpic key shared by Alice and Bob.


## Project

In this thesis, the BB84 protocol has been implemented by writing a Python code based on *Qiskit*.
Qiskit is an open-source framework which allows you to interface with quantum computers provided by IBM.
*IBM Quantum Experience* is a cloud platform by which you can interact with IBM's quantum computers.

[IBM Quantum Experience](https://www.google.com/search?channel=fs&client=ubuntu&q=ibm+quantum+experience)

[Qiskit Textbook](https://qiskit.org/textbook/preface.html)


Full description of the BB84 protocol
-------------------------------------
See:
* The thesis (Italian): Docs/*Tesi_Rinaldi_826346*
* The slides (Italian / English): Docs/Slides
* The schemes (Italian): Docs/Schemi

## Programs

Notice: you may adjust some commands in the code, in order to obtain the correct graphics (for example) or to perform the right experiment.

### a) Simulation: Programs/Simulation/runner.py

The program runs a simulation of the protocol. In runtime, you can choose 3 options:
1. Simulation without hacker's attack;
2. Simulation with an attack which is based on direct measurement of the transmitted qubits;
3. Simulation with an attack based on the Entanglement between qubit in the |0> state and the trasmitted qubits.

Finally a data analysis is automatically performed. You will obtain some graphics related to the analysis.

### b) Noise testing programs: Programs/Noise_tests

* noise_testing_santiago.py --> In order to evaluate if the noise depends on the number of qubits in parallel.
* noise_testing_ent_q0q1.py --> In order to evaluate the noise with respect to the couples of entangled qubits.

### c) Plots of the noise tests: Programs/Plots

There are two programs, one for the tests without Entanglement (noise_plots.py), 
the other for the tests with Entanglement (noise_plots_entanglement.py).
They build up some histograms with values which you have to insert.

### d) Experiment on quantum computer: Programs/Experiment/bb84_qkd_realdevice.py

With this program, you can run the BB84 protocol on a IBM quantum computer.

Make sure:
* to set up the correct backend name (for example, *ibmq_santiago*)
* to uncomment/comment out the correct part of the code in order to perform the experiment (for example, *Scenario 1-2* or *Scenario 3*: one of them must always be commented out, and the other must always be uncommented).

### e) Data analysis related to the experiment - Programs/Data_analysis/daan.py

You have to set the input name of the data file. Then the program will build up the graphics of the experiment.

## Graphics

In the directory Graphics/ you can find the main plots of the thesis.

Usually:
1. **Figure 1** shows the percentage of the same basis or different basis choice;
2. **Figure 2** shows the percentage of identical or different correlated bits;
3. **Figure 3** shows the percentage of identical or different correlated bits, distinguishing between the values of the results and referring to the **{|0>, |1>} basis** choice;
4. **Figure 4** is the same of Figure 3, but referring to the **{|+>, |->} basis** choice.

However:

* **Simulation**: sim_s1_fig1.pdf means *graphic of the simulation, Scenario 1, Figure 1*.
* **Noise**: noise_test_0.pdf and noise_test_1.pdf are the plots of the noise in case of Scenario 1-2, the other are the plots in case of Scenario 3.
* **Experiment**: exp_s1_santiago_fig1.pdf means *graphic of the experiment, Scenario 1, used device (backend name), Figure 1*.
* **Definitive_slide_experiment_graphics**: these are the graphics inserted in the slides.
