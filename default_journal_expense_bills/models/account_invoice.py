# -*- coding: utf-8 -*-
# © 2016 Jérôme Guerriat
# © 2016 Niboo SPRL (<https://www.niboo.be/>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from openerp import fields, models


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    def _get_default_journal(self):
        journal_type = self._context.get('journal_type', False)

        # By default, take out_invoice because that's the odoo way
        if not journal_type:
            invoice_type = self._context.get('type', 'out_invoice')
            journal_type = 'purchase'
            if invoice_type in ('out_invoice', 'out_refund'):
                journal_type = 'sale'

        user = self.env['res.users'].browse(self._uid)

        journals = self.env['account.journal'].search([
            ('type', '=', journal_type),
            ('company_id', '=', user.company_id.id),
        ])
        if journals:
            if journal_type == 'purchase':
                journals_filtered = journals.filtered(
                    lambda r: r.subtype == 'vendor_bills')

                if journals_filtered:
                    journals = journals_filtered

            return journals[0]

        return False

    journal_id = fields.Many2one('account.journal',
                                 default=_get_default_journal)
