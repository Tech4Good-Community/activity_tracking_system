

from frappe import _
import frappe
from datetime import datetime, timedelta

@frappe.whitelist()
def get_current_month():
    today = datetime.today()
    year = today.year
    month = today.month
    
    # Check if the current year is a leap year
    is_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    
    # Calculate the last day of February based on whether it's a leap year or not
    if is_leap_year:
        last_day_of_february = 29
    else:
        last_day_of_february = 28
    
    # Set the last day of the month based on the month
    if month == 2:  
        last_day_of_month = last_day_of_february
    elif month in [4, 6, 9, 11]: 
        last_day_of_month = 30
    else:
        last_day_of_month = 31
    
    first_day_of_month = today.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    last_day_of_month = today.replace(day=last_day_of_month, hour=23, minute=59, second=59, microsecond=999999)
    
    return first_day_of_month, last_day_of_month

@frappe.whitelist()
def get_previous_month():
    today = datetime.today()
    year = today.year
    month = (today.month)-1
    
     # Check if the current year is a leap year
    is_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    
    # Calculate the last day of February based on whether it's a leap year or not
    if is_leap_year:
        last_day_of_february = 29
    else:
        last_day_of_february = 28
    
    # Set the last day of the month based on the month
    if month == 2:  
        last_day_of_month = last_day_of_february
    elif month in [4, 6, 9, 11]: 
        last_day_of_month = 30
    else:
        last_day_of_month = 31
    
    first_day_of_month = today.replace(month=month, day=1, hour=0, minute=0, second=0, microsecond=0)
    last_day_of_month = today.replace(month = month, day=last_day_of_month, hour=23, minute=59, second=59, microsecond=999999)
    
    return first_day_of_month, last_day_of_month

@frappe.whitelist()
def get_activities_current_month():
    first_day_of_month, last_day_of_month = get_current_month()
    
    activities_count = frappe.db.count("Activity", filters={"activity_to_be_completed_in_which_month": 
                                                             ["between", [first_day_of_month, last_day_of_month]]})
    
    activities = frappe.get_all("Activity", filters={"activity_to_be_completed_in_which_month": 
                                                      ["between", [first_day_of_month, last_day_of_month]]})
    
    return activities_count


@frappe.whitelist()
def get_non_financial_activities_current_month():
    first_day_of_month, last_day_of_month = get_current_month()
    non_financial_activities_count = frappe.db.count("Activity", filters={"activity_to_be_completed_in_which_month": 
                                                             ["between", [first_day_of_month, last_day_of_month]], "type_of_activity": "Non-financial Activity"})
    activities = frappe.get_all("Activity", filters={"activity_to_be_completed_in_which_month": 
                                                             ["between", [first_day_of_month, last_day_of_month]], "type_of_activity": "Non-financial Activity"})
    return non_financial_activities_count

@frappe.whitelist()
def get_financial_activities_current_month():
    first_day_of_month, last_day_of_month = get_current_month()
    financial_activities_count = frappe.db.count("Activity", filters={"activity_to_be_completed_in_which_month": 
                                                             ["between", [first_day_of_month, last_day_of_month]], "type_of_activity": "Financial Activity"})
   
    return financial_activities_count

@frappe.whitelist()
def get_payment_not_processed_financial_activities_current_month():
    first_day_of_month, last_day_of_month = get_current_month()
    activities_count = frappe.db.count("Activity", filters={"activity_to_be_completed_in_which_month": 
                                                             ["between", [first_day_of_month, last_day_of_month]], "type_of_activity": "Financial Activity", "status_of_the_activity":"Activity Completed But Payment Not Processed"}) 
    return activities_count

