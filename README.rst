Ansible - An IT automation tool
===============================

`Ansible`_ is an open source application licensed under the GPL.
    GNU GENERAL PUBLIC LICENSE, Version 3, 29 June 2007

Description or Purpose
----------------------
.. Briefly describe what the appliance does 

Ansible is an IT automation tool. It can configure systems, deploy software,
and orchestrate more advanced IT tasks such as continuous deployments
or zero downtime rolling updates.

This appliance includes all the standard features in `TurnKey Core`_.

Additional Features
-------------------
.. Add or remove additional features from the list below

- Latest stable release of Ansible (currently v1.9.2)
- Ansible installed from Ubuntu Ansible PPA (trusty)
- Sudo support for the ansible user.
- SSL support out of the box.
- Webmin modules for managing and configuring server.

Usage
-----

For examples of how to use the Ansible appliance, see `Usage`_.

Documentation
-------------
- See the latest documentation at http://docs.ansible.com
- https://github.com/ansible
- http://jpmens.net/2012/06/06/configuration-management-with-ansible/
- http://devopsu.com/guides/ansible-ubuntu-debian.html
- https://github.com/fourkitchens/server-playbooks

Credentials *(passwords set at first boot)*
-------------------------------------------

-  Webmin, SSH: username **root**
-  Ansible: username **ansible**  

.. Edit above to remove references to MySQL, phpMyAdmin, etc if not used in your appliance.  Add a line for additional application credentials, if any, set at first boot.

.. _Usage: docs/usage.rst
.. _Ansible: http://docs.ansible.com/ansible/index.html
.. _TurnKey Core: http://www.turnkeylinux.org/core
