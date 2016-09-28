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


class ResPartner(models.Model):
    _inherit = 'res.partner'

    project_key = fields.Char('Project Identifier Key')
    project_partner_sequence = fields.Many2one('ir.sequence')

    @api.constrains('project_key')
    def check_project_key(self):
        if not self.project_partner_sequence and self.project_key:
            self.create_sequence()
            # we should update existing tasks nop?
            # tasks = self.env['project.task'].search([('project_key', '=', False)])


    @api.multi
    def create_sequence(self):
        self.ensure_one()
        code = 'project.task.order.' + self.project_key
        sequence = self.env['ir.sequence'].search([('code', '=', code)])
        if not sequence:
            name = 'project task order - ' + self.name
            sequence = self.env["ir.sequence"].sudo().create({
                'code': code,
                'name': name,
                'prefix': '%s-' % self.project_key
            })
            self.sudo().project_sequence = sequence

    _sql_constraints = [
        ('unique_project_key',
         'UNIQUE (project_key)',
         'Project key should be unique')
    ]
