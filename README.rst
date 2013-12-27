#MyApp# - Descriptive Title
=======================================

`#MyApp#`_ is an open source application licensed under the GPL.

Description or Purpose
----------------------
.. Briefly describe what the appliance does 

This appliance includes all the standard features in `TurnKey Core`_,
and on top of that:

Additional Features
-------------------
.. Add or remove additional features from the list below

- SSL support out of the box.
- `PHPMyAdmin`_ administration frontend for MySQL (listening on port
  12322 - uses SSL).
- Postfix MTA (bound to localhost) to allow sending of email (e.g.,
  password recovery).
- Webmin modules for configuring Apache2, PHP, MySQL and Postfix.

Credentials *(passwords set at first boot)*
-------------------------------------------

-  Webmin, SSH, MySQL, phpMyAdmin: username **root**

.. Edit above to remove references to MySQL, phpMyAdmin, etc if not used in your appliance.  Add a line for additional application credentials, if any, set at first boot.

.. _#MyApp#: http://www.#MyApp#.org
.. _TurnKey Core: http://www.turnkeylinux.org/core
.. _PHPMyAdmin: http://www.phpmyadmin.net
