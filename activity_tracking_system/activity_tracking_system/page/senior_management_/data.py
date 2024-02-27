import frappe


@frappe.whitelist()
def get_upcoming_activities():
    today = frappe.utils.nowdate()
    end_of_month = frappe.utils.data.get_last_day(today)
    
    # Fetch activities whose start date is between today and end of the month
    activities = frappe.get_all("Activity", 
        filters={"activity_to_be_completed_in_which_month": (">=", today), "activity_to_be_completed_in_which_month": ("<=", end_of_month)},
        fields=["project_code", "project_name","activity_process_initiating_date","activity_to_be_completed_in_which_month" ,"type_of_activity", "status_of_the_activity", "assigned_to_which_department_for_support"])
    
    return activities