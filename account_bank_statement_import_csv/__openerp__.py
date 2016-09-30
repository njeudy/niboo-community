# -*- encoding: utf-8 -*-
# © 2016 Samuel Lefever, Jerome Sonnet
# © 2016 Niboo SPRL (<https://www.niboo.be/>), Be-Cloud
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    'name': 'Import CSV Bank Statement',
    'category' : 'Accounting & Finance',
    'version': '0.1',
    'author': 'Samuel Lefever (Niboo SPRL), Jerome Sonnet (Be-Cloud)',
    'description' : """
This module allows you to import the machine readable CSV Files from Luxembourg in Odoo: they are parsed and stored in human readable format in
Accounting / Bank and Cash / Bank Statements.

Bank Statements may be generated containing a subset of the CSV information (taking only those transaction lines that are required for the
creation of the Financial Accounting records). 
    
    """,
    'data': ['views/account_csv.xml'],
    'depends': ['account_bank_statement_import'],
    'external_dependencies': {
        'python': ['unicodecsv', 'chardet']
    },
    'demo': [],
    'auto_install': True,
    'installable': True,
}
