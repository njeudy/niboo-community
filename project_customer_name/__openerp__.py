# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Tobias Zehntner
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
    'name': 'Project - Customer Name before Project',
    'category': 'Project',
    'summary': 'Project - Customer name before project name',
    'website': '',
    'version': '9.1.0',
    'description': """
        - Customer name before project name
        """,
    'author': 'Niboo',
    'depends': [
        'project',
    ],
    'data': [
        'views/project_dashboard.xml'
    ],
    'qweb': [
    ],
    'demo': [
    ],
    'css': [
    ],
    'installable': True,
    'application': True,
}
