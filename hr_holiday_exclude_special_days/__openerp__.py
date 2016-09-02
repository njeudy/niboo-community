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
    'name': 'Leave: exclude weekends and public holidays',
    'category': 'Human Resources',
    'summary': 'Module to exclude weekends and public holidays from leave days',
    'website': '',
    'version': '9.1.0',
    'description': """
Module to modify the HR leave:

- Weekends and Public Holidays can be automatically excluded when counting the number of leave days.

        """,
    'author': 'Niboo',
    'depends': [
        'hr_holidays',
    ],
    'data': [
        'views/public_holiday.xml',
        'views/hr_holiday_views.xml',
        'views/res_company.xml',
        'security/ir.model.access.csv',
    ],
    'qweb' : [
    ],
    'demo': [
    ],
    'css': [
    ],
    'installable': True,
    'application': True,
}
