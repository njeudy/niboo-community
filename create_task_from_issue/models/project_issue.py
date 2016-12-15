# -*- coding: utf-8 -*-
# © 2016 Jérôme Guerriat
# © 2016 Niboo SPRL (<https://www.niboo.be/>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from openerp import api, models


class ProjectIssue(models.Model):
    _inherit = 'project.issue'

    @api.multi
    def create_task(self):
        self.ensure_one()

        current_sprint = self.env['project.sprint'].search([
            ('is_current_sprint','=',True)
        ])

        task = self.env['project.task'].create({
            'name': self.name,
            'description': self.description,
            'user_id': self._uid,
            'project_id': self.project_id.id,
            'sprint_id': current_sprint.id,
            'identifier': "-",
        })

        self.task_id = task.id
