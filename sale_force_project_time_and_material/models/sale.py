# -*- coding: utf-8 -*-
# © 2016 Pierre Faniel
# © 2016 Niboo SPRL (<https://www.niboo.be/>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from openerp import api, exceptions, models


class SaleOrders(models.Model):
    _inherit = 'sale.order'

    @api.multi
    @api.constrains('order_line')
    def check_invoice_policy(self):
        for order in self:
            for line in order.order_line:
                if line.product_id.invoice_policy == 'cost' \
                        and order.env.user.has_group(
                            'analytic.group_analytic_accounting') \
                        and not order.project_id:
                    raise exceptions.ValidationError(
                        'You must set a project (Analytic Account) for "Time '
                        'and Material" products.')
