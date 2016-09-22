# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Samuel Lefever
#    Copyright 2015 Niboo SPRL
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
from openerp.exceptions import ValidationError
from openerp.tools.translate import _


class AccountInvoiceLine(models.Model):

    _inherit = "account.invoice.line"

    analytic_distribution_ids = fields.Many2many(
        'account.analytic.distribution',
        'account_invoice_line_analytic_distrib_rel',
        'account_invoice_line_id',
        'analytic_distribution_id',
        string='Analytic Distribution')

    @api.one
    @api.constrains("analytic_distribution_ids")
    def _check_unique_analytic_account_per_move_line(self):
        analytic_accounts = []
        for account_analytic_distrib in self.analytic_distribution_ids:
            aa_id = account_analytic_distrib.analytic_account_id.id
            if aa_id in analytic_accounts:
                raise ValidationError('An analytic account can only be linked'
                                      'once per move.')
            analytic_accounts.append(aa_id)

    @api.constrains("analytic_distribution_ids")
    def check_analytic_distribution_ids(self):
        AccountAnalyticAxis = self.env['account.analytic.axis']
        return AccountAnalyticAxis.check_percent_on_axis(
            self.analytic_distribution_ids)


class AccountInvoice(models.Model):

    _inherit = "account.invoice"

    @api.model
    def line_get_convert(self, line, part):
        AccountInvoiceLine = self.env['account.invoice.line']
        res = super(AccountInvoice, self).line_get_convert(line, part)

        invoice_line = AccountInvoiceLine.browse(line.get('invl_id'))
        distribution_list = []
        for analytic_distribution in invoice_line.analytic_distribution_ids:
            distribution_list.append((4,analytic_distribution.id, False))
        res['analytic_distribution_ids'] = distribution_list
        return res
