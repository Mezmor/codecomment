Vagrant.configure("2") do |config|
  # sets box to Ubuntu 12.04 (32 bit?)
  config.vm.box = "hashicorp/precise32"

  # installs everything needed on the system
  config.vm.provision :shell, path: "vagrant/bootstrap.sh"
  #config.vm.synced_folder ".", "/home/vagrant"
  # enable below to debug launch problems.
  #config.vm.provider "virtualbox" do |v|
  #  v.gui = true
  #nd
end
