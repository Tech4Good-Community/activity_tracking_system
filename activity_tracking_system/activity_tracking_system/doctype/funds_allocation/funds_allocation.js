// Copyright (c) 2024, Tech4Good Community and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Funds Allocation", {
// 	refresh(frm) {

// 	},
// });

frappe.ui.form.on('Funds Allocation', {
    onload: function(frm) {
        // Your onload code here
    },
    refresh: function(frm) {
        if (frm.doc.__islocal) {
            frm.remove_custom_button('Request Edit');
        } else {
            // Check if the user has permission to view the button
            if (frappe.user.has_role('Human Resource Director')) {
                frm.add_custom_button(__('Request Edit'), function() {
                    // Custom button action
                    // For example, show an alert
                    frappe.msgprint('Custom button clicked!');
                });
            }
        }
    }
});


