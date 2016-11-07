# -*- coding: utf-8 -*-
# © 2015 Samuel Lefever, Jérôme Guerriat
# © 2015 Niboo SPRL (<https://www.niboo.be/>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    'name': 'Multiple Analytic Distribution',
    'version': '9.0.1.0.0',
    'category': 'Accounting & Finance',
    'License': 'AGPL-3',
    'summary': 'Distribute your accounting move through multiple universe',
    'description': """
With this module, you can allocate multiple times the same amount to different analytic account.
        """,
    'author': 'Niboo',
    'website': 'https://www.niboo.be',
    'depends': [
        'account',
        'hr_expense',
        'account_asset',
        'delete_odoo_project',
        'account_deferred_revenue',
    ],
    'data': [
        'data/project_data.xml',
        'data/ir_model_data.xml',
        'security/account_analytic_plan_security.xml',
        'security/ir.model.access.csv',
        'views/account_move_line.xml',
        'views/account_analytic_distribution.xml',
        'views/account_invoice.xml',
        'views/hr_expense.xml',
        'views/account_asset.xml',
        'views/account_analytic_account.xml',
        'views/account_analytic_axis.xml',
        'views/project_project.xml',
        'views/account_bank_statement.xml',
        'wizard/account_reconcile_writeoff_view.xml',
    ],
    'images': [
        'static/description/cover.png',
    ],
    'installable': True,
    'auto_install': False,
}
