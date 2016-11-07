# -*- coding: utf-8 -*-
# © 2015 Samuel Lefever
# © 2015 Niboo SPRL (<https://www.niboo.be/>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from openerp import api, exceptions, fields, models


class AccountInvoiceLine(models.Model):

    _inherit = 'account.invoice.line'

    analytic_distribution_ids = fields.Many2many(
        'account.analytic.distribution',
        'account_invoice_line_analytic_distrib_rel',
        'account_invoice_line_id',
        'analytic_distribution_id',
        string='Analytic Distribution')

    @api.one
    @api.constrains('analytic_distribution_ids')
    def _check_unique_analytic_account_per_move_line(self):
        analytic_accounts = []
        for account_analytic_distrib in self.analytic_distribution_ids:
            aa_id = account_analytic_distrib.analytic_account_id.id
            if aa_id in analytic_accounts:
                raise exceptions.ValidationError(
                    'An analytic account can only be linked once per move.')
            analytic_accounts.append(aa_id)

    @api.constrains('analytic_distribution_ids')
    def check_analytic_distribution_ids(self):
        AccountAnalyticAxis = self.env['account.analytic.axis']
        return AccountAnalyticAxis.check_percent_on_axis(
            self.analytic_distribution_ids)


class AccountInvoice(models.Model):

    _inherit = 'account.invoice'

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
