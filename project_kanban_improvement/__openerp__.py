# -*- coding: utf-8 -*-
# © 2016 Pierre Faniel
# © 2016 Niboo SPRL (<https://www.niboo.be/>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    'name': 'Project Kanban Improvement',
    'category': 'Project',
    'summary': 'Project - Kanban view design improvement',
    'website': 'https://www.niboo.be/',
    'version': '9.0.1.0.0',
    'license': 'AGPL-3',
    'description': '''
        - Customer's logo added in project Kanban box.
        - When when clicking on the project title, goes directly to project edition mode.
        ''',
    'author': 'Niboo',
    'depends': [
        'project',
    ],
    'data': [
        'views/project_dashboard.xml',
    ],
    'installable': True,
    'application': False,
}
