# from .utils.realtime import send_shujaa_update

app_name = "shujaa"
app_title = "shujaa"
app_publisher = "ITDept"
app_description = "shujaa Customizations"
app_email = "it@mirageclinicsclinics.com"
app_license = "mit"
# app_include_css = "/assets/shujaa/css/printview_custom.css"
# app_include_js = "/assets/shujaa/js/printview_script.js"
# required_apps = []

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/shujaa/css/shujaa.css"
# app_include_js = "/assets/shujaa/js/shujaa.js"

# include js, css files in header of web template
# web_include_css = "/assets/shujaa/css/shujaa.css"
# web_include_js = "/assets/shujaa/js/shujaa.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "shujaa/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = [
#     "shujaa/icons/shujaalogo.svg",
#     "shujaa/icons/shujaatv.svg",
#     "shujaa/icons/shujaaradio.svg"
# ]


# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "shujaa.utils.jinja_methods",
# 	"filters": "shujaa.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "shujaa.install.before_install"
# after_install = "shujaa.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "shujaa.uninstall.before_uninstall"
# after_uninstall = "shujaa.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "shujaa.utils.before_app_install"
# after_app_install = "shujaa.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "shujaa.utils.before_app_uninstall"
# after_app_uninstall = "shujaa.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "shujaa.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#     "*": {
#         "on_update": "shujaa.utils.realtime.send_shujaa_update",
#         "after_insert": "shujaa.utils.realtime.send_shujaa_update",
#         "on_trash": "shujaa.utils.realtime.send_shujaa_update",
#     }
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"shujaa.tasks.all"
# 	],
# 	"daily": [
# 		"shujaa.tasks.daily"
# 	],
# 	"hourly": [
# 		"shujaa.tasks.hourly"
# 	],
# 	"weekly": [
# 		"shujaa.tasks.weekly"
# 	],
# 	"monthly": [
# 		"shujaa.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "shujaa.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "shujaa.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "shujaa.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["shujaa.utils.before_request"]
# after_request = ["shujaa.utils.after_request"]

# Job Events
# ----------
# before_job = ["shujaa.utils.before_job"]
# after_job = ["shujaa.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"shujaa.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }