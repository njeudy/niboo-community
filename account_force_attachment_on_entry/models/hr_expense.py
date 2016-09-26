# -*- coding: utf-8 -*-
# © 2016 Jérôme Guerriat
# © 2016 Niboo SPRL (<https://www.niboo.be/>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from openerp import api, exceptions, models, fields


class HrExpense(models.Model):
    _inherit = "hr.expense"

    @api.multi
    def submit_expenses(self):
        # require the attachment on submitting an expense
        for expense in self:
            if not self.env['ir.attachment'].search(
                    [('res_model', '=', 'hr.expense'),
                     ('res_id', '=', expense.id)]):
                raise exceptions.ValidationError(
                    "You have to attach at least one document"
                    " to submit an expense.")

        super(HrExpense, self).submit_expenses()
