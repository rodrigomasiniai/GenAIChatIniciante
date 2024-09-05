#!/bin/bash

# Step 1: Uninstall NumPy 2.x
echo "Uninstalling NumPy 2.x..."
pip uninstall -y numpy

# Step 2: Install NumPy 1.x
echo "Installing NumPy 1.x..."
pip install "numpy<2.0"

# Step 3: Upgrade pybind11 to support NumPy 2.x if needed
echo "Upgrading pybind11 to version 2.12 or higher..."
pip install --upgrade pybind11

# Step 4: Reinstall affected libraries (e.g., torch) that might need to be rebuilt
echo "Force reinstalling torch to ensure compatibility with NumPy 2.x..."
pip install --upgrade --force-reinstall torch

echo "Process completed. Please verify your environment."
