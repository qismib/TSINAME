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
        ax.text(rect.get_x() + rect.get_width()/2., height + 3, ('%f' % round(height,2)).rstrip("0") + " %", ha='center', va='bottom', fontsize=14)	
        
        # '%f' % height + " %" means that I am substituting ''height + " %"'' 
        # in the string which is passed as argument of the function 
        # (height is passed as a float (--> '%f'), ''%'' as a string character)


# --------------------------------------------- Main program



noise = [9,54,46,1,7,1]


fig, ax = plt.subplots(figsize=(8, 7))

plt.suptitle("Backend: ibmq_5_yorktown", fontsize=16, fontweight="bold")
plt.title("Probability of having an error measuring two entangled qubits", fontsize=16)

ax.set_ylabel("Probability (%)", fontsize=16)
ax.set_xlabel("Entangled qubits", fontsize=16)

rectangle = ax.bar([1,2,3,4,5, 6], height=[noise[0], noise[1], noise[2], noise[3], noise[4], noise[5]], \
    tick_label=["Q0-Q1","Q0-Q2","Q1-Q2","Q2-Q3","Q2-Q4","Q3-Q4"], color=["r", "r", "r", "r", "r", "r"]) 
plt.axis([0.5, 6.5, 0, 110])

autolabel(rectangle)


# ---------------------------------------------------------------------------------------------------------------------------------------------------

# Double couple (TOTALS)


noise = [29,46]


fig, ax = plt.subplots(figsize=(8, 7))

ax.set_ylabel("Probability (%)", fontsize=16)
ax.set_xlabel("Entangled qubits", fontsize=16)

plt.suptitle("Backend: ibmq_5_yorktown", fontsize=16, fontweight="bold")
plt.title("Probability of having an error measuring two couples of entangled qubits\n(overall results)", fontsize=14)

rectangle = ax.bar([1,2], height=[noise[0], noise[1]], \
    tick_label=["Q0-Q1 and Q2-Q3", "Q0-Q2 and Q3-Q4"], color=["darkorange", "darkviolet"]) 
plt.axis([0.5, 2.5, 0, 110])

autolabel(rectangle)




# ---------------------------------------------------------------------------------------------------------------------------------------------------

# Double couple (PARTIALS)


noise = [53,5,40,52]


fig, ax = plt.subplots(figsize=(8, 7))

ax.set_ylabel("Probability (%)", fontsize=16)
ax.set_xlabel("Entangled qubits", fontsize=16)

plt.suptitle("Backend: ibmq_5_yorktown", fontsize=16, fontweight="bold")
plt.title("Probability of having an error measuring two couples of entangled qubits\n(separate couples)", fontsize=14)

rectangle = ax.bar([1,2,3,4], height=[noise[0], noise[1], noise[2], noise[3]], \
    tick_label=["Q0-Q1", "Q2-Q3", "Q0-Q2", "Q3-Q4"], color=["darkorange", "darkorange", "darkviolet", "darkviolet"]) 
plt.axis([0.5, 4.5, 0, 110])

autolabel(rectangle)




plt.show()
