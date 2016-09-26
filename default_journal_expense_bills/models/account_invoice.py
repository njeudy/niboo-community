# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Jerome Guerriat
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

from openerp import fields
from openerp import models


class AccountInvoice(models.Model):

    _inherit = "account.invoice"

    def _get_default_journal(self):
        journal_type = self._context.get('journal_type', False)

        # By default, take out_invoice because that's the odoo way
        if not journal_type:
            invoice_type = self._context.get('type', 'out_invoice')
            journal_type = 'purchase'
            if invoice_type in ('out_invoice', 'out_refund'):
                journal_type = 'sale'

        user = self.env["res.users"].browse(self._uid)

        journals = self.env['account.journal'].search([
            ('type', '=', journal_type),
            ('company_id', '=', user.company_id.id),
        ])
        if journals:
            if journal_type == 'purchase':
                journals_filtered = journals.filtered(
                    lambda r: r.subtype == "vendor_bills")

                if journals_filtered:
                    journals = journals_filtered

            return journals[0]

        return False

    journal_id = fields.Many2one('account.journal',
                                 default=_get_default_journal)
