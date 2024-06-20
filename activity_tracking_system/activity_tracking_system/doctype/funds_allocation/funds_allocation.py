import frappe
from frappe.model.document import Document

class FundsAllocation(Document):
    def validate(self):
        if self.funds_for_the_project == 0:
            frappe.throw(title='Error', msg='Please fill funds for the project field')
        

@frappe.whitelist()
def calculate_direct_cost(doc, salary_funds, travel_funds, equipment_funds, research_funds, activity_funds, consultant_funds, indirect_cost):
    salary = float(salary_funds)
    travel_funds_allocated = float(travel_funds)
    activity_funds_allocated = float(activity_funds)
    consultant_funds_allocated = float(consultant_funds)
    equipment_funds_allocated = float(equipment_funds)
    research_funds_allocated = float(research_funds)
    indirect_cost = float(indirect_cost)
    
    total_direct_cost = sum([salary, travel_funds_allocated, activity_funds_allocated, consultant_funds_allocated, equipment_funds_allocated, research_funds_allocated])
    
    grand_total = total_direct_cost + indirect_cost
    
    if grand_total != 0:
        indirect_cost_percentage = round(((indirect_cost/ grand_total) * 100), 1)
    else:
        indirect_cost_percentage = 0
    
    if total_direct_cost != 0:
        salary_percentage = round(((salary / total_direct_cost) * 100), 1)
        travel_percentage = round(((travel_funds_allocated / total_direct_cost) * 100), 2)
        activity_percentage = round(((activity_funds_allocated / total_direct_cost) * 100), 2)
        consultant_percentage = round(((consultant_funds_allocated / total_direct_cost) * 100), 2)
        equipment_percentage = round(((equipment_funds_allocated / total_direct_cost) * 100), 2)
        research_percentage = round(((research_funds_allocated / total_direct_cost) * 100), 2)
    else:
        salary_percentage = 0
        travel_percentage = 0
        activity_percentage = 0
        consultant_percentage = 0
        equipment_percentage = 0
        research_percentage = 0
    
    data = {
        "salary_percentage" : salary_percentage,
        "travel_percentage" : travel_percentage,
        "activity_percentage": activity_percentage,
        "consultant_percentage":consultant_percentage,
        "equipment_percentage": equipment_percentage,
        "research_percentage" : research_percentage,
        "indirect_cost_percentage": indirect_cost_percentage,
        "grand_total" : grand_total
        
    }
    
    return data


