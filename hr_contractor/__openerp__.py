# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Samuel Lefever
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
    'name': 'HR - Contractor',
    'category': 'HR',
    'summary': "Add a limited access group for project and timesheet management",
    'website': '',
    'version': '9.1.0',
    'description': """
    Add a group that has no access to customer, projects and analytic accounts.
    Access will be given only with "Followers".
        """,
    'author': 'Niboo',
    'depends': [
        'project',
        'project_timesheet',
    ],
    'data': [
        "security/ir_rule.xml",
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
