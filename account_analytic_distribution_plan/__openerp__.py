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
    'name': 'Multiple Analytic Distribution Plan',
    'version': '1.0',
    'category': 'Accounting & Finance',
    'description': """

        """,
    'author': 'Niboo SPRL',
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
    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