@frappe.whitelist()
def get_financial_activities_completion_percentage():
    today = datetime.today()
    fiscal_year = get_fiscal_year(today)
    start_date = fiscal_year[0]
    end_date = fiscal_year[1]

    total_financial_activities = frappe.db.count("Activity", filters={"activity_to_be_completed_in_which_month": ["between", [start_date, end_date]],
                                                                       "type_of_activity": "Financial Activity"})

    completed_financial_activities = frappe.db.count("Activity", filters={"activity_to_be_completed_in_which_month": ["between", [start_date, end_date]],
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

    total_non_financial_activities = frappe.db.count("Activity", filters={"activity_to_be_completed_in_which_month": ["between", [start_date, end_date]],
                                                                       "type_of_activity": "Non-financial Activity"})

    completed_non_financial_activities = frappe.db.count("Activity", filters={"activity_to_be_completed_in_which_month": ["between", [start_date, end_date]],
                                                                           "type_of_activity": "Non-financial Activity",
                                                                           "status_of_the_activity": "Activity Completed But Payment Not Required"})

    if total_non_financial_activities > 0:
        completion_percentage = round(((completed_non_financial_activities / total_non_financial_activities) * 100),2)
    else:
        completion_percentage = 0
    
    return completion_percentage

@frappe.whitelist()
def get_non_financial_activities_completed_on_time_current_month_percentage():
    first_day_of_month, last_day_of_month = get_current_month()
    
    total_non_financial_activites_completed = frappe.db.count("Activity", filters = {"type_of_activity": "Non-financial Activity",
                                                                                     "activity_completion_date": ["between", [first_day_of_month, last_day_of_month]],
                                                             "activity_to_be_completed_in_which_month":["between", [first_day_of_month, last_day_of_month]]})
    
    total_non_financial_activities =  frappe.db.count("Activity", filters = {"activity_to_be_completed_in_which_month":["between", [first_day_of_month, last_day_of_month]],
                                                             "type_of_activity": "Non-financial Activity"})
    
    if total_non_financial_activities > 0:
        percentage_of_non_financial_activities_completed = round(((total_non_financial_activites_completed / total_non_financial_activities) * 100),2)
    else:
        percentage_of_non_financial_activities_completed = 0
    
    return percentage_of_non_financial_activities_completed
    

@frappe.whitelist()
def get_financial_activities_completed_on_time():
    first_day_of_month, last_day_of_month = get_current_month()
    
    activities_count = frappe.db.count("Activity", filters={"type_of_activity": "Financial Activity",
                                                             "activity_completion_date":["between", [first_day_of_month, last_day_of_month]],
                                                             "activity_to_be_completed_in_which_month":["between", [first_day_of_month, last_day_of_month]]})
    
    return activities_count

@frappe.whitelist()
def get_num_of_non_financial_activities_due():
    first_day_of_month, last_day_of_month = get_current_month()

    completed_activities_count = frappe.db.count("Activity", filters={"type_of_activity": "Non-financial Activity",
                                                                      "activity_completion_date":["between", [first_day_of_month, last_day_of_month]],
                                                                      })

    total_activities_count = frappe.db.count("Activity", filters={"type_of_activity": "Non-financial Activity",
                                                                  "activity_to_be_completed_in_which_month": ["between", [first_day_of_month, last_day_of_month]]})

    due_activities_count = total_activities_count - completed_activities_count
    
    return due_activities_count

@frappe.whitelist()
def get_num_of_financial_activities_payment_processed():
    first_day_of_month, last_day_of_month = get_current_month()
    
    completed_activities_count = frappe.db.count("Activity", filters={"type_of_activity": "Financial Activity",
                                                                       "activity_completion_date":["between", [first_day_of_month, last_day_of_month]],
                                                                       "activity_to_be_completed_in_which_month": ["between", [first_day_of_month, last_day_of_month]],
                                                                    "status_of_the_activity":"Payment Processed"
                                                                    
                                                                      })
    return completed_activities_count

@frappe.whitelist()
def get_percentage_of_financial_activities_payment_processed():
    first_day_of_month, last_day_of_month = get_current_month()
    
    completed_activities_count = frappe.db.count("Activity", filters={"type_of_activity": "Financial Activity",
                                                                      "activity_completion_date":["between", [first_day_of_month, last_day_of_month]],
                                                                      "activity_to_be_completed_in_which_month": ["between", [first_day_of_month, last_day_of_month]]
                                                                     })
    payment_processed_activities = frappe.db.count("Activity", filters={"type_of_activity": "Financial Activity",
                                                                       "activity_completion_date": ["between", [first_day_of_month, last_day_of_month]],
                                                                       "activity_to_be_completed_in_which_month":["between", [first_day_of_month, last_day_of_month]],
                                                                       "status_of_the_activity":"Payment Processed"
                                                                      })
    if completed_activities_count > 0:
        percentage_of_financial_activities_processed_payment = round(((payment_processed_activities / completed_activities_count) * 100), 2)
    else:
        percentage_of_financial_activities_processed_payment = 0

    return percentage_of_financial_activities_processed_payment


@frappe.whitelist()
def get_budget_utilized_sum():
    first_day_of_month, last_day_of_month = get_current_month()


    # Query budget utilization records within the given time frame
    budget_utilization_records = frappe.get_all("Activity",
                                                filters={"type_of_activity": "Financial Activity",
                                                                      "activity_completion_date":["between", [first_day_of_month, last_day_of_month]]},
                                                fields=["sum(actual_amount_utilised) as actual_budget_utilised_for_the_current_month"])

    # Extract the sum of budget utilized from the query result
    total_utilized_sum = budget_utilization_records[0].actual_budget_utilised_for_the_current_month if budget_utilization_records else 0

    return total_utilized_sum

@frappe.whitelist()
def get_budget_allocated_sum():
    first_day_of_month, last_day_of_month = get_current_month()
    
    budget_allocated_records = frappe.get_all("Activity",
                                              filters={"type_of_activity": "Financial Activity",
                                                       "activity_completion_date": ["between", [first_day_of_month, last_day_of_month]]},
                                              fields=["sum(budget_approved_for_utilisation_in_the_tenure) as actual_budget_allocated_for_the_current_month"])
    
    total_allocated_sum = budget_allocated_records[0].actual_budget_allocated_for_the_current_month if budget_allocated_records else 0
    
    return total_allocated_sum

@frappe.whitelist()
def get_percentage_of_budget_utilised():
    total_utilized_sum = get_budget_utilized_sum()
    total_allocated_sum = get_budget_allocated_sum()
    
    if total_allocated_sum != 0:  # Avoid division by zero
        percentage_of_budget_utilised = round(((total_utilized_sum / total_allocated_sum) * 100), 2)
    else:
        percentage_of_budget_utilised = 0
    
    return percentage_of_budget_utilised

@frappe.whitelist()
def number_of_non_financial_activities_overdue_from_the_last_month():
    first_day_of_month, last_day_of_month = get_previous_month()
    activities_count = frappe.db.count("Activity", filters={"activity_to_be_completed_in_which_month": 
                                                             ["between", [first_day_of_month, last_day_of_month]], "type_of_activity": "Non-financial Activity", "status_of_the_activity": "Over Due"})
    return activities_count

@frappe.whitelist()
def number_of_financial_activities_overdue_from_the_last_month():
    first_day_of_month, last_day_of_month = get_previous_month()
    activities_count = frappe.db.count("Activity", filters={"activity_to_be_completed_in_which_month": 
                                                             ["between", [first_day_of_month, last_day_of_month]], "type_of_activity": "financial Activity", "status_of_the_activity": "Over Due"})
    return activities_count

@frappe.whitelist()
def get_activity_details():
    first_day_of_month, last_day_of_month = get_current_month()
    current_month = datetime.now().strftime('%B')
    activities_count = frappe.db.count("Activity", filters={"activity_to_be_completed_in_which_month": 
                                                             ["between", [first_day_of_month, last_day_of_month]]})
    
    # Fetching non-financial activities count
    non_financial_activities_count = frappe.db.count("Activity", filters={"activity_to_be_completed_in_which_month": 
                                                             ["between", [first_day_of_month, last_day_of_month]], 
                                                             "type_of_activity": "Non-financial Activity"})
    
    # Fetching financial activities count
    financial_activities_count = frappe.db.count("Activity", filters={"activity_to_be_completed_in_which_month": 
                                                             ["between", [first_day_of_month, last_day_of_month]], 
                                                             "type_of_activity": "Financial Activity"})

    # Fetching budget allocated for financial activities
    budget_allocated_records = frappe.get_all("Activity",
                                              filters={"type_of_activity": "Financial Activity",
                                                       "activity_to_be_completed_in_which_month": ["between", [first_day_of_month, last_day_of_month]]},
                                              fields=["sum(budget_approved_for_utilisation_in_the_tenure) as actual_budget_allocated_for_the_current_month"])
    
    actual_budget_allocated_for_the_current_month = budget_allocated_records[0].actual_budget_allocated_for_the_current_month if budget_allocated_records else 0


    financial_completed_activities_count = frappe.db.count("Activity", filters={"type_of_activity": "Financial Activity",
                                                                       "activity_completion_date":["between", [first_day_of_month, last_day_of_month]],
                                                                       "activity_to_be_completed_in_which_month": ["between", [first_day_of_month, last_day_of_month]],
                                                                    "status_of_the_activity":"Payment Processed"
                                                                    
                                                                      })
    
    total_utilized_sum = get_budget_utilized_sum()
    total_allocated_sum = get_budget_allocated_sum()
    
    if total_allocated_sum != 0:  # Avoid division by zero
        percentage_of_budget_utilised = round(((total_utilized_sum / total_allocated_sum) * 100), 2)
    else:
        percentage_of_budget_utilised = 0

    today = datetime.today()
    fiscal_year = get_fiscal_year(today)
    start_date = fiscal_year[0]
    end_date = fiscal_year[1]

    total_financial_activities_for_financial_year = frappe.db.count("Activity", filters={"activity_to_be_completed_in_which_month": ["between", [start_date, end_date]],
                                                                       "type_of_activity": "Financial Activity"})

    completed_financial_activities_for_financial_year = frappe.db.count("Activity", filters={"activity_to_be_completed_in_which_month": ["between", [start_date, end_date]],
                                                                           "type_of_activity": "Financial Activity",
                                                                           "status_of_the_activity": "Payment Processed"})

    if total_financial_activities_for_financial_year > 0:
        completion_percentage = round(((completed_financial_activities_for_financial_year / total_financial_activities_for_financial_year) * 100),2)
    else:
        completion_percentage = 0
    
    budget_utilization_records = frappe.get_all("Activity",
                                                filters={"type_of_activity": "Financial Activity",
                                                                      "activity_completion_date":["between", [first_day_of_month, last_day_of_month]]},
                                                fields=["sum(actual_amount_utilised) as actual_budget_utilised_for_the_current_month"])

    total_utilized_sum = budget_utilization_records[0].actual_budget_utilised_for_the_current_month if budget_utilization_records else 0
    
    completed_activities_count = frappe.db.count("Activity", filters={"type_of_activity": "Financial Activity",
                                                                      "activity_completion_date":["between", [first_day_of_month, last_day_of_month]],
                                                                      "activity_to_be_completed_in_which_month": ["between", [first_day_of_month, last_day_of_month]]
                                                                     })
    payment_processed_activities = frappe.db.count("Activity", filters={"type_of_activity": "Financial Activity",
                                                                       "activity_completion_date": ["between", [first_day_of_month, last_day_of_month]],
                                                                       "activity_to_be_completed_in_which_month":["between", [first_day_of_month, last_day_of_month]],
                                                                       "status_of_the_activity":"Payment Processed"
                                                                      })
    if completed_activities_count > 0:
        percentage_of_financial_activities_processed_payment = round(((payment_processed_activities / completed_activities_count) * 100), 2)
        print(percentage_of_financial_activities_processed_payment)
    else:
        percentage_of_financial_activities_processed_payment = 0

    
    due_payment_financial_activities_count = frappe.db.count("Activity", filters={"activity_to_be_completed_in_which_month": 
                                                             ["between", [first_day_of_month, last_day_of_month]], "type_of_activity": "Financial Activity", "status_of_the_activity":"Activity Completed But Payment Not Processed"}) 
    
    financial_activities_over_due_from_last_month = number_of_financial_activities_overdue_from_the_last_month()

    total_non_financial_activities = frappe.db.count("Activity", filters={"activity_to_be_completed_in_which_month": ["between", [start_date, end_date]],
                                                                       "type_of_activity": "Non-financial Activity"})

    completed_non_financial_activities = frappe.db.count("Activity", filters={"activity_to_be_completed_in_which_month": ["between", [start_date, end_date]],
                                                                           "type_of_activity": "Non-financial Activity",
                                                                           "status_of_the_activity": "Activity Completed But Payment Not Required"})

    if total_non_financial_activities > 0:
        non_financial_completion_percentage = round(((completed_non_financial_activities / total_non_financial_activities) * 100),2)
    else:
        non_financial_completion_percentage = 0

    non_financial_activities_overdue_count = number_of_non_financial_activities_overdue_from_the_last_month()

    total_non_financial_activites_completed = frappe.db.count("Activity", filters = {"type_of_activity": "Non-financial Activity",
                                                                                     "activity_completion_date": ["between", [first_day_of_month, last_day_of_month]],
                                                             "activity_to_be_completed_in_which_month":["between", [first_day_of_month, last_day_of_month]]})
    
    total_non_financial_activities =  frappe.db.count("Activity", filters = {"activity_to_be_completed_in_which_month":["between", [first_day_of_month, last_day_of_month]],
                                                             "type_of_activity": "Non-financial Activity"})
    
    if total_non_financial_activities > 0:
        percentage_of_non_financial_activities_completed = round(((total_non_financial_activites_completed / total_non_financial_activities) * 100),2)
    else:
        percentage_of_non_financial_activities_completed = 0
    
    non_financial_activites_due_count = get_num_of_non_financial_activities_due()


    return {
        "current_month": current_month,
        "activities_count": activities_count,
        "non_financial_activities_count": non_financial_activities_count,
        "payment_processed_actitivies_count":payment_processed_activities,
        "financial_activities_count": financial_activities_count,
        "actual_budget_allocated_for_the_current_month": actual_budget_allocated_for_the_current_month,
        "financial_activities_completed": financial_completed_activities_count,
        "percentage_of_budget_utilised":percentage_of_budget_utilised,
        "percentage_of_financial_activities_completed":completion_percentage,
        "actual_budget_utilised_for_current_month": total_utilized_sum,
        "percentage_of_financial_activities_process_payment":percentage_of_financial_activities_processed_payment,
        "due_payment_financial_activities_count":due_payment_financial_activities_count,
        "financial_activities_over_due_from_last_month":financial_activities_over_due_from_last_month,
        "non_financial_completion_percentage":non_financial_completion_percentage,
        "non_financial_activities_overdue_count": non_financial_activities_overdue_count,
        "percentage_of_non_financial_activities_completed":percentage_of_non_financial_activities_completed,
        "non_financial_activities_due_count":non_financial_activites_due_count
    }

