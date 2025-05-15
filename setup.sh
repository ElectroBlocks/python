#!/bin/bash
# Setup script for ElectroBlocks Python development environment

echo "Creating virtual environment..."
python3 -m venv venv

echo "Activating virtual environment..."
source venv/bin/activate

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Installing ElectroBlocks in editable mode..."
pip install -e .

echo "Setup complete. To activate later, run:"
echo "source venv/bin/activate"