# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Aurelien Muller & Jeremy Van Driessche
#    Copyright 2015 Niboo SPRL
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program. If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Web Database Management Security',
    'version': '2.0',
    'category': 'Hidden',
    'summary': 'Disable access to database management',
    'description': """,
Restrict usage of the database manager. Only the create database method is available.
""",
    'author': 'Niboo',
    'depends': ['base'],
    'auto_install': True,
    'data': [
    ],

    'bootstrap': True,
    #'installable': False,
}
