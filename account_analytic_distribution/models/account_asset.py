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


class AccountAssetAsset(models.Model):
    _inherit = 'account.asset.asset'

    analytic_distribution_ids = fields.Many2many(
        'account.analytic.distribution',
        'account_asset_asset_analytic_distrib_rel',
        'account_asset_asset_id',
        'analytic_distribution_id',
        string='Analytic Distribution')


class AccountInvoiceLine(models.Model):
    _inherit = 'account.invoice.line'

    @api.one
    def asset_create(self):
        if self.asset_category_id and self.asset_category_id.method_number > 1:
            distribution_ids = [(4, distrib.id, False)
                                for distrib in self.analytic_distribution_ids]
            vals = {
                'name': self.name,
                'code': self.invoice_id.number or False,
                'category_id': self.asset_category_id.id,
                'value': self.price_subtotal,
                'partner_id': self.invoice_id.partner_id.id,
                'company_id': self.invoice_id.company_id.id,
                'currency_id': self.invoice_id.currency_id.id,
                'date': self.asset_start_date or self.invoice_id.date_invoice,
                'invoice_id': self.invoice_id.id,
                'analytic_distribution_ids': distribution_ids,
            }
            asset_obj = self.env['account.asset.asset']

            changed_vals =\
                asset_obj.onchange_category_id_values(vals['category_id'])
            vals.update(changed_vals['value'])

            asset = self.env['account.asset.asset'].create(vals)
            if self.asset_category_id.open_asset:
                asset.validate()
        return True


class AccountAssetCategory(models.Model):

    _inherit = "account.asset.category"

    analytic_distribution_ids = fields.Many2many(
        'account.analytic.distribution',
        'account_asset_category_analytic_distrib_rel',
        'account_asset_category_id',
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

    @api.constrains("analytic_distribution_ids")
    def check_analytic_distribution_ids(self):
        axis_object = self.env['account.analytic.axis']
        return axis_object.check_percent_on_axis(
            self.analytic_distribution_ids)


class AccountAssetDepreciationLine(models.Model):

    _inherit = "account.asset.depreciation.line"

    @api.multi
    def create_move(self, post_move=True):
        created_moves = self.env['account.move']
        for line in self:
            asset = line.asset_id
            depreciation_date = \
                self.env.context.get('depreciation_date') or\
                line.depreciation_date or fields.Date.context_today(self)

            company_currency = asset.company_id.currency_id
            current_currency = asset.currency_id

            amount = current_currency.compute(line.amount, company_currency)
            sign = (asset.category_id.journal_id.type in
                    ('purchase', 'sale', 'general') and 1) or -1

            asset_name = \
                asset.name + ' (%s/%s)' % (line.sequence, asset.method_number)

            reference = asset.code
            journal_id = asset.category_id.journal_id.id
            partner_id = asset.partner_id.id
            categ_type = asset.category_id.type
            debit_account = asset.category_id.account_asset_id.id
            credit_account = asset.category_id.account_depreciation_id.id

            if categ_type == 'purchase':
                distribution_list = asset.category_id.analytic_distribution_ids
                distribution_ids = \
                    [(4, analytic_distribution.id, False)
                     for analytic_distribution in distribution_list]
            else:
                distribution_list = asset.analytic_distribution_ids
                distribution_ids = \
                    [(4,analytic_distribution.id, False)
                     for analytic_distribution in distribution_list]

            move_line_1 = {
                'name': asset_name,
                'account_id': credit_account,
                'debit': 0.0,
                'credit': amount,
                'journal_id': journal_id,
                'partner_id': partner_id,
                'currency_id': company_currency != current_currency
                               and current_currency.id or False,
                'amount_currency': company_currency != current_currency
                                   and - sign * line.amount or 0.0,
                'analytic_distribution_ids':
                    distribution_ids if categ_type == 'sale' else [],
                'date': depreciation_date,
            }
            move_line_2 = {
                'name': asset_name,
                'account_id': debit_account,
                'credit': 0.0,
                'debit': amount,
                'journal_id': journal_id,
                'partner_id': partner_id,
                'currency_id': company_currency != current_currency
                               and current_currency.id or False,
                'amount_currency': company_currency != current_currency
                                   and sign * line.amount or 0.0,
                'analytic_distribution_ids':
                    distribution_ids if categ_type == 'purchase' else [],
                'date': depreciation_date,
            }
            move_vals = {
                'ref': reference,
                'date': depreciation_date or False,
                'journal_id': line.asset_id.category_id.journal_id.id,
                'line_ids': [(0, 0, move_line_1), (0, 0, move_line_2)],
                'asset_id': line.asset_id.id,
                }
            move = self.env['account.move'].create(move_vals)
            line.write({'move_id': move.id, 'move_check': True})
            created_moves |= move

        if post_move and created_moves:
            created_moves.post()
        return [x.id for x in created_moves]
