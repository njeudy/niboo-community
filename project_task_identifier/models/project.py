# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Gael Rabier
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
from openerp import models, fields, api
from openerp import exceptions
from openerp import _


class ProjectTask(models.Model):
    _inherit = 'project.task'

    identifier = fields.Char('Identifier',
                                  compute='compute_identifier',
                                  store=True)
    is_created = fields.Boolean('Is Created', default=False,
                                compute='_compute_is_created')

    @api.depends('project_id.partner_id')
    def compute_identifier(self):
        for task in self:
            if not task.id:
                continue

            if task.project_id.partner_id:
                partner = task.project_id.partner_id.commercial_partner_id

                if not partner.project_key:
                    continue
                    raise exceptions.Warning(_('Partner Linked to a project '
                                               'should have a project key '
                                               'setted.'))

                if task.identifier and task.identifier.startswith(partner.project_key):
                    continue

                code = 'project.task.order.' + partner.project_key
                sequence = self.env['ir.sequence'].search([('code', '=', code)])
                if not sequence:
                    sequence = partner.create_sequence()
                id = sequence.next_by_code(code)
                task.identifier = id

    @api.multi
    def _compute_is_created(self):
        for task in self:
            if task.id:
                task.is_created = True

    @api.model
    def name_search(self, name, args=None, operator='ilike', limit=100):
        args = args or []
        domain = []
        if name:
            domain = ['|', ('name', operator, name), ('identifier', operator, name)]
        pos = self.search(domain + args, limit=limit)
        return pos.name_get()

    @api.multi
    @api.depends('name', 'identifier')
    def name_get(self):
        result = []
        for task in self:
            name = (task.identifier or "") + " - " +task.name
            result.append((task.id, name))
        return result
