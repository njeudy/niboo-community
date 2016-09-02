# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Jérôme Guerriat
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

from openerp import fields
from openerp import models
from openerp import api
from openerp import tools
from datetime import datetime, timedelta

class HRHolidays(models.Model):
    _inherit = "hr.holidays"

    # Read dates in user timezone
    @api.multi
    def onchange_date_from(self, date_to, date_from):
        date_from_user_tz = self.change_to_user_tz(date_from)
        date_to_user_tz = self.change_to_user_tz(date_to)
        return super(HRHolidays, self).onchange_date_from(date_to_user_tz,
                                                          date_from_user_tz)

    @api.multi
    def onchange_date_to(self, date_to, date_from):
        date_from_user_tz = self.change_to_user_tz(date_from)
        date_to_user_tz = self.change_to_user_tz(date_to)
        return super(HRHolidays, self).onchange_date_to(date_to_user_tz,
                                                        date_from_user_tz)

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
        for n in range(int((date_to - date_from).days)+1):
            yield date_from + timedelta(n)

    @api.model
    def onchange_date_with_emp(self, holiday_ids, date_to, date_from, employee_id,
                               type_change):
        # convert to user timezone
        date_to = self.change_to_user_tz(date_to)
        date_from = self.change_to_user_tz(date_from)

        # call onchange method depending on field changed
        if type_change == "date_to":
            result = self.onchange_date_to(date_to, date_from)
        else:
            result = self.onchange_date_from(date_to, date_from)

        # retrieve employee and the public leaves in its company

        employee = self.env['hr.employee'].browse(int(employee_id))
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

            if is_public_leave or\
                    (date.weekday() == 5 and deduct_saturday) or\
                    (date.weekday() == 6 and deduct_sunday):
                days_to_deduct += 1

        result['value']['number_of_days_temp'] -= days_to_deduct
        return result
