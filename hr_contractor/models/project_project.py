# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Jérôme Guerriat
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


class ProjectProject(models.Model):
    _inherit = 'project.project'

    @api.multi
    def message_subscribe(self, partner_ids=None, channel_ids=None,
                          subtype_ids=None, force=True):

        for project in self:
            partners = self.env['res.partner'].browse(partner_ids)

            partner_names = ', '.join(map(str, partners.mapped('name')))

            if project.analytic_account_id.partner_id:
                project.analytic_account_id.partner_id.message_subscribe(
                    partner_ids,
                    channel_ids,
                    subtype_ids,
                    force)
                project.message_post(
                    body="Partner(s) %s now have access to this project"
                         % partner_names
                )
            else:
                project.message_post(
                    body="""
Partner(s) %s were added as follower but do not have access to this project.
Please select a customer they follow to give access to this project"""
                         % partner_names
                )

            super(ProjectProject, project).message_subscribe(partner_ids,
                                                             channel_ids,
                                                             subtype_ids,
                                                             force)

    @api.multi
    def message_unsubscribe(self, partner_ids=None, channel_ids=None):
        partners = self.env['res.partner'].browse(partner_ids)
        partner_names = partners.mapped('name')

        for project in self:
            project.analytic_account_id.partner_id.message_unsubscribe(
                partner_ids,
                channel_ids)

            super(ProjectProject, project).message_unsubscribe(partner_ids,
                                                             channel_ids)
            project.message_post(
                body="Partner(s) removed from followers" % partner_names
            )
