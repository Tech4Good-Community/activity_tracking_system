// Copyright (c) 2024, Tech4Good Community and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Funds Allocation", {
// 	refresh(frm) {

// 	},
// });

frappe.ui.form.on('Funds Allocation', {
    after_save: function(frm) {
        frappe.call({
            method: 'activity_tracking_system.activity_tracking_system.doctype.funds_allocation.funds_allocation.calculate_direct_cost',
            args: {
                doc: frm.doc
            },
            callback: function(r) {
                if(r.message) {
                    console.log(r.message[0])
                }
            }
        })






    }
    
});


