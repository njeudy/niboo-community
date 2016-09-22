# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Samuel Lefever
#    Copyright 2015 Niboo SPRL
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
from openerp import api
from openerp.exceptions import ValidationError
from openerp.tools.translate import _

class AccountMoveLine(models.Model):

    _inherit = "account.move.line"

    distribution_plan_id = fields.Many2one('account.analytic.distribution.plan',
                                              string="Distribution Plan",)

    @api.onchange('distribution_plan_id')
    def _onchange_distribution_plan_id(self):
        self.analytic_distribution_ids = \
            self.distribution_plan_id.analytic_distribution_ids

    def _create_writeoff(self, vals):
        writeoff = super(AccountMoveLine, self)._create_writeoff(vals)
        if self._context.get("analytic_distribution_ids"):
            move = writeoff.move_id
            impact_line = move.line_ids.filtered(
                lambda r: r.account_id.id == vals['account_id'])

            for line in impact_line:
                line.analytic_distribution_ids =\
                self._context.get("analytic_distribution_ids")

        return writeoff
