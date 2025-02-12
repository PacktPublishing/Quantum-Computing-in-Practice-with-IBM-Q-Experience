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

print("Ch 4: Three-qubit coin toss")
print("---------------------------")


qc = QuantumCircuit(3, 6)

qc.h([0,1,2])
qc.measure([0,1,2],[0,1,2])

display(qc.draw('mpl'))

# Run the simple quantum circuit on local Sampler 
job = Sampler().run([qc])
quasi_dists = job.result().quasi_dists
counts = quasi_dists[0].binary_probabilities()

#Plot the results
display(plot_distribution(counts))

print(counts)

qc.barrier([0,1,2])
qc.reset([0,1,2])

qc.h(0)
qc.cx(0,1)
qc.cx(0,2)
qc.measure([0,1,2],[0,1,2]) #<- verify should this be 3,4,5? Why?

display(qc.draw('mpl'))

# Run the simple quantum circuit on local Sampler 
job = Sampler().run([qc])
quasi_dists = job.result().quasi_dists
counts = quasi_dists[0].binary_probabilities()

#Plot the results
display(plot_distribution(counts))

print(counts)

