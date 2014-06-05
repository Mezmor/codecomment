===Instructions for Vagrant===
First install vagrant:
::
	apt-get install vagrant
modify appropriately depending on your distribution

Navigate to the directory containing the vagrant file:
::
	cd codecomment/
Start the virtual machine:
::
	vagrant up

Files should sync automatically to the virtual machine allowing you to write everything locally and run on the machine.

===Notes===
(read: problems encountered while installing on Arch Linux...)
If you have not used virtualization software before you may need to enable flags in BIOS.  Check your systems BIOS if problems occur

If you get an error that your Guest Host virtualbox version does not match your version, you need to install a plugin to handle updating the Guest Host.
See: https://github.com/dotless-de/vagrant-vbguest