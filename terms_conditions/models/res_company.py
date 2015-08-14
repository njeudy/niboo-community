# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Gael Rabier, Samuel Lefever
#    Copyright 2015 Niboo SPRL
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

from openerp.models import Model, api, _
from openerp.fields import One2many, Selection, Text

class ir_attachment(Model):

    #Private attributes
    _inherit = 'ir.attachment'

    #Fields declaration
    description = Text('Description', translate=True)
    language = Selection([
        ('default',_('Default')),
        ('en_US',_('English')),
        ('fr_BE',_('French')),
        ('nl_NL',_('Dutch')),
    ])

    #Constraints
    _sql_constraints = [(
        'unique_language',
        'unique(res_id, language)',
        _('You can only add one document per language'),
    )]


class res_company(Model):

    #Private attributes
    _inherit = "res.company"

    #Fields declaration
    terms_and_conditions = One2many('ir.attachment',
                                    compute='_get_terms_and_conditions',
                                    inverse='_set_terms_and_conditions')


    @api.one
    def _get_terms_and_conditions(self):
        self.terms_and_conditions = self.env['ir.attachment'].search([
            ('res_model', '=', 'res.company'),
            ('type', '=', 'binary'),
            ('res_id', '=', self.id)
        ])


    @api.one
    def _set_terms_and_conditions(self):
        attachments = []
        terms_and_conditions = self.env['ir.attachment'].search([
            ('res_model', '=', 'res.company'),
            ('type', '=', 'binary'),
            ('res_id', '=', self.id)
        ])

        for document in terms_and_conditions:
            if document not in self.terms_and_conditions:
                document.unlink()

        for document in self.terms_and_conditions:
            if document not in terms_and_conditions:
                attachments.append(self.env['ir.attachment'].create({
                    'res_model':'res.company',
                    'name':document.name,
                    'datas':document.datas,
                    'language':document.language,
                    'res_id':self.id,
                    'type':'binary',
                }))