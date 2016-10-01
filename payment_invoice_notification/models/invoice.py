# -*- coding: utf-8 -*-
# © 2016 Jérémy Van Driessche
# © 2016 Niboo SPRL (<https://www.niboo.be/>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from openerp import fields, models


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    state = fields.Selection('_get_invoice_state',
                             help='''
* The 'Draft' status is used when a user is encoding a new and unconfirmed Invoice.
* The 'Pro-forma' when invoice is in Pro-forma status,invoice does not have an invoice number.
* The 'Mark as paid' status is used when invoice is paid but not reconciled.
* The 'Open' status is used when user create invoice,a invoice number is generated.Its in open status till user does not pay invoice.
* The 'Paid' status is set automatically when the invoice is paid. Its related journal entries may or may not be reconciled.
* The 'Cancelled' status is used when user cancel invoice.
             ''')

    def _get_invoice_state(self):
        return [
            ('draft', 'Draft'),
            ('markaspaid', 'Mark as paid'),
            ('proforma', 'Pro-forma'),
            ('proforma2', 'Pro-forma'),
            ('open', 'Open'),
            ('paid', 'Paid'),
            ('cancel', 'Cancelled'),
        ]
