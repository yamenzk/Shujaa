import frappe

ALLOWED_DOCTYPES = {
    "Weekly Plan",
    "Daily Workout Plan",
    "Daily Meal Plan",
    "Workout Template",
    "Chat",
    "Exercise",
    "Ingredient",
    "Client",
    "Muscle Group",
    "Membership",
    "Card",
}

def send_shujaa_update(doc, method):
    """
    Send a real-time update for allowed DocTypes to the website room.
    
    :param doc: The document that was changed
    :param method: The method that was called (e.g., "on_update", "after_insert", "on_trash")
    """
    if doc.doctype not in ALLOWED_DOCTYPES:
        return

    update_type = {
        "on_update": "update",
        "after_insert": "create",
        "on_trash": "delete"
    }.get(method, "update")

    frappe.publish_realtime(
        "shujaa_update",
        {
            "doctype": doc.doctype,
            "name": doc.name,
            "update_type": update_type,
            "modified": frappe.utils.now(),
        },
        room="website",
        after_commit=True
    )