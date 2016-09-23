# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Pierre Faniel
#    Copyright 2016 Niboo SPRL
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
    'name': 'Work Log Wizard',
    'category': 'HR',
    'summary': 'Log work on timesheets with a wizard',
    'website': '',
    'version': '1.0',
    'description': """
        This module allows logging work efficently on timesheets with a wizard.
        The user launches the wizard with a button at the top of the timesheet
        and can define project, task, product, date and hours.
        """,
    'author': 'Niboo',
    'depends': [
        'hr_timesheet',
        'hr_timesheet_task',
        'project',
        'project_timesheet',
    ],
    'data': [
        'views/hr_timesheet.xml',
    ],
    'qweb': [],
    'demo': [
    ],
    'css': [
    ],
    'installable': True,
    'application': False,
}
