# -*- coding: utf-8 -*-
# © 2016 Pierre Faniel
# © 2016 Niboo SPRL (<https://www.niboo.be/>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from openerp import api, exceptions, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.multi
    @api.constrains('state', 'project_id')
    def check_unique_project(self):
        """
        Checks if there is another unclosed sale order for the project
        """
        SaleOrder = self.env['sale.order']
        for order in self:
            if order.state not in ['cancel', 'done'] and SaleOrder.search(
                    [('project_id', '=', order.project_id.id),
                     ('state', 'not in', ['cancel', 'done']),
                     ('id', '!=', order.id)]):
                raise exceptions.ValidationError(
                    'You already have an opened quotation for this project.')
