# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Benoit Forgette
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
    'name': 'HR - Timesheets design',
    'category': 'HR',
    'summary': 'An awsome presentation',
    'website': '',
    'version': '9.1.0',
    'description': """
        Display the timesheet in a more convenient way
        """,
    'author': 'Niboo',
    'depends': [
        'hr_timesheet',
        'hr_timesheet_sheet',
        'hr_timesheet_task',
    ],
    'data': [
        'views/hr_timesheet_assets.xml',
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
