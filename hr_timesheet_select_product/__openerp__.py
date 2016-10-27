# -*- coding: utf-8 -*-
# © 2016 Pierre Faniel
# © 2016 Niboo SPRL (<https://www.niboo.be/>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    'name': 'Timesheet - Select product',
    'category': 'HR',
    'summary': 'Select a product for each timesheet entry',
    'website': 'https://www.niboo.be/',
    'version': '9.0.1.0.0',
    'license': 'AGPL-3',
    'description': '''
Create precise invoices by allowing employees to select a service product for each timesheet log.
This makes it possible to keep an overview on logged hours differentiated by seniority and pay grade.
        ''',
    'author': 'Niboo',
    'depends': ['sale_timesheet', 'project_timesheet', 'hr_timesheet_sheet'],
    'data': [
        'views/project_task.xml',
    ],
    'images': [
        'static/description/hr_timesheet_select_product_cover.png',
    ],
    'installable': True,
    'application': False,
}
