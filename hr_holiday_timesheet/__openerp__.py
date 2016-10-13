# -*- coding: utf-8 -*-
# © 2016 Jerome Guerriat
# © 2016 Niboo SPRL (<https://www.niboo.be/>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    'name': 'HR - Holiday On Timesheet',
    'category': 'HR',
    'summary': "Timesheet shows employee's holidays",
    'website': '',
    'version': '9.1.0',
    'description': """
    When a leave is approved, this module create analytic lines for the holidays to appear in the timesheet
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
    'qweb': [
    ],
    'demo': [
    ],
    'css': [
    ],
    'images': [
      'static/description/hr_holiday_timesheet_cover.png',
    ],
    'installable': True,
    'application': True,
}
