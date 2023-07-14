#!/bin/bash

# install python3
if command -v python3 &> /dev/null; then
    echo "You've already installed python3"
else
    apt-get update
    # -y auto answers yes to input
    apt-get install -y python3
fi  # Add this line to close the 'if' block

venv=".venv"

# start venv
if [ -d "$venv" ]; then
    source .venv/bin/activate
else
    python3 -m venv .venv
    echo "Starting venv"
    source .venv/bin/activate
fi  # Add this line to close the 'if' block

# install pip3
if command -v pip3 &> /dev/null; then
    echo "You've already installed pip3"
else
    curl -O https://bootstrap.pypa.io/get-pip.py
    python3 get-pip.py
fi  # Add this line to close the 'if' block

pip install -r requirements.txt

# perms
chmod +x "main.py"
echo "Executable permissions enabled"
echo "Please run run.sh"