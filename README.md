# aviLsc

## Goals
These Ansible playbooks deploy Avi in an ubuntu VM/Server(s).

## Prerequisites:
1. Make sure the Avi Software is available as defined in the params file
2. Make sure a Vm (to host the Avi Controller) is reachable
3. Make sure n Vm(s) (to host the Avi SEs) is/are reachable

## Environment:

Playbook(s) has/have been tested against:

### Ansible

```
avi@ansible:~/aviLsc$ ansible --version
ansible 2.9.5
  config file = /etc/ansible/ansible.cfg
  configured module search path = [u'/home/avi/.ansible/plugins/modules', u'/usr/share/ansible/plugins/modules']
  ansible python module location = /home/avi/.local/lib/python2.7/site-packages/ansible
  executable location = /home/avi/.local/bin/ansible
  python version = 2.7.12 (default, Oct  8 2019, 14:14:10) [GCC 5.4.0 20160609]
avi@ansible:~/aviLsc$
```

### Ubuntu

```
avi@controller:~$ cat /etc/os-release
NAME="Ubuntu"
VERSION="16.04.5 LTS (Xenial Xerus)"
ID=ubuntu
ID_LIKE=debian
PRETTY_NAME="Ubuntu 16.04.5 LTS"
VERSION_ID="16.04"
HOME_URL="http://www.ubuntu.com/"
SUPPORT_URL="http://help.ubuntu.com/"
BUG_REPORT_URL="http://bugs.launchpad.net/ubuntu/"
VERSION_CODENAME=xenial
UBUNTU_CODENAME=xenial
avi@controller:~$
```

### Docker

```
avi@controller:~$ docker -v
Docker version 18.09.7, build 2d0083d
avi@controller:~$
```

### Avi version

```
docker_install-18.2.7-9129.tar
docker_install-18.2.8-9205.tar.gz
docker_install-18.2.9-9147.tar.gz
```

## Input/Parameters:

1. An inventory file with the following format (could be 1 or 3 controller hosts):
```
---
all:
  children:
    se:
      hosts:
        192.168.142.129:
        192.168.142.130:
    controller:
      hosts:
        192.168.142.135:


  vars:
    ansible_user: avi
    ansible_ssh_private_key_file: "/home/avi/.ssh/id_rsa.local"
s
```

2. All the paramaters/variables are stored in var/params.yml


## Use the ansible playbook to
1. Install docker to all the SEs and controllers
2. Copy the Avi software (from the ansible host) to all the Controllers
4. Install the Avi Software in all the Controllers
5. Generate a yaml file with the version information
```
avi@ansible:~/ansible/aviLsc$ more ../aviLscBootstrap/vars/aviVersion.yml
api_version: 18.2.8
```

## Run the playbook:
ansible-playbook -i hosts main.yml
or using tags:
ansible-playbook -i hostsLocal main.yml --tags "se"
ansible-playbook -i hostsLocal main.yml --tags "controller"
ansible-playbook -i hostsLocal main.yml --tags "creds"

## Improvement:
