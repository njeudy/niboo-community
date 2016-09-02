# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Jerome Guerriat
#    Copyright 2015 Niboo SPRL
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program. If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.models import Model, api, _
from datetime import datetime, timedelta
from openerp.exceptions import Warning
from openerp.osv import fields as osv_fields


class HRHolidays(Model):
    _inherit = "hr.holidays"

    @api.one
    @api.constrains('number_of_days_temp')
    def validate_number_of_days(self):
        if self.number_of_days_temp != 0.5 and\
                                self.number_of_days_temp % 1 != 0:
            raise Warning(_("You can only enter 0.5 or an integer number"))

    @api.multi
    def holidays_validate(self):
        """
        Method used to create timesheet lines when a holiday is approved
        :return:
        """
        return_value = super(HRHolidays, self).holidays_validate()
        for holiday in self.filtered(lambda r: r.state == "validate"):
            if not holiday.employee_id:
                continue

            if not holiday.employee_id.user_id:
                raise Warning(_("You can't validate a leave"
                                " for employee without user"))
            if holiday.number_of_days > 0:
                continue

            date_from = datetime.strptime(holiday.date_from,
                                              "%Y-%m-%d %H:%M:%S")

            ts_date = osv_fields.datetime.context_timestamp(self._cr,
                                                        self._uid,
                                                        date_from,
                                                        self._context)

            employee = holiday.employee_id
            account = self.env.ref('hr_holiday_timesheet.analytic_absences')

            if holiday.number_of_days == -0.5:
                self.create_leave_analytic_line(
                    account, employee,
                    ts_date.replace(hour=0, minute=0, second=0,
                microsecond=0), 4)

            elif (holiday.number_of_days % 1) == 0:
                for nb_days in range(0, abs(int(holiday.number_of_days))):

                    concerned_day = ts_date + timedelta(nb_days)
                    concerned_day.replace(hour=0, minute=0, second=0,
                                          microsecond=0)

                    self.create_leave_analytic_line(account,
                                                    employee,
                                                    concerned_day,
                                                    8)
        return return_value

    @api.multi
    def holidays_refuse(self):
        return_value = super(HRHolidays, self).holidays_refuse()
        for holiday in self:
            lines = self.env['account.analytic.line'].sudo().search(
                [('leave_id', '=', holiday.id)])
            lines.sudo().unlink()
        return return_value

    def create_leave_analytic_line(self, account, employee, concerned_day,
                                   unit_amount):
        return self.env['account.analytic.line'].sudo().create({
            'account_id': account.id,
            'company_id': employee.company_id.id,
            'amount': 0,
            'date': concerned_day,
            'name': '/',
            'amount_currency': 0,
            'is_timesheet': True,
            'unit_amount': unit_amount,
            'user_id': employee.user_id.id,
            'leave_id': self.id
        })

    @api.model
    def create(self, vals):
        if vals['type'] == 'remove' and \
                self.env['hr_timesheet_sheet.sheet'].search([
                    ('date_from', '<', vals['date_to']),
                    ('date_to', '>', vals['date_from']),
                    ('employee_id', '=', vals['employee_id']),
                    ('state', '!=', 'draft')
                ]):
            raise Warning(_("You can't book a holiday for a period for which"
                            " you already have submitted your timesheet "))

        holiday = super(HRHolidays, self).create(vals)
        return holiday
