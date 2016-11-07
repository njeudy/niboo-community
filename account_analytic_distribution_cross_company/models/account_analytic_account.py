# -*- coding: utf-8 -*-
# © 2015 Jérôme Guerriat
# © 2015 Niboo SPRL (<https://www.niboo.be/>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from openerp import fields, models


class AccountAnalyticAccount(models.Model):

    _inherit = 'account.analytic.account'

    company_id = fields.Many2one(required=False)
    currency_id = fields.Many2one('res.currency', related='', readonly=False,
                                  string='Currency', required=True)


class AccountAnalyticLine(models.Model):

    _inherit = 'account.analytic.line'

    currency_id = fields.Many2one(related='account_id.currency_id',
                                  string='Currency', readonly=True)
    move_currency_id = fields.Many2one(related='move_id.currency_id',
                                       string='Move Currency', readonly=True)
    amount_currency = fields.Monetary(currency_field='move_currency_id')
