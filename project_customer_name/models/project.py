# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Tobias Zehntner
#    Copyright 2016 Niboo SPRL
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
