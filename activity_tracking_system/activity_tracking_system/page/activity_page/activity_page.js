frappe.pages['activity-page'].on_page_load = function(wrapper) {
    // Create the page with the specified title and layout
    var page = frappe.ui.make_app_page({
        parent: wrapper,
        title: 'Activity',
        single_column: true
    });

    // Function to handle navigation to Current Month Details
    function goToCurrentMonthDetail() {
        window.location.href = "current-month-detail";
    }

    // Set primary action button to navigate to Current Month Details
    page.set_primary_action("Current Month Details", goToCurrentMonthDetail);

    // Add a dropdown field for selecting the type of activity
    page.type_of_activity = page.add_field({
        fieldname: "type_of_activity",
        label: __("Type of Activity"),
        fieldtype: "Select",
        options: ["Financial", "Non-financial"]
    });

    // Add a field for selecting the supporting department
    page.supporting_department = page.add_field({
        fieldname: "supporting_department",
        label: __("Department"),
        fieldtype: "Link",
        options: "Department"
    });

    var activity_list_container = $('<div class="main-container"></div>').appendTo(page.body);

    // Function to refresh the page content
    page.refresh = function() {
        var type_of_activity = page.type_of_activity.get_value();
        var department = page.supporting_department.get_value();
        activity_list_container.empty();

        // Fetch activities and notifications
        frappe.call({
            method: 'activity_tracking_system.activity_tracking_system.doctype.activity.activity.get_all_activities',
            args: {
                type_of_activity: type_of_activity,
                supporting_department: department
            },
            callback: function(response) {
                if (response.message) {
                    var activities = response.message[0]; // First array contains activities
                    var notification_activities = response.message[1]; // Second array contains notification activities
                    var activities_html = frappe.render_template("activity_page", { activities: activities, notification_activities: notification_activities });
                    activity_list_container.append(activities_html);
                }
            }
        });
    };

    // Refresh page content when type of activity changes
    page.type_of_activity.$input.on('change', function() {
        page.refresh();
    });

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

    // Initial page load
    page.refresh();
};
