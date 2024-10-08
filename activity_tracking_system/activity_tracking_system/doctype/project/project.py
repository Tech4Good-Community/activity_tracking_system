# Copyright (c) 2024, Tech4Good Community and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Project(Document):
    def validate(self):
        if self.end_date:
            if self.end_date <= self.start_date:
                frappe.throw(title='Error', msg='Project End date cannot be lesser than Project Start date')
