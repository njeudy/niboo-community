# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Pierre Faniel
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

from openerp import api
from openerp import exceptions
from openerp import fields
from openerp import models


class TimesheetWorkLogger(models.TransientModel):
    _name = 'hr_timesheet.work.logger'

    time_spent = fields.Float('Time To Log', required=True)
    date_started = fields.Date('Date Started',
                               default=lambda self: fields.Date.today(),
                               required=True)
    description = fields.Text('Description', required=True)
    analytic_account_id = fields.Many2one('account.analytic.account', 'Project',
                                 required=True)
    task_id = fields.Many2one('project.task', 'Task')
    product_id = fields.Many2one('product.product', 'Product')

    @api.multi
    @api.constrains('time_spent')
    def check_time_spent(self):
        self.ensure_one()
        if self.time_spent == 0:
            raise exceptions.ValidationError('Time To Log cannot be zero')
        if self.time_spent < 0:
            raise exceptions.ValidationError('Time To Log cannot be negative')

    @api.onchange('analytic_account_id')
    def _onchange_analytic_account_id(self):
        domain = {'task_id': [], 'product_id': []}

        # Remove the task if it is not matching with the project
        if self.task_id and self.task_id.project_id.analytic_account_id !=\
                self.analytic_account_id:
            self.task_id = False

        # Allow to select only task from the project
        if self.analytic_account_id:
            domain['task_id'] = [('analytic_account_id', '=', self.analytic_account_id.id)]

            SaleOrder = self.env['sale.order']
            sale_order = SaleOrder.search(
                [('project_id', '=', self.analytic_account_id.id)])
            product_ids = [line.product_id.id for line in sale_order.sudo().order_line]
            domain['product_id'] = [('id', 'in', product_ids)]

        return {'domain': domain}

    @api.onchange('task_id')
    def _onchange_task_id(self):
        if self.task_id:
            self.analytic_account_id = self.task_id.analytic_account_id

    @api.multi
    def submit_log_work(self):
        self.env['account.analytic.line'].create({
            'unit_amount': self.time_spent,
            'account_id': self.analytic_account_id.id,
            'name': self.description,
            'is_timesheet': True,
            'product_id': self.product_id.id,
            'date': self.date_started,
            'task_id': self.task_id.id,
        })


class HrTimesheetSheet(models.Model):
    _inherit = 'hr_timesheet_sheet.sheet'

    @api.multi
    def log_work_action(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'view_id': self.env.ref(
                'hr_timesheet_work_log_wizard.work_logger_wizard').id,
            'name': 'Log work',
            'target': 'new',
            'res_model': 'hr_timesheet.work.logger',
            'view_type': 'form',
            'view_mode': 'form',
            'context': {}
        }
