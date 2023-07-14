#!bin/bash

# install python3
if command -v python3 &> /dev/null; then
    echo "You've already installed python3"
else
    apt-get update
    # -y auto answers yes to input
    apt-get install -y python3 

venv=".venv"

# start venv
if [ -d "$venv" ]; then
    source .venv/bin/activate
else
    python3 -m venv .venv
    echo "Starting venv"
    source .venv/bin/activate

# install pip3
if command -v pip3 &> /dev/null; then
    echo "You've already installed pip3"
else
    curl -O https://bootstrap.pypa.io/get-pip.py

pip install -r requirements.txt

# perms
chmod +x "main.py"
echo "Executable permisions enabled"
echo "please run run.sh"