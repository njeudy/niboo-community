# -*- coding: utf-8 -*-
# © 2015 Gael Rabier
# © 2015 Niboo SPRL (<https://www.niboo.be/>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from openerp import api, fields, models
from openerp.tools.safe_eval import safe_eval as eval
from pyPdf import PdfFileWriter, PdfFileReader
import base64
from cStringIO import StringIO


class IrActionsReportXML(models.Model):
    _inherit = 'ir.actions.report.xml'

    add_terms_conditions = fields.Boolean(string='add Terms and Conditions',
                                          default=False)
    terms_conditions_language_field = fields.Char('Language field')


class Report(models.Model):
    _inherit = 'report'

    @api.multi
    def get_pdf(self, report_name, html=None, data=None):
        report = self._get_report_from_name(report_name)
        report_pdf = super(Report, self).get_pdf(self, report_name, html,
                                                 data)

        if report.add_terms_conditions and len(self) == 1:
            report_pdf = self.add_terms_and_conditions(report_pdf, report)
        return report_pdf

    @api.model
    def add_terms_and_conditions(self, original_report_pdf, original_report):

        terms_and_conditions_decoded = False
        default_terms_and_conditions_decoded = False

        # todo change user language to report language (client language)

        language_field = original_report.terms_conditions_language_field
        model = original_report.model

        object = self.env[model].browse(self.ids)
        localdict = {'o': object}
        eval('document_language = o.%s' % language_field, localdict,
             mode='exec', nocopy=True)
        document_language = localdict.get('document_language',
                                          self._context.get('lang'))

        company = object.company_id
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
