frappe.pages['senior-management-'].on_page_load = function(wrapper) {
    var page = frappe.ui.make_app_page({
        parent: wrapper,
        title: 'Senior Management Home Page',
        single_column: true
    });
    page.set_title('Senior Management');
    page.set_indicator('Pending', 'orange');
    let $btn = page.set_secondary_action('Refresh', () => refresh(), 'octicon octicon-sync');

    // Fetch and display number of activities for the current month
    fetch_activitiesCount()
        .then(activitiesCount => {
            render_numberCard(activitiesCount);
        })
        .catch(err => {
            console.error('Error fetching activities count', err);
        });

    function fetch_activitiesCount() {
        // Use Frappe API to call the Python function
        return frappe.call({
            method: 'activity_tracking_system.utils.get_activities_current_month', // Adjust to your app name
            callback: function(response) {
                if (response.message) {
					console.log(response.message)
                    return response.message;
                } else {
                    return 0;
                }
            }
        });
    }

    function render_numberCard(activitiesCount) {
        // Render number of activities in a number card
        var $numberCard = $('<div class="number-card">').html('<div class="number">' + activitiesCount + '</div><div class="text">Activities this month</div>');
        // Append number card to the page
        page.wrapper.find('.page-content').append($numberCard);
    }

    // Other actions and buttons...
};
