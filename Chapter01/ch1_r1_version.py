#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created Nov 2020
Updated Jan 2025

@author: hassi
"""
# Import Qiskit
import qiskit

# Set version variable to the current Qiskit version
version=qiskit.__version__

# Print the version number for the Qiskit component

print("Qiskit version:")
print("===============")
print(version)
    
#Alternatively, use the following code
print("Qiskit version: ",qiskit.version.get_version_info())
