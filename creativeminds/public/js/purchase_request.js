frappe.ui.form.on('Purchase Request', {
	refresh(frm) {
		
		frm.add_custom_button('Create Purchase Invoice', () => {
            frappe.new_doc('Purchase Invoice', {
                purchase_request: frm.doc.name,
            })
        })
	}
})