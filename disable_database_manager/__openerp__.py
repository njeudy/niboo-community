# -*- coding: utf-8 -*-
# © 2016 Dutry Alexandre
# © 2016 Niboo SPRL (<https://www.niboo.be/>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html)

{
    'name': 'DB Blocking manager',

    'summary': 'Block database manager',

    'description': '''
Prevents any access to the database manager or its functionalities.
    ''',

    'author': 'Niboo',
    'website': 'http://www.niboo.be',

    'version': '0.1',

    'depends':['web'],

    'data': [
        'views/webclient_templates.xml',
    ],

    'auto_install': True,
    'installable': True,
    'active': True,
}
