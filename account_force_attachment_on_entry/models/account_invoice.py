# -*- coding: utf-8 -*-
# © 2016 Jérôme Guerriat
# © 2016 Niboo SPRL (<https://www.niboo.be/>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from openerp import api, exceptions, models, fields


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    @api.multi
    def invoice_validate(self):
        # for each invoice, ensure that there is at least one attached document
        for invoice in self.filtered(lambda inv: inv.type == 'in_invoice'):
            if not self.env['ir.attachment'].search(
                    [('res_model', '=', 'account.invoice'),
                     ('res_id', '=', invoice.id)]):
                raise exceptions.ValidationError(
                    "You have to attach at least one document"
                    " to validate a Vendor Bill.")

        super(AccountInvoice, self).invoice_validate()
