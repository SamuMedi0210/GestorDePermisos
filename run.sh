#!/bin/bash
cd /tmp/cc-agent/65393810/project/login
export PYTHONPATH=/tmp/cc-agent/65393810/project/login:$PYTHONPATH
python3 -m flet run main.py --web
