from frappe import _

def get_data():
	return [
		{
			"label": _("Documents"),
			"icon": "icon-star",
			"items": [
				{
					"type": "doctype",
					"name": "Task",
					"description": _("Project activity / task."),
				},
				{
					"type": "doctype",
					"name": "Project",
					"description": _("Project master."),
				},
                               {
                                        "type": "doctype",
                                        "name": "Sprint",
                                        "description": _("Project Sprint master."),
                                },
                               {
                                        "type": "doctype",
                                        "name": "Release Report",
                                        "description": _("Project Release Report."),
                                },
                              {
                                        "type": "doctype",
                                        "name": "Project Health Weekly Report",
                                        "description": _("Project Health Weekly Report."),
                                },
				{
					"type": "doctype",
					"name": "Time Log",
					"description": _("Time Log for tasks."),
				},
				{
					"type": "doctype",
					"name": "Time Log Batch",
					"description": _("Batch Time Logs for billing."),
				},
				{
					"type": "doctype",
					"name": "Activity Type",
					"description": _("Types of activities for Time Sheets"),
				},
			]
		},

		{
			"label": _("Requirement Tracking"),
			"icon": "icon-eye-open",
			"items": [
				{
					"type": "doctype",
					"name": "Business Requirements",
					"description": _("Business Requirement description.")
				},
				{
					"type": "doctype",
					"name": "Functional Requirement",
					"description": _("Functional Requirement description.")
				},
			]
		},

		{
			"label": _("ChangeRequest and Support"),
			"icon": "icon-resize-small",
			"items": [
				{
					"type": "doctype",
					"name": "Wale",
					"description": _("Non-Project based.")
				},
				{
					"type": "doctype",
					"name": "Vesta Si",
					"description": _("Non-Project based.")
				},
				{
					"type": "doctype",
					"name": "HealthSnapp",
					"description": _("Non-Project based.")
				},
				{
					"type": "doctype",
					"name": "Digitales",
					"description": _("Non-Project based.")
				},
			]
		},





		{
			"label": _("Tools"),
			"icon": "icon-wrench",
			"items": [
				{
					"type": "report",
					"route": "Gantt/Task",
					"doctype": "Task",
					"name": "Gantt Chart",
					"description": _("Gantt chart of all tasks.")
				},
			]
		},
		{
			"label": _("Standard Reports"),
			"icon": "icon-list",
			"items": [
				{
					"type": "report",
					"is_query_report": True,
					"name": "Daily Time Log Summary",
					"doctype": "Time Log"
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Project wise Stock Tracking",
					"doctype": "Project"
				},
			]
		},
	]
