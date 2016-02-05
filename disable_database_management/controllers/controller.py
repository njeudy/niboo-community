# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Aurelien Muller & Jeremy Van Driessche
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

from openerp import http
import openerp
import jinja2
import sys
import os

if hasattr(sys, 'frozen'):
    # When running on compiled windows binary, we don't have access to package loader.
    path = os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'views'))
    loader = jinja2.FileSystemLoader(path)
else:
    loader = jinja2.PackageLoader('openerp.addons.tra_web_database', "views")

db_monodb = http.db_monodb
env = jinja2.Environment(loader=loader, autoescape=True)

class DatabaseSecurity(openerp.addons.web.controllers.main.Database):

    def _render_template(self, **d):
        d.setdefault('manage',True)
        d['insecure'] = openerp.tools.config['admin_passwd'] == 'admin'
        d['list_db'] = openerp.tools.config['list_db']
        d['langs'] = openerp.service.db.exp_list_lang()
        # databases list
        d['databases'] = []
        try:
            d['databases'] = http.db_list()
        except openerp.exceptions.AccessDenied:
            monodb = db_monodb()
            if monodb:
                d['databases'] = [monodb]

        return env.get_template("database_manager.html").render(d)


    @http.route()
    def selector(self, **kw):
        print "hello"
        return self._render_template(manage=False)


    @http.route()
    def duplicate(self, master_pwd, name, new_name):
        error = "You are not allowed to do such operations"
        return self._render_template(error=error)


    @http.route()
    def drop(self, master_pwd, name):
        error = "You are not allowed to do such operations"
        return self._render_template(error=error)


    @http.route()
    def backup(self, master_pwd, name, backup_format = 'zip'):
        error = "You are not allowed to do such operations"
        return self._render_template(error=error)


    @http.route()
    def restore(self, master_pwd, backup_file, name, copy=False):
        error = "You are not allowed to do such operations"
        return self._render_template(error=error)


    @http.route()
    def change_password(self, master_pwd, master_pwd_new):
        error = "You are not allowed to do such operations"
        return self._render_template(error=error)
