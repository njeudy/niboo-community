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
    'name': 'Project - Scrum',
    'category': "Project",
    'summary': 'Adds the ability to create Sprints and Scrum teams.',
    'website': 'https://www.niboo.be/',
    'version': '9.0.1.0.0',
    'license': 'AGPL-3',
    'description': """
        This module allows you to organize your tasks with the Scrum methodology. Using sprints, you can easily plan when your tasks should be done.
        """,
    'author': 'Niboo',
    'depends': ['project'],
    'data': [
        'views/project_view.xml',
        'security/ir.model.access.csv',
    ],
    'qweb': [],
    'images': [
        'static/description/project_scrum_cover.png',
    ],
    'demo': [
    ],
    'css': [
    ],
    'installable': True,
    'application': True,
}
