# -*- coding: utf-8 -*-
# © 2016 Jérôme Guerriat
# © 2016 Niboo SPRL (<https://www.niboo.be/>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from openerp import fields
from openerp import models
from openerp import api
from openerp import tools
from datetime import datetime, timedelta


class HRHolidays(models.Model):
    _inherit = "hr.holidays"

    # api.onchange for date_from and date_to that we remove in XML
    # Read dates in user timezone, deduct special days
    @api.onchange('date_from', 'employee_id')
    def compute_days_date_from(self):

        if not self.date_to or not self.date_from:
            return

        date_from_user_tz = self.change_to_user_tz(self.date_from)
        date_to_user_tz = self.change_to_user_tz(self.date_to)
        # call original odoo function with correct timezone
        result = self.onchange_date_from(date_to_user_tz, date_from_user_tz)
        number_of_days = result['value']['number_of_days_temp']
        days_without_special_days = self.deduct_special_days(number_of_days,
                                                               date_from_user_tz,
                                                               date_to_user_tz,
                                                               self.employee_id)

        self.number_of_days_temp = days_without_special_days

    @api.onchange('date_to', 'employee_id')
    def compute_days_date_to(self):

        if not self.date_to or not self.date_from:
            return

        date_from_user_tz = self.change_to_user_tz(self.date_from)
        date_to_user_tz = self.change_to_user_tz(self.date_to)
        # call original odoo function with correct timezone
        result = self.onchange_date_to(date_to_user_tz, date_from_user_tz)
        number_of_days = result['value']['number_of_days_temp']

        days_without_special_days = self.deduct_special_days(number_of_days,
                                                               date_from_user_tz,
                                                               date_to_user_tz,
                                                               self.employee_id)

        self.number_of_days_temp = days_without_special_days

    def change_to_user_tz(self, date):
        """
        Take date and return it in the user timezone
        :param date:
        :return:
        """
        if not date:
            return False
        date_object = datetime.strptime(date,
                                        tools.DEFAULT_SERVER_DATETIME_FORMAT)
        date_user_tz = fields.Datetime.context_timestamp(self.sudo(self._uid),
                                                         date_object)
        date_user_tz_string = date_user_tz.strftime("%Y-%m-%d %H:%M:%S")
        return date_user_tz_string

    # Get date range with exact dates
    def daterange(self, date_from, date_to):
        DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
        date_from = datetime.strptime(date_from, DATETIME_FORMAT)
        date_to = datetime.strptime(date_to, DATETIME_FORMAT)
        for n in range(int((date_to - date_from).days) + 1):
            yield date_from + timedelta(n)

    def deduct_special_days(self, number_of_days, date_from, date_to, employee):
        # retrieve public leaves in employee's company
        public_leave_ids = self.env['hr.public_holiday'].search([
            ('company_id', '=', employee.company_id.id)]
        )

        deduct_saturday = employee.company_id.deduct_saturday_in_leave
        deduct_sunday = employee.company_id.deduct_sunday_in_leave

        # for each date in the selected period, check if a public holiday exists
        # of if we should deduct the weekend days
        days_to_deduct = 0
        for date in self.daterange(date_from, date_to):
            is_public_leave = str(date.date()) \
                              in public_leave_ids.mapped("date")

            if is_public_leave or \
                    (date.weekday() == 5 and deduct_saturday) or \
                    (date.weekday() == 6 and deduct_sunday):
                days_to_deduct += 1

        days_without_special_days = number_of_days - days_to_deduct
        return days_without_special_days
