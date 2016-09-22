# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Jérôme Guerriat
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

class AccountAnalyticDistributionPlan(models.Model):

    _name = "account.analytic.distribution.plan"
    _description = "Analytic Distribution Plan"

    name = fields.Char("Distribution Plan Name",required=True)

    analytic_distribution_ids = fields.Many2many(
        'account.analytic.distribution', # related object
        'account_analytic_distrib_distrib_plan_rel', # name of the table
        'analytic_distribution_plan_id', # name of "these" id
        'analytic_distribution_id', # name of "those" id
        string='Analytic Distribution')

    @api.constrains("analytic_distribution_ids")
    def check_analytic_distribution_ids(self):
        AccountAnalyticAxis = self.env['account.analytic.axis']
        return AccountAnalyticAxis.check_percent_on_axis(
            self.analytic_distribution_ids)
