# -*- coding: utf-8 -*-
# © 2016 Jerome Guerriat
# © 2016 Niboo SPRL (<https://www.niboo.be/>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from openerp import _, api, exceptions, fields, models
from datetime import datetime, timedelta
from openerp.osv import fields as osv_fields


class HRHolidays(models.Model):
    _inherit = 'hr.holidays'

    message = fields.Char('Selected days', compute='_compute_number_of_days')
    number_of_days_temp = fields.Float(compute='deduct_special_days')

    # Inherit function from module hr_holiday_exclude_special_days
    # Use new get_number_of_days (multiples of half days) and add message
    def deduct_special_days(self, number_of_days, date_from, date_to, employee):
        multiple_of_half_days = self.get_number_of_days()
        days_without_special_days, special_days_dict = \
            super(HRHolidays, self).deduct_special_days(multiple_of_half_days,
                                                        date_from, date_to,
                                                        employee)

        time_from = self.str_to_timezone(self.date_from)
        time_to = self.str_to_timezone(self.date_to)
        message = ''
        for timestamp in self.datespan(time_from, time_to):
            if timestamp.date() in special_days_dict:
                message = '%s<span>%s %s<br/></span>' % (
                    message, timestamp.date(),
                    special_days_dict[timestamp.date()])
            else:
                if self.is_full_day(timestamp, time_from, time_to):
                    message = '%s<span>%s <b>Full day</b><br/></span>' % (
                        message, timestamp.date())
                else:
                    message = '%s<span>%s <b>Half day</b><br/></span>' % (
                        message, timestamp.date())

        self.message = message
        return days_without_special_days, special_days_dict

    def get_number_of_days(self):
        self.ensure_one()
        leave_days = 0
        time_from = self.str_to_timezone(self.date_from)
        time_to = self.str_to_timezone(self.date_to)
        for timestamp in self.datespan(time_from, time_to):
            if self.is_full_day(timestamp, time_from, time_to):
                leave_days += 1
            else:
                leave_days += 0.5
        return leave_days

    @api.multi
    @api.constrains('number_of_days')
    def _check_number_of_days(self):
        for holiday in self:
            if holiday.type == "remove"\
                    and holiday.number_of_days\
                    and holiday.number_of_days % 0.5 != 0:
                raise exceptions.ValidationError(
                    _('Please select a multiple of 0.5 days'))

    @api.multi
    def holidays_validate(self):
        '''
        Method used to create timesheet lines when a holiday is approved
        :return:
        '''
        return_value = super(HRHolidays, self).holidays_validate()
        for holiday in self.filtered(lambda r: r.state == 'validate'):
            if not holiday.employee_id:
                continue

            if not holiday.employee_id.user_id:
                raise Warning(_('You can\'t validate a leave'
                                ' for employee without user'))
            if holiday.number_of_days > 0:
                continue

            employee = holiday.employee_id
            account = self.env.ref('hr_holiday_timesheet.analytic_absences')

            time_from = self.str_to_timezone(holiday.date_from)
            time_to = self.str_to_timezone(holiday.date_to)

            for timestamp in self.datespan(time_from, time_to):
                is_full_day = holiday.is_full_day(timestamp, time_from, time_to)
                date = timestamp.date()

                time = employee.company_id.hours_per_day
                if is_full_day:
                    self.create_leave_analytic_line(account, employee,
                                                    date, time)
                else:
                    time /= 2
                    self.create_leave_analytic_line(account, employee,
                                                    date, time)

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
            raise Warning(_('You can\'t book a holiday for a period for which'
                            ' you already have submitted your timesheet '))

        return super(HRHolidays, self).create(vals)

    @api.multi
    def is_full_day(self, timestamp, time_from, time_to):
        self.ensure_one()
        date_from = time_from.date()
        date_to = time_to.date()

        return (timestamp.date() == date_from and time_from.hour < 12)\
            or (timestamp.date() == date_to and time_to.hour >= 12)\
            or (timestamp.date() != date_to and timestamp.date() != date_from)

    def datespan(self, start_date, end_date, delta=timedelta(days=1)):
        current_date = start_date
        while current_date.date() <= end_date.date():
            yield current_date
            current_date += delta

    def str_to_timezone(self, time_string):
        time_obj = datetime.strptime(time_string, '%Y-%m-%d %H:%M:%S')

        return osv_fields.datetime.context_timestamp(self._cr,
                                                     self._uid,
                                                     time_obj,
                                                     self._context)
