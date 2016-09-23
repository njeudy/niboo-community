# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Multiple Analytic Distribution',
    'version': '1.0',
    'category': 'Accounting & Finance',
    'description': """

        """,
    'author': 'Niboo SPRL',
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
        'views/account_move_line.xml',
        'views/account_analytic_distribution.xml',
        'views/account_invoice.xml',
        'views/hr_expense.xml',
        'views/account_asset.xml',
        'views/account_analytic_account.xml',
        'views/account_analytic_axis.xml',
        'views/project_project.xml',
        'views/account_bank_statement.xml',
        'security/account_analytic_plan_security.xml',
        'security/ir.model.access.csv',
        'wizard/account_reconcile_writeoff_view.xml',
    ],
    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
