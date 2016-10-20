# -*- coding: utf-8 -*-
# © 2016 Pierre Faniel
# © 2016 Niboo SPRL (<https://www.niboo.be/>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    'name': 'HR - Timesheets design',
    'category': 'HR',
    'summary': 'A more user-friendly timesheet',
    'website': 'https://www.niboo.be/',
    'version': '9.0.1.0.0',
    'license': 'AGPL-3',
    'description': """
        Groups the tasks on a timesheet by customer and gives the option to easily hide tasks.
        """,
    'author': 'Niboo',
    'depends': [
        'hr_timesheet',
        'hr_timesheet_sheet',
        'hr_timesheet_task',
    ],
    'data': [
        'views/hr_timesheet.xml',
        'views/hr_timesheet_assets.xml',
    ],
    'qweb': [
        'static/src/xml/hr_timesheet.xml',
    ],
    'demo': [
    ],
    'css': [

    ],
    'images': [
        'static/description/timesheet_cover.png',
    ],
    'installable': True,
    'application': True,
}
