# -*- coding: utf-8 -*-
# © 2015 Jérôme Guerriat
# © 2015 Niboo SPRL (<https://www.niboo.be/>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from openerp import api, fields, models


class AccountAnalyticDistributionPlan(models.Model):

    _name = 'account.analytic.distribution.plan'
    _description = 'Analytic Distribution Plan'

    name = fields.Char('Distribution Plan Name',required=True)

    analytic_distribution_ids = fields.Many2many(
        'account.analytic.distribution',
        'account_analytic_distrib_distrib_plan_rel',
        'analytic_distribution_plan_id',
        'analytic_distribution_id',
        'Analytic Distribution')

    @api.constrains('analytic_distribution_ids')
    def check_analytic_distribution_ids(self):
        AccountAnalyticAxis = self.env['account.analytic.axis']
        return AccountAnalyticAxis.check_percent_on_axis(
            self.analytic_distribution_ids)
