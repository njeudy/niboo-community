# -​*- coding: utf-8 -*​-
# © 2016 Tobias Zehntner
# © 2016 Niboo SPRL (<https://www.niboo.be/>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from openerp import fields, models


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    subscription_id = fields.Many2one('sale.subscription',
                                      'Related subscription')
