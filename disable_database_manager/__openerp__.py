# -*- coding: utf-8 -*-
# © 2016 Dutry Alexandre
# © 2016 Niboo SPRL (<https://www.niboo.be/>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html)

{
    'name': 'DB Blocking manager',
    'summary': 'Block database manager',
    'description': '''
Prevents any access to the database manager or its features.
    ''',
    'author': 'Niboo',
    'license': 'AGPL-3',
    'website': 'https://www.niboo.be',
    'version': '9.0.1.0.0',
    'depends': [
        'web',
    ],
    'data': [
        'views/webclient_templates.xml',
    ],
    'images': [
        'static/description/disable_database_manager_cover.png',
    ],
    'auto_install': True,
    'installable': True,
    'active': True,
}
