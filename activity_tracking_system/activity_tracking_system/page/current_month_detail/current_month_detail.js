frappe.pages['current-month-detail'].on_page_load = function(wrapper) {
    var page = frappe.ui.make_app_page({
        parent: wrapper,
        title: 'Current Month Details',
        single_column: true
    });


     // Add buttons to navigate to Activity and Home pages
     page.set_primary_action('Go to Activity Page', function() {
        frappe.set_route('activity-page');
    });

    page.set_secondary_action('Go to Home', function() {
        frappe.set_route('app');
    });

    // Fetch the activity details from the server
    frappe.call({
        method: 'activity_tracking_system.utils.get_activity_details', // Update with the correct path
        callback: function(response) {
            if (response.message) {
				console.log(response.message)
                // Render the HTML template with the fetched data
                var rendered_html = frappe.render_template("current_month_detail", response.message);
                
                // Append the rendered HTML content to the main page container
                $(page.main).html(rendered_html);
            }
        }
    });
}
