# Copyright (c) 2024, Tech4Good Community and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe import _

class Activity(Document):
    def validate(self):
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
def get_all_activities():
    activities = frappe.get_all("Activity", fields=["name","activity" ,"type_of_activity", "city", "state", "activity_to_be_completed_in_which_month"])
    print(activities)
    return activities




    #frappe.msgprint(_("Activity {0} created in Planning Sheet {1}").format(new_activity.activity, planning_sheet.name))






