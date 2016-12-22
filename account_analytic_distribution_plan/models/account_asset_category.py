# -*- coding: utf-8 -*-
# © 2015 Jérôme Guerriat
# © 2015 Niboo SPRL (<https://www.niboo.be/>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from openerp import api, fields, models


class AccountAssetCategory(models.Model):

    _inherit = 'account.asset.category'

    distribution_plan_id = fields.Many2one(
        'account.analytic.distribution.plan', 'Distribution Plan')

    @api.onchange('distribution_plan_id')
    def _onchange_distribution_plan_id(self):
        self.analytic_distribution_ids = \
            self.distribution_plan_id.analytic_distribution_ids
