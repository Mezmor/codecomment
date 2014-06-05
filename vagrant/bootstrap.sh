#!/usr/bin/env bash
apt-get update
apt-get install -y python-pip
pip install virtualenv virtualenvwrapper


# if virtualenvwrapper hasn't already been added the the bashrc.
if [[ -n $(which virtualenvwrapper.sh) ]]; then
	touch .bashrc
	echo "source /usr/local/bin/virtualenvwrapper.sh" >> .bashrc
fi
source /home/vagrant/.bashrc
mkvirtualenv codecomm
workon codecomm
pip install -r "/vagrant/requirements/requirements.txt"
