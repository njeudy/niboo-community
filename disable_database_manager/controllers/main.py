# -*- coding: utf-8 -*-
# © 2016 Dutry Alexandre
# © 2016 Niboo SPRL (<https://www.niboo.be/>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html)

import os
import sys

import jinja2
import openerp
import simplejson
from openerp import http
from openerp.addons.web.controllers.main import Database
from openerp.exceptions import except_orm
from openerp.http import request

if hasattr(sys, 'frozen'):

    path = os.path.realpath(os.path.join(os.path.dirname(__file__),
                                         '..', 'views'))
    loader = jinja2.FileSystemLoader(path)
else:
    loader = jinja2.PackageLoader('openerp.addons.db_manager', 'views')

env = jinja2.Environment(loader=loader, autoescape=True)
env.filters["json"] = simplejson.dumps

class Database_restrict(Database):

    @http.route('/web/database/selector', type='http', auth='none')
    def selector(self, **kw):
        try:
            dbs = http.db_list()
            if not dbs:
                return http.local_redirect('/web/database/manager')
        except openerp.exceptions.AccessDenied:
            dbs = False
        return env.get_template(
            'database_selector_no_manager_access.html').render({
            'databases': dbs,
            'debug': request.debug,
            'error': kw.get('error')
        })

    @http.route('/web/database/manager', type='http', auth='none')
    def manager(self, **kw):
        return http.local_redirect('/web/database/selector')

    @http.route('/web/database/backup', type='http', auth='none',
                methods=['POST'], csrf=False)
    def backup(self, master_pwd, name, backup_format='zip'):
        return http.local_redirect('/web/database/selector')

    @http.route('/web/database/drop', type='json', auth='none',
                methods=['POST'], csrf=False)
    def drop(self, master_pwd, name):
        return {'error': 'AccessDenied', 'title': 'Deleting databases is not permitted'}

    @http.route('/web/database/duplicate', type='json', auth='none')
    def duplicate(self, fields):
        return {'error': 'AccessDenied', 'title': 'Duplicating databases is not permitted'}

    @http.route('/web/database/create', type='json', auth='none',
                methods=['POST'], csrf=False)
    def create(self):
        return {'error': 'AccessDenied', 'title': 'Creating databases is not permitted'}

    @http.route('/web/database/change_password', type='json', auth='none')
    def change_password(self, fields):
        return {'error': 'AccessDenied', 'title': 'Changing password is not permitted'}

    @http.route('/web/database/restore', type='http', auth='none')
    def restore(self, db_file, restore_pwd, new_db, mode):
        return http.local_redirect('/web/database/selector')
