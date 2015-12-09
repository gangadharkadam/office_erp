# Copyright (c) 2013, Web Notes Technologies Pvt. Ltd. and Contributors and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.model.mapper import get_mapped_doc

class BusinessRequirements(Document):
	pass

@frappe.whitelist()
def make_functional_requirements(source_name, target_doc=None):
	def postprocess(source, target):
		pass
	doc = get_mapped_doc("Business Requirements", source_name, {
		"Business Requirements": {
			"doctype": "Functional Requirement",
			"field_map": {
				"br_description": "br_description"
			}
		},
		
	}, target_doc, postprocess)

	return doc
