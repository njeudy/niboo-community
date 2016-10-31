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
