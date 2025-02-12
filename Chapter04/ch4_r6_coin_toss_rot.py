#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created Nov 2020, updated Jan 2025

@author: hassi
"""

from qiskit import QuantumCircuit, transpile
from qiskit_aer.primitives import Sampler
from qiskit.visualization import plot_distribution, plot_bloch_multivector
from qiskit_aer import AerSimulator
from qiskit.quantum_info import Statevector

from IPython.display import display

from math import pi

# Function that returns the state vector (Psi) for the circuit
def get_psi(circuit, title):
    show_bloch=True
    if show_bloch:
        psi = Statevector(circuit)
        print(title)
        display(psi.draw(output = 'latex'))
        display(qc.draw('mpl'))
        display(plot_bloch_multivector(psi)) 
        

print("Ch 4: More Cheating quantum coin toss")
print("-------------------------------------")

qc = QuantumCircuit(1, 1)
get_psi(qc, 'Qubit in ground state |0>')
qc.h(0)
get_psi(qc, 'Qubit in super position')
qc.ry(pi/8,0)
get_psi(qc, 'Qubit pi/8 radians closer to |1>') 
qc.measure(0, 0)

display(qc.draw('mpl'))

# Run the simple quantum circuit on local Sampler 
job = Sampler().run([qc])
quasi_dists = job.result().quasi_dists
counts = quasi_dists[0].binary_probabilities()

#Plot the results
display(plot_distribution(counts))

print("\nSampler: ", counts)


# Transpile for simulator
simulator = AerSimulator()
circ = transpile(qc, simulator)

# Run and get counts
result = simulator.run(circ).result()
counts = result.get_counts(circ)

display(plot_distribution(counts))
print("\nAerSimulator counts: ", counts)
