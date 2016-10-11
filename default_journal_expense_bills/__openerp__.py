# -*- coding: utf-8 -*-
# © 2016 Jérôme Guerriat
# © 2016 Niboo SPRL (<https://www.niboo.be/>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    'name': 'Account - Default Journal for Expense and Vendor Bill',
    'category': 'Accounting & Finance',
    'summary': 'Automatically select the proper journal for expenses and vendor bills.',
    'website': 'https://odoo-community.org/',
    'license': 'AGPL-3',
    'version': '9.0.1.0.0',
    'description': '''
        This module selects automatically the proper journal for expenses
        and vendor bills after they have been defined in the accounting
        configuration.

        Configuration
        =============
        Choose the subtype for a journal in Account > Configuration > Journal:
        Set the journal for Vendor Bills to
        - Type: Purchase
        - Subtype: Vendor Bills
        Set the journal for Expenses to
        - Type: Purchase
        - Subtype: Expenses

        The journal that has 'Vendor Bills' or 'Expenses' selected will be set as
        default when creating the corresponding new records. Please note that
        the journal type must be set to 'Purchase'.

        ''',
    'author': 'Niboo, Odoo Community Association (OCA)',
    'depends': [
        'hr_expense',
        'account'
    ],
    'data': [
        'views/account_journal.xml',
    ],
    'images': [
        'static/description/default_journal_expense_bills_cover.png',
    ],
    'installable': True,
    'application': False,
}
