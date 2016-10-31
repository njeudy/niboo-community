# -*- coding: utf-8 -*-
# © 2015 Jérôme Guerriat, Pierre Faniel
# © 2015 Niboo SPRL (<https://www.niboo.be/>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from openerp import api, fields, models


class AccountAnalyticAccount(models.Model):

    _inherit = 'account.analytic.account'

    analytic_account_axis_id = fields.Many2one(
        'account.analytic.axis', string='Analytic Axis', required=True)

    @api.model
    def default_get(self, fields):
        res = super(AccountAnalyticAccount, self).default_get(fields)
        if 'analytic_account_axis_id' not in res:
            AnalyticAxis = self.env['account.analytic.axis']
            axis = AnalyticAxis.search([], limit=1)
            if not axis:
                axis = AnalyticAxis.create({
                    'name': 'Dummy Axis',
                    'active': False,
                })
            res['analytic_account_axis_id'] = axis.id
        return res
