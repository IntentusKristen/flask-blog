#!/bin/bash

cd /root/flask-blog

git fetch && git reset origin/main --hard

python -m venv python3-virtualenv

source python3-virtualenv/bin/activate

pip install -r requirements.txt

cd /etc/systemd/system

systemctl daemon-reload
systemctl restart myportfolio