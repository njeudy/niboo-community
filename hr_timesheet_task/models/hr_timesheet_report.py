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

from openerp import models, fields


class HrTimesheetReport(models.Model):
    _inherit = "hr.timesheet.report"

    task_id = fields.Many2one('project.task', 'Task', readonly=True)

    def _select(self):
        return super(HrTimesheetReport, self)._select()+""",
            aal.task_id
        """

    def _group_by(self):
        return super(HrTimesheetReport, self)._group_by()+""",
            task_id"""
