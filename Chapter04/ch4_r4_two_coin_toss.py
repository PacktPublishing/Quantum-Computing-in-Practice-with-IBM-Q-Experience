#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created Nov 2020, updated Feb 2025

@author: hassi
"""

from qiskit import QuantumCircuit
from qiskit_aer.primitives import Sampler
from qiskit.visualization import plot_distribution

from IPython.display import display


print("Ch 4: Quantum double coin toss")
print("------------------------------")

qc = QuantumCircuit(2, 2)

qc.h([0,1])
qc.measure([0,1],[0,1])

display(qc.draw('mpl'))

# Run the simple quantum circuit on local Sampler 
job = Sampler().run([qc])
quasi_dists = job.result().quasi_dists
counts = quasi_dists[0].binary_probabilities()

#Plot the results
display(plot_distribution(counts))

print("\nSampler: ", counts)


# Alternatively run on Aersimulator        
from qiskit import transpile
from qiskit_aer import AerSimulator

# Transpile for simulator
simulator = AerSimulator()
circ = transpile(qc, simulator)

# Run and get counts
result = simulator.run(circ).result()
counts = result.get_counts(circ)

display(plot_distribution(counts))
print("\nAerSimulator counts: ", counts)


