====
Vagrant Guide
====
Install
--------
First install vagrant:
::
	apt-get install vagrant virtualbox-4.3
Navigate to the code directory and run the Vagrantfile:
::
	cd codecomment/
	vagrant up
This will setup a virtual machine and install the dev stack on it.  (See Vagrantfile and vagrant/bootstrap.sh for specifics)

Use
--------
All code you write on your local machine will be automatically synced to the folder /home/vagrant/codecomment on the vm.  You can write everything 
on your end and then test it out on the virtual machine.

To test code on the vm first:
::
	vagrant ssh
This will give you ssh access to the vm.  Then:
::
	cd codecomment/
	workon codecomm
	./manage.py runserver 0.0.0.0:8000
You can then see the server on your local computer by navigating to 
::
	http://127.0.0.1:8001

Essential Commands
--------

::
	vagrant up
This configures and launches the server.  If the Vagrantfile has been modified, it will make any changes necessary.
::
	vagrant reload
Restarts the vm.  Most of the time this will be all you need to run for any changes you made to the Vagrantfile while it was running.
::
	vagrant halt
Shuts down the vm.

::
	vagrant ssh
This gives you shell access to the server.  Use this to test code or for deployment testing or whatever.
::
	vagrant destroy
This is the command you run if the vm has gone wrong.  It will wipe the vm completely allowing you to install a fresh one.
::
	vagrant provision
This will update packages/settings on the server based on vagrant/bootstrap.sh .  Run this after making/adding anything to the bootstrap file.


Notes
--------
(read: problems encountered while installing on Arch Linux...)
If you have not used virtualization software before you may need to enable flags in BIOS.  Check your systems BIOS if problems occur

If you get an error that your Guest Host virtualbox version does not match your version, you may need to install a plugin to handle updating the Guest Host.
See: https://github.com/dotless-de/vagrant-vbguest
Actually you probably don't need that. 
 