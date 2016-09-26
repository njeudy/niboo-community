# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Jerome Guerriat
#    Copyright 2016 Niboo SPRL
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

from openerp import fields
from openerp import models
from openerp import api
from openerp import _
from openerp.exceptions import Warning


class AccountJournal(models.Model):

    _inherit = "account.journal"

    subtype = fields.Selection([
        ('expense', 'Expenses'),
        ('vendor_bills', 'Vendor Bills'),
        ('other', 'Other'),
    ])


class AccountChartTemplate(models.Model):
    _inherit = "account.chart.template"
    _description = "Templates for Account Chart"

    @api.multi
    def _prepare_all_journals(self, acc_template_ref, company, journals_dict=None):
        journal_data = super(AccountChartTemplate, self)._prepare_all_journals(
            acc_template_ref, company, journals_dict)

        for item in journal_data:
            if item['name'] == 'Vendor Bills':
                item['subtype'] = "vendor_bills"

        return journal_data
