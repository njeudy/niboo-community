# -*- coding: utf-8 -*-
# © 2016 Jerome Guerriat
# © 2016 Niboo SPRL (<https://www.niboo.be/>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    'name': 'Timesheet - Include leaves',
    'category': 'HR',
    'summary': "Keep track of your leaves directly from your timesheet",
    'website': 'http://www.niboo.be',
    'license': 'AGPL-3',
    'version': '9.0.1.0',
    'description': """
    Keep an overview of your leaves by having them displayed directly on your timesheet.
    As soon as a leave is approved, it will show up on the employee's timesheet on a designated line.
        """,
    'author': 'Niboo',
    'depends': [
        'hr_timesheet',
        'hr_timesheet_sheet',
        'hr_holidays',
    ],
    'data': [
        'data/holiday_account.xml',
        'views/view_holiday_request.xml',
        'views/res_company_view.xml',
    ],
    'images': [
      'static/description/hr_holiday_timesheet_cover.png',
    ],
    'installable': False,
    'application': False,
}
