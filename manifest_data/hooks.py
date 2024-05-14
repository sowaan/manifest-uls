from . import __version__ as app_version

app_name = "manifest_data"
app_title = "Manifest Data"
app_publisher = "fariz.khanzada@sowaan.com"
app_description = "Manifest Data is a custom ERPNext application designed to streamline the process of uploading and managing data from text files into ERPNext. With Manifest Data, users can effortlessly upload text files containing structured data, and the application automatically parses and inserts the data into designated doctypes and their corresponding fields within the ERPNext instance. This application simplifies the data import process, saving time and reducing the risk of errors associated with manual data entry. Whether it\'s importing customer information, inventory data, or any other type of data, Manifest Data offers a seamless solution for efficiently populating ERPNext with external data sources."
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "fariz.khanzada@sowaan.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/manifest_data/css/manifest_data.css"
# app_include_js = "/assets/manifest_data/js/manifest_data.js"

# include js, css files in header of web template
# web_include_css = "/assets/manifest_data/css/manifest_data.css"
# web_include_js = "/assets/manifest_data/js/manifest_data.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "manifest_data/public/scss/website"

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

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "manifest_data.install.before_install"
# after_install = "manifest_data.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "manifest_data.uninstall.before_uninstall"
# after_uninstall = "manifest_data.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "manifest_data.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"manifest_data.tasks.all"
#	],
#	"daily": [
#		"manifest_data.tasks.daily"
#	],
#	"hourly": [
#		"manifest_data.tasks.hourly"
#	],
#	"weekly": [
#		"manifest_data.tasks.weekly"
#	]
#	"monthly": [
#		"manifest_data.tasks.monthly"
#	]
# }

# Testing
# -------

# before_tests = "manifest_data.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "manifest_data.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "manifest_data.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Request Events
# ----------------
# before_request = ["manifest_data.utils.before_request"]
# after_request = ["manifest_data.utils.after_request"]

# Job Events
# ----------
# before_job = ["manifest_data.utils.before_job"]
# after_job = ["manifest_data.utils.after_job"]

# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"manifest_data.auth.validate"
# ]

