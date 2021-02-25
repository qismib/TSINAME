import matplotlib.pyplot as plt
from matplotlib.collections import EventCollection
import numpy as np

plt.rc('xtick', labelsize=16) 
plt.rc('ytick', labelsize=16) 


def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., height + 3, '%f' % height + " %", ha='center', va='bottom')	
        
        # '%f' % height + " %" means that I am substituting ''height + " %"'' 
        # in the string which is passed as argument of the function 
        # (height is passed as a float (--> '%f'), ''%'' as a string character)


# --------------------------------------------- Main program
"""
# Santiago, |0> test

qubit_number = [1,2,3,4,5]

noise = [1,0,5.05,1,2]


fig, ax = plt.subplots(figsize=(8, 7))

ax.set_ylabel("Probability (%)")
ax.set_xlabel("N (number of qubits in parallel)")

rectangle = ax.bar([1,2,3,4,5], height=[noise[0], noise[1], noise[2], noise[3], noise[4]], \
    tick_label=["1", "2", "3", "4", "5"], color=["b", "b", "b", "b", "b"]) 
plt.axis([0.5, 5.5, 0, 110])

autolabel(rectangle)

ax.plot(qubit_number, noise, color='tab:blue')

plt.suptitle("Backend: ibmq_santiago", fontsize=15, fontweight="bold")
plt.title("Probability of having an error with N qubits in parallel\n|0> test", fontsize=12)

# ---------------------------------------------------------------------------------------------------------------------------------------------------

# Santiago, |-> test

qubit_number = [1,2,3,4,5]

noise = [2,3,2.02,1,3]


fig, ax = plt.subplots(figsize=(8, 7))

ax.set_ylabel("Probability (%)")
ax.set_xlabel("N (number of qubits in parallel)")

rectangle = ax.bar([1,2,3,4,5], height=[noise[0], noise[1], noise[2], noise[3], noise[4]], \
    tick_label=["1", "2", "3", "4", "5"], color=["b", "b", "b", "b", "b"]) 
plt.axis([0.5, 5.5, 0, 110])

autolabel(rectangle)

ax.plot(qubit_number, noise, color='tab:blue')

plt.suptitle("Backend: ibmq_santiago", fontsize=15, fontweight="bold")
plt.title("Probability of having an error with N qubits in parallel\n| - > test", fontsize=12)

# ---------------------------------------------------------------------------------------------------------------------------------------------------



# Vigo, |0> test

qubit_number = [1,2,3,4,5]

noise = [3,3,2.02,1,6]


fig, ax = plt.subplots(figsize=(8, 7))

ax.set_ylabel("Probability (%)")
ax.set_xlabel("N (number of qubits in parallel)")

rectangle = ax.bar([1,2,3,4,5], height=[noise[0], noise[1], noise[2], noise[3], noise[4]], \
    tick_label=["1", "2", "3", "4", "5"], color=["g", "g", "g", "g", "g"]) 
plt.axis([0.5, 5.5, 0, 110])

autolabel(rectangle)

ax.plot(qubit_number, noise, color='tab:green')

plt.suptitle("Backend: ibmq_vigo", fontsize=15, fontweight="bold")
plt.title("Probability of having an error with N qubits in parallel\n|0> test", fontsize=12)

# ---------------------------------------------------------------------------------------------------------------------------------------------------

# Vigo, |-> test

qubit_number = [1,2,3,4,5]

noise = [12,3,4.04,5,5]


fig, ax = plt.subplots(figsize=(8, 7))

ax.set_ylabel("Probability (%)")
ax.set_xlabel("N (number of qubits in parallel)")

rectangle = ax.bar([1,2,3,4,5], height=[noise[0], noise[1], noise[2], noise[3], noise[4]], \
    tick_label=["1", "2", "3", "4", "5"], color=["g", "g", "g", "g", "g"]) 
plt.axis([0.5, 5.5, 0, 110])

autolabel(rectangle)

ax.plot(qubit_number, noise, color='tab:green')

plt.suptitle("Backend: ibmq_vigo", fontsize=15, fontweight="bold")
plt.title("Probability of having an error with N qubits in parallel\n| - > test", fontsize=12)

# ---------------------------------------------------------------------------------------------------------------------------------------------------


# Yorktown, |0> test

qubit_number = [1,2,3,4,5]

noise = [0,2,7.07,10,5]


fig, ax = plt.subplots(figsize=(8, 7))

ax.set_ylabel("Probability (%)")
ax.set_xlabel("N (number of qubits in parallel)")

rectangle = ax.bar([1,2,3,4,5], height=[noise[0], noise[1], noise[2], noise[3], noise[4]], \
    tick_label=["1", "2", "3", "4", "5"], color=["r", "r", "r", "r", "r"]) 
plt.axis([0.5, 5.5, 0, 110])

autolabel(rectangle)

ax.plot(qubit_number, noise, color='tab:red')

plt.suptitle("Backend: ibmq_5_yorktown", fontsize=15, fontweight="bold")
plt.title("Probability of having an error with N qubits in parallel\n|0> test", fontsize=12)

# ---------------------------------------------------------------------------------------------------------------------------------------------------

# Yorktown, |-> test

qubit_number = [1,2,3,4,5]

noise = [8,4,29.29,28,21]


fig, ax = plt.subplots(figsize=(8, 7))

ax.set_ylabel("Probability (%)")
ax.set_xlabel("N (number of qubits in parallel)")

rectangle = ax.bar([1,2,3,4,5], height=[noise[0], noise[1], noise[2], noise[3], noise[4]], \
    tick_label=["1", "2", "3", "4", "5"], color=["r", "r", "r", "r", "r"]) 
plt.axis([0.5, 5.5, 0, 110])

autolabel(rectangle)

ax.plot(qubit_number, noise, color='tab:red')

plt.suptitle("Backend: ibmq_5_yorktown", fontsize=15, fontweight="bold")
plt.title("Probability of having an error with N qubits in parallel\n| - > test", fontsize=12)
"""
# ---------------------------------------------------------------------------------------------------------------------------------------------------


