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


class TestDistributionPlan(TransactionCase):

    def setUp(self):
        super(TestDistributionPlan, self).setUp()
        self.createObjects()

    def test_distribution_plan_invoice_line(self):
        """
        Test that adding a distribution plan to an account move line
        correctly replace the list of distribution ids
        :return:
        """
        self.account_invoice_line.write(
            {'distribution_plan_id': self.distribution_plan.id})
        self.account_invoice_line._onchange_distribution_plan_id()

        self.assertEquals(
            len(self.account_invoice_line.analytic_distribution_ids), 3)

    def test_distribution_plan_assets(self):
        """
        Test that adding a distribution plan to an asset
        correctly replace the list of distribution ids
        :return:
        """
        self.account_asset_category.write(
            {'distribution_plan_id': self.distribution_plan.id})
        self.account_asset_category._onchange_distribution_plan_id()
        self.assertEquals(
            len(self.account_asset_category.analytic_distribution_ids), 3)

    def test_distribution_hr_expenses(self):
        """
        Test that adding a distribution plan to an hr expense
        correctly replace the list of distribution ids
        :return:
        """
        self.hr_expense.write(
            {'distribution_plan_id': self.distribution_plan.id})
        self.hr_expense._onchange_distribution_plan_id()
        self.assertEquals(
            len(self.hr_expense.analytic_distribution_ids), 3)

    def test_distribution_move_line(self):
        """
        Test that adding a distribution plan to a move line
        correctly replace the list of distribution ids
        :return:
        """
        self.account_move_line1.write(
            {'distribution_plan_id': self.distribution_plan.id})
        self.account_move_line1._onchange_distribution_plan_id()
        self.assertEquals(
            len(self.account_move_line1.analytic_distribution_ids), 3)

    def createObjects(self):
        self.Belgium = self.env.ref('base.be')
        self.Admin = self.env.ref('base.user_root')

        self.axis_sale = self.env['account.analytic.axis'].create({
            'name': "sale axis",

        })

        self.axis_travel = self.env['account.analytic.axis'].create({
            'name': "travel axis",
        })

        self.account_type = self.env['account.account.type'].create({
            'name': 'Tests'
        })

        self.account = self.env['account.account'].create({
            'name': "account test",
            'code': "llll",
            'user_type_id': self.account_type.id
        })

        self.analytic_account1 = self.env['account.analytic.account'].create({
            'name': "account 1",
            'analytic_account_axis_id': self.axis_sale.id,
            'currency_id': self.env.ref('base.EUR').id
        })

        self.analytic_account2 = self.env['account.analytic.account'].create({
            'name': "account 2",
            'analytic_account_axis_id': self.axis_sale.id,
            'currency_id': self.env.ref('base.EUR').id
        })

        self.analytic_account3 = self.env['account.analytic.account'].create({
            'name': "account 3",
            'analytic_account_axis_id': self.axis_travel.id,
            'currency_id': self.env.ref('base.EUR').id
        })

        self.analytic_distribution1 = \
            self.env['account.analytic.distribution'].create({
                'rate': '25',
                'analytic_account_id': self.analytic_account1.id,
            })

        self.analytic_distribution2 = \
            self.env['account.analytic.distribution'].create({
                'rate': '75',
                'analytic_account_id': self.analytic_account2.id,
            })

        self.analytic_distribution3 = \
            self.env['account.analytic.distribution'].create({
                'rate': '100',
                'analytic_account_id': self.analytic_account3.id
            })

        self.distribution_plan = \
            self.env['account.analytic.distribution.plan'].create({
                'name':"test plan",
                'analytic_distribution_ids':[
                    (6, _, [self.analytic_distribution1.id,
                            self.analytic_distribution2.id,
                            self.analytic_distribution3.id])]
            })

        self.account_journal = self.env['account.journal'].create({
            'code': 'xxxx',
            'name': 'journal',
            'type': 'sale'
        })

        self.account_move = self.env['account.move'].create({
            'journal_id': self.account_journal.id
        })

        self.account_move_line1 = self.env['account.move.line'].create({
            'move_id': self.account_move.id,
            'name': 'testes',
            'account_id': self.account.id,
        })

        self.account_asset_category = self.env['account.asset.category'].create({
            'account_depreciation_id': self.account.id,
            'journal_id': self.account_journal.id,
            'account_asset_id': self.account.id,
            'name': "test asset"
        })

        self.partner = self.env['res.partner'].create({
            'name': 'partner',
            'user_id': self.Admin.id

        })

        self.account_invoice = self.env['account.invoice'].create({
            'account_id': self.account.id,
            'partner_id': self.partner.id,
            'user_id': self.Admin.id
        })

        self.account_invoice_line = self.env['account.invoice.line'].create({
            'price_unit': 10,
            'account_id': self.account.id,
            'name': "tests invoice"
        })

        self.employee = self.env['hr.employee'].create({
            'name': "jerome",
        })

        self.product = self.env['product.product'].create({
            'name': "produit"
        })

        self.hr_expense = self.env['hr.expense'].create({
            'name': 'test',
            'employee_id': self.employee.id,
            'product_id': self.product.id,
            'unit_amount': 10
        })
