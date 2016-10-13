# © 2016 Jérôme Guerriat
# © 2016 Niboo SPRL (<https://www.niboo.be/>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from openerp import models, api
from openerp.exceptions import UserError


class HRTimesheetSheet(models.Model):
    _inherit = 'hr_timesheet_sheet.sheet'

    @api.multi
    def unlink(self):
        for ts in self:
            if any(line.leave_id for line in ts.timesheet_ids):
                raise UserError(
                    "You can't delete a timesheet with leaves."
                )
        return super(HRTimesheetSheet, self).unlink()
