# -*- coding: utf-8 -*-
# © 2015 Gael Rabier
# © 2015 Niboo SPRL (<https://www.niboo.be/>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from openerp import api, exceptions, models
from openerp.osv import orm


class SaleSubscription(models.Model):
    _inherit = 'sale.subscription'

    # Add subscription_id to generated invoice
    @api.model
    def _prepare_invoice_data(self, contract):
        invoice = super(SaleSubscription, self)._prepare_invoice_data(contract)
        invoice['subscription_id'] = contract.id
        return invoice

    # Show only invoices related to subscription
    @api.multi
    def action_subscription_invoice(self):
        self.ensure_one()
        invoice_ids = self.env['account.invoice'].search(
            [('subscription_id', '=', self.id)])
        values = super(SaleSubscription, self).action_subscription_invoice()
        values['domain'] = [['id', 'in', [id.id for id in invoice_ids]]]
        return values

    @api.model
    def create(self, vals):
        account_analytic_id = vals.get('analytic_account_id')

        if account_analytic_id:
            analytic_account = self.env['account.analytic.account'].browse(
                account_analytic_id)
            name = analytic_account.name
            code = analytic_account.code
            del(vals['partner_id'])

        subscription = super(SaleSubscription, self).create(vals)

        if account_analytic_id and analytic_account:
            subscription.write({'name': name, 'code': code})
        return subscription

    @api.multi
    def name_get(self):
        # Ensures that the name remains the the project name
        return orm.BaseModel.name_get(self)

    @api.multi
    def write(self, vals):
        if 'analytic_account_id' in vals:
            raise exceptions.Warning('You can not edit the analytic of a '
                                     'subscription already created.')
        return super(SaleSubscription, self).write(vals)

    # When generating first invoice, set subscription.state to 'in progress'
    @api.multi
    def recurring_invoice(self):
        for subscription in self:
            if subscription.state == 'draft':
                subscription['state'] = 'open'
        return super(SaleSubscription, self).recurring_invoice()
