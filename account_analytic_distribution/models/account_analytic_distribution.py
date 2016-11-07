# -*- coding: utf-8 -*-
# © 2015 Samuel Lefever
# © 2015 Niboo SPRL (<https://www.niboo.be/>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from openerp import api, fields, models


class AccountAnalyticDistribution(models.Model):

    _name = "account.analytic.distribution"
    _description = "Analytic Distribution"
    _rec_name = "name"

    analytic_account_id = fields.Many2one('account.analytic.account',
                                          'Analytic Account',
                                          required=True,)
    name = fields.Char('Name', compute="_compute_name", store=True)
    rate = fields.Float('Rate (%)', required=True)
    move_line_ids = fields.Many2many('account.move.line',
                                     'account_move_line_analytic_distrib_rel',
                                     'analytic_distribution_id',
                                     'move_line_id')

    account_analytic_axis_id = fields.Many2one(
        related='analytic_account_id.analytic_account_axis_id',
        string='Axis',
        readonly=True)

    _defaults = {
        'rate': 100.0
    }

    @api.multi
    @api.depends('analytic_account_id', 'rate')
    def _compute_name(self):
        for analytic_distribution in self:
            aa = analytic_distribution.analytic_account_id
            name = '%s (%s)' % (aa.name, aa.analytic_account_axis_id.name)

            if analytic_distribution.rate:
                name = '%d%% in %s' % (analytic_distribution.rate,
                                       name,)
            analytic_distribution.name = name

    _sql_constraints = [
        ('unique_distribution',
         'UNIQUE (rate, analytic_account_id)',
         'You should only have one distribution for the same rate and account!')
    ]