# Total



fig, ax = plt.subplots(figsize=(10, 6))
ax.set_ylabel("Probability (%)")
ax.set_xlabel("N (number of qubits in parallel)")
plt.suptitle("Noise tests", fontsize=15, fontweight="bold")
plt.title("Probability of having an error with N qubits in parallel", fontsize=12)
plt.axis([0.5, 5.5, -12, 45])

sfasamento1 = [0.1, 0.1, 0.1, 0.1, 0.1]
sfasamento2 = [0.06, 0.06, 0.06, 0.06, 0.06]
sfasamento3 = [0.03, 0.03, 0.03, 0.03, 0.03]

ax.axvspan(0.8, 1.2, alpha=0.2)   # Serve a colorare una certa area
ax.axvspan(1.8, 2.2, alpha=0.2)
ax.axvspan(2.8, 3.2, alpha=0.2)
ax.axvspan(3.8, 4.2, alpha=0.2)
ax.axvspan(4.8, 5.2, alpha=0.2)

# Santiago, |0> test
x = [1,2,3,4,5]
y = [1,0,5.05,1,2]
yerr = np.sqrt(100)

for k in range(5):
    x[k] = x[k] + sfasamento1[k]

ax.plot(x, y, color="b", label="ibmq_santiago: |0> test")
plt.errorbar(x, y, yerr=yerr, fmt="bo")


# Santiago, |-> test
x = [1,2,3,4,5]
y = [2,3,2.02,1,3]
yerr = np.sqrt(100)

for k in range(5):
    x[k] = x[k] - sfasamento1[k]

ax.plot(x, y, "b--", label="ibmq_santiago: |-> test")
plt.errorbar(x, y, yerr=yerr, fmt="bo")



# Vigo, |0> test
x = [1,2,3,4,5]
y = [3,3,2.02,1,6]
yerr = np.sqrt(100)

for k in range(5):
    x[k] = x[k] + sfasamento2[k]

ax.plot(x, y, color="g", label="ibmq_vigo: |0> test")
plt.errorbar(x, y, yerr=yerr, fmt="go")

# Vigo, |-> test
x = [1,2,3,4,5]
y = [12,3,4.04,5,5]
yerr = np.sqrt(100)

for k in range(5):
    x[k] = x[k] - sfasamento2[k]

ax.plot(x, y, "g--", label="ibmq_vigo: |-> test")
plt.errorbar(x, y, yerr=yerr, fmt="go")



# Yorktown, |0> test
x = [1,2,3,4,5]
y = [0,2,7.07,10,5]
yerr = np.sqrt(100)

for k in range(5):
    x[k] = x[k] + sfasamento3[k]

ax.plot(x, y, color="r", label="ibmq_5_yorktown: |0> test")
plt.errorbar(x, y, yerr=yerr, fmt="ro")

# Yorktown, |-> test
x = [1,2,3,4,5]
y = [8,4,29.29,28,21]
yerr = np.sqrt(100)

for k in range(5):
    x[k] = x[k] - sfasamento3[k]

ax.plot(x, y, "r--", label="ibmq_5_yorktown: |-> test")
plt.errorbar(x, y, yerr=yerr, fmt="ro")



