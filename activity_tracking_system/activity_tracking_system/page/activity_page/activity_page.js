frappe.pages['activity-page'].on_page_load = function(wrapper) {
    var page = frappe.ui.make_app_page({
        parent: wrapper,
        title: 'Activity',
        single_column: true
    });

    function goToCurrentMonthDetail() {
        window.location.href = "current-month-detail";
    }

    page.set_primary_action("Current Month Details", goToCurrentMonthDetail);

    // Create a Select field for supporting department
    page.supporting_department = page.add_field({
        fieldname: "supporting_department",
        label: __("Department"),
        fieldtype: "Select",
        options: []  // Initialize with an empty array
    });

    // Function to populate the Select field with Department records
    function loadDepartmentOptions() {
        frappe.call({
            method: 'frappe.client.get_list',
            args: {
                doctype: 'Department',
                fields: ['name'],
                limit_page_length: 0
            },
            callback: function(response) {
                if (response.message) {
                    var departments = response.message;
                    var options = departments.map(department => department.name);
                    page.supporting_department.df.options = options;
                    page.supporting_department.refresh();
                }
            }
        });
    }

    var activity_list_container = $('<div class="main-container"></div>').appendTo(page.body);

    page.refresh = function() {
        var filters = {
            supporting_department: page.supporting_department.get_value()
        };

        frappe.call({
            method: 'activity_tracking_system.activity_tracking_system.doctype.activity.activity.get_all_activities',
            args: {
                filters: JSON.stringify(filters)
            },
            callback: function(response) {
                if (response.message) {
                    var activities = response.message[0];
                    var notification_activities = response.message[1];
                    var activities_html = frappe.render_template("activity_page", { activities: activities, notification_activities: notification_activities });
                    activity_list_container.empty().append(activities_html);
                }
            }
        });
    };

    // Refresh page content when supporting department changes
    page.supporting_department.$input.on('change', function() {
        page.refresh();
    });

    var customButtonContainer = $('<div class="custom-button-container"></div>').appendTo(page.body);

    // Create Activity button
    var activityButtonContainer = $('<div class="custom-button"></div>').appendTo(customButtonContainer);
    var activityButton = $('<button>Activity</button>').appendTo(activityButtonContainer);
    activityButton.on('click', function() {
        window.location.href = "/app/activity";
    });

    // Create Project button
    var projectButtonContainer = $('<div class="custom-button"></div>').appendTo(customButtonContainer);
    var projectButton = $('<button>Project</button>').appendTo(projectButtonContainer);
    projectButton.on('click', function() {
        window.location.href = "/app/project";
    });

    // Create Funder Detail button
    var funderDetailButtonContainer = $('<div class="custom-button"></div>').appendTo(customButtonContainer);
    var funderDetailButton = $('<button>Funder Detail</button>').appendTo(funderDetailButtonContainer);
    funderDetailButton.on('click', function() {
        window.location.href = "/app/funder-details";
    });

    // Create Planning Sheet button
    var planningSheetButtonContainer = $('<div class="custom-button"></div>').appendTo(customButtonContainer);
    var planningSheetButton = $('<button>Planning Sheet</button>').appendTo(planningSheetButtonContainer);
    planningSheetButton.on('click', function() {
        window.location.href = "/app/planning-sheet";
    });

    // Load department options and refresh the page initially
    loadDepartmentOptions();
    page.refresh();
};
