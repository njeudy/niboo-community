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
from openerp import exceptions
from openerp import models


class SaleOrders(models.Model):
    _inherit = 'sale.order'

    @api.multi
    @api.constrains('order_line')
    def check_invoice_policy(self):
        for order in self:
            for line in order.order_line:
                if line.product_id.invoice_policy == 'cost' and \
                        not order.project_id:
                    raise exceptions.ValidationError(
                        'You must set a project for Time and Material'
                        ' products')


