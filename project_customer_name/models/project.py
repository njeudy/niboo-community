# -*- coding: utf-8 -*-
# © 2016 Jérôme Guerriat
# © 2016 Niboo SPRL (<https://www.niboo.be/>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from openerp import models
from openerp import fields
from openerp import api


class ProjectProject(models.Model):
    _inherit = 'project.project'

    customer_name = fields.Char(related='partner_id.name')

    @api.multi
    def name_get(self):
        result = []
        for project in self:
            name = project.name
            if project.partner_id:
                name = project.partner_id.name + ' - ' + name

            result.append((project.id, name))

        return result
