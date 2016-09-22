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

from openerp import fields
from openerp import models


class AccountAnalyticAccount(models.Model):

    _inherit = "account.analytic.account"

    company_id = fields.Many2one(required=False)
    currency_id = fields.Many2one('res.currency', related='', string="Currency", readonly=False, required=True)

class account_analytic_line(models.Model):

    _inherit = 'account.analytic.line'

    currency_id = fields.Many2one(related="account_id.currency_id", string="Currency", readonly=True)
    move_currency_id = fields.Many2one(related="move_id.currency_id", string="Move Currency", readonly=True)
    amount_currency = fields.Monetary(currency_field='move_currency_id')
