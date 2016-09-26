# -*- coding: utf-8 -*-
# © 2016 Jérôme Guerriat
# © 2016 Niboo SPRL (<https://www.niboo.be/>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    'name': 'Default Journal for Expenses and Vendor Bills',
    'category': 'Accounting & Finance',
    'summary': 'Automatically select the proper journal for expenses and vendor bills.',
    'website': '',
    'version': '9.1.0',
    'description': '''
        This module selects automatically the proper journal for expenses
        and vendor bills after they have been defined in the accounting
        configuration.

        Choose the subtype for a journal in Account > Configuration > Journal.
        The one that has 'Vendor Bills' or 'Expenses' selected will be
        set as default when creating new records.

        ''',
    'author': 'Niboo',
    'depends': [
        'hr_expense',
        'account'
    ],
    'data': [
        'views/account_journal.xml',
    ],
    'qweb': [
    ],
    'demo': [
    ],
    'css': [
    ],
    'installable': True,
    'application': True,
}
