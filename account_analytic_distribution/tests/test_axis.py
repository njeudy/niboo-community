# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Jérôme Guerriat
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


from openerp.tests.common import TransactionCase
from openerp import _
from openerp.exceptions import ValidationError


class TestAxis(TransactionCase):

    def setUp(self):
        super(TestAxis, self).setUp()
        self.createObjects()

    def test_analytic_account_unique_move_line(self):
        """
        Test that the same analytic account can't be linked twice to the same
        move line
        :return:
        """
        with self.assertRaises(ValidationError):
            self.account_move_line1.write(
                {'analytic_distribution_ids':[
                    (6, _, [self.analytic_distribution1.id,
                            self.analytic_distribution2.id])]
                 }
            )

    def test_analytic_account_sums_to_100_move_line(self):
        """
        Test that move line are saved only if axis of their distribution
        meets the "100%" requirement
        :return:
        """
        self.account_move_line1.write(
                {'analytic_distribution_ids':[
                    (6, _, [self.analytic_distribution1.id,
                            self.analytic_distribution3.id])]
                 }
            )
        with self.assertRaises(ValidationError):
            self.account_move_line1.write(
                {'analytic_distribution_ids':[
                    (6, _, [self.analytic_distribution1.id,
                            self.analytic_distribution4.id])]
                 }
            )



    def test_analytic_account_unique_asset_category(self):
        """
        Test that the same analytic account can't be linked twice to the same
        asset category
        :return:
        """
        with self.assertRaises(ValidationError):
            self.account_asset_category.write(
                {'analytic_distribution_ids':[
                    (6, _, [self.analytic_distribution1.id,
                            self.analytic_distribution2.id])]
                 }
            )

    def test_analytic_account_sums_to_100_asset_category(self):
        """
        Test that asset category are saved only if axis of their distribution
        meets the "100%" requirement
        :return:
        """
        self.account_asset_category.write(
                {'analytic_distribution_ids':[
                    (6, _, [self.analytic_distribution1.id,
                            self.analytic_distribution3.id])]
                 }
            )
        with self.assertRaises(ValidationError):
            self.account_asset_category.write(
                {'analytic_distribution_ids':[
                    (6, _, [self.analytic_distribution1.id,
                            self.analytic_distribution4.id])]
                 }
            )


    def test_analytic_account_unique_invoice_line(self):
        """
        Test that the same analytic account can't be linked twice to the same
        invoice line
        :return:
        """
        with self.assertRaises(ValidationError):
            self.account_invoice_line.write(
                {'analytic_distribution_ids':[
                    (6, _, [self.analytic_distribution1.id,
                            self.analytic_distribution2.id])]
                 }
            )

    def test_analytic_account_sums_to_100_invoice_line(self):
        """
        Test that invoice line are saved only if axis of their distribution
        meets the "100%" requirement
        :return:
        """
        self.account_invoice_line.write(
                {'analytic_distribution_ids':[
                    (6, _, [self.analytic_distribution1.id,
                            self.analytic_distribution3.id])]
                 }
            )

        with self.assertRaises(ValidationError):
            self.account_invoice_line.write(
                {'analytic_distribution_ids':[
                    (6, _, [self.analytic_distribution1.id,
                            self.analytic_distribution4.id])]
                 }
            )

    def test_analytic_account_unique_hr_expense(self):
        """
        Test that the same analytic account can't be linked twice to the same
        hr expense
        :return:
        """
        with self.assertRaises(ValidationError):
            self.hr_expense.write(
                {'analytic_distribution_ids':[
                    (6, _, [self.analytic_distribution1.id,
                            self.analytic_distribution2.id])]
                 }
            )

    def test_analytic_account_sums_to_100_hr_expense(self):
        """
        Test that hr expenses are saved only if axis of their distribution
        meets the "100%" requirement
        :return:
        """
        self.hr_expense.write(
                {'analytic_distribution_ids':[
                    (6, _, [self.analytic_distribution1.id,
                            self.analytic_distribution3.id])]
                 }
            )
        with self.assertRaises(ValidationError):
            self.hr_expense.write(
                {'analytic_distribution_ids':[
                    (6, _, [self.analytic_distribution1.id,
                            self.analytic_distribution4.id])]
                 }
            )


    # def test_sale_provoke_analytic_lines_creation(self):
    #     """
    #     Test that creating an invoice provoke the creation of analytic lines
    #
    #     :return:
    #     """
    #     self.account_invoice_line.write(
    #         {'analytic_distribution_ids':[
    #             (6, _, [self.analytic_distribution1.id,
    #                     self.analytic_distribution3.id])]
    #          }
    #     )
    #     self.account_invoice_sale.write(
    #         {
    #             'invoice_line_ids':[
    #                 (6, _, [self.account_invoice_line2.id,
    #                         self.account_invoice_line3.id])]
    #         }
    #     )
    #
    #     analytic_lines_75 = self.env['account.analytic.line'].search([
    #         ('amount','=','-75'),
    #         ('account_id','=',self.analytic_account1.id)
    #     ])
    #     analytic_lines_25 = self.env['account.analytic.line'].search([
    #         ('amount','=','-25'),
    #         ('account_id','=',self.analytic_account1.id)
    #     ])
    #
    #     self.assertTrue(analytic_lines_25==analytic_lines_75==1)



    def createObjects(self):
        self.Belgium = self.env.ref('base.be')
        self.Admin = self.env.ref('base.user_root')

        self.axis_sale = self.env['account.analytic.axis'].create({
            'name':"sale axis",
        })

        self.account_type = self.env['account.account.type'].create({
            'name':'Tests'
        })

        self.account = self.env['account.account'].create({
            'name':"account test",
            'code':"llll",
            'user_type_id':self.account_type.id
        })

        self.analytic_account1 = self.env['account.analytic.account'].create({
            'name':"account 1",
            'analytic_account_axis_id':self.axis_sale.id,
            'currency_id':self.env.ref('base.EUR').id
        })

        self.analytic_account2 = self.env['account.analytic.account'].create({
            'name':"account 1",
            'analytic_account_axis_id':self.axis_sale.id,
            'currency_id':self.env.ref('base.EUR').id
        })

        self.analytic_distribution1 = self.env['account.analytic.distribution'].\
            create({
            'rate':'25',
            'analytic_account_id':self.analytic_account1.id
        })

        self.analytic_distribution2 = self.env['account.analytic.distribution'].\
            create({
            'rate':'75',
            'analytic_account_id':self.analytic_account1.id
        })

        self.analytic_distribution3 = self.env['account.analytic.distribution'].\
            create({
            'rate':'75',
            'analytic_account_id':self.analytic_account2.id
        })

        self.analytic_distribution4 = self.env['account.analytic.distribution'].\
            create({
            'rate':'50',
            'analytic_account_id':self.analytic_account2.id
        })
        self.account_journal = self.env['account.journal'].create({
            'code':'xxxx',
            'name':'journal',
            'type':'sale'
        })

        self.account_move = self.env['account.move'].create({
            'journal_id':self.account_journal.id
        })

        self.account_move_line1 = self.env['account.move.line'].create({
            'move_id':self.account_move.id,
            'name':'testes',
            'account_id':self.account.id,
        })

        self.account_asset_category = self.env['account.asset.category'].create({
            'account_depreciation_id':self.account.id,
            'journal_id':self.account_journal.id,
            'account_asset_id':self.account.id,
            'name':"test asset"
        })

        self.partner = self.env['res.partner'].create({
            'name':'partner',
            'user_id':self.Admin.id

        })

        self.account_invoice = self.env['account.invoice'].create({
            'account_id':self.account.id,
            'partner_id':self.partner.id,
            'user_id':self.Admin.id,
        })

        self.account_invoice_purchase = self.env['account.invoice'].create({
            'account_id':self.account.id,
            'partner_id':self.partner.id,
            'user_id':self.Admin.id,
            'type':'in_invoice'
        })

        self.account_invoice_sale = self.env['account.invoice'].create({
            'account_id':self.account.id,
            'partner_id':self.partner.id,
            'user_id':self.Admin.id,
            'type':'in_invoice'
        })

        self.account_invoice_line = self.env['account.invoice.line'].create({
            'price_unit':100,
            'account_id':self.account.id,
            'name':"tests invoice"
        })

        self.account_invoice_line2 = self.env['account.invoice.line'].create({
            'price_unit':100,
            'account_id':self.account.id,
            'name':"tests invoice"
        })

        self.account_invoice_line3 = self.env['account.invoice.line'].create({
            'price_unit':100,
            'account_id':self.account.id,
            'name':"tests invoice"
        })

        self.employee = self.env['hr.employee'].create({
            'name':"jerome",
        })

        self.product = self.env['product.product'].create({
            'name':"produit"
        })

        self.hr_expense = self.env['hr.expense'].create({
            'name':'test',
            'employee_id':self.employee.id,
            'product_id':self.product.id,
            'unit_amount':100
        })
