# -*- coding: utf-8 -*-
# © 2016 Jérôme Guerriat
# © 2016 Niboo SPRL (<https://www.niboo.be/>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from openerp import models, api


class AccountMove(models.Model):
    _inherit = "account.move"

    @api.multi
    def button_cancel(self):
        super(AccountMove, self).button_cancel()
        for move in self:
            for line in move.line_ids:
                line.analytic_line_ids.sudo().unlink()

        return True
