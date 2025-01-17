====================
POS Payment Terminal
====================

.. 
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! This file is generated by oca-gen-addon-readme !!
   !! changes will be overwritten.                   !!
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! source digest: sha256:27c2e3861ae4059d293af62a9955550f6445c9bdbc2dfcdf364735d1910832d1
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

.. |badge1| image:: https://img.shields.io/badge/maturity-Beta-yellow.png
    :target: https://odoo-community.org/page/development-status
    :alt: Beta
.. |badge2| image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
.. |badge3| image:: https://img.shields.io/badge/github-OCA%2Fpos-lightgray.png?logo=github
    :target: https://github.com/OCA/pos/tree/12.0/pos_payment_terminal
    :alt: OCA/pos
.. |badge4| image:: https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :target: https://translation.odoo-community.org/projects/pos-12-0/pos-12-0-pos_payment_terminal
    :alt: Translate me on Weblate
.. |badge5| image:: https://img.shields.io/badge/runboat-Try%20me-875A7B.png
    :target: https://runboat.odoo-community.org/builds?repo=OCA/pos&target_branch=12.0
    :alt: Try me on Runboat

|badge1| |badge2| |badge3| |badge4| |badge5|

This module adds support for credit card reader and checks printer
in the Point of Sale.

**Table of contents**

.. contents::
   :local:

Installation
============

This module is designed to be installed on the
*main Odoo server*. On the *POSbox*, you should install the module
*hw_x* depending on the protocol implemented in your device.
`Ingenico <http://en.wikipedia.org/wiki/Ingenico>`
and old Sagem devices support the Telium protocol implemented in the
*hw_telium_payment_terminal* module.

Configuration
=============

* Go to Point of Sale > Configuration > Point of Sale, and check
  the field "Payment Terminal"

.. figure:: https://raw.githubusercontent.com/OCA/pos/12.0/pos_payment_terminal/static/description/pos_config_form.png

* Then, in the same point of sale form, click on "Payment Methods" to
  set correctly your account journals.
  This module support two payment modes : *card* and *check*, this
  option is available in te Point of sale tab.

.. figure:: https://raw.githubusercontent.com/OCA/pos/12.0/pos_payment_terminal/static/description/account_journal_form.png

Usage
=====

In the frontend of the POS, when you select a payment method that has a payment mode *card* or *check*, you will have a *Start Transaction* button : if you click on that button, the amount, the currency and the payment mode will be sent to the POSbox.

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/OCA/pos/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us to smash it by providing a detailed and welcomed
`feedback <https://github.com/OCA/pos/issues/new?body=module:%20pos_payment_terminal%0Aversion:%2012.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

Do not contact contributors directly about support or help with technical issues.

Credits
=======

Authors
~~~~~~~

* Aurélien DUMAINE
* GRAP
* Akretion

Contributors
~~~~~~~~~~~~

* Aurelien Dumaine
* Alexis de Lattre <alexis.delattre@akretion.com>
* Sylvain LE GAL (https://twitter.com/legalsylvain)

Maintainers
~~~~~~~~~~~

This module is maintained by the OCA.

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

This module is part of the `OCA/pos <https://github.com/OCA/pos/tree/12.0/pos_payment_terminal>`_ project on GitHub.

You are welcome to contribute. To learn how please visit https://odoo-community.org/page/Contribute.
