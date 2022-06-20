#!/bin/bash

tmux kill-server

cd flask-blog

tmux new -s redeploy

git fetch && git reset origin/main --hard

python -m venv python3-virtualenv

source python3-virtualenv/bin/activate

pip install requirements.txt

flask run --host=0.0.0.0
