odoo.define('account_analytic_distribution_cross_company.PivotView', function (require) {
"use strict";
/*---------------------------------------------------------
 * Odoo Pivot Table view
 *---------------------------------------------------------*/

var core = require('web.core');
var crash_manager = require('web.crash_manager');
var formats = require('web.formats');
var framework = require('web.framework');
var session = require('web.session');
var Sidebar = require('web.Sidebar');
var utils = require('web.utils');
var View = require('web.View');

var _lt = core._lt;
var _t = core._t;
var total = _t("Total");

var PivotView = core.view_registry.get('pivot');

PivotView = PivotView.extend({
    prepare_fields: function (fields) {
        var self = this,
            groupable_types = ['many2one', 'char', 'boolean', 
                               'selection', 'date', 'datetime'];
        this.fields = fields;
        _.each(fields, function (field, name) {
            if ((name !== 'id') && (field.store === true)) {
                if (field.type === 'integer' || field.type === 'float' || field.type === 'monetary' || field.type === 'char') {
                    self.measures[name] = field;
                }
                if (_.contains(groupable_types, field.type)) {
                    self.groupable_fields[name] = field;
                }
            }
        });
        this.measures.__count__ = {string: "Quantity", type: "integer"};
    },

});

core.view_registry.add('pivot', PivotView);

return PivotView;

});

