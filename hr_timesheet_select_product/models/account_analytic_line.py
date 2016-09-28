# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Pierre Faniel
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
from openerp import api
from openerp import models


class AccountAnalyticLine(models.Model):
    _inherit = 'account.analytic.line'

    def _get_sale_order_line(self, vals=None):
        result = dict(vals or {})
        if self.is_timesheet:
            if result.get('so_line'):
                sol = self.env['sale.order.line'].browse([result['so_line']])
            else:
                sol = self.so_line

            if sol and sol.product_id != self.product_id:
                sol = False

            if not sol and self.account_id and self.product_id:
                domain = [
                    ('order_id.project_id', '=', self.account_id.id),
                    ('state', '=', 'sale'),
                    ('product_id.track_service', '=', 'timesheet'),
                    ('product_id.type', '=', 'service'),
                    ('product_id','=',self.product_id.id)]
                sol = self.env['sale.order.line'].search(domain, limit=1)
            if sol:
                result.update({
                    'so_line': sol.id,
                    'product_id': sol.product_id.id,
                })
                result = self._get_timesheet_cost(result)

        result = super(AccountAnalyticLine, self)._get_sale_order_line(
            vals=result)
        return result
