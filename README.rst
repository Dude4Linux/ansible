Ansible - Radically simple IT automation platform
=================================================

`Ansible`_ is a simple, agentless IT automation engine that automates
cloud provisioning, configuration management, application deployment and
intra-service ochestration. It can configure systems, deploy software,
and streamline advanced IT tasks such as continuous deployments or zero
downtime rolling updates.

This appliance includes all the standard features in `TurnKey Core`_, and on top of that:

- Latest stable release of Ansible (currently v1.9.2)
- Ansible installed via pip
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

.. _Usage: https://github.com/turnkeylinux-apps/ansible/blob/master/docs/usage.rst
.. _Ansible: http://docs.ansible.com/ansible/index.html
.. _TurnKey Core: https://www.turnkeylinux.org/core
