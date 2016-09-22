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
from openerp.exceptions import ValidationError


class AccountAnalyticAxis(models.Model):

    _name = "account.analytic.axis"
    _description = "Analytic axis"

    name = fields.Char("Axis name")

    analytic_account_id = fields.One2many('account.analytic.account',
                                          'analytic_account_axis_id',
                                          'Analytic account')

    def check_percent_on_axis(self, distributions):
        distribution_by_axis = {}
        for distribution in distributions:
            axis = distribution.analytic_account_id.analytic_account_axis_id
            distribution_by_axis.setdefault(axis, [])
            distribution_by_axis[axis].append(distribution)

        message = ''
        for axis, distributions in distribution_by_axis.iteritems():
            try:
                axis._check_percent_on_axis(distributions)
            except Exception, e:
                message += e.name

        if message:
            raise ValidationError(message)
        return True

    def _check_percent_on_axis(self, distributions):
        total = sum(distribution.rate for distribution in distributions)
        if round(total, 2) != 100.0 and round(total, 2) != 0.0:
            raise ValidationError('Axis %s has a total of %s %% \n' %
                                  (self.name, total))
