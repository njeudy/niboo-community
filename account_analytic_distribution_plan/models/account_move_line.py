# -*- coding: utf-8 -*-
# © 2015 Samuel Lefever
# © 2015 Niboo SPRL (<https://www.niboo.be/>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from openerp import api, fields, models


class AccountMoveLine(models.Model):

    _inherit = 'account.move.line'

    distribution_plan_id = fields.Many2one(
        'account.analytic.distribution.plan', 'Distribution Plan')

    @api.onchange('distribution_plan_id')
    def _onchange_distribution_plan_id(self):
        self.analytic_distribution_ids = \
            self.distribution_plan_id.analytic_distribution_ids

    def _create_writeoff(self, vals):
        writeoff = super(AccountMoveLine, self)._create_writeoff(vals)
        if self._context.get('analytic_distribution_ids'):
            move = writeoff.move_id
            impact_line = move.line_ids.filtered(
                lambda r: r.account_id.id == vals['account_id'])

            for line in impact_line:
                line.analytic_distribution_ids =\
                self._context.get('analytic_distribution_ids')
        return writeoff
