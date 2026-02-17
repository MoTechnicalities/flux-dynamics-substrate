#!/bin/bash
# Running Flux Experiments

export PYTHONPATH=$PYTHONPATH:$(pwd)/src

echo "Running Flux Sensitivity Analysis..."
python3 src/flux_experiments.py

echo "Experiment Complete."
