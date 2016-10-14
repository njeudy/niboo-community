# -*- coding: utf-8 -*-
# © 2016 Pierre Faniel
# © 2016 Niboo SPRL (<https://www.niboo.be/>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    'name': 'Force selection of project on sale order',
    'category': 'Sales Management',
    'summary': 'Force selection of project on sale order containing time and material products',
    'website': 'https://www.niboo.be/',
    'version': '9.0.1.0.0',
    'license': 'AGPL-3',
    'description': """
        On a Sale Order, this module will make the field 'Project' a requirement
        if the order contains a product which invoice policy is based on time and
        material. This applies only if the project field is visible, i.e.
        the user has the group 'Analytic Accounting'.
        """,
    'author': 'Niboo',
    'depends': ['sale'],
    'images': [
        'static/description/sale_force_project_time_and_material_cover.png',
    ],
    'installable': True,
    'application': False,
}
