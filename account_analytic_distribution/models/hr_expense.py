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

class HRExpense(models.Model):

    _inherit = "hr.expense"

    analytic_distribution_ids = fields.Many2many(
        'account.analytic.distribution',
        'account_expense_analytic_distrib_rel',
        'account_exepense_id',
        'analytic_distribution_id',
        string='Analytic Distribution')

    @api.one
    @api.constrains("analytic_distribution_ids")
    def _check_unique_analytic_account_per_move_line(self):
        analytic_accounts = []
        for account_analytic_distrib in self.analytic_distribution_ids:
            aa_id = account_analytic_distrib.analytic_account_id.id
            if aa_id in analytic_accounts:
                raise ValidationError('An analytic account can only be linked'
                                      'once per move.')
            analytic_accounts.append(aa_id)

    @api.model
    def _prepare_move_line(self, line):
        res = super(HRExpense, self)._prepare_move_line(line)
        res['analytic_distribution_ids'] = line.get('analytic_distribution_ids', [])
        return res

    @api.model
    def _move_line_get(self):
        account_move = []
        for expense in self:
            if expense.product_id:
                account = expense.product_id.product_tmpl_id._get_product_accounts()['expense']
                if not account:
                    raise UserError(_("No Expense account found for the product %s (or for it's category), please configure one.") % (expense.product_id.name))
            else:
                account = self.env['ir.property'].with_context(force_company=expense.company_id.id).get('property_account_expense_categ_id', 'product.category')
                if not account:
                    raise UserError(_('Please configure Default Expense account for Product expense: `property_account_expense_categ_id`.'))

            distribution_list = []
            for analytic_distribution in self.analytic_distribution_ids:
                distribution_list.append((4,analytic_distribution.id, False))

            move_line = {
                    'type': 'src',
                    'name': expense.name.split('\n')[0][:64],
                    'price_unit': expense.unit_amount,
                    'quantity': expense.quantity,
                    'price': expense.total_amount,
                    'account_id': account.id,
                    'product_id': expense.product_id.id,
                    'uom_id': expense.product_uom_id.id,
                    'analytic_distribution_ids': distribution_list,
                }
            account_move.append(move_line)

            # Calculate tax lines and adjust base line
            taxes = expense.tax_ids.compute_all(expense.unit_amount, expense.currency_id, expense.quantity, expense.product_id)
            account_move[-1]['price'] = taxes['total_excluded']
            account_move[-1]['tax_ids'] = expense.tax_ids.id
            for tax in taxes['taxes']:
                account_move.append({
                    'type': 'tax',
                    'name': tax['name'],
                    'price_unit': tax['amount'],
                    'quantity': 1,
                    'price': tax['amount'],
                    'account_id': tax['account_id'] or move_line['account_id'],
                    'tax_line_id': tax['id'],
                })
        return account_move

    @api.constrains("analytic_distribution_ids")
    def check_analytic_distribution_ids(self):
        AccountAnalyticAxis = self.env['account.analytic.axis']
        return AccountAnalyticAxis.check_percent_on_axis(
            self.analytic_distribution_ids)
