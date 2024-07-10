frappe.ui.form.on('Funds Allocation', {
    after_save: function(frm) {
        frappe.call({
            method: 'activity_tracking_system.activity_tracking_system.doctype.funds_allocation.funds_allocation.calculate_direct_cost',
            args: {
                doc: frm.doc,
                salary_funds: frm.doc.salary_funds_allocated,
                travel_funds: frm.doc.travel__funds_allocated,
                activity_funds: frm.doc.activity_funds_allocated,
                consultant_funds: frm.doc.consultant_funds_allocated,
                equipment_funds: frm.doc.equipment_funds_allocated,
                research_funds: frm.doc.research_funds_allocated,
                indirect_cost : frm.doc.indirect_funds_allocated
                
            },
            callback: function(r) {
                if(r.message) {
                    frappe.model.set_value(frm.doctype, frm.docname, 'salary_percentage_of_allocation', r.message["salary_percentage"]);
                    frappe.model.set_value(frm.doctype, frm.docname, 'travel_percentage_of_allocation', r.message["travel_percentage"]);
                    frappe.model.set_value(frm.doctype, frm.docname, 'activity__percentage_of_allocation',r.message["activity_percentage"]);
                    frappe.model.set_value(frm.doctype, frm.docname, 'consultant_percentage_of_allocation',r.message["consultant_percentage"]);
                    frappe.model.set_value(frm.doctype, frm.docname, 'equipment_percentage_of_allocation',r.message["equipment_percentage"]);
                    frappe.model.set_value(frm.doctype, frm.docname, 'research_percentage_of_allocation', r.message["research_percentage"]);
                    frappe.model.set_value(frm.doctype, frm.docname, 'indirect_percentage_of_allocation', r.message["indirect_cost_percentage"]);
                    frappe.model.set_value(frm.doctype, frm.docname, 'grand_total', r.message["grand_total"]);

                    frappe.model.set_value(frm.doctype, frm.docname, 'excess_fund', r.message["grand_total"] - frm.doc.funds_for_the_project);

                    frm.save();
                }
            }
        });
    }
});
