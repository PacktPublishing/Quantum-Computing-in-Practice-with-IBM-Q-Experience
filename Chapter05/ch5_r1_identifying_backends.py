#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created Nov 2020
Updated Aug 2021, Updated Feb 2025

@author: hassi
"""

from qiskit import QuantumCircuit
from qiskit_ibm_runtime import QiskitRuntimeService
from qiskit.visualization import plot_distribution
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager

#Optional: When running in an iPhyton environment
from IPython.display import display

print("Ch 5: Identifying backends")
print("--------------------------")


# Set service and select backend
print("Getting service...")
if not QiskitRuntimeService().active_account:
    print("Loading account")
    QiskitRuntimeService().load_account()
service = QiskitRuntimeService()

print("\nAvailable backends:")
backends=service.backends(operational=True, simulator=False)
for item in backends:
    print("\nName: ",item.name, "\nJobs in queue: ",item.status().pending_jobs)

# Create a quantum circuit to test
qc = QuantumCircuit(2,2)

qc.h(0)
qc.cx(0,1)
qc.measure([0,1],[0,1])

print("\nQuantum circuit:")
print(qc)

select_backend=input("\nType in the name of a backend to run the job: ")
backend = service.backend(select_backend)

# Transpile and display the circuit for the backend
tr_qc = generate_preset_pass_manager(backend=backend, optimization_level=3).run(qc)
display(tr_qc.draw("mpl", idle_wires=False))
print("\nQuantum circuit transpiled for: ", backend.name)

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







