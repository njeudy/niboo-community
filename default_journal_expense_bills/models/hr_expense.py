# -*- coding: utf-8 -*-
# © 2016 Jérôme Guerriat
# © 2016 Niboo SPRL (<https://www.niboo.be/>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from openerp import fields, models


class HrExpense(models.Model):
    _inherit = 'hr.expense'

    def _get_default_journal(self):
        user = self.env['res.users'].browse(self._uid)
        journal_ids = self.env['account.journal'].search([
            ('type', '=', 'purchase'),
            ('company_id', '=', user.company_id.id),
        ])
        if journal_ids:
            expense_journal = journal_ids.filtered(
                lambda r: r.subtype == 'expense')

            if expense_journal:
                return expense_journal[0]

            return journal_ids[0]

        return False

    journal_id = fields.Many2one('account.journal',
                                 default=_get_default_journal)
