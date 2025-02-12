#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created Nov 2020
Updated March 2025

@author: hassi
"""

from qiskit_ibm_runtime import QiskitRuntimeService

from IPython.core.display import display

print("Ch 5: Least busy backend")
print("------------------------")

# Set service 
print("Getting service...")
if not QiskitRuntimeService().active_account:
    print("Loading account")
    QiskitRuntimeService().load_account()
service = QiskitRuntimeService()

# Finding the least busy backend
backend = service.least_busy()
print("Least busy backend:", backend.name)

filtered_backend = service.least_busy(operational=True, min_num_qubits=127)

print("\nLeast busy backend with at least 127 qubits:", filtered_backend.name)

print("\nAvailable backends:")
backends=service.backends()
for item in backends:
    print("\nName: ",item.name, "\nJobs in queue: ",item.status().pending_jobs,"\nNumber of qubits: ", item.num_qubits)