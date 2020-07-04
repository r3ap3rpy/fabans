### Environment

The hardware layout looks like this.

![layout](/pics/layout.png)

For the virtual machines I use [VMware Workstation 15](https://www.vmware.com/products/workstation-pro.html), for the *router* I use [GNS3](https://gns3.com/software/download-vm).

From user perspective the username used on all devices is *fabric* with the password *fabric*, yes the ansible is configured to use the fabric username.

In the videos I show you everything except the installation of the operating systems.

The host machine is a [Windows 10](https://www.microsoft.com/hu-hu/software-download/windows10) laptop with [Python3.7 x64](https://www.python.org/downloads/release/python-370/) installed.

## Python setup

If you have downloaded the git repository you can navigate inside it and issue the *virtualenv fap* command.
After your environment is ready issue the *fap\Scripts\activate.bat*.
Now you can install the module *pip install fabric*.
A new command will become available which is called *fab* that allows you to execute tasks defined in a *fabfile.py* on your current directory.

## Ansible setup

Login to the management machine, install the epel-repository with the *sudo yum install epel-release -y*.
Then install ansible with the *sudo yum install ansible -y*.

# Later

The ansible setup requires to you to create the */etc/ansible/group_vars* folder.
Then create the */etc/ansible/group_vars/all.yml* file.
In that file you need to add the following lines.

``` yaml
ansible_user: fabric
```

Then edit the */etc/ansible/ansible.cfg* file to enable auto host key adding and configure the private key that is to be used when running ansible commands.

## Pubkey auth.

Create the fabric user on each of the systems.
Then switch to that user on your centos machine and issue the *ssh-keygen -t rsa -b 2048* command. Leave everything blank.

Then copy the key to each of the hosts with the *ssh-copy-id <hostname>*.
After the copy is completed you should copy down the public and private keys to your local machine under the *~/.ssh* folder.
Edit the config file in that same folder so it looks something like this.

``` text
Host *
	User fabric
	IdentityFile C:\Users\<username>\.ssh\id_rsa
```