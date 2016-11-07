# -*- coding: utf-8 -*-
# © 2015 Samuel Lefever
# © 2015 Niboo SPRL (<https://www.niboo.be/>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    'name': 'Multiple Analytic Distribution Plan',
    'version': '9.0.1.0.0',
    'summary': 'Manage analytic accounting through multiple universe with the possibility to prepare distribution to reuse',
    'category': 'Accounting & Finance',
    'description': """
This module allows you to prepare plan for recurring distribution (like salary)
        """,
    'author': 'Niboo',
    'website': 'https://www.niboo.be',
    'depends': ['account_analytic_distribution'],
    'data': [
        'views/account_analytic_distribution_plan.xml',
        'views/account_invoice.xml',
        'views/account_asset_category.xml',
        'views/account_move_line.xml',
        'views/account_bank_statement.xml',
        'views/hr_expense.xml',
        # 'views/account_move_line.xml',
        'security/ir.model.access.csv',
        'wizard/account_reconcile_writeoff_view.xml',
    ],
    'images': [
        'static/description/cover.png',
    ],
    'installable': True,
    'auto_install': False,
}
