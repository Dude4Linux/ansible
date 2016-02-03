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

Resources
---------

- `Latest official Ansible documentation <http://docs.ansible.com>`_
- `Ansible on GitHub <https://github.com/ansible>`_
- `Configuration management with Ansible <http://jpmens.net/2012/06/06/configuration-management-with-ansible/>`_
- `Ansible playbooks for use in setting up servers <https://github.com/fourkitchens/server-playbooks>`_

Credentials *(passwords set at first boot)*
-------------------------------------------

-  Webmin, SSH: username **root**
-  Ansible: username **ansible**  

.. _Usage: https://github.com/turnkeylinux-apps/ansible/blob/master/docs/usage.rst
.. _Ansible: http://docs.ansible.com/ansible/index.html
.. _TurnKey Core: https://www.turnkeylinux.org/core
