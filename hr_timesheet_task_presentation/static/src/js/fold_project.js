$(document).ready(function () {
    $('.oe_timesheet_weekly_account').on('click', function () {
        var test = $(this).parent().next();
        while (test.find(">:first-child").hasClass("oe_timesheet_weekly_account_task")) {
            test.css('display', test.css('display') == "none" ? '' : 'none');
            test = test.next();
        }
    });
});
