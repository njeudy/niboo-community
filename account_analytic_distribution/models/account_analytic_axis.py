# -*- coding: utf-8 -*-
# © 2015 Jérôme Guerriat, Pierre Faniel
# © 2015 Niboo SPRL (<https://www.niboo.be/>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from openerp import exceptions, fields, models


class AccountAnalyticAxis(models.Model):

    _name = 'account.analytic.axis'
    _description = 'Analytic axis'

    name = fields.Char('Axis name')
    active = fields.Boolean('Active', default=True)
    analytic_account_ids = fields.One2many('account.analytic.account',
                                           'analytic_account_axis_id',
                                           'Analytic Accounts')

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
            raise exceptions.ValidationError(message)
        return True

    def _check_percent_on_axis(self, distributions):
        total = sum(distribution.rate for distribution in distributions)
        if round(total, 2) != 100.0 and round(total, 2) != 0.0:
            raise exceptions.ValidationError(
                'Axis %s has a total of %s %% \n' % (self.name, total))
