Ansible® - An IT automation tool
================================

`Ansible`_ is an IT automation tool. It can configure systems, deploy software, and orchestrate more advanced IT tasks such as continuous deployments or zero downtime rolling updates.

Quick Start
-----------

This appliance uses ssh-agent and keychain to manage keys for Ansible.  This is one way of using the same identity to manage multiple hosts with SSO.

Login as the ansible user.  The first time you login, you will be asked to re-enter the passphrase for the id_rsa key.  This is the same password you used to login as ansible.  If you later change the account password, you will also need to change the id_rsa passphrase.

::

    $ ssh ansible@ansible
    
    ...snip...
    
     * keychain 2.7.1 ~ http://www.funtoo.org
     * Starting ssh-agent...
     * Adding 1 ssh key(s): /home/ansible/.ssh/id_rsa
    Enter passphrase for /home/ansible/.ssh/id_rsa:
     * ssh-add: Identities added: /home/ansible/.ssh/id_rsa
    
    ansible@ansible ~$

Now you should be able to execute some simple commands.

::

    ansible@ansible ~$ ansible@ansible ~$ ansible localhost -m ping
    localhost | success >> {
        "changed": false, 
        "ping": "pong"
    }
    
    ansible@ansible ~$ ansible@ansible ~$ ansible localhost -m setup
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

Add remote hosts that you want to manage to the Ansible inventory, /etc/ansible/hosts. You can edit the file with sudo and vim or nano. Read the documentation on `Inventory`_ or consult the hosts.example file to setup hosts and groups of hosts.  Add the following section to the inventory file.

::

    [turnkey]
    <turnkey_app>
    

Replace "<turnkey_app>" with the hostname of your TurnKey appliance or it's fully qualified domain name.  The name must be resolvable by DNS.

By default, Ansible will connect to the remote host as user=root. If you want to use a different user, add  "ansible_ssh_user=<username>" following the hostname.

Now you should be able to run 'ping' on <turnkey_app> or [turnkey] group using a password.  Use option '-k' to prompt for a password.

::

    ansible@ansible ~$ ansible <turnkey_app> -k -m ping
    SSH password: 
    <turnkey_app> | success >> {
        "changed": false,
        "ping": "pong"
    }

Using SSH Keys
--------------

Using and managing passwords for many hosts can be problematic and doing it securely requires the use of Ansible `Vault`_ or one of the Lookup strategies, `Password`_ or `Passwordstore`_.

Using SSH Keys is simpler and just as secure. In any case, the ansible user will have root access to all the managed hosts, so exercise the proper security measures to protect the Ansible host and the ansible user/password.

Login to the ansible account and copy the public key to <turnkey_app>.

::

    ansible@ansible ~$ ssh-copy-id root@<turnkey_app>
    /usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
    /usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new keys
    
    root@<turnkey_app>'s password: 
    

    Number of key(s) added: 1
    
    Now try logging into the machine, with:   "ssh 'root@<turnkey_app>'"
    and check to make sure that only the key(s) you wanted were added.

You should now be able to run plays and playbooks without needing to prompt for the password.

::

    ansible@ansible ~$ ansible <turnkey_app> -m ping
    <turnkey_app> | success >> {
        "changed": false,
        "ping": "pong"
    }

Playbooks
---------

An alternative to manually installing the ssh key in the previous step, is to use the init.yml playbook.  This playbook will install the ansible ssh key and also check to make sure that python and other necessary packages are installed on the managed host.  Use the '-k' option to prompt for the root password and the '-l' option to limit the action to <turnkey_app>, otherwise the playbook would run on all hosts in the inventory file.  The init.yml playbook should be run once on each ansible managed host.

::

    ansible@ansible ~$ cd playbooks/
    ansible@ansible ~/playbooks$ ansible-playbook init.yml -k -l <turnkey_app>
    SSH password: 
    
    PLAY [all] ***********************************************************************************************************
    
    TASK [INIT | Install python support for Ansible] *********************************************************************
    changed: [<turnkey_app>]
    
    TASK [setup] *********************************************************************************************************
    ok: [<turnkey_app>]
    
    TASK [INIT | Make sure essential software is installed] **************************************************************
    ok: [<turnkey_app>] => (item=[u'python', u'python-apt', u'lsb-release'])
    
    TASK [INIT | Install ssh public key from current account] ************************************************************
    ok: [<turnkey_app>]
    
    PLAY RECAP ***********************************************************************************************************
    <turnkey_app>                        : ok=4    changed=1    unreachable=0    failed=0   
    

TurnKey Facts
-------------

After the TurnKey appliance has been initialized by init.yml, you can then gather facts about the appliance.  These facts can then be used in playbooks to control the flow of execution.

::

    ansible@ansible /etc/lighttpd$ ansible <turnkey_app> -m turnkey_facts
    <turnkey_app> | SUCCESS => {
        "ansible_facts": {
            "turnkey": true, 
            "turnkey_app": "lamp ", 
            "turnkey_arch": "amd64", 
            "turnkey_deb": "jessie", 
            "turnkey_ver": "14.1", 
            "turnkey_version_output": "turnkey-lamp-14.1-jessie-amd64"
        }, 
        "changed": false
    }

Documentation
-------------
- See the latest documentation at https://docs.ansible.com/ansible/index.html
- https://github.com/ansible
- http://jpmens.net/2012/06/06/configuration-management-with-ansible/
- http://devopsu.com/guides/ansible-ubuntu-debian.html
- https://github.com/fourkitchens/server-playbooks

Ansible® is a registered trademark of Ansible, Inc. in the United States and other countries.

.. _Ansible: https://docs.ansible.com/ansible/index.html
.. _Inventory: https://docs.ansible.com/ansible/intro_inventory.html
.. _Vault: https://docs.ansible.com/ansible/playbooks_vault.html
.. _Password: https://docs.ansible.com/ansible/playbooks_lookups.html#the-password-lookup
.. _Passwordstore: https://docs.ansible.com/ansible/playbooks_lookups.html#the-passwordstore-lookup
