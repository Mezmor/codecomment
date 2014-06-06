#!/usr/bin/env bash
sudo apt-get update
sudo apt-get install -y python-pip
sudo pip install virtualenv virtualenvwrapper


# if virtualenvwrapper hasn't already been added the the bashrc.
if [[ -n $(which virtualenvwrapper.sh) ]]; then
	touch .bashrc
	echo "source /usr/local/bin/virtualenvwrapper.sh" >> /home/vagrant/.bashrc
fi
source /home/vagrant/.bashrc

# for some reason sourcing the bash file didn't properly source the wrapper. So you need to do:
source /usr/local/bin/virtualenvwrapper.sh
mkvirtualenv codecomm
workon codecomm
sudo pip install -r "/vagrant/requirements/requirements.txt"
