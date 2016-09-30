# -*- coding: utf-8 -*-
# © 2016 Dutry Alexandre
# © 2016 Niboo SPRL (<https://www.niboo.be/>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html)

import json
import os
import sys

import jinja2
import openerp
from openerp import http
from openerp.addons.web.controllers.main import Database
from openerp.exceptions import AccessError
from openerp.tools import topological_sort

if hasattr(sys, 'frozen'):
    path = os.path.realpath(os.path.join(os.path.dirname(__file__),
                                         '..', 'views'))
    loader = jinja2.FileSystemLoader(path)
else:
    loader = jinja2.PackageLoader('openerp.addons.disable_database_manager', 'views')

env = jinja2.Environment(loader=loader, autoescape=True)
env.filters["json"] = json.dumps

db_monodb = http.db_monodb

class Database_restrict(Database):

    def _render_template(self, **db):
        db.setdefault('manage',True)
        db['insecure'] = openerp.tools.config['admin_passwd'] == 'admin'
        db['list_db'] = openerp.tools.config['list_db']
        db['langs'] = openerp.service.db.exp_list_lang()
        db['countries'] = openerp.service.db.exp_list_countries()
        # databases list
        db['databases'] = []
        try:
            db['databases'] = http.db_list()
        except openerp.exceptions.AccessDenied:
            monodb = db_monodb()
            if monodb:
                db['databases'] = [monodb]
        return env.get_template(
            'database_selector_no_manager_access.html').render(db)

    @http.route('/web/database/manager', type='http', auth='none')
    def manager(self, **kw):
        return http.local_redirect('/web/database/selector')

    @http.route('/web/database/backup', type='http', auth='none',
                methods=['POST'], csrf=False)
    def backup(self, master_pwd, name, backup_format='zip'):
        return http.local_redirect('/web/database/selector')

    @http.route('/web/database/drop', type='http', auth='none',
                methods=['POST'], csrf=False)
    def drop(self, master_pwd, name):
        return http.local_redirect('/web/database/selector')

    @http.route('/web/database/duplicate', type='http', auth='none',
                methods=['POST'], csrf=False)
    def duplicate(self, master_pwd, name, new_name):
        return http.local_redirect('/web/database/selector')

    @http.route('/web/database/create', type='http', auth='none',
                methods=['POST'], csrf=False)
    def create(self):
        return http.local_redirect('/web/database/selector')

    @http.route('/web/database/change_password', type='http', auth='none',
                methods=['POST'], csrf=False)
    def change_password(self, master_pwd, master_pwd_new):
        return http.local_redirect('/web/database/selector')

    @http.route('/web/database/restore', type='http', auth='none',
                methods=['POST'], csrf=False)
    def restore(self, master_pwd, backup_file, name, copy=False):
        return http.local_redirect('/web/database/selector')
