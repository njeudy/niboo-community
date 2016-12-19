# -*- coding: utf-8 -*-
# © 2016 Jérôme Guerriat
# © 2016 Niboo SPRL (<https://www.niboo.be/>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    'name': 'Project - Task Identifier',
    'category': 'Project',
    'summary': 'Add an identifier on tasks (project-sequence number)',
    'website': 'https://www.niboo.be/',
    'version': '10.0.1.0.0',
    'license': 'AGPL-3',
    'author': 'Niboo',
    'depends': [
        'project',
    ],
    'data': [
        'views/project_task_view.xml',
        'views/res_partner_view.xml',
    ],
    'images': [
        'static/description/project_task_identifier_cover.png',
    ],
    'installable': True,
    'application': False,
}
