# -*- coding: utf-8 -*-
# © 2016 Pierre Faniel
# © 2016 Niboo SPRL (<https://www.niboo.be/>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    'name': 'Timesheet - Work Logger',
    'category': 'HR',
    'summary': 'Log work on timesheets with a wizard',
    'license': 'AGPL-3',
    'website': 'https://www.niboo.be',
    'version': '9.0.1.0.0',
    'description': '''
Allows logging work efficiently on timesheets. The user launches the wizard from
either within the timesheet or a task. There they can define project, task,
product, description, date and hours.
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
    ],
    'images': [
        'static/description/hr_timesheet_work_log_wizard_cover.png',
    ],
    'installable': True,
    'application': False,
}
