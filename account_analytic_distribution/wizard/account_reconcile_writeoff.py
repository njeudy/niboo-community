# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Jérôme Guerriat
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

from openerp import models, fields, api
import logging

_logger = logging.getLogger(__name__)


class AccountMoveLineReconcileWriteoff(models.Model):

    _inherit = "account.move.line.reconcile.writeoff"

    analytic_distribution_ids = fields.Many2many(
        'account.analytic.distribution',
        'account_move_line_reconcile_writeoff_analytic_distrib_rel',
        'writeoff_line_id',
        'analytic_distribution_id',
        string='Analytic Distribution')

    @api.multi
    def trans_rec_reconcile(self):
        if self.analytic_distribution_ids:
            return super(AccountMoveLineReconcileWriteoff,
                         self.with_context(analytic_distribution_ids=
                                           self.analytic_distribution_ids)
                         ).trans_rec_reconcile()
        else:
            return super(AccountMoveLineReconcileWriteoff,
                         self).trans_rec_reconcile()
