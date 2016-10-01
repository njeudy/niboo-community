# -*- coding: utf-8 -*-
# © 2016 Jérémy Van Driessche
# © 2016 Niboo SPRL (<https://www.niboo.be/>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    'name': 'Payment Invoice Notification',
    'category': 'Payment',
    'summary': 'Add a notification on the invoice if it is already paid',
    'website': 'https://www.niboo.be/',
    'version': '8.0.1.0.0',
    'author': 'Niboo',
    'license': 'AGPL-3',
    'description': '''
Add a state on the invoice between "open" and "paid".
It will notify that the invoice is already paid but not reconciled.
        ''',
    'depends': [
        'account',
        'account_cancel',
        'payment'
    ],
    'data': [
        'data/invoice_wkf.xml',
        'views/invoice_view.xml',
        'views/report_invoice.xml',
    ],
    'images': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}

