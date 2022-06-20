#!/bin/bash

tmux kill-server

cd flask-blog

git fetch && git reset origin/main --hard

python -m venv python3-virtualenv

pip install requirements.txt

source python3-virtualenv/bin/activate

tmux new -s redeployed_sess

:attach-session -t . -c flask-blog

tmux detach

flask run --host=0.0.0.0
