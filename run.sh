#!/usr/bin/env bash

# Check if the virtual environment exists
if [ ! -d "venv" ]; then
  echo "Virtual environment not found. Creating a new one..."
  python -m venv venv

  if [ $? -ne 0 ]; then
    echo "Error creating virtual environment. Exiting."
    exit 1
  fi

  source venv/scripts/activate

  echo "Installing requirements..."
  pip install -r requirements.txt

  if [ $? -ne 0 ]; then
    echo "Error installing requirements. Exiting."
    exit 1
  fi
else
  source venv/scripts/activate
fi

# Export all environment variables inside .env
set -a
source .env
set +a

# Run the script
python main.py