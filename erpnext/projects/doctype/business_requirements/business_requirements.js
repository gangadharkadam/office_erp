
cur_frm.cscript.refresh=function(){
	
		cur_frm.add_custom_button(__('Make Functinal Requirements'),this.make_functional_requirement, 'icon-retweet');
}
cur_frm.cscript.make_functional_requirement = function() {
	frappe.model.open_mapped_doc({
		method: "erpnext.projects.doctype.business_requirements.business_requirements.make_functional_requirements",
		frm: cur_frm
	});
}
