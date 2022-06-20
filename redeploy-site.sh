#!/bin/bash

tmux kill-server

cd flask-blog

git fetch && git reset origin/main --hard

tmux new -s redeploy

tmux detach-client -P -s redeploy

python -m venv python3-virtualenv

source python3-virtualenv/bin/activate

pip install requirements.txt

flask run --host=0.0.0.0
