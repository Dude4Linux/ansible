Ansible - An IT automation tool
===============================

`Ansible`_ is an IT automation tool. It can configure systems, deploy software,
and orchestrate more advanced IT tasks such as continuous deployments
or zero downtime rolling updates.

This appliance includes all the standard features in `TurnKey Core`_, and on top of that:

- Stable release of Ansible v1.9.4
- Ansible installed via pip
- Sudo support for the ansible user.
- SSL support out of the box.
- Webmin modules for managing and configuring server.

Usage
-----

For examples of how to use the Ansible appliance, see `Usage`_.

Documentation
-------------
- See the latest documentation at http://docs.ansible.com/ansible/
- https://github.com/ansible
- http://jpmens.net/2012/06/06/configuration-management-with-ansible/
- http://devopsu.com/guides/ansible-ubuntu-debian.html
- https://github.com/fourkitchens/server-playbooks

Credentials *(passwords set at first boot)*
-------------------------------------------

-  Webmin, SSH: username **root**
-  Ansible: username **ansible**  


.. _Usage: docs/usage.rst
.. _Ansible: http://docs.ansible.com/ansible/index.html
.. _TurnKey Core: https://www.turnkeylinux.org/core
