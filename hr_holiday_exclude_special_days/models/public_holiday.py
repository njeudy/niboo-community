# -*- coding: utf-8 -*-
# © 2016 Jérôme Guerriat
# © 2016 Niboo SPRL (<https://www.niboo.be/>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from openerp import fields
from openerp import models


class PublicHoliday(models.Model):
    _name = "hr.public_holiday"

    date = fields.Date("Public Holiday Date", required=True)
    company_id = fields.Many2one('res.company', string="Company", required=True)
    name = fields.Char(string="Holiday Name", required=True)

    _sql_constraints = [
        ('unique_date',
         'UNIQUE (date, company_id)',
         'You should only have one public holiday per company and date')
    ]
