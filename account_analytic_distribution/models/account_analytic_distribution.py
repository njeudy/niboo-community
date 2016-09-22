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
