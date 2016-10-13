# -*- coding: utf-8 -*-
# © 2016 Jerome Guerriat
# © 2016 Niboo SPRL (<https://www.niboo.be/>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from openerp import fields
from openerp import models


class ResCompany(models.Model):
    _inherit = "res.company"

    hours_per_day = fields.Float(default="8",
                                 help="The hours employees need to log"
                                      " per day in order for a timesheet"
                                      " to be valid.")
