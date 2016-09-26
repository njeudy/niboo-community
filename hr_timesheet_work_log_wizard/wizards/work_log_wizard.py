# -*- coding: utf-8 -*-
# © 2016 Pierre Faniel
# © 2016 Niboo SPRL (<https://www.niboo.be/>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from openerp import api, exceptions, fields, models


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

    display_task = fields.Boolean('Display task')
    display_product = fields.Boolean('Display product')

    @api.multi
    @api.constrains('time_spent')
    def check_time_spent(self):
        self.ensure_one()
        if self.time_spent == 0:
            raise exceptions.ValidationError('Time To Log cannot be zero')
        if self.time_spent < 0:
            raise exceptions.ValidationError('Time To Log cannot be negative')

    @api.multi
    @api.onchange('analytic_account_id', 'task_id')
    def display_task_and_product(self):
        self.ensure_one()
        # Do not display selection of task/product if there are none
        self.display_task = True
        self.display_product = True

        if self.analytic_account_id:
            Task = self.env['project.task']
            task_ids = Task.search([
                ('analytic_account_id', '=', self.analytic_account_id.id)])

            SaleOrder = self.env['sale.order']
            sale_order = SaleOrder.search(
                [('project_id', '=', self.analytic_account_id.id)])
            product_ids = [line.product_id.id for line in
                           sale_order.sudo().order_line]

            if not task_ids:
                self.display_task = False
            if not product_ids:
                self.display_product = False

    @api.onchange('analytic_account_id')
    def _onchange_analytic_account_id(self):
        domain = {'task_id': [], 'product_id': []}

        # Remove the task if it is not matching with the project
        if self.task_id and self.task_id.project_id.analytic_account_id !=\
                self.analytic_account_id:
            self.task_id = False

        # Allow to select only task and product from the project
        if self.analytic_account_id:
            SaleOrder = self.env['sale.order']
            sale_order = SaleOrder.search(
                [('project_id', '=', self.analytic_account_id.id)])
            product_ids = [line.product_id.id for line in
                           sale_order.sudo().order_line]

            domain['task_id'] = [
                ('analytic_account_id', '=', self.analytic_account_id.id)]
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
