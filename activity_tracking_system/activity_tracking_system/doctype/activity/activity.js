// Copyright (c) 2024, Tech4Good Community and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Activity", {
// 	refresh(frm) {

// 	},
// });

frappe.ui.form.on('Activity', {
    refresh: function(frm) {
        frm.add_custom_button(__('Update to Planning Sheet'), function() {
            frappe.call({
                method: 'activity_tracking_system.activity_tracking_system.doctype.activity.activity.create_activity_in_planning_sheet',
                args: { doc_name: frm.doc.name },
                callback: function(response) {
                    frappe.msgprint('Activity updated in Planning Sheet');
                }
            });
        });
    },
    state(frm){
        frm.set_query("city", (doc) => {
            return {
                filters : {
                    "state" : doc.state
                }
            }
        });
    }
});


