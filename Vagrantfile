Vagrant.configure("2") do |config|
  # sets box to Ubuntu 12.04 (32 bit?)
  config.vm.box = "hashicorp/precise32"
  
  # this lets us access these ports on the vm from our local host.
  # Run the server on vagrant with ./manage.py runserver 0.0.0.0:8000 which 
  # forwards it to port 8001 and is accessible at http://127.0.0.1:8001
  config.vm.network "forwarded_port",guest: 80, host: 8080
  config.vm.network "forwarded_port",guest: 8000, host: 8001
  # installs everything needed on the system. privileged is false to make venv not as root
  config.vm.provision :shell, path: "vagrant/bootstrap.sh", privileged: false
  config.vm.synced_folder ".", "/home/vagrant/codecomment"
  # enable below to debug launch problems.
  #config.vm.provider "virtualbox" do |v|
  #  v.gui = true
  #end
end
