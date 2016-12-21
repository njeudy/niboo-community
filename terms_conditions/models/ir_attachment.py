# -*- coding: utf-8 -*-
# © 2016 Pierre Faniel
# © 2016 Niboo SPRL (<https://www.niboo.be/>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from openerp import api, exceptions, fields, models


class IrAttachment(models.Model):
    _inherit = 'ir.attachment'

    is_terms_and_conditions = fields.Boolean('Terms and Conditions')
    description = fields.Text('Description', translate=True)
    language_id = fields.Many2one('res.lang', 'Language')

    @api.constrains('language_id', 'res_id')
    @api.multi
    def _check_language_id(self):
        IrAttachment = self.env['ir.attachment']
        for attachment in self:
            language_id = attachment.language_id.id \
                if attachment.language_id else None
            if IrAttachment.search([
                ('res_id', '=', attachment.res_id),
                ('id', '!=', attachment.id),
                ('res_model', '=', 'res.company'),
                ('language_id', '=', language_id),
                ('is_terms_and_conditions', '=', True),
            ]):
                raise exceptions.ValidationError(
                    'You can only add one document per language')
