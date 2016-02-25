# -*- coding: utf-8 -*-

{
    'name': 'Payment Invoice Notification',
    'category': 'Payment',
    'summary': 'Add a notification on the invoice if it is already paid',
    'website': '',
    'version': '1.0',
    'description': """
Add a state on the invoice between "open" and "paid"
It will notify that the invoice is already paid but not reconcilied.
        """,
    'author': 'Niboo',
    'depends': ['account','account_cancel','payment'],
    'data': [
        'data/invoice_wkf.xml',
        'views/invoice_view.xml',
        'views/report_invoice.xml',
    ],
    'qweb': [],
    'demo': [
    ],
    'css': [
    ],
    'installable': True,
    'application': True,
    'auto_install': True,
}

