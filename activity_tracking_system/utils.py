

from frappe import _
import frappe
from datetime import datetime, timedelta

@frappe.whitelist()
def get_current_month():
    today = datetime.today()
    first_day_of_month = today.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    last_day_of_month = today.replace(day=1, month=today.month % 12 + 1, hour=0, minute=0, second=0, microsecond=0) - timedelta(days=1)
    
    return first_day_of_month, last_day_of_month

@frappe.whitelist()
def get_activities_current_month():
    first_day_of_month, last_day_of_month = get_current_month()
    activities_count = frappe.db.count("Activity", filters={"activity_process_initiating_date": (">=", first_day_of_month), "activity_process_initiating_date": ("<", last_day_of_month)})
    print(activities_count)
    return activities_count

@frappe.whitelist()
def get_non_financial_activities_current_month():
    first_day_of_month, last_day_of_month = get_current_month()
    activities_count = frappe.db.count("Activity", filters={"activity_process_initiating_date": (">=", first_day_of_month), "activity_process_initiating_date": ("<", last_day_of_month), "type_of_activity": "Non-financial Activity"})
    print(activities_count)
    return activities_count

@frappe.whitelist()
def get_financial_activities_current_month():
    first_day_of_month, last_day_of_month = get_current_month()
    activities_count = frappe.db.count("Activity", filters={"activity_process_initiating_date": (">=", first_day_of_month), "activity_process_initiating_date": ("<", last_day_of_month), "type_of_activity": "Financial Activity"})
    print(activities_count)
    return activities_count

@frappe.whitelist()
def get_payment_not_processed_financial_activities_current_month():
    first_day_of_month, last_day_of_month = get_current_month()
    activities_count = frappe.db.count("Activity", filters={"activity_process_initiating_date": (">=", first_day_of_month), "activity_process_initiating_date": ("<", last_day_of_month), "type_of_activity": "Financial Activity", "status_of_the_activity":"Activity Completed But Payment Not Processed"})
    print(activities_count)
    return activities_count

@frappe.whitelist()
def get_financial_activities_completion_percentage():
    today = datetime.today()
    fiscal_year = get_fiscal_year(today)
    start_date = fiscal_year[0]
    end_date = fiscal_year[1]

    total_financial_activities = frappe.db.count("Activity", filters={"activity_process_initiating_date": (">=", start_date),
                                                                       "activity_process_initiating_date": ("<=", end_date),
                                                                       "type_of_activity": "Financial Activity"})

    completed_financial_activities = frappe.db.count("Activity", filters={"activity_process_initiating_date": (">=", start_date),
                                                                           "activity_process_initiating_date": ("<=", end_date),
                                                                           "type_of_activity": "Financial Activity",
                                                                           "status_of_the_activity": "Payment Processed"})

    if total_financial_activities > 0:
        completion_percentage = round(((completed_financial_activities / total_financial_activities) * 100),2)
    else:
        completion_percentage = 0
    
    return completion_percentage

def get_fiscal_year(date):
    fiscal_year_start = date.replace(month=1, day=1)
    fiscal_year_end = date.replace(month=12, day=31)
    
    return fiscal_year_start, fiscal_year_end

@frappe.whitelist()
def get_non_financial_activities_completion_percentage():
    today = datetime.today()
    fiscal_year = get_fiscal_year(today)
    start_date = fiscal_year[0]
    end_date = fiscal_year[1]

    total_non_financial_activities = frappe.db.count("Activity", filters={"activity_process_initiating_date": (">=", start_date),
                                                                       "activity_process_initiating_date": ("<=", end_date),
                                                                       "type_of_activity": "Non-financial Activity"})
    print(total_non_financial_activities)

    completed_non_financial_activities = frappe.db.count("Activity", filters={"activity_process_initiating_date": (">=", start_date),
                                                                           "activity_process_initiating_date": ("<=", end_date),
                                                                           "type_of_activity": "Non-financial Activity",
                                                                           "status_of_the_activity": "Activity Completed But Payment Not Required"})

    if total_non_financial_activities > 0:
        completion_percentage = round(((completed_non_financial_activities / total_non_financial_activities) * 100),2)
    else:
        completion_percentage = 0
    
    return completion_percentage