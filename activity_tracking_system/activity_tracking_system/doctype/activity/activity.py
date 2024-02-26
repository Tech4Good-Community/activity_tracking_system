# Copyright (c) 2024, Tech4Good Community and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Activity(Document):
	def validate(self):
		if self.activity_completion_date:
			if self.activity_completion_date < self.activity_process_initiating_date:
					frappe.throw(title='Error', msg='Initiation date cannot be greater than completion date')
		if self.activity_to_be_completed_in_which_month < self.activity_process_initiating_date:
					frappe.throw(title='Error', msg='Completion date cannot be lesser than intitalisation date')
