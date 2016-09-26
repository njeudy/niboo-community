odoo.define('readonly_sheet.sheet', function (require) {
    "use strict";

    var core = require('web.core');

    var _t = core._t;

    var WeeklyTimesheet = core.form_custom_registry.get('weekly_timesheet').extend({
        events: {
            "click .oe_timesheet_weekly_account a": "go_to",
            "click .oe_timesheet_weekly_account_task a": "go_to_task",
        },

        initialize_content: function() {
            var self = this;
            self.set('effective_readonly', true);
            self._super();
        },

        display_data: function() {
            var self = this;
            self._super();
            self.add_listener_on_oe_timesheet_weekly_box();
        },
        add_listener_on_oe_timesheet_weekly_box: function(){
            var self = this;

            var on_closed = function(reason) {
                if (!_.isObject(reason)) {
                    self.view.recursive_reload();
                }
            };

            var result_handler = function () {
                if (on_closed) { on_closed.apply(null, arguments); }
                if (self.getParent() && self.getParent().on_action_executed) {
                    return self.getParent().on_action_executed.apply(null, arguments);
                }
            };

            $(".oe_timesheet_weekly_box:parent").off('click.box');
            $(".oe_timesheet_weekly_box:parent").on('click.box', function (event) {
                var project_and_task = $(event.currentTarget).attr('data-account-task').split(',');
                var project_id = project_and_task[0];
                var task_id = project_and_task[1];

                var days_offest = $(event.currentTarget).attr('data-day-count');
                var date_start = self.field_manager.get_field_value("date_from");
                var millis = new Date(date_start).getTime();
                millis += days_offest * 24 * 60 * 60 *1000;
                var true_date = new Date(millis);

                self.do_action({
                    name: _t("Log Work"),
                    type: "ir.actions.act_window",
                    res_model: "hr_timesheet.work.logger",
                    domain : [],
                    views: [[false, "form"]],
                    target: 'new',
                    context: {
                        'default_analytic_account_id':parseInt(project_id),
                        'default_task_id':parseInt(task_id),
                        'default_date_started':true_date,
                    },
                },{on_close: result_handler});
            });
        }
    });

    core.form_custom_registry.add('weekly_timesheet', WeeklyTimesheet);

});
