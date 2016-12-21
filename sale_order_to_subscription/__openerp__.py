# -*- coding: utf-8 -*-
# © 2015 Gael Rabier
# © 2015 Niboo SPRL (<https://www.niboo.be/>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    'name': 'Sale Order to Subscriptions',
    'category': 'sales',
    'summary': 'Creates subscriptions based on sale order',
    'website': 'https://www.niboo.be/',
    'version': '9.0.1.0.0',
    'license': 'AGPL-3',
    'description': """
Creates subscriptions based on sale order, linked to the same analytic account
as the sale order
        """,
    'author': 'Niboo',
    'depends': [
        'account',
        'sale_contract',
    ],
    'data': [
        'data/sale_subscription.xml',
        'views/sale_order.xml',
        'views/sale_subscription.xml',
        'views/account_invoice.xml',
    ],
    'images': [
        'static/description/cover.png',
    ],
    'installable': True,
    'application': False,
}
