# -*- coding: utf-8 -*-
# © 2015 Samuel Lefever
# © 2015 Niboo SPRL (<https://www.niboo.be/>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    'name': 'Multiple Analytic Distribution Cross Company',
    'summary': 'Manage analytic accounting through multiple companies',
    'version': '9.0.1.0.0',
    'category': 'Accounting & Finance',
    'license': 'AGPL-3',
    'description': '''
Manage your analytic accounting for your multiple companies and universe in Odoo.
        ''',
    'author': 'Niboo',
    'website': 'https://www.niboo.be',
    'depends': [
        'account_analytic_distribution'
    ],
    'data': [
        'report/account_analytic_report_view.xml',
        'security/account_analytic_plan_security.xml',
        'security/ir.model.access.csv',
        'views/webclient_templates.xml',
        'views/account_analytic_view.xml',
    ],
    'images': [
        'static/description/cover.png',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
