frappe.pages['activity-page'].on_page_load = function(wrapper) {
    var page = frappe.ui.make_app_page({
        parent: wrapper,
        title: 'Activity',
        single_column: true
    });

    // Create a container for the activity cards
    var activity_box = $('<div class="activity-box">').appendTo(page.body);

    // HTML template for activity cards
    var template = `
        <div class="activity-card">
            <div class="activity-name">{{ activity_name }}</div>
            <div class="activity-type">{{ activity_type }}</div>
			<div class ="activity-city">{{ activity_city }}</div>
			<div class="activity-completion-date"> {{ activity_completion_date }}</div>
        </div>
    `;

    frappe.call({
        method: 'activity_tracking_system.activity_tracking_system.doctype.activity.activity.get_all_activities',
        callback: function(response) {
            var activities = response.message;
            if (!template) {
                console.error('Activity card template not found');
                return;
            }
            $.each(activities, function(i, activity) {
                // Replace placeholders with actual data
                var activity_html = template
                    .replace('{{ activity_name }}', activity.activity)
                    .replace('{{ activity_type }}', activity.type_of_activity)
					.replace('{{ activity_city }}', activity.city)
					.replace('{{ activity_completion_date }}', activity.activity_to_be_completed_in_which_month)
                // Append the rendered HTML to the activity box
                activity_box.append(activity_html);
            });
        }
    });
}
