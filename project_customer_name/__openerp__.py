# -*- coding: utf-8 -*-
# © 2016 Tobias Zehntner
# © 2016 Niboo SPRL (<https://www.niboo.be/>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    'name': 'Project - Customer name',
    'category': 'Project',
    'summary': 'Put customer name on projects tiles',
    'website': 'https://www.niboo.be/',
    'version': '9.0.1.0.0',
    'description': """
        This module puts the customer names on the projects tiles and the taks tiles.
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
    'images': [
    ],
    'demo': [
    ],
    'css': [
    ],
    'installable': True,
    'application': True,
}
