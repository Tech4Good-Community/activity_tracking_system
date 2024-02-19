import frappe
from frappe.model.document import Document

class FundsAllocation(Document):
    def validate(self):
        if self.funds_for_the_project == 0:
            frappe.throw(title='Error', msg='Please fill funds for the project field')
        
        if not self.get('__islocal'):  # Check if the document is not being newly created
            calculate_direct_cost(self)

@frappe.whitelist()
def calculate_direct_cost(doc):
    salary = doc.salary_funds_allocated
    funds_for_the_project = doc.funds_for_the_project
    travel_funds_allocated = doc.travel__funds_allocated  
    activity_funds_allocated = doc.activity_funds_allocated
    consultant_funds_allocated = doc.consultant_funds_allocated
    equipment_funds_allocated = doc.equipment_funds_allocated
    research_funds_allocated = doc.research_funds_allocated
    
    total_direct_cost = sum([salary, travel_funds_allocated, activity_funds_allocated, consultant_funds_allocated, equipment_funds_allocated, research_funds_allocated])
    print(total_direct_cost)
    if total_direct_cost != 0:
        salary_percentage = round(((salary / total_direct_cost) * 100),2)
        travel_percentage = round(((travel_funds_allocated / total_direct_cost) * 100),2)
        activity_percentage = round(((activity_funds_allocated / total_direct_cost) * 100),2)
        consultant_percentage =  round(((consultant_funds_allocated / total_direct_cost) * 100),2)
        equipment_percentage = round(((equipment_funds_allocated / total_direct_cost) * 100),2)
        research_percentage = round(((research_funds_allocated / total_direct_cost) * 100),2)
    else:
        salary_percentage = 0
        travel_percentage = 0
        activity_percentage = 0
        consultant_percentage = 0
        equipment_percentage = 0
        research_percentage = 0
    return_list = [salary_percentage, travel_percentage, activity_percentage, consultant_percentage, equipment_percentage, research_percentage] 
    print(return_list) 
    return return_list
        #frappe.set_value(doc.doctype, doc.name, 'salary_percentage_of_allocation', salary_percentage)

