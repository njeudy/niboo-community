# -*- coding: utf-8 -*-
# © 2015 Samuel Lefever
# © 2015 Niboo SPRL (<https://www.niboo.be/>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from openerp import api, models


class AccountMoveLine(models.Model):

    _inherit = 'account.move.line'

    @api.one
    def _prepare_analytic_lines(self):
        '''
        Prepare the values used to create() an account.analytic.line upon
        validation of an account.move.line having an analytic account.
        This method is intended to be extended in other modules.
        '''
        vals_list = super(AccountMoveLine, self)._prepare_analytic_lines()[0]
        for vals in vals_list:
            AnalyticAccount = self.env['account.analytic.account']
            account_analytic = AnalyticAccount.browse(vals['account_id'])
            currency = self.company_id.currency_id
            if currency != account_analytic.currency_id:
                vals['amount'] = currency.compute(
                    vals['amount'], account_analytic.currency_id)
        return vals_list
