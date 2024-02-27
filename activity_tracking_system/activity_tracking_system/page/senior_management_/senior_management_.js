frappe.pages['senior-management-'].on_page_load = function(wrapper) {
    var page = frappe.ui.make_app_page({
        parent: wrapper,
        title: 'Senior Management Home Page',
        single_column: true
    });
    page.set_title('Senior Management');

    // Fetch and display number of activities for the current month
    fetch_activitiesCount()
        .then(activitiesCount => {
            render_numberCard(activitiesCount);
        })
        .catch(err => {
            console.error('Error fetching activities count', err);
        });

    // Fetch and display upcoming activities
    fetch_upcomingActivities()
        .then(upcomingActivities => {
            render_upcomingActivities(upcomingActivities);
        })
        .catch(err => {
            console.error('Error fetching upcoming activities', err);
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

    function fetch_upcomingActivities() {
        console.log("Senior management")
        return frappe.call({
            method: 'activity_tracking_system.activity_tracking_system.page.senior_management_.data.get_upcoming_activities',
            callback: function(response) {
                if (response.message) {
					console.log(response.message)
                    return response.message;
                } else {
                    return [];
                }
            }
        });
    }
	function render_upcomingActivities(upcomingActivities) {
		// Check if upcomingActivities is an array
		if (Array.isArray(upcomingActivities)) {
			// Render upcoming activities from the array
			renderActivitiesFromArray(upcomingActivities);
		} 
		// Check if upcomingActivities is an object
		else if (typeof upcomingActivities === 'object' && upcomingActivities !== null) {
			// Render upcoming activities from the object
			renderActivitiesFromObject(upcomingActivities);
		} else {
			console.error('Upcoming activities data is neither an array nor an object:', upcomingActivities);
		}
	}
	
	function renderActivitiesFromArray(upcomingActivities) {
		var $upcomingActivitiesList = $('<ul class="upcoming-activities-list">');
		upcomingActivities.forEach(function(activity) {
			console.log("Project Code:", activity.project_code);
			console.log("Project Name:", activity.project_name);
			var $activityItem = $('<li>').text(activity['Project Code'] + ': ' + activity[project_name]);
			$upcomingActivitiesList.append($activityItem);
		});
		page.wrapper.find('.page-content').append($upcomingActivitiesList);
	}
	
	function renderActivitiesFromObject(upcomingActivities) {
		var $upcomingActivitiesList = $('<ul class="upcoming-activities-list">');
		Object.keys(upcomingActivities).forEach(function(key) {
			var activity = upcomingActivities[key];
			console.log("Project Code:", activity.project_code);
			console.log("Project Name:", activity.project_name);
			var $activityItem = $('<li>').text(activity.project_code + ': ' + activity.project_name);
			$upcomingActivitiesList.append($activityItem);
		});
		page.wrapper.find('.page-content').append($upcomingActivitiesList);
	}
	
	
	
	
	
	
	
	

    // Other actions and buttons...
};
