# -*- coding: utf-8 -*-
# © 2016 Jerome Guerriat
# © 2016 Niboo SPRL (<https://www.niboo.be/>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from openerp import fields, api, models


class AccountAnalyticLine(models.Model):

    _inherit = "account.analytic.line"

    leave_id = fields.Many2one('hr.holidays', string="Related Leave")
