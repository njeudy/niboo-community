# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Joël Grand-Guillaume, modified by Van Driessche Jérémy
#    Copyright 2010-2015 Camptocamp SA
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Payment Invoice Notification',
    'category': 'Payment',
    'summary': 'Add a notification on the invoice if it is already paid',
    'website': '',
    'version': '1.0',
    'description': """
Add a state on the invoice between "open" and "paid"
It will notify that the invoice is already paid but not reconcilied.
        """,
    'author': 'Niboo',
    'depends': ['account','account_cancel','payment'],
    'data': [
        'data/invoice_wkf.xml',
        'views/invoice_view.xml',
        'views/report_invoice.xml',
    ],
    'qweb': [],
    'demo': [
    ],
    'css': [
    ],
    'installable': True,
    'application': True,
    'auto_install': True,
}

