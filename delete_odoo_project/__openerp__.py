# -*- coding: utf-8 -*-
# © 2015 Jérôme Guerriat
# © 2015 Niboo SPRL (<https://www.niboo.be/>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).


{
    'name': 'Delete Odoo demo project',
    'category': 'Project',
    'summary': 'Remove the Odoo demo project',
    'website': 'https://www.niboo.be/',
    'version': '9.0.1.0.0',
    'license': 'AGPL-3',
    'description': '''
This module deletes the default project "Start here to discover Odoo", its tasks and analytic account
        ''',
    'author': 'Niboo',
    'depends': [
        'project',
    ],
    'data': [
        'data/project_data.xml',
    ],
    'images': [
        '/static/description/delete_odoo_project_cover.png',
    ],
    'installable': False,
    'application': False,
}
