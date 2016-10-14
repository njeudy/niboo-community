# -*- coding: utf-8 -*-
# © 2016 Jérôme Guerriat
# © 2016 Niboo SPRL (<https://www.niboo.be/>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    'name': 'Account - delete analytic lines from cancelled move',
    'category': 'Accounting & Finance',
    'summary': 'Delete analytic lines when move is cancelled',
    'website': 'https://www.niboo.be/',
    'version': '9.0.1.0.0',
    'license': 'AGPL-3',
    'description': """
This module deletes the corresponding analytic lines when an account move is cancelled.
        """,
    'author': 'Niboo SPRL',
    'website': 'https://www.niboo.be',
    'depends': [
        'account_accountant',
        'account_cancel',
        'analytic',
    ],
    'data': [

    ],
    'images': [
        'static/description/delete_analytic_lines_cover.png',
    ],
    'demo': [],
    'test': [],
    'installable': True,
    'application': False,
}

