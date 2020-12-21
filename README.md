# TSINAME
BB84 - Three Scenarios Implementation - No Attack, Measurement-based attack, Entanglement-based attack

A) Simulation - program "bb84_qkd.py"
------------------------------------
The program runs a simulation of the protocol. In runtime, you can choose 3 options:
1. Simulation without hacker's attack;
2. Simulation with an attack which is based on direct measurement of the transmitted qubits;
3. Simulation with an attack based on the Entanglement between qubit in the |0> state and the trasmitted qubits.

Finally it creates a data file, which is the input of the program "bb84_data_analysis.py".

B) Data analysis - program "bb84_data_analysis.py"
-------------------------------------------------
The program reads the datas contained in the output file of the "bb84_qkd" program, and performs the data analysis.

C) Slides
---------
For further details on the protocol, the programs or the data analysis, here are the slides!
