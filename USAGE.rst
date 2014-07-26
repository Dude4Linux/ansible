Ansible - An IT automation tool
=================================

`Ansible`_ is an IT automation tool. It can configure systems, deploy software,
and orchestrate more advanced IT tasks such as continuous deployments
or zero downtime rolling updates.

Quick Start
-----------

Login as the ansible user.  You should be able to execute some simple commands.

::

    ansible localhost -m ping
    localhost | success >> {
        "changed": false, 
        "ping": "pong"
    }
    
    ansible localhost -m setup
    localhost | success >> {
        "ansible_facts": {
        ...snip...
    }

The second command should return a JSON formated list of 'facts' gathered from the localhost.

Terminology
-----------

::

- Playbooks     A playbook is composed of one or more plays in a list. Playbooks are expressed in YAML format.
- Plays         Map a group of hosts to well defined roles represented by a list of tasks.
- Roles         Unit of organization for hosts implementing a specific behavior e.g. webserver.
- Tasks         Call to a module to effect pre-defined changes of state.
- Modules       Gather facts or control system resources like services, packages, or files to effect a change in system state.

Summary of Commands
-------------------

::

- ansible              run ad-hoc task or play on a host or group of hosts
- ansible-playbook     run a series of plays or tasks on a host or group of hosts
- ansible-pull         run ansible from the client host in pull mode
- ansible-doc          display help for ansible plays
- ansible-vault        store sensitive credentials in an encrypted file
- ansible-galaxy       download and run ansible plays from the community website

Inventory
---------

Add remote hosts that you want to manage with Ansible to /etc/ansible/hosts. You can edit the file with sudo and vim or nano. Read the documentation on Inventory or consult the hosts.example file to setup hosts and groups of hosts.

By default, Ansible will connect to the remote host as user=root. If you want to use a different user add the var, ansible_ssh_user=<username> following the hostname.

Now you should be able to run 'ping' on a remote host or group using a password.

::

    ansible remotehost -k -m ping
    SSH password: 
    remotehost | success >> {
        "changed": false,
        "ping": "pong"
    }

Using SSH Keys
--------------

Using and managing passwords for many hosts can be problematic and doing it securely requires the use of ansible-vault. Using SSH Keys is simpler and just as secure. In either case, the ansible user will have root access to all the managed hosts, so exercise the proper security measures to protect the Ansible host and the ansible user/password.

Login to the ansible account and copy the public key to all of the managed hosts.

::

    ssh-copy-id root@remotehost
    root@remotehost's password: 
    Now try logging into the machine, with "ssh 'root@remotehost'", and check in:
    
      ~/.ssh/authorized_keys
    
    to make sure we haven't added extra keys that you weren't expecting.


You should now be able to run plays and playbooks without needing to prompt for the password.

::

    ansible remotehost -m ping
    remotehost | success >> {
        "changed": false, 
        "ping": "pong"
    }

Documentation
-------------
- See the latest documentation at http://docs.ansible.com
- https://github.com/ansible
- http://jpmens.net/2012/06/06/configuration-management-with-ansible/
- http://devopsu.com/guides/ansible-ubuntu-debian.html
- https://github.com/fourkitchens/server-playbooks


.. _Ansible: http://docs.ansible.com
