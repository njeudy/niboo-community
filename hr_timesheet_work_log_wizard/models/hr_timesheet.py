# -*- coding: utf-8 -*-
# © 2016 Pierre Faniel
# © 2016 Niboo SPRL (<https://www.niboo.be/>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from openerp import api, models


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
