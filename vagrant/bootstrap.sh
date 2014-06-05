#!/usr/bin/env bash
apt-get update
apt-get install -y python-pip
pip install virtualenv
touch .bashrc
echo "source /usr/local/bin/virtualenvwrapper.sh" >> .bashrc
source ~/.bashrc
mkvirtualenv codecomm

