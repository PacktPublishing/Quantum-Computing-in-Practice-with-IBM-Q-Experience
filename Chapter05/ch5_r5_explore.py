#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created Nov 2020, Updated Feb 2025

@author: hassi
"""

from qiskit_ibm_runtime import QiskitRuntimeService

print("Ch 5: Explore a backend")
print("-----------------------")

# Set service 
print("Getting service...")
if not QiskitRuntimeService().active_account:
    print("Loading account")
    QiskitRuntimeService().load_account()
service = QiskitRuntimeService()


# Get all available and operational backends.
print("Getting the available backends...")
available_backends=service.backends(operational=True)

# Fish out criteria to compare
print("{0:20} {1:<10} {2:<10} {3:<10}".format("Name","#Qubits","Max exp.","Pending jobs"))
print("{0:20} {1:<10} {2:<10} {3:<10}".format("----","-------","--------","------------"))

for n in range(0, len(available_backends)):
    backend = service.backend(available_backends[n].name)
    print("{0:20} {1:<10} {2:<10} {3:<10}".format(backend.name,backend.num_qubits,backend.max_experiments,backend.status().pending_jobs))

# Select the least busy backend
least_busy_backend = service.least_busy()

# Print out qubit properties for the backend.
print("\nQubit data for backend:",least_busy_backend.status().backend_name)

for q in range (0, least_busy_backend.num_qubits):
    print("\nQubit",q,":")
    for n in range (0, len(least_busy_backend.properties().qubits[0])):
        print(least_busy_backend.properties().qubits[q][n].name,"=",least_busy_backend.properties().qubits[q][n].value,least_busy_backend.properties().qubits[q][n].unit)

