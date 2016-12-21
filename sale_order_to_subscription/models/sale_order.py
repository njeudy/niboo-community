# -*- coding: utf-8 -*-
# © 2015 Gael Rabier
# © 2015 Niboo SPRL (<https://www.niboo.be/>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from openerp import api, fields, models
from dateutil.relativedelta import relativedelta
from datetime import date


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    subscription_id = fields.Many2one('sale.subscription', 'Subscription')

    @api.multi
    def action_confirm(self):
        super(SaleOrder, self).action_confirm()
        for order in self:
            order.create_contract()

    def create_contract(self):
        """ Create a contract based on the order's quote template's contract
        template """
        self.ensure_one()

        if any(self.order_line.mapped('product_id').mapped(
                'recurring_invoice')):

            subscription_values = self._prepare_contract_data()

            invoice_line_ids = []
            product = False
            for line in self.order_line:
                if line.product_id and line.product_id.recurring_invoice:
                    invoice_line_ids.append((0, 0, {
                        'product_id': line.product_id.id,
                        'name': line.name,
                        'sold_quantity': line.product_uom_qty,
                        'discount': line.discount,
                        'uom_id': line.product_uom.id,
                        'price_unit': line.price_unit,
                    }))
                    product = line.product_id
            if invoice_line_ids:
                subscription_values.update({
                    'recurring_invoice_line_ids': invoice_line_ids,
                    'analytic_account_id': self.project_id.id,
                })

                deferred_revenue_category = product.deferred_revenue_category_id
                if deferred_revenue_category:
                    subscription_values.update({
                        'asset_category_id': deferred_revenue_category.id,
                    })

            subscription = self.env['sale.subscription'].\
                create(subscription_values)

            if subscription:
                self.subscription_id = subscription.id

    def _prepare_contract_data(self):
        template = self.env.ref(
            'sale_order_to_subscription.subscription_generic_template')
        values = {
            'state': 'open',
            'code': self.project_id.code,
            'type': 'contract',
            'template_id': template.id,
            'partner_id': self.partner_id.id,
            'manager_id': self.user_id.id,
            'date_start': fields.Date.today(),
            'description': self.note,
            'pricelist_id': self.pricelist_id.id,
            'recurring_rule_type': template.recurring_rule_type,
            'recurring_interval': template.recurring_interval,
        }
        # compute the next date
        today = date.today()
        periods = {'daily': 'days', 'weekly': 'weeks',
                   'monthly': 'months', 'yearly': 'years'}
        invoicing_period = relativedelta(
            **{periods[values['recurring_rule_type']]:
                values['recurring_interval']})
        recurring_next_date = today + invoicing_period
        values['recurring_next_date'] = fields.Date.to_string(
                recurring_next_date)

        return values

    _sql_constraints = [
        ('project_id_exists_when_needed',
         'CHECK ((state IN (\'sent\',\'sale\',\'done\') '
            'AND project_id IS NOT NULL ) '
            'OR state NOT IN (\'sent\',\'sale\',\'done\'))',
         'An analytic account is needed when sale order are not draft or '
         'canceled'),
    ]
