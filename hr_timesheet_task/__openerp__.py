# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Jérôme Guerriat
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
    'name': 'HR - Tasks In Timesheets',
    'category': 'HR',
    'summary': 'Allow the user to select task in a timesheet',
    'website': '',
    'version': '9.1.0',
    'description': """
    The user is now able to select a task in a timesheet
        """,
    'author': 'Niboo',
    'depends': [
        'hr_timesheet_sheet',
        'project_timesheet',
    ],
    'data': [
        'views/hr_timesheet_assets.xml',
        'views/hr_timesheet_view.xml',
    ],
    'qweb': [
        'static/src/xml/hr_timesheet.xml',
    ],
    'demo': [
    ],
    'css': [
    ],
    'installable': True,
    'application': True,
}
