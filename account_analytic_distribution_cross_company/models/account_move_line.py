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

    @api.one
    def _prepare_analytic_lines(self):
        """ Prepare the values used to create() an account.analytic.line upon validation of an account.move.line having
            an analytic account. This method is intended to be extended in other modules.
        """

        vals_list = super(AccountMoveLine, self)._prepare_analytic_lines()[0]
        for vals in vals_list:
            AccountAnalyticAccount = self.env['account.analytic.account']
            account_analytic = AccountAnalyticAccount.browse(vals['account_id'])
            currency = self.company_id.currency_id
            if currency != account_analytic.currency_id:
                vals['amount'] = currency.compute(
                    vals['amount'], account_analytic.currency_id)

        return vals_list
