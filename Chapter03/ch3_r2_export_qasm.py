#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created Nov 2020, updated Jan 2025

@author: hassi
"""

# For this simple recipe we will only need the random_circuit method
from qiskit.circuit.random.utils import random_circuit

print("Ch 3: Moving between worlds 2")
print("-----------------------------")

# First we create and print a random quantum circuit
print("Random quantum circuit")
print("----------------------\n")
circ=random_circuit(2,2,measure=True)
print(circ)


# Next, we export the circuit as QASM code. If you include a filename you can also save the QASM code as a text file on your local machine
print("\nOpenQASM code")
print("-------------\n")

from qiskit.qasm2 import dumps
qasm_str = dumps(circ)
print(qasm_str)

#Save the QASM string as a .qasm file
with open("Circuit.qasm", "w") as text_file:
    print(qasm_str, file=text_file)


