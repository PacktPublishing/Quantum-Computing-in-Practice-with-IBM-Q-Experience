#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created Nov 2020
Updated Aug 2021, March 2023, Feb 2025

@author: hassi
"""

# Import the required Qiskit classes

from qiskit import QuantumCircuit
from qiskit.visualization import plot_gate_map, plot_error_map, plot_circuit_layout
from qiskit_ibm_runtime import QiskitRuntimeService
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager

# Import the backend visualization methods

from IPython.core.display import display

print("Ch 5: Backend visualization")
print("---------------------------")

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
print("{0:20} {1:<10}".format("Name","#Qubits"))
print("{0:20} {1:<10}".format("----","-------"))

for n in range(0, len(available_backends)):
    backend = service.backend(available_backends[n].name)    
    print("{0:20} {1:<10}".format(backend.name,backend.num_qubits))

# Select a backend or go for the least busy backend with more than 1 qubits
backend_input = input("Enter the name of a backend, or X for the least busy:")
if backend_input not in ["X","x"]:
    backend = service.get_backend(backend_input)
else:
    backend = backend = service.least_busy()
# Display the gate and error map for the backend.
print("\nQubit data for backend:",backend.status().backend_name)

display(plot_gate_map(backend, plot_directed=True))
display(plot_error_map(backend))

# Create and transpile a 2 qubit Bell circuit
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0,1)

display(qc.draw('mpl'))

qc_transpiled = generate_preset_pass_manager(backend=backend, optimization_level=3).run(qc)
display(qc_transpiled.draw("mpl", idle_wires=False))

# Display the circuit layout for the backend.
display(plot_circuit_layout(qc_transpiled, backend, view='physical'))

