# -*- coding: utf-8 -*-
# © 2016 Pierre Faniel
# © 2016 Niboo SPRL (<https://www.niboo.be/>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    'name': 'Project - Light Workflow',
    'category': 'Project',
    'summary': 'Add a workflow to project tasks',
    'website': 'https://www.niboo.be/',
    'version': '1.0',
    'description': '''
Allows you to add a new workflow for task with task step
    ''',
    'license': 'AGPL-3',
    'author': 'Niboo',
    'depends': [
        'project',
    ],
    'data': [
        'views/project.xml',
        'security/ir.model.access.csv',
    ],
    'images': [
        'static/description/versioning_cover.png',
    ],
    'installable': True,
    'application': False,
}
