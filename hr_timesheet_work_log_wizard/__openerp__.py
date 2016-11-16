# -*- coding: utf-8 -*-
# © 2016 Pierre Faniel
# © 2016 Niboo SPRL (<https://www.niboo.be/>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    'name': 'Timesheet - Work Logger',
    'category': 'HR',
    'summary': 'Makes logging time easy and efficient',
    'license': 'AGPL-3',
    'website': 'https://www.niboo.be',
    'version': '9.0.1.0.0',
    'description': '''
Add a wizard to simply log your work:
- Direct access from timesheets and tasks: click on the Log Work button or directly on the desired timesheet table cell
- Choose a task, and the corresponding project is automatically set
- Makes it possible to specify a product for each entry
- Forces user to specify which project they worked on
- Makes user describe the work they have done
        ''',
    'author': 'Niboo',
    'depends': [
        'project_timesheet',
        'hr_timesheet_task',
    ],
    'data': [
        'wizards/work_log_wizard.xml',
        'views/hr_timesheet.xml',
        'views/project_task.xml',
        'views/analytic_view.xml',
    ],
    'images': [
        'static/description/hr_timesheet_work_log_wizard_cover.png',
    ],
    'installable': True,
    'application': False,
}
