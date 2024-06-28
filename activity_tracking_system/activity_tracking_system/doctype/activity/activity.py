
import frappe
from frappe.model.document import Document
from frappe import _
import json, datetime

class Activity(Document):
    def validate(self):
 # Check if all date fields are filled
        if not self.activity_completion_date or not self.activity_process_initiating_date or not self.activity_to_be_completed_in_which_month:
            frappe.throw(_("Please fill all date fields: Activity Completion Date, Activity Process Initiating Date, and Activity To Be Completed In Which Month."), title=_("Missing Date Fields"))
       #Was showing unknown error if condition occured.
        if self.activity_completion_date:
            if self.activity_completion_date < self.activity_process_initiating_date:
                frappe.throw(title='Error', msg='Initiation date cannot be greater than completion date')
        if self.activity_to_be_completed_in_which_month:
            if self.activity_to_be_completed_in_which_month < self.activity_process_initiating_date:
                frappe.throw(title='Error', msg='Completion date cannot be lesser than initiation date')


@frappe.whitelist()
def create_activity_in_planning_sheet(doc_name):
    doc = frappe.get_doc("Activity", doc_name)

    planning_sheet = frappe.get_doc("Planning Sheet", doc.planning_sheet)
    existing_activities = [activity.activity for activity in planning_sheet.activities_for_approval]

    if doc_name not in existing_activities:
        new_activity = planning_sheet.append("activities_for_approval", {})
        new_activity.activity = doc_name
        new_activity.activity_type = doc.type_of_activity
        new_activity.city = doc.city
        new_activity.state = doc.state

        doc.save()
        planning_sheet.save(ignore_permissions=True)
        frappe.msgprint(f"Activity {doc_name} added to the planning sheet.")
    else:
        frappe.msgprint(f"Activity {doc_name} already exists in the planning sheet.")


@frappe.whitelist()
def get_all_activities(filters=None):
    try:
        filters = json.loads(filters or '{}')
        current_date = datetime.date.today()
        start_of_month = current_date.replace(day=1)
        end_of_month = current_date.replace(day=1, month=current_date.month % 12 + 1, year=current_date.year if current_date.month < 12 else current_date.year + 1) - datetime.timedelta(days=1)

        activity_filters = {
            'activity_to_be_completed_in_which_month': ['>=', start_of_month],
            'activity_to_be_completed_in_which_month': ['<=', end_of_month],
        }
            
        if 'supporting_department' in filters and filters['supporting_department']:
            activity_filters['assigned_to_which_department_for_support'] = filters['supporting_department']

        print(activity_filters)
        activities = frappe.db.get_list('Activity',
            fields=['name', 'activity', 'type_of_activity', 'city', 'assigned_to_which_department_for_support', 'activity_to_be_completed_in_which_month'],
            filters=activity_filters
        )

        notification_activities = frappe.db.get_list('Activity',
            fields=['activity', 'activity_completion_date'],
            filters={
                'activity_completion_date': ['>=', current_date],
                'activity_completion_date': ['<=', end_of_month]
            }
        )

        # Filter out activities without a completion date
        notification_activities = [activity for activity in notification_activities if activity.get('activity_completion_date') is not None]

        # Format dates for display
        for activity in activities:
            activity['activity_to_be_completed_in_which_month'] = frappe.utils.formatdate(activity['activity_to_be_completed_in_which_month'], 'MMMM YYYY')
        for activity in notification_activities:
            activity['activity_completion_date'] = frappe.utils.formatdate(activity['activity_completion_date'], 'dd MMMM YYYY')
        
        return activities, notification_activities
    except Exception as e:
        frappe.log_error(message=frappe.get_traceback(), title="Error in get_activities_for_current_month")
        raise e







