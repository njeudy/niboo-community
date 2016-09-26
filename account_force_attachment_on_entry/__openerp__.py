# -*- coding: utf-8 -*-
# © 2016 Jérôme Guerriat
# © 2016 Niboo SPRL (<https://www.niboo.be/>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    'name': 'Force attachments on financial entries',
    'category': 'Accounting & Finance',
    'summary': 'Force attachments on Vendor Bill and Expense',
    'website': 'http://www.niboo.be',
    'version': '1.0',
    'description': """
        This module makes it required to attach at least one document to vendor
        bills and expenses before they can be validated/submitted.
        """,
    'author': 'Niboo',
    'depends': [
        'account',
        'hr_expense',
        'document',
    ],
    'data': [
    ],
    'qweb': [],
    'demo': [
    ],
    'css': [
    ],
    'installable': True,
    'application': False,
}