x0 = [0.5,5.5]
y0 = [0,0]
plt.plot(x0, y0, "c:", label="Ideal case (no noise)", linewidth=2)
plt.legend()

# -------------------------------------------------------------------------------------------

# Total ma separato per i due tipi

fig, ax = plt.subplots(figsize=(10, 6))
ax.set_ylabel("Probability (%)", fontsize=16)
ax.set_xlabel("N (number of qubits in parallel)", fontsize=16)
plt.title("Probability of having an error with N qubits in parallel\n|0> test", fontsize=16)
plt.axis([0.5, 5.5, -12, 45])

sfasamento1 = [-0.1, -0.1, -0.1, -0.1, -0.1]
sfasamento2 = [0, 0, 0, 0, 0]
sfasamento3 = [0.1, 0.1, 0.1, 0.1, 0.1]

ax.axvspan(0.8, 1.2, alpha=0.2)   # Serve a colorare una certa area
ax.axvspan(1.8, 2.2, alpha=0.2)
ax.axvspan(2.8, 3.2, alpha=0.2)
ax.axvspan(3.8, 4.2, alpha=0.2)
ax.axvspan(4.8, 5.2, alpha=0.2)

# Santiago, |0> test
x = [1,2,3,4,5]
y = [1,0,5.05,1,2]
yerr = np.sqrt(100)

for k in range(5):
    x[k] = x[k] + sfasamento1[k]

ax.plot(x, y, "b-.", label="ibmq_santiago")
plt.errorbar(x, y, yerr=yerr, fmt="bo")


# Vigo, |0> test
x = [1,2,3,4,5]
y = [3,3,2.02,1,6]
yerr = np.sqrt(100)

for k in range(5):
    x[k] = x[k] + sfasamento2[k]

ax.plot(x, y, "g-.", label="ibmq_vigo")
plt.errorbar(x, y, yerr=yerr, fmt="go")


# Yorktown, |0> test
x = [1,2,3,4,5]
y = [0,2,7.07,10,5]
yerr = np.sqrt(100)

for k in range(5):
    x[k] = x[k] + sfasamento3[k]

ax.plot(x, y, "r-.", label="ibmq_5_yorktown")
plt.errorbar(x, y, yerr=yerr, fmt="ro")



x0 = [0.5,5.5]
y0 = [0,0]
plt.plot(x0, y0, "c:", label="Ideal case (no noise)", linewidth=2)
plt.legend()


# ------------------------------------

fig, ax = plt.subplots(figsize=(10, 6))
ax.set_ylabel("Probability (%)", fontsize=16)
ax.set_xlabel("N (number of qubits in parallel)", fontsize=16)
plt.title("Probability of having an error with N qubits in parallel\n|-> test", fontsize=16)
plt.axis([0.5, 5.5, -12, 45])

sfasamento1 = [-0.1, -0.1, -0.1, -0.1, -0.1]
sfasamento2 = [0, 0, 0, 0, 0]
sfasamento3 = [0.1, 0.1, 0.1, 0.1, 0.1]

ax.axvspan(0.8, 1.2, alpha=0.2)   # Serve a colorare una certa area
ax.axvspan(1.8, 2.2, alpha=0.2)
ax.axvspan(2.8, 3.2, alpha=0.2)
ax.axvspan(3.8, 4.2, alpha=0.2)
ax.axvspan(4.8, 5.2, alpha=0.2)


# Santiago, |-> test
x = [1,2,3,4,5]
y = [2,3,2.02,1,3]
yerr = np.sqrt(100)

for k in range(5):
    x[k] = x[k] + sfasamento1[k]

ax.plot(x, y, "b-.", label="ibmq_santiago")
plt.errorbar(x, y, yerr=yerr, fmt="bo")


# Vigo, |-> test
x = [1,2,3,4,5]
y = [12,3,4.04,5,5]
yerr = np.sqrt(100)

for k in range(5):
    x[k] = x[k] + sfasamento2[k]

ax.plot(x, y, "g-.", label="ibmq_vigo")
plt.errorbar(x, y, yerr=yerr, fmt="go")


# Yorktown, |-> test
x = [1,2,3,4,5]
y = [8,4,29.29,28,21]
yerr = np.sqrt(100)

for k in range(5):
    x[k] = x[k] + sfasamento3[k]

ax.plot(x, y, "r-.", label="ibmq_5_yorktown")
plt.errorbar(x, y, yerr=yerr, fmt="ro")



x0 = [0.5,5.5]
y0 = [0,0]
plt.plot(x0, y0, "c:", label="Ideal case (no noise)", linewidth=2)
plt.legend()

plt.show()
