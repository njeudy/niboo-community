# -*- coding: utf-8 -*-
# © 2016 Pierre Faniel
# © 2016 Niboo SPRL (<https://www.niboo.be/>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    'name': 'Project - Version Management',
    'category': 'Project',
    'summary': 'Allows to add a version on project and task',
    'website': 'https://www.niboo.be/',
    'version': '9.0.1.0.0',
    'description': '''
Allows to add a version on project and task.
    ''',
    'author': 'Niboo',
    'depends': [
        'project',
    ],
    'data': [
        'data/project_version_state.xml',
        'views/project.xml',
        'views/project_version_state.xml',
    ],
    'installable': True,
    'application': False,
}
