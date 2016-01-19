# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Gael Rabier
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
from openerp.fields import Boolean, Char
from openerp.tools.safe_eval import safe_eval as eval
from pyPdf import PdfFileWriter, PdfFileReader
import base64
from cStringIO import StringIO


class IrActionsReportXML(Model):
    _inherit = "ir.actions.report.xml"

    add_terms_conditions = Boolean(string='add Terms and Conditions',
                                   default=False)
    terms_conditions_language_field = Char('Language field')


class Report(Model):
    _inherit = "report"

    @api.v7
    def get_pdf(self, cr, uid, ids, report_name, html=None, data=None,
                context=None):

        report = self._get_report_from_name(cr, uid, report_name)
        report_pdf = super(Report, self).get_pdf(cr, uid, ids, report_name,
                                                 html, data, context)

        if report.add_terms_conditions and len(ids) == 1:
            report_pdf = self.add_terms_and_conditions(cr, uid, ids, report_pdf,
                                                       report, context)

        return report_pdf

    @api.model
    def add_terms_and_conditions(self, ids, original_report_pdf,
                                 original_report):

        terms_and_conditions_decoded = False
        default_terms_and_conditions_decoded = False


        user = self.env['res.users'].browse(self._uid)

        # todo change user language to report language (client language)

        language_field = original_report.terms_conditions_language_field
        model = original_report.model

        object = self.env[model].browse(ids)
        localdict = {'o': object}
        eval('document_language = o.%s' % language_field, localdict,
             mode="exec", nocopy=True)
        document_language = localdict.get('document_language',
                                          self._context.get('lang'))

        company = model.company_id
        # todo check language
        terms_and_conditions_list = company.terms_and_conditions

        for terms_and_conditions in terms_and_conditions_list:
            if terms_and_conditions.language == document_language:
                terms_and_conditions_decoded =\
                    base64.decodestring(terms_and_conditions.datas)
            if terms_and_conditions.language == 'default':
                default_terms_and_conditions_decoded = \
                    base64.decodestring(terms_and_conditions.datas)

        if not terms_and_conditions_decoded:
            terms_and_conditions_decoded = \
                default_terms_and_conditions_decoded or False

        if terms_and_conditions_decoded:
            writer = PdfFileWriter()
            stream_original_report = StringIO(original_report_pdf)
            reader_original_report = PdfFileReader(stream_original_report)
            stream_terms_and_conditions = StringIO(terms_and_conditions_decoded)
            reader_terms_and_conditions = PdfFileReader(
                stream_terms_and_conditions)
            for page in range(0, reader_original_report.getNumPages()):
                writer.addPage(reader_original_report.getPage(page))

            for page in range(0, reader_terms_and_conditions.getNumPages()):
                writer.addPage(reader_terms_and_conditions.getPage(page))

            stream_to_write = StringIO()
            writer.write(stream_to_write)

            combined_pdf = stream_to_write.getvalue()

            return combined_pdf
        else:
            return original_report_pdf

