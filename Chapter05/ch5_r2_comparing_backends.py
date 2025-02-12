#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created Nov 2020
Updated March 2023
Updated Feb 2025

@author: hassi
"""

from qiskit import QuantumCircuit
from qiskit_ibm_runtime import QiskitRuntimeService
from qiskit.visualization import plot_distribution
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager

from qiskit_ibm_runtime import SamplerV2 as Sampler


from IPython.core.display import display

print("Ch 5: Comparing backends")
print("------------------------")

# Set service 
print("Getting service...")
if not QiskitRuntimeService().active_account:
    print("Loading account")
    QiskitRuntimeService().load_account()
service = QiskitRuntimeService()

# Cceate a Bell circuit 
qc = QuantumCircuit(2,2)

qc.h(0)
qc.cx(0,1)
qc.measure([0,1],[0,1])

print("\nQuantum circuit:")
print(qc)

# Get all available and operational backends.
print("\nAvailable backends:")
backends=service.backends(operational=True, simulator=False)
for item in backends:
    print("\nName: ",item.name, "\nJobs in queue: ",item.status().pending_jobs)
print("\nAvailable backends:", backends)

# Run the program on all backends and create a counts dictionary with the results from the executions.
counts = {}
for n in range(0, len(backends)):
    print('Run on:', backends[n].name)
    backend = service.backend(backends[n].name)
    tr_qc = generate_preset_pass_manager(backend=backend, optimization_level=3).run(qc)
    sampler = Sampler(mode=backend)
    
    job = sampler.run([(tr_qc)])
    print(f">>> Job ID: {job.job_id()}")
    print(f">>> Job Status: {job.status()}")
    result = job.result()
    counts[backends[n].name] = result[0].data.c.get_counts()

#Display the data that we want to plot.
print("\nRaw results:", counts)

#Optionally define the histogram colors. 
colors = ['green','darkgreen','red','darkred', 'orange','yellow','blue','darkblue','purple']

#Plot the counts dictionary values in a histogram, using the counts dictionary keys as legend.
display(plot_distribution(list(counts.values()), title = "Bell results on all available backends", legend=list(counts), color = colors[0:len(backends)], bar_labels = True))

