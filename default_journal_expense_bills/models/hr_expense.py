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


class HrExpense(models.Model):

    _inherit = "hr.expense"

    def _get_default_journal(self):
        user = self.env["res.users"].browse(self._uid)
        journal_ids = self.env['account.journal'].search([
            ('type', '=', "purchase"),
            ('company_id', '=', user.company_id.id),
        ])
        if journal_ids:
            expense_journal = journal_ids.filtered(
                lambda r: r.subtype == "expense")

            if expense_journal:
                return expense_journal[0]

            return journal_ids[0]

        return False

    journal_id = fields.Many2one('account.journal',
                                 default=_get_default_journal)
