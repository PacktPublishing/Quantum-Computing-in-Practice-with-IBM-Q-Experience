#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created Nov 2020, updated Jan 2025

@author: hassi
"""

from qiskit import QuantumCircuit
from qiskit.visualization import plot_gate_map, plot_distribution
from qiskit_ibm_runtime import QiskitRuntimeService
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager

#Optional: When running in an iPhyton environment
from IPython.display import display

#If you haven't, add your API token from https://quantum.ibm.com
#QiskitRuntimeService.save_account(channel="ibm_quantum", token="TOKEN", set_as_default=True, overwrite=True)

print("Ch 4: Quantum coin toss on IBM Quantum backend")
print("----------------------------------------------")

#Create the small circuit

qc = QuantumCircuit(2, 2)

#Add the Bell state
qc.h(0)
qc.cx(0,1)
qc.measure([0,1],[0,1])

# Display the raw circuit
display(qc.draw('mpl'))

# Set service and select backend
service = QiskitRuntimeService()
service.backends()
backend = service.least_busy(operational=True, simulator=False)
print("Backend: ", backend.name)

# Transpile and display the circuit for the backend
tr_qc = generate_preset_pass_manager(backend=backend, optimization_level=3).run(qc)
display(tr_qc.draw("mpl", idle_wires=False))

#Optional: Visualize the coupling directional map for the backend
display(plot_gate_map(backend, plot_directed=True))

# Run as sampler 
from qiskit_ibm_runtime import SamplerV2 as Sampler
sampler = Sampler(mode=backend)

job = sampler.run([(tr_qc)])
print(f">>> Job ID: {job.job_id()}")
print(f">>> Job Status: {job.status()}")

#Get results as counts of the possible outputs
result = job.result()
counts = result[0].data.c.get_counts()

#Print and plot the results
print(f"Counts for the 'c' output register: {counts}")
display(plot_distribution(counts))
