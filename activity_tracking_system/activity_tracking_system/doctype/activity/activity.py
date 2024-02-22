# Copyright (c) 2024, Tech4Good Community and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Activity(Document):
	def validate(self):
		if self.activity_completion_date < self.activity_process_initiating_date:
				frappe.throw(title='Error', msg='Initiation date cannot be greater than completion date')

