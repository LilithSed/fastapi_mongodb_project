# -*- coding: utf-8 -*-
# Products List with details and Permission Codes
products = [
    {
        "product": "Acquisition",
        "modules": [
            {
                "name": {"en": "Manage Acquisitions", "ar": "Manage Acquisitions"},
                "description": {
                    "en": "Ability to create, update, delete and view Acquisitions",
                    "ar": "Ability to create, update, delete and view Acquisitions",
                },
                "permissions": [
                    {
                        "code": "acquisition.create",
                        "name": {"en": "create", "ar": "Create"},
                        "description": {"en": "Create", "ar": "Create"},
                    },
                    {
                        "code": "acquisition.update",
                        "name": {"en": "Update", "ar": "Update"},
                        "description": {"en": "Update", "ar": "Update"},
                    },
                    {
                        "code": "acquisition.delete",
                        "name": {"en": "Delete", "ar": "Delete"},
                        "description": {"en": "Delete", "ar": "Delete"},
                    },
                    {
                        "code": "acquisition.view",
                        "name": {"en": "View", "ar": "View"},
                        "description": {"en": "View", "ar": "View"},
                    },
                ],
                "triggers": [
                    {
                        "code": "acquisition.buy.channel",
                        "name": {"en": "Buy Channel", "ar": "Buy Channel"},
                        "description": {
                            "en": "Acquisitions By Channel",
                            "ar": "Acquisitions By Channel",
                        },
                    },
                    {
                        "code": "acquisition.my.channel",
                        "name": {"en": "My Channel", "ar": "My Channel"},
                        "description": {
                            "en": "Acquisitions My Channel",
                            "ar": "Acquisitions My Channel",
                        },
                    },
                ],
            }
        ],
    },
    {
        "product": "Agency",
        "modules": [
            {
                "name": {"en": "Agency", "ar": "Agency"},
                "description": {"en": "Agency", "ar": "Agency"},
                "permissions": [
                    {
                        "code": "agency.create",
                        "name": {"en": "create", "ar": "Create"},
                        "description": {"en": "Create", "ar": "Create"},
                    },
                    {
                        "code": "agency.update",
                        "name": {"en": "Update", "ar": "Update"},
                        "description": {"en": "Update", "ar": "Update"},
                    },
                    {
                        "code": "agency.delete",
                        "name": {"en": "Delete", "ar": "Delete"},
                        "description": {"en": "Delete", "ar": "Delete"},
                    },
                    {
                        "code": "agency.view",
                        "name": {"en": "View", "ar": "View"},
                        "description": {"en": "View", "ar": "View"},
                    },
                ],
                "triggers": [],
            }
        ],
    },
    {
        "product": "Assessments",
        "modules": [
            {
                "name": {"en": "Manage Application", "ar": "Manage Application"},
                "description": {"en": "Manage Application", "ar": "Manage Application"},
                "permissions": [
                    {
                        "code": "assessment.application.create",
                        "name": {"en": "create", "ar": "Create"},
                        "description": {"en": "Create", "ar": "Create"},
                    },
                    {
                        "code": "assessment.application.update",
                        "name": {"en": "update", "ar": "update"},
                        "description": {"en": "update", "ar": "update"},
                    },
                    {
                        "code": "assessment.application.delete",
                        "name": {"en": "Delete", "ar": "Delete"},
                        "description": {"en": "Delete", "ar": "Delete"},
                    },
                    {
                        "code": "assessment.application.view",
                        "name": {"en": "View", "ar": "View"},
                        "description": {"en": "View", "ar": "View"},
                    },
                ],
                "triggers": [
                    {
                        "code": "assessment.application.move.applicants",
                        "name": {"en": "Move Applicants", "ar": "Move Applicants"},
                        "description": {
                            "en": "Allow The User To Move an Applicant From One Stage To Another",
                            "ar": "Allow The User To Move an Applicant From One Stage To Another",
                        },
                    },
                    {
                        "code": "assessment.application.manage.weight",
                        "name": {"en": "Manage Weight", "ar": "Manage Weight"},
                        "description": {
                            "en": "Allow The User To Manage The Weights of the A.I Readings & Analysis To Rank Applicants",
                            "ar": "Allow The User To Manage The Weights of the A.I Readings & Analysis To Rank Applicants",
                        },
                    },
                    {
                        "code": "assessment.application.manage.teams",
                        "name": {"en": "Manage Teams", "ar": "Manage Teams"},
                        "description": {
                            "en": "Allow The User To Add, Edit or Remove Team Members Working On The Assigned Application",
                            "ar": "Allow The User To Add, Edit or Remove Team Members Working On The Assigned Application",
                        },
                    },
                    {
                        "code": "assessment.application.share.applicant",
                        "name": {"en": "Share Applicant", "ar": "Share Applicant"},
                        "description": {
                            "en": "Allow The User To share Applicants Internally or Externally",
                            "ar": "Allow The User To share Applicants Internally or Externally",
                        },
                    },
                    {
                        "code": "assessment.application.manage.stage",
                        "name": {"en": "Manage Stage", "ar": "Manage Stage"},
                        "description": {
                            "en": "Allow The User To Add, Move, Delete Stages That Were Added From Within The Application",
                            "ar": "Allow The User To Add, Move, Delete Stages That Were Added From Within The Application",
                        },
                    },
                    {
                        "code": "assessment.application.change.applicants.pipelines",
                        "name": {
                            "en": "Change Applicants Pipelines",
                            "ar": "Change Applicants Pipelines",
                        },
                        "description": {
                            "en": "Allow The User To Move Applicants From One Pipeline To Another From Within The Application",
                            "ar": "Allow The User To Move Applicants From One Pipeline To Another From Within The Application",
                        },
                    },
                    {
                        "code": "assessment.application.send.questionnaire",
                        "name": {
                            "en": "Send Questionnaire",
                            "ar": "Send Questionnaire",
                        },
                        "description": {
                            "en": "Allow The User To Send Questionnaires",
                            "ar": "Allow The User To Send Questionnaires",
                        },
                    },
                    {
                        "code": "assessment.application.send.assessment",
                        "name": {"en": "Send Assessment", "ar": "Send Assessment"},
                        "description": {
                            "en": "Allow The User To Send Assessments",
                            "ar": "Allow The User To Send Assessments",
                        },
                    },
                    {
                        "code": "assessment.application.schedule.meetings",
                        "name": {"en": "Schedule Meetings", "ar": "Schedule Meetings"},
                        "description": {
                            "en": "Allow The User To Schedule, Edit And Delete Meetings",
                            "ar": "Allow The User To Schedule, Edit And Delete Meetings",
                        },
                    },
                    {
                        "code": "assessment.application.manage.evaluation",
                        "name": {"en": "Manage Evaluation", "ar": "Manage Evaluation"},
                        "description": {
                            "en": "Allow the user to fill out evaluation forms",
                            "ar": "Allow the user to fill out evaluation forms",
                        },
                    },
                    {
                        "code": "assessment.application.view.logs",
                        "name": {"en": "View Logs", "ar": "View Logs"},
                        "description": {
                            "en": "Allow the user to view logs of all changes",
                            "ar": "Allow the user to view logs of all changes",
                        },
                    },
                    {
                        "code": "assessment.application.manage.workflow",
                        "name": {"en": "Manage Workflow", "ar": "Manage Workflow"},
                        "description": {
                            "en": "Allow the user to manage workflows related to the applicant",
                            "ar": "Allow the user to manage workflows related to the applicant",
                        },
                    },
                    {
                        "code": "assessment.application.view.workflow",
                        "name": {"en": "View Workflow", "ar": "View Workflow"},
                        "description": {
                            "en": "Allow the user to only view the related workflows related to the applicant",
                            "ar": "Allow the user to only view the related workflows related to the applicant",
                        },
                    },
                    {
                        "code": "assessment.application.manage.attachments",
                        "name": {
                            "en": "Manage Attachments",
                            "ar": "Manage Attachments",
                        },
                        "description": {
                            "en": "Allow the user to view, upload and download attachments related to the applicant",
                            "ar": "Allow the user to view, upload and download attachments related to the applicant",
                        },
                    },
                    {
                        "code": "assessment.application.discussion",
                        "name": {"en": "Discussion", "ar": "Discussion"},
                        "description": {
                            "en": "Allow the user to participate in discussions related to the applicant",
                            "ar": "Allow the user to participate in discussions related to the applicant",
                        },
                    },
                    {
                        "code": "assessment.application.personality.analysis",
                        "name": {
                            "en": "Personality Analysis",
                            "ar": "Personality Analysis",
                        },
                        "description": {
                            "en": "Allow the user to view the applicants personality analysis",
                            "ar": "Allow the user to view the applicants personality analysis",
                        },
                    },
                    {
                        "code": "assessment.application.notes",
                        "name": {"en": "Notes", "ar": "Notes"},
                        "description": {
                            "en": "Allow the user to add, edit and manage application notes",
                            "ar": "Allow the user to add, edit and manage application notes",
                        },
                    },
                    {
                        "code": "assessment.application.add.applicant",
                        "name": {"en": "Add Applicant", "ar": "Add Applicant"},
                        "description": {
                            "en": "Allow the user to add additional applicants to the assessment",
                            "ar": "Allow the user to add additional applicants to the assessment",
                        },
                    },
                    {
                        "code": "assessment.application.extend.deadline",
                        "name": {"en": "Extend Deadline", "ar": "Extend Deadline"},
                        "description": {
                            "en": "Allow the user to extend deadline for the assessment",
                            "ar": "Allow the user to extend deadline for the assessment",
                        },
                    },
                    {
                        "code": "assessment.application.download.report",
                        "name": {"en": "Download Report", "ar": "Download Report"},
                        "description": {
                            "en": "Allow the user to download report related to assigned assessment",
                            "ar": "Allow the user to download report related to assigned assessment",
                        },
                    },
                    {
                        "code": "assessment.application.download.all.assessment.reports",
                        "name": {
                            "en": "Download All Assessment Reports",
                            "ar": "Download All Assessment Reports",
                        },
                        "description": {
                            "en": "Allow the user to download all reports and analytics related to all assessments",
                            "ar": "Allow the user to download all reports and analytics related to all assessments",
                        },
                    },
                ],
            },
            {
                "name": {"en": "Manage Templates", "ar": "Manage Templates"},
                "description": {"en": "Manage Templates", "ar": "Manage Templates"},
                "permissions": [
                    {
                        "code": "assessment.template.create",
                        "name": {"en": "create", "ar": "Create"},
                        "description": {"en": "Create", "ar": "Create"},
                    },
                    {
                        "code": "assessment.template.update",
                        "name": {"en": "update", "ar": "update"},
                        "description": {"en": "update", "ar": "update"},
                    },
                    {
                        "code": "assessment.template.delete",
                        "name": {"en": "Delete", "ar": "Delete"},
                        "description": {"en": "Delete", "ar": "Delete"},
                    },
                    {
                        "code": "assessment.template.view",
                        "name": {"en": "View", "ar": "View"},
                        "description": {"en": "View", "ar": "View"},
                    },
                ],
                "triggers": [],
            },
        ],
    },
    {
        "product": "Billing",
        "modules": [
            {
                "name": {"en": "Billing", "ar": "Billing"},
                "description": {"en": "Billing", "ar": "Billing"},
                "permissions": [],
                "triggers": [
                    {
                        "code": "billing.allow",
                        "name": {"en": "Billing", "ar": "Billing"},
                        "description": {
                            "en": "Allow user to access billing settings where they can upgrade/downgrade their subscription",
                            "ar": "Allow user to access billing settings where they can upgrade/downgrade their subscription",
                        },
                    },
                    {
                        "code": "billing.view.invoice",
                        "name": {"en": "View Invoice", "ar": "View Invoice"},
                        "description": {
                            "en": "Allow user to access billing history",
                            "ar": "Allow user to access billing history",
                        },
                    },
                ],
            }
        ],
    },
    {
        "product": "Branding",
        "modules": [
            {
                "name": {"en": "Manage Branding", "ar": "Manage Branding"},
                "description": {"en": "Manage Branding", "ar": "Manage Branding"},
                "permissions": [
                    {
                        "code": "branding.create",
                        "name": {"en": "create", "ar": "Create"},
                        "description": {"en": "Create", "ar": "Create"},
                    },
                    {
                        "code": "branding.update",
                        "name": {"en": "Update", "ar": "Update"},
                        "description": {"en": "Update", "ar": "Update"},
                    },
                    {
                        "code": "branding.delete",
                        "name": {"en": "Delete", "ar": "Delete"},
                        "description": {"en": "Delete", "ar": "Delete"},
                    },
                    {
                        "code": "branding.view",
                        "name": {"en": "View", "ar": "View"},
                        "description": {"en": "View", "ar": "View"},
                    },
                ],
                "triggers": [
                    {
                        "code": "branding.signup.requirement",
                        "name": {
                            "en": "Signup Requirement",
                            "ar": "Signup Requirement",
                        },
                        "description": {
                            "en": "Allow the user to create or edit signup requirements",
                            "ar": "Allow the user to create or edit signup requirements",
                        },
                    },
                    {
                        "code": "branding.publish",
                        "name": {"en": "PUBLISH", "ar": "PUBLISH"},
                        "description": {
                            "en": "Allow user to publish career site",
                            "ar": "Allow user to publish career site",
                        },
                    },
                ],
            }
        ],
    },
    {
        "product": "Chart",
        "modules": [
            {
                "name": {"en": "Chart", "ar": "Chart"},
                "description": {"en": "Chart", "ar": "Chart"},
                "permissions": [
                    {
                        "code": "chart.dashboard.create",
                        "name": {"en": "create", "ar": "Create"},
                        "description": {"en": "Create", "ar": "Create"},
                    },
                    {
                        "code": "chart.dashboard.update",
                        "name": {"en": "Update", "ar": "Update"},
                        "description": {"en": "Update", "ar": "Update"},
                    },
                    {
                        "code": "chart.dashboard.delete",
                        "name": {"en": "Delete", "ar": "Delete"},
                        "description": {"en": "Delete", "ar": "Delete"},
                    },
                    {
                        "code": "chart.dashboard.view",
                        "name": {"en": "View", "ar": "View"},
                        "description": {"en": "View", "ar": "View"},
                    },
                ],
                "triggers": [
                    {
                        "code": "chart.dashboard.all.dashboards",
                        "name": {
                            "en": "View All Dashboards",
                            "ar": "View All Dashboards",
                        },
                        "description": {
                            "en": "Allow the user to view all dashboards",
                            "ar": "Allow the user to view all dashboards",
                        },
                    },
                    {
                        "code": "chart.dashboard.analytics.product",
                        "name": {
                            "en": "View Analytics Product",
                            "ar": "View Analytics Product",
                        },
                        "description": {
                            "en": "Allow the user to view analytics product",
                            "ar": "Allow the user to view analytics product",
                        },
                    },
                    {
                        "code": "chart.dashboard.generated.reports.list",
                        "name": {
                            "en": "View Generated Reports List",
                            "ar": "View Generated Reports List",
                        },
                        "description": {
                            "en": "Allow the user to view generated reports list",
                            "ar": "Allow the user to view generated reports list",
                        },
                    },
                ],
            }
        ],
    },
    {
        "product": "Form",
        "modules": [
            {
                "name": {"en": "Manage Template", "ar": "Manage Template"},
                "description": {"en": "Manage Template", "ar": "Manage Template"},
                "permissions": [
                    {
                        "code": "form.template.create",
                        "name": {"en": "create", "ar": "Create"},
                        "description": {"en": "Create", "ar": "Create"},
                    },
                    {
                        "code": "form.template.update",
                        "name": {"en": "Update", "ar": "Update"},
                        "description": {"en": "Update", "ar": "Update"},
                    },
                    {
                        "code": "form.template.delete",
                        "name": {"en": "Delete", "ar": "Delete"},
                        "description": {"en": "Delete", "ar": "Delete"},
                    },
                    {
                        "code": "form.template.view",
                        "name": {"en": "View", "ar": "View"},
                        "description": {"en": "View", "ar": "View"},
                    },
                ],
                "triggers": [],
            },
            {
                "name": {"en": "Forms Type", "ar": "Forms Type"},
                "description": {"en": "Forms Type", "ar": "Forms Type"},
                "permissions": [
                    {
                        "code": "form.type.create",
                        "name": {"en": "create", "ar": "Create"},
                        "description": {"en": "Create", "ar": "Create"},
                    },
                    {
                        "code": "form.type.update",
                        "name": {"en": "Update", "ar": "Update"},
                        "description": {"en": "Update", "ar": "Update"},
                    },
                    {
                        "code": "form.type.delete",
                        "name": {"en": "Delete", "ar": "Delete"},
                        "description": {"en": "Delete", "ar": "Delete"},
                    },
                    {
                        "code": "form.type.view",
                        "name": {"en": "View", "ar": "View"},
                        "description": {"en": "View", "ar": "View"},
                    },
                ],
                "triggers": [],
            },
        ],
    },
    {
        "product": "Hiring",
        "modules": [
            {
                "name": {"en": "Application", "ar": "Application"},
                "description": {"en": "Application", "ar": "Application"},
                "permissions": [
                    {
                        "code": "hiring.application.create",
                        "name": {"en": "create", "ar": "Create"},
                        "description": {"en": "Create", "ar": "Create"},
                    },
                    {
                        "code": "hiring.application.update",
                        "name": {"en": "update", "ar": "update"},
                        "description": {"en": "update", "ar": "update"},
                    },
                    {
                        "code": "hiring.application.delete",
                        "name": {"en": "delete", "ar": "delete"},
                        "description": {"en": "delete", "ar": "delete"},
                    },
                    {
                        "code": "hiring.application.view",
                        "name": {"en": "view", "ar": "view"},
                        "description": {"en": "view", "ar": "view"},
                    },
                ],
                "triggers": [
                    {
                        "code": "hiring.application.move.applicants",
                        "name": {"en": "Move Applicants", "ar": "Move Applicants"},
                        "description": {
                            "en": "Allow the user to move an applicant from one stage to another",
                            "ar": "Allow the user to move an applicant from one stage to another",
                        },
                    },
                    {
                        "code": "hiring.application.manage.weight",
                        "name": {"en": "Manage Weight", "ar": "Manage Weight"},
                        "description": {
                            "en": "Allow the user to manage the weights of the A.I readings & analysis to rank applicants",
                            "ar": "Allow the user to manage the weights of the A.I readings & analysis to rank applicants",
                        },
                    },
                    {
                        "code": "hiring.application.manage.teams",
                        "name": {
                            "en": "Allow the user to add, edit or remove team members working on the assigned application",
                            "ar": "Allow the user to add, edit or remove team members working on the assigned application",
                        },
                        "description": {"en": "Manage Teams", "ar": "Manage Teams"},
                    },
                    {
                        "code": "hiring.application.share.applicant",
                        "name": {"en": "Share Applicant", "ar": "Share Applicant"},
                        "description": {
                            "en": "Allow the user to share applicants internally or externally",
                            "ar": "Allow the user to share applicants internally or externally",
                        },
                    },
                    {
                        "code": "hiring.application.manage.stage",
                        "name": {"en": "Manage Stage", "ar": "Manage Stage"},
                        "description": {
                            "en": "Allow the user to add, move, delete stages that were added from within the application",
                            "ar": "Allow the user to add, move, delete stages that were added from within the application",
                        },
                    },
                    {
                        "code": "hiring.application.change.applicants.pipelines",
                        "name": {
                            "en": "Change Applicants Pipelines",
                            "ar": "Change Applicants Pipelines",
                        },
                        "description": {
                            "en": "Allow the user to move applicants from one pipeline to another from within the application",
                            "ar": "Allow the user to move applicants from one pipeline to another from within the application",
                        },
                    },
                    {
                        "code": "hiring.application.send.questionnaire",
                        "name": {
                            "en": "Send Questionnaire",
                            "ar": "Send Questionnaire",
                        },
                        "description": {
                            "en": "Allow the user to send questionnaires",
                            "ar": "Allow the user to send questionnaires",
                        },
                    },
                    {
                        "code": "hiring.application.send.video.assessment",
                        "name": {
                            "en": "Send Video Assessment",
                            "ar": "Send Video Assessment",
                        },
                        "description": {
                            "en": "Allow the user to send assessments",
                            "ar": "Allow the user to send assessments",
                        },
                    },
                    {
                        "code": "hiring.application.send.offer",
                        "name": {"en": "Send Offer", "ar": "Send Offer"},
                        "description": {
                            "en": "Allow the user to send and generate offers",
                            "ar": "Allow the user to send and generate offers",
                        },
                    },
                    {
                        "code": "hiring.application.send.contract",
                        "name": {"en": "Send Contract", "ar": "Send Contract"},
                        "description": {
                            "en": "Allow the user to send and generate contracts",
                            "ar": "Allow the user to send and generate contracts",
                        },
                    },
                    {
                        "code": "hiring.application.send.assessment",
                        "name": {"en": "Send Assessment", "ar": "Send Assessment"},
                        "description": {
                            "en": "Allow the user to send assessments",
                            "ar": "Allow the user to send assessments",
                        },
                    },
                    {
                        "code": "hiring.application.schedule.meetings",
                        "name": {"en": "Schedule Meetings", "ar": "Schedule Meetings"},
                        "description": {
                            "en": "Allow the user to schedule, edit and delete meetings",
                            "ar": "Allow the user to schedule, edit and delete meetings",
                        },
                    },
                    {
                        "code": "hiring.application.rate.applicants",
                        "name": {"en": "Rate Applicants", "ar": "Rate Applicants"},
                        "description": {
                            "en": "Allow the user to rate applicants",
                            "ar": "Allow the user to rate applicants",
                        },
                    },
                    {
                        "code": "hiring.application.manage.evaluation",
                        "name": {"en": "Manage Evaluation", "ar": "Manage Evaluation"},
                        "description": {
                            "en": "Allow the user to fill out evaluation forms",
                            "ar": "Allow the user to fill out evaluation forms",
                        },
                    },
                    {
                        "code": "hiring.application.view.logs",
                        "name": {"en": "View Logs", "ar": "View Logs"},
                        "description": {
                            "en": "Allow The User To View Logs Of All Changes",
                            "ar": "Allow The User To View Logs Of All Changes",
                        },
                    },
                    {
                        "code": "hiring.application.manage.workflow",
                        "name": {"en": "Manage Workflow", "ar": "Manage Workflow"},
                        "description": {
                            "en": "Allow the user to manage workflows related to the applicant",
                            "ar": "Allow the user to manage workflows related to the applicant",
                        },
                    },
                    {
                        "code": "hiring.application.view.workflow",
                        "name": {"en": "View Workflow", "ar": "View Workflow"},
                        "description": {
                            "en": "Allow the user to only view the related workflows related to the applicant",
                            "ar": "Allow the user to only view the related workflows related to the applicant",
                        },
                    },
                    {
                        "code": "hiring.application.manage.attachments",
                        "name": {
                            "en": "Manage Attachments",
                            "ar": "Manage Attachments",
                        },
                        "description": {
                            "en": "Allow the user to view, upload and download attachments related to the applicant",
                            "ar": "Allow the user to view, upload and download attachments related to the applicant",
                        },
                    },
                    {
                        "code": "hiring.application.discussion",
                        "name": {"en": "Discussion", "ar": "Discussion"},
                        "description": {
                            "en": "Allow the user to participate in discussions related to the applicant",
                            "ar": "Allow the user to participate in discussions related to the applicant",
                        },
                    },
                    {
                        "code": "hiring.application.personality.analysis",
                        "name": {
                            "en": "Personality Analysis",
                            "ar": "Personality Analysis",
                        },
                        "description": {
                            "en": "Allow the user to view the applicants personality analysis",
                            "ar": "Allow the user to view the applicants personality analysis",
                        },
                    },
                    {
                        "code": "hiring.application.notes",
                        "name": {"en": "Notes", "ar": "Notes"},
                        "description": {
                            "en": "Allow the user to add, edit and manage application notes",
                            "ar": "Allow the user to add, edit and manage application notes",
                        },
                    },
                    {
                        "code": "hiring.application.pending.vacancies",
                        "name": {"en": "Pending Vacancies", "ar": "Pending Vacancies"},
                        "description": {
                            "en": "Allow the user to manage pending vacancies",
                            "ar": "Allow the user to manage pending vacancies",
                        },
                    },
                    {
                        "code": "hiring.application.form.builder.status",
                        "name": {
                            "en": "FORM BUILDER STATUS",
                            "ar": "FORM BUILDER STATUS",
                        },
                        "description": {
                            "en": "Allow the user to change any form builder status",
                            "ar": "Allow the user to change any form builder status",
                        },
                    },
                    {
                        "code": "hiring.application.form.builder.manual",
                        "name": {
                            "en": "FORM BUILDER MANUAL",
                            "ar": "FORM BUILDER MANUAL",
                        },
                        "description": {
                            "en": "Allow the user to create manual request",
                            "ar": "Allow the user to create manual request",
                        },
                    },
                    {
                        "code": "hiring.application.rearrange.stages",
                        "name": {"en": "REARRANGE STAGES", "ar": "REARRANGE STAGES"},
                        "description": {
                            "en": "Allow the user to re arrange stages",
                            "ar": "Allow the user to re arrange stages",
                        },
                    },
                    {
                        "code": "hiring.application.recuriter.manager",
                        "name": {"en": "Recruiter Manager", "ar": "Recruiter Manager"},
                        "description": {
                            "en": "Allow the user to manage recruiter",
                            "ar": "Allow the user to manage recruiter",
                        },
                    },
                    {
                        "code": "hiring.application.create.publish.job",
                        "name": {
                            "en": "Create and Publish Job",
                            "ar": "Create and Publish Job",
                        },
                        "description": {
                            "en": "Allow the user to create and publish the job",
                            "ar": "Allow the user to create and publish the job",
                        },
                    },
                    {
                        "code": "hiring.application.push.to.hrms",
                        "name": {"en": "Push to HRMS", "ar": "Push to HRMS"},
                        "description": {
                            "en": "Allow the user to push to HRMS",
                            "ar": "Allow the user to push to HRMS",
                        },
                    },
                    {
                        "code": "hiring.application.bulk.select",
                        "name": {"en": "Bulk Select", "ar": "Bulk Select"},
                        "description": {
                            "en": "Allow the user to click on bulk select",
                            "ar": "Allow the user to click on bulk select",
                        },
                    },
                    {
                        "code": "hiring.application.move.to.another.job",
                        "name": {
                            "en": "Move to Another Job",
                            "ar": "Move to Another Job",
                        },
                        "description": {
                            "en": "Allow the user to move candidate to another job",
                            "ar": "Allow the user to move candidate to another job",
                        },
                    },
                    {
                        "code": "hiring.application.add.candidate",
                        "name": {"en": "Add Candidate", "ar": "Add Candidate"},
                        "description": {
                            "en": "Allow the user to add a candidate",
                            "ar": "Allow the user to add a candidate",
                        },
                    },
                    {
                        "code": "hiring.application.delete.attachment",
                        "name": {"en": "Delete Attachment", "ar": "Delete Attachment"},
                        "description": {
                            "en": "Allow the user to delete attachment",
                            "ar": "Allow the user to delete attachment",
                        },
                    },
                    {
                        "code": "hiring.application.assign.user",
                        "name": {"en": "Assign User", "ar": "Assign User"},
                        "description": {
                            "en": "Allow the user to assign a user",
                            "ar": "Allow the user to assign a user",
                        },
                    },
                    {
                        "code": "hiring.application.assessment.test",
                        "name": {"en": "Assessment Test", "ar": "Assessment Test"},
                        "description": {
                            "en": "Allow the user to view assessment test in candidate card",
                            "ar": "Allow the user to view assessment test in candidate card",
                        },
                    },
                    {
                        "code": "hiring.application.reactivate.job",
                        "name": {"en": "Re Activate Job", "ar": "Re Activate Job"},
                        "description": {
                            "en": "Allow the user to re activate the job",
                            "ar": "Allow the user to re activate the job",
                        },
                    },
                    {
                        "code": "hiring.application.move.to.onboarding",
                        "name": {
                            "en": "Move to Onboarding",
                            "ar": "Move to Onboarding",
                        },
                        "description": {
                            "en": "Allow the user to move candidate to onboarding",
                            "ar": "Allow the user to move candidate to onboarding",
                        },
                    },
                ],
            },
            {
                "name": {"en": "Manage Visa Request", "ar": "Manage Visa Request"},
                "description": {
                    "en": "Manage Visa Request",
                    "ar": "Manage Visa Request",
                },
                "permissions": [],
                "triggers": [
                    {
                        "code": "hiring.manage.visa.request.view.visa.reservation",
                        "name": {
                            "en": "View Visa Reservation",
                            "ar": "View Visa Reservation",
                        },
                        "description": {
                            "en": "View reservation request and view the reserved visas",
                            "ar": "View reservation request and view the reserved visas",
                        },
                    },
                    {
                        "code": "hiring.manage.visa.request.visa.allocation",
                        "name": {
                            "en": "Request Visa Allocation",
                            "ar": "Request Visa Allocation",
                        },
                        "description": {
                            "en": "Request new visa allocation for a candidate",
                            "ar": "Request new visa allocation for a candidate",
                        },
                    },
                    {
                        "code": "hiring.manage.visa.request.view.visa.allocation",
                        "name": {
                            "en": "View Visa Allocation",
                            "ar": "View Visa Allocation",
                        },
                        "description": {
                            "en": "View allocation request",
                            "ar": "View allocation request",
                        },
                    },
                    {
                        "code": "hiring.manage.visa.request.confirm.visa.allocation",
                        "name": {
                            "en": "Confirm Visa Allocation",
                            "ar": "Confirm Visa Allocation",
                        },
                        "description": {
                            "en": "Approve visa allocation request",
                            "ar": "Approve visa allocation request",
                        },
                    },
                    {
                        "code": "hiring.manage.visa.request.cancel.visa.allocation",
                        "name": {
                            "en": "Cancel Visa Allocation",
                            "ar": "Cancel Visa Allocation",
                        },
                        "description": {
                            "en": "Reject/Withdraw visa allocation request",
                            "ar": "Reject/Withdraw visa allocation request",
                        },
                    },
                    {
                        "code": "hiring.manage.visa.request.allocate.on.behalf",
                        "name": {
                            "en": "Allocate on Behalf",
                            "ar": "Allocate on Behalf",
                        },
                        "description": {
                            "en": "Request visa allocation on behalf of other users",
                            "ar": "Request visa allocation on behalf of other users",
                        },
                    },
                    {
                        "code": "hiring.manage.visa.request.upload.attachments",
                        "name": {
                            "en": "Upload Attachments",
                            "ar": "Upload Attachments",
                        },
                        "description": {
                            "en": "Upload attachments in allocation/reservation requests",
                            "ar": "Upload attachments in allocation/reservation requests",
                        },
                    },
                    {
                        "code": "hiring.manage.visa.request.view.attachments",
                        "name": {"en": "View Attachments", "ar": "View Attachments"},
                        "description": {
                            "en": "View attachments in allocation/reservation requests",
                            "ar": "View attachments in allocation/reservation requests",
                        },
                    },
                    {
                        "code": "hiring.manage.visa.request.view.candidate.visa",
                        "name": {
                            "en": "View Candidate Visa",
                            "ar": "View Candidate Visa",
                        },
                        "description": {
                            "en": "View the details of candidate visa",
                            "ar": "View the details of candidate visa",
                        },
                    },
                    {
                        "code": "hiring.manage.visa.request.manage.status",
                        "name": {"en": "Manage Status", "ar": "Manage Status"},
                        "description": {
                            "en": "Move candidate visa across visa pipeline stages",
                            "ar": "Move candidate visa across visa pipeline stages",
                        },
                    },
                    {
                        "code": "hiring.manage.visa.request.mass.allocation",
                        "name": {"en": "Mass Allocation", "ar": "Mass Allocation"},
                        "description": {
                            "en": "Mass allocate visas for different applicants",
                            "ar": "Mass allocate visas for different applicants",
                        },
                    },
                ],
            },
            {
                "name": {"en": "Manage Pipeline", "ar": "Manage Pipeline"},
                "description": {"en": "Manage Pipeline", "ar": "Manage Pipeline"},
                "permissions": [
                    {
                        "code": "hiring.manage.pipeline.create",
                        "name": {"en": "create", "ar": "Create"},
                        "description": {"en": "Create", "ar": "Create"},
                    },
                    {
                        "code": "hiring.manage.pipeline.update",
                        "name": {"en": "Update", "ar": "Update"},
                        "description": {"en": "Update", "ar": "Update"},
                    },
                    {
                        "code": "hiring.manage.pipeline.delete",
                        "name": {"en": "Delete", "ar": "Delete"},
                        "description": {"en": "Delete", "ar": "Delete"},
                    },
                    {
                        "code": "hiring.manage.pipeline.view",
                        "name": {"en": "View", "ar": "View"},
                        "description": {"en": "View", "ar": "View"},
                    },
                ],
                "triggers": [],
            },
            {
                "name": {
                    "en": "Pre-Screening Approval",
                    "ar": "Pre-Screening Approval",
                },
                "description": {
                    "en": "Pre-Screening Approval",
                    "ar": "Pre-Screening Approval",
                },
                "permissions": [
                    {
                        "code": "hiring.prescreening.approval.create",
                        "name": {"en": "create", "ar": "Create"},
                        "description": {"en": "Create", "ar": "Create"},
                    },
                    {
                        "code": "hiring.prescreening.approval.update",
                        "name": {"en": "Update", "ar": "Update"},
                        "description": {"en": "Update", "ar": "Update"},
                    },
                    {
                        "code": "hiring.prescreening.approval.delete",
                        "name": {"en": "Delete", "ar": "Delete"},
                        "description": {"en": "Delete", "ar": "Delete"},
                    },
                    {
                        "code": "hiring.prescreening.approval.view",
                        "name": {"en": "View", "ar": "View"},
                        "description": {"en": "View", "ar": "View"},
                    },
                ],
                "triggers": [
                    {
                        "code": "hiring.prescreening.approval.pipeline",
                        "name": {"en": "Pipelines", "ar": "Pipelines"},
                        "description": {
                            "en": "Add candidate to Pipeline",
                            "ar": "Add candidate to Pipeline",
                        },
                    },
                    {
                        "code": "hiring.prescreening.approval.add.candidate",
                        "name": {"en": "Add Candidate", "ar": "Add Candidate"},
                        "description": {
                            "en": "Allow the user to add a candidate",
                            "ar": "Allow the user to add a candidate",
                        },
                    },
                    {
                        "code": "hiring.prescreening.approval.assign.user",
                        "name": {"en": "Assign User", "ar": "Assign User"},
                        "description": {
                            "en": "Allow the user to assign a user",
                            "ar": "Allow the user to assign a user",
                        },
                    },
                ],
            },
            {
                "name": {"en": "Resume Matching", "ar": "Resume Matching"},
                "description": {"en": "Resume Matching", "ar": "Resume Matching"},
                "permissions": [],
                "triggers": [
                    {
                        "code": "hiring.resume.matching.schedule",
                        "name": {"en": "Schedule", "ar": "Schedule"},
                        "description": {
                            "en": "Schedule a meeting",
                            "ar": "Schedule a meeting",
                        },
                    },
                    {
                        "code": "hiring.resume.matching.add.to.pipeline",
                        "name": {"en": "Add to Pipeline", "ar": "Add to Pipeline"},
                        "description": {
                            "en": "Add candidate to Pipeline",
                            "ar": "Add candidate to Pipeline",
                        },
                    },
                    {
                        "code": "hiring.resume.matching.share",
                        "name": {"en": "Share", "ar": "Share"},
                        "description": {
                            "en": "Share candidate cv",
                            "ar": "Share candidate cv",
                        },
                    },
                    {
                        "code": "hiring.resume.matching.match.eva.rec",
                        "name": {"en": "Match EVA-REC", "ar": "Match EVA-REC"},
                        "description": {
                            "en": "Match with EVA-REC",
                            "ar": "Match with EVA-REC",
                        },
                    },
                    {
                        "code": "hiring.resume.matching.match.document",
                        "name": {"en": "Match Document", "ar": "Match Document"},
                        "description": {
                            "en": "Match with document",
                            "ar": "Match with document",
                        },
                    },
                    {
                        "code": "hiring.resume.matching.upload",
                        "name": {"en": "Upload", "ar": "Upload"},
                        "description": {
                            "en": "Upload a document",
                            "ar": "Upload a document",
                        },
                    },
                    {
                        "code": "hiring.resume.matching.filter",
                        "name": {"en": "Filter", "ar": "Filter"},
                        "description": {
                            "en": "Filter Candidates",
                            "ar": "Filter Candidates",
                        },
                    },
                    {
                        "code": "hiring.resume.matching.create",
                        "name": {"en": "Create", "ar": "Create"},
                        "description": {
                            "en": "Add New Resumes",
                            "ar": "Add New Resumes",
                        },
                    },
                    {
                        "code": "hiring.resume.matching.delete",
                        "name": {"en": "Delete", "ar": "Delete"},
                        "description": {"en": "Delete Resume", "ar": "Delete Resume"},
                    },
                    {
                        "code": "hiring.resume.matching.view",
                        "name": {"en": "View", "ar": "View"},
                        "description": {"en": "View Resume", "ar": "View Resume"},
                    },
                ],
            },
            {
                "name": {"en": "Manage Score-Card", "ar": "Manage Score-Card"},
                "description": {"en": "Manage Score-Card", "ar": "Manage Score-Card"},
                "permissions": [],
                "triggers": [
                    {
                        "code": "hiring.manage.scorecard.view.evaluation.connected.to.job",
                        "name": {
                            "en": "View Evaluation Connected to Job",
                            "ar": "View Evaluation Connected to Job",
                        },
                        "description": {
                            "en": "Allow the user to view evaluation connected to job",
                            "ar": "Allow the user to view evaluation connected to job",
                        },
                    },
                    {
                        "code": "hiring.manage.scorecard.manage.template",
                        "name": {"en": "Manage Template", "ar": "Manage Template"},
                        "description": {
                            "en": "Allow the user to to manage template",
                            "ar": "Allow the user to to manage template",
                        },
                    },
                    {
                        "code": "hiring.manage.scorecard.preview.template",
                        "name": {"en": "Preview Template", "ar": "Preview Template"},
                        "description": {
                            "en": "Allow the user to preview template",
                            "ar": "Allow the user to preview template",
                        },
                    },
                    {
                        "code": "hiring.manage.scorecard.edit.assignees",
                        "name": {"en": "Edit Assignees", "ar": "Edit Assignees"},
                        "description": {
                            "en": "Allow the user to edit assignees",
                            "ar": "Allow the user to edit assignees",
                        },
                    },
                    {
                        "code": "hiring.manage.scorecard.view.assignees",
                        "name": {"en": "View Assignees", "ar": "View Assignees"},
                        "description": {
                            "en": "Allow the user to view assignees",
                            "ar": "Allow the user to view assignees",
                        },
                    },
                    {
                        "code": "hiring.manage.scorecard.manage.reminder.setting",
                        "name": {
                            "en": "Manage Reminder Setting",
                            "ar": "Manage Reminder Setting",
                        },
                        "description": {
                            "en": "Allow the user to manage reminder setting",
                            "ar": "Allow the user to manage reminder setting",
                        },
                    },
                    {
                        "code": "hiring.manage.scorecard.download.report",
                        "name": {
                            "en": "Download Report (Candidate Level)",
                            "ar": "Download Report (Candidate Level)",
                        },
                        "description": {
                            "en": "Allow the user to download report on candidate level",
                            "ar": "Allow the user to download report on candidate level",
                        },
                    },
                    {
                        "code": "hiring.manage.scorecard.send.reminder",
                        "name": {
                            "en": "Send Reminder (Candidate Level)",
                            "ar": "Send Reminder (Candidate Level)",
                        },
                        "description": {
                            "en": "Allow the user to send reminder on candidate level",
                            "ar": "Allow the user to send reminder on candidate level",
                        },
                    },
                    {
                        "code": "hiring.manage.scorecard.rating.by.block",
                        "name": {"en": "Rating By Block", "ar": "Rating By Block"},
                        "description": {
                            "en": "Allow the user to view rating by block",
                            "ar": "Allow the user to view rating by block",
                        },
                    },
                    {
                        "code": "hiring.manage.scorecard.rating.by.member",
                        "name": {"en": "Rating By Member", "ar": "Rating By Member"},
                        "description": {
                            "en": "Allow the user to view rating by members",
                            "ar": "Allow the user to view rating by members",
                        },
                    },
                    {
                        "code": "hiring.manage.scorecard.assign.board",
                        "name": {"en": "Assign Board", "ar": "Assign Board"},
                        "description": {
                            "en": "Allow the user to view assign board",
                            "ar": "Allow the user to view assign board",
                        },
                    },
                    {
                        "code": "hiring.manage.scorecard.view.score.summary",
                        "name": {
                            "en": "View Score Summary",
                            "ar": "View Score Summary",
                        },
                        "description": {
                            "en": "Allow the user to view the score summary",
                            "ar": "Allow the user to view the score summary",
                        },
                    },
                    {
                        "code": "hiring.manage.scorecard.download.score.summary",
                        "name": {
                            "en": "Download Score Summary",
                            "ar": "Download Score Summary",
                        },
                        "description": {
                            "en": "Allow the user to download the score summary",
                            "ar": "Allow the user to download the score summary",
                        },
                    },
                    {
                        "code": "hiring.manage.scorecard.share.score.summary",
                        "name": {
                            "en": "Share Score Summary",
                            "ar": "Share Score Summary",
                        },
                        "description": {
                            "en": "Allow the user to share the score summary",
                            "ar": "Allow the user to share the score summary",
                        },
                    },
                    {
                        "code": "hiring.manage.scorecard.send.reminder.score.summary",
                        "name": {
                            "en": "Send Reminder Score Summary",
                            "ar": "Send Reminder Score Summary",
                        },
                        "description": {
                            "en": "Allow the user to to send reminder from score summary",
                            "ar": "Allow the user to to send reminder from score summary",
                        },
                    },
                ],
            },
            {
                "name": {"en": "Search Database", "ar": "Search Database"},
                "description": {"en": "Search Database", "ar": "Search Database"},
                "permissions": [
                    {
                        "code": "hiring.search.database.view",
                        "name": {"en": "View", "ar": "View"},
                        "description": {"en": "View", "ar": "View"},
                    }
                ],
                "triggers": [
                    {
                        "code": "hiring.search.database.filter.candidate",
                        "name": {"en": "Filter Candidates", "ar": "Filter Candidates"},
                        "description": {
                            "en": "Filter Candidates",
                            "ar": "Filter Candidates",
                        },
                    },
                    {
                        "code": "hiring.search.database.match.candidate",
                        "name": {"en": "Match Candidate", "ar": "Match Candidate"},
                        "description": {
                            "en": "Match candidate with applications",
                            "ar": "Match candidate with applications",
                        },
                    },
                    {
                        "code": "hiring.search.database.schedule.interview",
                        "name": {
                            "en": "Schedule Interview",
                            "ar": "Schedule Interview",
                        },
                        "description": {
                            "en": "Schedule Meeting With an Applicant",
                            "ar": "Schedule Meeting With an Applicant",
                        },
                    },
                    {
                        "code": "hiring.search.database.add.to.pipeline",
                        "name": {"en": "Add to Pipeline", "ar": "Add to Pipeline"},
                        "description": {
                            "en": "Add candidate to Pipeline",
                            "ar": "Add candidate to Pipeline",
                        },
                    },
                    {
                        "code": "hiring.search.database.favourite.applicant",
                        "name": {
                            "en": "Favourite applicant",
                            "ar": "Favourite applicant",
                        },
                        "description": {
                            "en": "add candidate to favorite",
                            "ar": "add candidate to favorite",
                        },
                    },
                    {
                        "code": "hiring.search.database.view.cv",
                        "name": {"en": "View CV", "ar": "View CV"},
                        "description": {
                            "en": "View Candidate CV",
                            "ar": "View Candidate CV",
                        },
                    },
                    {
                        "code": "hiring.search.database.compare.candidate",
                        "name": {"en": "Compare candidate", "ar": "Compare candidate"},
                        "description": {
                            "en": "Compare candidate",
                            "ar": "Compare candidate",
                        },
                    },
                    {
                        "code": "hiring.search.database.add.candidate",
                        "name": {"en": "Add Candidate", "ar": "Add Candidate"},
                        "description": {
                            "en": "Allow the user to add a candidate",
                            "ar": "Allow the user to add a candidate",
                        },
                    },
                    {
                        "code": "hiring.search.database.assign.user",
                        "name": {"en": "Assign User", "ar": "Assign User"},
                        "description": {
                            "en": "Allow the user to assign a user",
                            "ar": "Allow the user to assign a user",
                        },
                    },
                ],
            },
            {
                "name": {"en": "Template", "ar": "Template"},
                "description": {"en": "Template", "ar": "Template"},
                "permissions": [
                    {
                        "code": "hiring.template.create",
                        "name": {"en": "create", "ar": "Create"},
                        "description": {"en": "Create", "ar": "Create"},
                    },
                    {
                        "code": "hiring.template.update",
                        "name": {"en": "Update", "ar": "Update"},
                        "description": {"en": "Update", "ar": "Update"},
                    },
                    {
                        "code": "hiring.template.delete",
                        "name": {"en": "Delete", "ar": "Delete"},
                        "description": {"en": "Delete", "ar": "Delete"},
                    },
                    {
                        "code": "hiring.template.view",
                        "name": {"en": "View", "ar": "View"},
                        "description": {"en": "View", "ar": "View"},
                    },
                ],
                "triggers": [],
            },
        ],
    },
    {
        "product": "Integration",
        "modules": [
            {
                "name": {"en": "Manage Integrations", "ar": "Manage Integrations"},
                "description": {
                    "en": "Manage Integrations",
                    "ar": "Manage Integrations",
                },
                "permissions": [],
                "triggers": [
                    {
                        "code": "integration.sap",
                        "name": {
                            "en": "Integrations With SAP",
                            "ar": "Integrations With SAP",
                        },
                        "description": {
                            "en": "Allow user to integrate with the following 3rd party vendor",
                            "ar": "Allow user to integrate with the following 3rd party vendor",
                        },
                    },
                    {
                        "code": "integration.oracle",
                        "name": {
                            "en": "Integrations With ORACLE",
                            "ar": "Integrations With ORACLE",
                        },
                        "description": {
                            "en": "Allow user to integrate with the following 3rd party vendor",
                            "ar": "Allow user to integrate with the following 3rd party vendor",
                        },
                    },
                    {
                        "code": "integration.slack",
                        "name": {
                            "en": "Integrations With SLACK",
                            "ar": "Integrations With SLACK",
                        },
                        "description": {
                            "en": "Allow user to integrate with the following 3rd party vendor",
                            "ar": "Allow user to integrate with the following 3rd party vendor",
                        },
                    },
                    {
                        "code": "integration.zoom",
                        "name": {
                            "en": "Integrations With ZOOM",
                            "ar": "Integrations With ZOOM",
                        },
                        "description": {
                            "en": "Allow user to integrate with the following 3rd party vendor",
                            "ar": "Allow user to integrate with the following 3rd party vendor",
                        },
                    },
                    {
                        "code": "integration.meet",
                        "name": {
                            "en": "Integrations With MEET",
                            "ar": "Integrations With MEET",
                        },
                        "description": {
                            "en": "Allow user to integrate with the following 3rd party vendor",
                            "ar": "Allow user to integrate with the following 3rd party vendor",
                        },
                    },
                    {
                        "code": "integration.docusign",
                        "name": {
                            "en": "Integrations With DOCUSIGN",
                            "ar": "Integrations With DOCUSIGN",
                        },
                        "description": {
                            "en": "Allow user to integrate with the following 3rd party vendor",
                            "ar": "Allow user to integrate with the following 3rd party vendor",
                        },
                    },
                ],
            }
        ],
    },
    {
        "product": "Onboarding",
        "modules": [
            {
                "name": {"en": "Flow", "ar": "Flow"},
                "description": {"en": "Flow", "ar": "Flow"},
                "permissions": [
                    {
                        "code": "onboarding.flow.create",
                        "name": {"en": "Create", "ar": "Create"},
                        "description": {"en": "Create", "ar": "Create"},
                    },
                    {
                        "code": "onboarding.flow.update",
                        "name": {"en": "Update", "ar": "Update"},
                        "description": {"en": "Update", "ar": "Update"},
                    },
                    {
                        "code": "onboarding.flow.delete",
                        "name": {"en": "Delete", "ar": "Delete"},
                        "description": {"en": "Delete", "ar": "Delete"},
                    },
                    {
                        "code": "onboarding.flow.view",
                        "name": {"en": "View", "ar": "View"},
                        "description": {"en": "View", "ar": "View"},
                    },
                ],
                "triggers": [],
            },
            {
                "name": {"en": "Folder", "ar": "Folder"},
                "description": {"en": "Folder", "ar": "Folder"},
                "permissions": [
                    {
                        "code": "onboarding.folder.create",
                        "name": {"en": "Create", "ar": "Create"},
                        "description": {"en": "Create", "ar": "Create"},
                    },
                    {
                        "code": "onboarding.folder.update",
                        "name": {"en": "Update", "ar": "Update"},
                        "description": {"en": "Update", "ar": "Update"},
                    },
                    {
                        "code": "onboarding.folder.delete",
                        "name": {"en": "Delete", "ar": "Delete"},
                        "description": {"en": "Delete", "ar": "Delete"},
                    },
                    {
                        "code": "onboarding.folder.view",
                        "name": {"en": "View", "ar": "View"},
                        "description": {"en": "View", "ar": "View"},
                    },
                ],
                "triggers": [],
            },
            {
                "name": {"en": "Manage Directory", "ar": "Manage Directory"},
                "description": {"en": "Manage Directory", "ar": "Manage Directory"},
                "permissions": [],
                "triggers": [
                    {
                        "code": "onboarding.manage.directory.view",
                        "name": {"en": "View Directory", "ar": "View Directory"},
                        "description": {
                            "en": "Allow the user to view directory",
                            "ar": "Allow the user to view directory",
                        },
                    },
                    {
                        "code": "onboarding.manage.directory.invite.candidates",
                        "name": {"en": "Invite Candidates", "ar": "Invite Candidates"},
                        "description": {
                            "en": "Allow the user to invite candidates",
                            "ar": "Allow the user to invite candidates",
                        },
                    },
                    {
                        "code": "onboarding.manage.directory.reorder",
                        "name": {"en": "Reorder", "ar": "Reorder"},
                        "description": {
                            "en": "Allow the user to reorder space/folder/flow",
                            "ar": "Allow the user to reorder space/folder/flow",
                        },
                    },
                    {
                        "code": "onboarding.manage.directory.link",
                        "name": {"en": "Link", "ar": "Link"},
                        "description": {
                            "en": "Allow the user to link flow",
                            "ar": "Allow the user to link flow",
                        },
                    },
                ],
            },
            {
                "name": {"en": "Manage Onboarding", "ar": "Manage Onboarding"},
                "description": {"en": "Manage Onboarding", "ar": "Manage Onboarding"},
                "permissions": [],
                "triggers": [
                    {
                        "code": "onboarding.manage.view.activity",
                        "name": {"en": "View Activity", "ar": "View Activity"},
                        "description": {
                            "en": "Allow the user to view activity",
                            "ar": "Allow the user to view activity",
                        },
                    },
                    {
                        "code": "onboarding.manage.view.all.flows",
                        "name": {"en": "View All Flows", "ar": "View All Flows"},
                        "description": {
                            "en": "Allow the user to view all flows",
                            "ar": "Allow the user to view all flows",
                        },
                    },
                    {
                        "code": "onboarding.manage.view.members",
                        "name": {"en": "View Members", "ar": "View Members"},
                        "description": {
                            "en": "Allow the user to view members",
                            "ar": "Allow the user to view members",
                        },
                    },
                    {
                        "code": "onboarding.manage.view.task",
                        "name": {"en": "View Tasks", "ar": "View Tasks"},
                        "description": {
                            "en": "Allow the user to view tasks",
                            "ar": "Allow the user to view tasks",
                        },
                    },
                    {
                        "code": "onboarding.manage.recent.activity",
                        "name": {
                            "en": "View Responses: Recent Activity",
                            "ar": "View Responses: Recent Activity",
                        },
                        "description": {
                            "en": "Allow the user to view responses - recent activity",
                            "ar": "Allow the user to view responses - recent activity",
                        },
                    },
                    {
                        "code": "onboarding.manage.assigned.to.view",
                        "name": {
                            "en": "View Responses: Assigned to view",
                            "ar": "View Responses: Assigned to view",
                        },
                        "description": {
                            "en": "Allow the user to view responses - assigned to view",
                            "ar": "Allow the user to view responses - assigned to view",
                        },
                    },
                ],
            },
            {
                "name": {"en": "Space", "ar": "Space"},
                "description": {"en": "Space", "ar": "Space"},
                "permissions": [
                    {
                        "code": "onboarding.space.create",
                        "name": {"en": "Create", "ar": "Create"},
                        "description": {"en": "Create", "ar": "Create"},
                    },
                    {
                        "code": "onboarding.space.update",
                        "name": {"en": "Update", "ar": "Update"},
                        "description": {"en": "Update", "ar": "Update"},
                    },
                    {
                        "code": "onboarding.space.delete",
                        "name": {"en": "Delete", "ar": "Delete"},
                        "description": {"en": "Delete", "ar": "Delete"},
                    },
                    {
                        "code": "onboarding.space.view",
                        "name": {"en": "View", "ar": "View"},
                        "description": {"en": "View", "ar": "View"},
                    },
                ],
                "triggers": [],
            },
        ],
    },
    {
        "product": "Security",
        "modules": [
            {
                "name": {"en": "Manage Roles", "ar": "Manage Roles"},
                "description": {"en": "Manage Roles", "ar": "Manage Roles"},
                "permissions": [
                    {
                        "code": "security.roles.create",
                        "name": {"en": "create", "ar": "Create"},
                        "description": {"en": "Create", "ar": "Create"},
                    },
                    {
                        "code": "security.roles.update",
                        "name": {"en": "Update", "ar": "Update"},
                        "description": {"en": "Update", "ar": "Update"},
                    },
                    {
                        "code": "security.roles.delete",
                        "name": {"en": "Delete", "ar": "Delete"},
                        "description": {"en": "Delete", "ar": "Delete"},
                    },
                    {
                        "code": "security.roles.view",
                        "name": {"en": "View", "ar": "View"},
                        "description": {"en": "View", "ar": "View"},
                    },
                ],
                "triggers": [],
            },
            {
                "name": {
                    "en": "Manage Automated Access",
                    "ar": "Manage Automated Access",
                },
                "description": {
                    "en": "Manage Automated Access",
                    "ar": "Manage Automated Access",
                },
                "permissions": [
                    {
                        "code": "security.automated.access.create",
                        "name": {"en": "create", "ar": "Create"},
                        "description": {"en": "Create", "ar": "Create"},
                    },
                    {
                        "code": "security.automated.access.update",
                        "name": {"en": "Update", "ar": "Update"},
                        "description": {"en": "Update", "ar": "Update"},
                    },
                    {
                        "code": "security.automated.access.delete",
                        "name": {"en": "Delete", "ar": "Delete"},
                        "description": {"en": "Delete", "ar": "Delete"},
                    },
                    {
                        "code": "security.automated.access.view",
                        "name": {"en": "View", "ar": "View"},
                        "description": {"en": "View", "ar": "View"},
                    },
                ],
                "triggers": [],
            },
            {
                "name": {
                    "en": "Manage Time Based Access",
                    "ar": "Manage Time Based Access",
                },
                "description": {
                    "en": "Manage Time Based Access",
                    "ar": "Manage Time Based Access",
                },
                "permissions": [
                    {
                        "code": "security.time.based.access.create",
                        "name": {"en": "create", "ar": "Create"},
                        "description": {"en": "Create", "ar": "Create"},
                    },
                    {
                        "code": "security.time.based.access.update",
                        "name": {"en": "Update", "ar": "Update"},
                        "description": {"en": "Update", "ar": "Update"},
                    },
                    {
                        "code": "security.time.based.access.delete",
                        "name": {"en": "Delete", "ar": "Delete"},
                        "description": {"en": "Delete", "ar": "Delete"},
                    },
                    {
                        "code": "security.time.based.access.view",
                        "name": {"en": "View", "ar": "View"},
                        "description": {"en": "View", "ar": "View"},
                    },
                ],
                "triggers": [],
            },
            {
                "name": {"en": "Manage MFA", "ar": "Manage MFA"},
                "description": {"en": "Manage MFA", "ar": "Manage MFA"},
                "permissions": [],
                "triggers": [
                    {
                        "code": "security.mfa.generate.recovery.code",
                        "name": {
                            "en": "Generate Recovery Code",
                            "ar": "Generate Recovery Code",
                        },
                        "description": {
                            "en": "Generate Recovery Codes for user, by administrator on behalf of the user or by user himself.",
                            "ar": "Generate Recovery Codes for user, by administrator on behalf of the user or by user himself.",
                        },
                    },
                    {
                        "code": "security.mfa.view.recovery.code",
                        "name": {
                            "en": "View Recovery Codes",
                            "ar": "View Recovery Codes",
                        },
                        "description": {
                            "en": "Access MFA Settings and employees/user's recovery codes.",
                            "ar": "Access MFA Settings and employees/user's recovery codes.",
                        },
                    },
                    {
                        "code": "security.mfa.manage.setting",
                        "name": {
                            "en": "Manage MFA Settings",
                            "ar": "Manage MFA Settings",
                        },
                        "description": {
                            "en": "Enable or disable MFA on account Level",
                            "ar": "Enable or disable MFA on account Level",
                        },
                    },
                ],
            },
        ],
    },
    {
        "product": "Setup and Administration",
        "modules": [
            {
                "name": {"en": "Manage Branch", "ar": "Manage Branch"},
                "description": {"en": "Manage Branch", "ar": "Manage Branch"},
                "permissions": [
                    {
                        "code": "administration.branch.create",
                        "name": {"en": "Create", "ar": "Create"},
                        "description": {"en": "Create", "ar": "Create"},
                    },
                    {
                        "code": "administration.branch.update",
                        "name": {"en": "Update", "ar": "Update"},
                        "description": {"en": "Update", "ar": "Update"},
                    },
                    {
                        "code": "administration.branch.delete",
                        "name": {"en": "Delete", "ar": "Delete"},
                        "description": {"en": "Delete", "ar": "Delete"},
                    },
                    {
                        "code": "administration.branch.view",
                        "name": {"en": "View", "ar": "View"},
                        "description": {"en": "View", "ar": "View"},
                    },
                ],
                "triggers": [],
            },
            {
                "name": {"en": "Manage Categories", "ar": "Manage Categories"},
                "description": {"en": "Manage Categories", "ar": "Manage Categories"},
                "permissions": [
                    {
                        "code": "administration.categories.create",
                        "name": {"en": "Create", "ar": "Create"},
                        "description": {"en": "Create", "ar": "Create"},
                    },
                    {
                        "code": "administration.categories.update",
                        "name": {"en": "Update", "ar": "Update"},
                        "description": {"en": "Update", "ar": "Update"},
                    },
                    {
                        "code": "administration.categories.delete",
                        "name": {"en": "Delete", "ar": "Delete"},
                        "description": {"en": "Delete", "ar": "Delete"},
                    },
                    {
                        "code": "administration.categories.view",
                        "name": {"en": "View", "ar": "View"},
                        "description": {"en": "View", "ar": "View"},
                    },
                ],
                "triggers": [],
            },
            {
                "name": {"en": "Manage Data Roles", "ar": "Manage Data Roles"},
                "description": {"en": "Manage Data Roles", "ar": "Manage Data Roles"},
                "permissions": [
                    {
                        "code": "administration.data.roles.create",
                        "name": {"en": "Create", "ar": "Create"},
                        "description": {"en": "Create", "ar": "Create"},
                    },
                    {
                        "code": "administration.data.roles.update",
                        "name": {"en": "Update", "ar": "Update"},
                        "description": {"en": "Update", "ar": "Update"},
                    },
                    {
                        "code": "administration.data.roles.delete",
                        "name": {"en": "Delete", "ar": "Delete"},
                        "description": {"en": "Delete", "ar": "Delete"},
                    },
                    {
                        "code": "administration.data.roles.view",
                        "name": {"en": "View", "ar": "View"},
                        "description": {"en": "View", "ar": "View"},
                    },
                ],
                "triggers": [],
            },
            {
                "name": {"en": "Manage Users", "ar": "Manage Users"},
                "description": {"en": "Manage Users", "ar": "Manage Users"},
                "permissions": [
                    {
                        "code": "administration.user.create",
                        "name": {"en": "Create", "ar": "Create"},
                        "description": {"en": "Create", "ar": "Create"},
                    },
                    {
                        "code": "administration.user.update",
                        "name": {"en": "Update", "ar": "Update"},
                        "description": {"en": "Update", "ar": "Update"},
                    },
                    {
                        "code": "administration.user.delete",
                        "name": {"en": "Delete", "ar": "Delete"},
                        "description": {"en": "Delete", "ar": "Delete"},
                    },
                    {
                        "code": "administration.user.view",
                        "name": {"en": "View", "ar": "View"},
                        "description": {"en": "View", "ar": "View"},
                    },
                ],
                "triggers": [],
            },
            {
                "name": {"en": "Manage Teams", "ar": "Manage Teams"},
                "description": {"en": "Manage Teams", "ar": "Manage Teams"},
                "permissions": [
                    {
                        "code": "administration.team.create",
                        "name": {"en": "Create", "ar": "Create"},
                        "description": {"en": "Create", "ar": "Create"},
                    },
                    {
                        "code": "administration.team.update",
                        "name": {"en": "Update", "ar": "Update"},
                        "description": {"en": "Update", "ar": "Update"},
                    },
                    {
                        "code": "administration.team.delete",
                        "name": {"en": "Delete", "ar": "Delete"},
                        "description": {"en": "Delete", "ar": "Delete"},
                    },
                    {
                        "code": "administration.team.view",
                        "name": {"en": "View", "ar": "View"},
                        "description": {"en": "View", "ar": "View"},
                    },
                ],
                "triggers": [],
            },
            {
                "name": {
                    "en": "Manage Education Classification",
                    "ar": "Manage Education Classification",
                },
                "description": {
                    "en": "Manage Education Classification",
                    "ar": "Manage Education Classification",
                },
                "permissions": [
                    {
                        "code": "administration.education.classification.create",
                        "name": {"en": "Create", "ar": "Create"},
                        "description": {"en": "Create", "ar": "Create"},
                    },
                    {
                        "code": "administration.education.classification.update",
                        "name": {"en": "Update", "ar": "Update"},
                        "description": {"en": "Update", "ar": "Update"},
                    },
                    {
                        "code": "administration.education.classification.delete",
                        "name": {"en": "Delete", "ar": "Delete"},
                        "description": {"en": "Delete", "ar": "Delete"},
                    },
                    {
                        "code": "administration.education.classification.view",
                        "name": {"en": "View", "ar": "View"},
                        "description": {"en": "View", "ar": "View"},
                    },
                ],
                "triggers": [],
            },
            {
                "name": {
                    "en": "Manage Offer Classification",
                    "ar": "Manage Offer Classification",
                },
                "description": {
                    "en": "Manage Offer Classification",
                    "ar": "Manage Offer Classification",
                },
                "permissions": [
                    {
                        "code": "administration.offer.classification.create",
                        "name": {"en": "Create", "ar": "Create"},
                        "description": {"en": "Create", "ar": "Create"},
                    },
                    {
                        "code": "administration.offer.classification.update",
                        "name": {"en": "Update", "ar": "Update"},
                        "description": {"en": "Update", "ar": "Update"},
                    },
                    {
                        "code": "administration.offer.classification.delete",
                        "name": {"en": "Delete", "ar": "Delete"},
                        "description": {"en": "Delete", "ar": "Delete"},
                    },
                    {
                        "code": "administration.offer.classification.view",
                        "name": {"en": "View", "ar": "View"},
                        "description": {"en": "View", "ar": "View"},
                    },
                ],
                "triggers": [],
            },
            {
                "name": {
                    "en": "Manage Personal Classification",
                    "ar": "Manage Personal Classification",
                },
                "description": {
                    "en": "Manage Personal Classification",
                    "ar": "Manage Personal Classification",
                },
                "permissions": [
                    {
                        "code": "administration.personal.classification.create",
                        "name": {"en": "Create", "ar": "Create"},
                        "description": {"en": "Create", "ar": "Create"},
                    },
                    {
                        "code": "administration.personal.classification.update",
                        "name": {"en": "Update", "ar": "Update"},
                        "description": {"en": "Update", "ar": "Update"},
                    },
                    {
                        "code": "administration.personal.classification.delete",
                        "name": {"en": "Delete", "ar": "Delete"},
                        "description": {"en": "Delete", "ar": "Delete"},
                    },
                    {
                        "code": "administration.personal.classification.view",
                        "name": {"en": "View", "ar": "View"},
                        "description": {"en": "View", "ar": "View"},
                    },
                ],
                "triggers": [],
            },
            {
                "name": {
                    "en": "Manage Position Classification",
                    "ar": "Manage Position Classification",
                },
                "description": {
                    "en": "Manage Position Classification",
                    "ar": "Manage Position Classification",
                },
                "permissions": [
                    {
                        "code": "administration.position.classification.create",
                        "name": {"en": "Create", "ar": "Create"},
                        "description": {"en": "Create", "ar": "Create"},
                    },
                    {
                        "code": "administration.position.classification.update",
                        "name": {"en": "Update", "ar": "Update"},
                        "description": {"en": "Update", "ar": "Update"},
                    },
                    {
                        "code": "administration.position.classification.delete",
                        "name": {"en": "Delete", "ar": "Delete"},
                        "description": {"en": "Delete", "ar": "Delete"},
                    },
                    {
                        "code": "administration.position.classification.view",
                        "name": {"en": "View", "ar": "View"},
                        "description": {"en": "View", "ar": "View"},
                    },
                ],
                "triggers": [],
            },
            {
                "name": {
                    "en": "Manage Work Classification",
                    "ar": "Manage Work Classification",
                },
                "description": {
                    "en": "Manage Work Classification",
                    "ar": "Manage Work Classification",
                },
                "permissions": [
                    {
                        "code": "administration.work.classification.create",
                        "name": {"en": "Create", "ar": "Create"},
                        "description": {"en": "Create", "ar": "Create"},
                    },
                    {
                        "code": "administration.work.classification.update",
                        "name": {"en": "Update", "ar": "Update"},
                        "description": {"en": "Update", "ar": "Update"},
                    },
                    {
                        "code": "administration.work.classification.delete",
                        "name": {"en": "Delete", "ar": "Delete"},
                        "description": {"en": "Delete", "ar": "Delete"},
                    },
                    {
                        "code": "administration.work.classification.view",
                        "name": {"en": "View", "ar": "View"},
                        "description": {"en": "View", "ar": "View"},
                    },
                ],
                "triggers": [],
            },
            {
                "name": {"en": "Employee", "ar": "Employee"},
                "description": {"en": "Employee", "ar": "Employee"},
                "permissions": [
                    {
                        "code": "administration.employee.create",
                        "name": {"en": "Create", "ar": "Create"},
                        "description": {"en": "Create", "ar": "Create"},
                    },
                    {
                        "code": "administration.employee.update",
                        "name": {"en": "Update", "ar": "Update"},
                        "description": {"en": "Update", "ar": "Update"},
                    },
                    {
                        "code": "administration.employee.delete",
                        "name": {"en": "Delete", "ar": "Delete"},
                        "description": {"en": "Delete", "ar": "Delete"},
                    },
                    {
                        "code": "administration.employee.view",
                        "name": {"en": "View", "ar": "View"},
                        "description": {"en": "View", "ar": "View"},
                    },
                ],
                "triggers": [],
            },
            {
                "name": {"en": "Manage Hierarchy", "ar": "Manage Hierarchy"},
                "description": {"en": "Manage Hierarchy", "ar": "Manage Hierarchy"},
                "permissions": [
                    {
                        "code": "administration.hierarchy.create",
                        "name": {"en": "Create", "ar": "Create"},
                        "description": {"en": "Create", "ar": "Create"},
                    },
                    {
                        "code": "administration.hierarchy.update",
                        "name": {"en": "Update", "ar": "Update"},
                        "description": {"en": "Update", "ar": "Update"},
                    },
                    {
                        "code": "administration.hierarchy.delete",
                        "name": {"en": "Delete", "ar": "Delete"},
                        "description": {"en": "Delete", "ar": "Delete"},
                    },
                    {
                        "code": "administration.hierarchy.view",
                        "name": {"en": "View", "ar": "View"},
                        "description": {"en": "View", "ar": "View"},
                    },
                ],
                "triggers": [],
            },
            {
                "name": {
                    "en": "Manage Hierarchy Level",
                    "ar": "Manage Hierarchy Level",
                },
                "description": {
                    "en": "Manage Hierarchy Level",
                    "ar": "Manage Hierarchy Level",
                },
                "permissions": [
                    {
                        "code": "administration.hierarchy.level.create",
                        "name": {"en": "Create", "ar": "Create"},
                        "description": {"en": "Create", "ar": "Create"},
                    },
                    {
                        "code": "administration.hierarchy.level.update",
                        "name": {"en": "Update", "ar": "Update"},
                        "description": {"en": "Update", "ar": "Update"},
                    },
                    {
                        "code": "administration.hierarchy.level.delete",
                        "name": {"en": "Delete", "ar": "Delete"},
                        "description": {"en": "Delete", "ar": "Delete"},
                    },
                    {
                        "code": "administration.hierarchy.level.view",
                        "name": {"en": "View", "ar": "View"},
                        "description": {"en": "View", "ar": "View"},
                    },
                ],
                "triggers": [],
            },
            {
                "name": {"en": "Manage Job Titles", "ar": "Manage Job Titles"},
                "description": {"en": "Manage Job Titles", "ar": "Manage Job Titles"},
                "permissions": [
                    {
                        "code": "administration.job.titles.create",
                        "name": {"en": "Create", "ar": "Create"},
                        "description": {"en": "Create", "ar": "Create"},
                    },
                    {
                        "code": "administration.job.titles.update",
                        "name": {"en": "Update", "ar": "Update"},
                        "description": {"en": "Update", "ar": "Update"},
                    },
                    {
                        "code": "administration.job.titles.delete",
                        "name": {"en": "Delete", "ar": "Delete"},
                        "description": {"en": "Delete", "ar": "Delete"},
                    },
                    {
                        "code": "administration.job.titles.view",
                        "name": {"en": "View", "ar": "View"},
                        "description": {"en": "View", "ar": "View"},
                    },
                ],
                "triggers": [],
            },
            {
                "name": {"en": "Manage Locations", "ar": "Manage Locations"},
                "description": {"en": "Manage Locations", "ar": "Manage Locations"},
                "permissions": [
                    {
                        "code": "administration.locations.create",
                        "name": {"en": "Create", "ar": "Create"},
                        "description": {"en": "Create", "ar": "Create"},
                    },
                    {
                        "code": "administration.locations.update",
                        "name": {"en": "Update", "ar": "Update"},
                        "description": {"en": "Update", "ar": "Update"},
                    },
                    {
                        "code": "administration.locations.delete",
                        "name": {"en": "Delete", "ar": "Delete"},
                        "description": {"en": "Delete", "ar": "Delete"},
                    },
                    {
                        "code": "administration.locations.view",
                        "name": {"en": "View", "ar": "View"},
                        "description": {"en": "View", "ar": "View"},
                    },
                ],
                "triggers": [],
            },
            {
                "name": {
                    "en": "Manage Organization Group",
                    "ar": "Manage Organization Group",
                },
                "description": {
                    "en": "Manage Organization Group",
                    "ar": "Manage Organization Group",
                },
                "permissions": [
                    {
                        "code": "administration.organization.group.create",
                        "name": {"en": "Create", "ar": "Create"},
                        "description": {"en": "Create", "ar": "Create"},
                    },
                    {
                        "code": "administration.organization.group.update",
                        "name": {"en": "Update", "ar": "Update"},
                        "description": {"en": "Update", "ar": "Update"},
                    },
                    {
                        "code": "administration.organization.group.delete",
                        "name": {"en": "Delete", "ar": "Delete"},
                        "description": {"en": "Delete", "ar": "Delete"},
                    },
                    {
                        "code": "administration.organization.group.view",
                        "name": {"en": "View", "ar": "View"},
                        "description": {"en": "View", "ar": "View"},
                    },
                ],
                "triggers": [],
            },
            {
                "name": {"en": "Manage Positions", "ar": "Manage Positions"},
                "description": {"en": "Manage Positions", "ar": "Manage Positions"},
                "permissions": [
                    {
                        "code": "administration.positions.create",
                        "name": {"en": "Create", "ar": "Create"},
                        "description": {"en": "Create", "ar": "Create"},
                    },
                    {
                        "code": "administration.positions.update",
                        "name": {"en": "Update", "ar": "Update"},
                        "description": {"en": "Update", "ar": "Update"},
                    },
                    {
                        "code": "administration.positions.delete",
                        "name": {"en": "Delete", "ar": "Delete"},
                        "description": {"en": "Delete", "ar": "Delete"},
                    },
                    {
                        "code": "administration.positions.view",
                        "name": {"en": "View", "ar": "View"},
                        "description": {"en": "View", "ar": "View"},
                    },
                ],
                "triggers": [],
            },
            {
                "name": {
                    "en": "Manage Positions Titles",
                    "ar": "Manage Positions Titles",
                },
                "description": {
                    "en": "Manage Positions Titles",
                    "ar": "Manage Positions Titles",
                },
                "permissions": [
                    {
                        "code": "administration.positions.titles.create",
                        "name": {"en": "Create", "ar": "Create"},
                        "description": {"en": "Create", "ar": "Create"},
                    },
                    {
                        "code": "administration.positions.titles.update",
                        "name": {"en": "Update", "ar": "Update"},
                        "description": {"en": "Update", "ar": "Update"},
                    },
                    {
                        "code": "administration.positions.titles.delete",
                        "name": {"en": "Delete", "ar": "Delete"},
                        "description": {"en": "Delete", "ar": "Delete"},
                    },
                    {
                        "code": "administration.positions.titles.view",
                        "name": {"en": "View", "ar": "View"},
                        "description": {"en": "View", "ar": "View"},
                    },
                ],
                "triggers": [],
            },
            {
                "name": {"en": "Manage Projects", "ar": "Manage Projects"},
                "description": {"en": "Manage Projects", "ar": "Manage Projects"},
                "permissions": [
                    {
                        "code": "administration.project.create",
                        "name": {"en": "Create", "ar": "Create"},
                        "description": {"en": "Create", "ar": "Create"},
                    },
                    {
                        "code": "administration.project.update",
                        "name": {"en": "Update", "ar": "Update"},
                        "description": {"en": "Update", "ar": "Update"},
                    },
                    {
                        "code": "administration.project.delete",
                        "name": {"en": "Delete", "ar": "Delete"},
                        "description": {"en": "Delete", "ar": "Delete"},
                    },
                    {
                        "code": "administration.project.view",
                        "name": {"en": "View", "ar": "View"},
                        "description": {"en": "View", "ar": "View"},
                    },
                ],
                "triggers": [],
            },
            {
                "name": {"en": "Manage Sponsors", "ar": "Manage Sponsors"},
                "description": {"en": "Manage Sponsors", "ar": "Manage Sponsors"},
                "permissions": [
                    {
                        "code": "administration.sponsor.create",
                        "name": {"en": "Create", "ar": "Create"},
                        "description": {"en": "Create", "ar": "Create"},
                    },
                    {
                        "code": "administration.sponsor.update",
                        "name": {"en": "Update", "ar": "Update"},
                        "description": {"en": "Update", "ar": "Update"},
                    },
                    {
                        "code": "administration.sponsor.delete",
                        "name": {"en": "Delete", "ar": "Delete"},
                        "description": {"en": "Delete", "ar": "Delete"},
                    },
                    {
                        "code": "administration.sponsor.view",
                        "name": {"en": "View", "ar": "View"},
                        "description": {"en": "View", "ar": "View"},
                    },
                ],
                "triggers": [],
            },
            {
                "name": {"en": "Manage Sub Category", "ar": "Manage Sub Category"},
                "description": {
                    "en": "Manage Sub Category",
                    "ar": "Manage Sub Category",
                },
                "permissions": [
                    {
                        "code": "administration.sub.category.create",
                        "name": {"en": "Create", "ar": "Create"},
                        "description": {"en": "Create", "ar": "Create"},
                    },
                    {
                        "code": "administration.sub.category.update",
                        "name": {"en": "Update", "ar": "Update"},
                        "description": {"en": "Update", "ar": "Update"},
                    },
                    {
                        "code": "administration.sub.category.delete",
                        "name": {"en": "Delete", "ar": "Delete"},
                        "description": {"en": "Delete", "ar": "Delete"},
                    },
                    {
                        "code": "administration.sub.category.view",
                        "name": {"en": "View", "ar": "View"},
                        "description": {"en": "View", "ar": "View"},
                    },
                ],
                "triggers": [],
            },
            {
                "name": {"en": "Pre Screening", "ar": "Pre Screening"},
                "description": {"en": "Pre Screening", "ar": "Pre Screening"},
                "permissions": [
                    {
                        "code": "administration.pre.screening.create",
                        "name": {"en": "Create", "ar": "Create"},
                        "description": {"en": "Create", "ar": "Create"},
                    },
                    {
                        "code": "administration.pre.screening.update",
                        "name": {"en": "Update", "ar": "Update"},
                        "description": {"en": "Update", "ar": "Update"},
                    },
                    {
                        "code": "administration.pre.screening.delete",
                        "name": {"en": "Delete", "ar": "Delete"},
                        "description": {"en": "Delete", "ar": "Delete"},
                    },
                    {
                        "code": "administration.pre.screening.view",
                        "name": {"en": "View", "ar": "View"},
                        "description": {"en": "View", "ar": "View"},
                    },
                ],
                "triggers": [
                    {
                        "code": "administration.pre.screening.assign",
                        "name": {"en": "Assign", "ar": "Assign"},
                        "description": {
                            "en": "Assign To Pre Screening",
                            "ar": "Assign To Pre Screening",
                        },
                    },
                    {
                        "code": "administration.pre.screening.post",
                        "name": {"en": "Post", "ar": "Post"},
                        "description": {
                            "en": "Post To Pre Screening",
                            "ar": "Post To Pre Screening",
                        },
                    },
                ],
            },
            {
                "name": {"en": "Manage Self Service", "ar": "Manage Self Service"},
                "description": {
                    "en": "Manage Self Service",
                    "ar": "Manage Self Service",
                },
                "permissions": [],
                "triggers": [
                    {
                        "code": "administration.self.service.job.requisition",
                        "name": {"en": "Job Requisition", "ar": "Job Requisition"},
                        "description": {
                            "en": "Allow the user to manage approvals assigned to them",
                            "ar": "Allow the user to manage approvals assigned to them",
                        },
                    },
                    {
                        "code": "administration.self.service.approval.tracking.viewer",
                        "name": {
                            "en": "Approval Tracking Viewer",
                            "ar": "Approval Tracking Viewer",
                        },
                        "description": {
                            "en": "Allow the user to view all approval tracking",
                            "ar": "Allow the user to view all approval tracking",
                        },
                    },
                    {
                        "code": "administration.self.service.approval.tracking.user",
                        "name": {
                            "en": "Approval Tracking User",
                            "ar": "Approval Tracking User",
                        },
                        "description": {
                            "en": "Allow the user to manage all approval tracking",
                            "ar": "Allow the user to manage all approval tracking",
                        },
                    },
                    {
                        "code": "administration.self.service.workflow.approval",
                        "name": {
                            "en": "Workflow Approvals",
                            "ar": "Workflow Approvals",
                        },
                        "description": {
                            "en": "Allow the user to approve the job requisitions",
                            "ar": "Allow the user to approve the job requisitions",
                        },
                    },
                    {
                        "code": "administration.self.service.internal.vacancies",
                        "name": {
                            "en": "Internal Vacancies",
                            "ar": "Internal Vacancies",
                        },
                        "description": {
                            "en": "Allow the user to apply to internal vacancies",
                            "ar": "Allow the user to apply to internal vacancies",
                        },
                    },
                    {
                        "code": "administration.self.service.non.budgeted.requisition",
                        "name": {
                            "en": "NON-Budgeted Requisition",
                            "ar": "NON-Budgeted Requisition",
                        },
                        "description": {
                            "en": "Allow the user to request for a non-budgeted vacancy",
                            "ar": "Allow the user to request for a non-budgeted vacancy",
                        },
                    },
                    {
                        "code": "administration.self.service.request.visa.reservation",
                        "name": {
                            "en": "Request Visa Reservation",
                            "ar": "Request Visa Reservation",
                        },
                        "description": {
                            "en": "Request new visa reservation from GR",
                            "ar": "Request new visa reservation from GR",
                        },
                    },
                    {
                        "code": "administration.self.service.job.posting",
                        "name": {
                            "en": "View Visa Reservation",
                            "ar": "View Visa Reservation",
                        },
                        "description": {
                            "en": "View reservation request and view the reserved visas",
                            "ar": "View reservation request and view the reserved visas",
                        },
                    },
                    {
                        "code": "administration.self.service.cancel.visa.reservation",
                        "name": {
                            "en": "Cancel Visa Reservation",
                            "ar": "Cancel Visa Reservation",
                        },
                        "description": {
                            "en": "Reject/Decline visa reservation request",
                            "ar": "Reject/Decline visa reservation request",
                        },
                    },
                    {
                        "code": "administration.self.service.view.visa.allocation",
                        "name": {
                            "en": "View Visa Allocation",
                            "ar": "View Visa Allocation",
                        },
                        "description": {
                            "en": "View allocation request",
                            "ar": "View allocation request",
                        },
                    },
                    {
                        "code": "administration.self.service.reserve.on.behalf",
                        "name": {"en": "Reserve on Behalf", "ar": "Reserve on Behalf"},
                        "description": {
                            "en": "Request visa reservation on behalf of other users",
                            "ar": "Request visa reservation on behalf of other users",
                        },
                    },
                    {
                        "code": "administration.self.service.view.allocation.request",
                        "name": {
                            "en": "View All Allocation Requests",
                            "ar": "View All Allocation Requests",
                        },
                        "description": {
                            "en": "View all allocation requests that belong to other users",
                            "ar": "View all allocation requests that belong to other users",
                        },
                    },
                    {
                        "code": "administration.self.service.view.reservation.request",
                        "name": {
                            "en": "View All Reservation Requests",
                            "ar": "View All Reservation Requests",
                        },
                        "description": {
                            "en": "View all reservation requests that belong to other users",
                            "ar": "View all reservation requests that belong to other users",
                        },
                    },
                    {
                        "code": "administration.self.service.upload.attachment",
                        "name": {
                            "en": "Upload Attachments",
                            "ar": "Upload Attachments",
                        },
                        "description": {
                            "en": "Upload attachments in allocation/reservation requests",
                            "ar": "Upload attachments in allocation/reservation requests",
                        },
                    },
                    {
                        "code": "administration.self.service.view.attachment",
                        "name": {"en": "View Attachments", "ar": "View Attachments"},
                        "description": {
                            "en": "View attachments in allocation/reservation requests",
                            "ar": "View attachments in allocation/reservation requests",
                        },
                    },
                    {
                        "code": "administration.self.service.request.visa.allocation",
                        "name": {
                            "en": "Request Visa Allocation",
                            "ar": "Request Visa Allocation",
                        },
                        "description": {
                            "en": "Request new visa allocation for a candidate",
                            "ar": "Request new visa allocation for a candidate",
                        },
                    },
                    {
                        "code": "administration.self.service.request.more.information",
                        "name": {
                            "en": "Request More Information",
                            "ar": "Request More Information",
                        },
                        "description": {
                            "en": "Request more information about the requests",
                            "ar": "Request more information about the requests",
                        },
                    },
                    {
                        "code": "administration.self.service.cancel.visa.allocation",
                        "name": {
                            "en": "Cancel Visa Allocation",
                            "ar": "Cancel Visa Allocation",
                        },
                        "description": {
                            "en": "Reject/Withdraw visa allocation request",
                            "ar": "Reject/Withdraw visa allocation request",
                        },
                    },
                    {
                        "code": "administration.self.service.allocate.on.Behalf",
                        "name": {
                            "en": "Allocate on Behalf",
                            "ar": "Allocate on Behalf",
                        },
                        "description": {
                            "en": "Request visa allocation on behalf of other users",
                            "ar": "Request visa allocation on behalf of other users",
                        },
                    },
                    {
                        "code": "administration.self.service.view.task",
                        "name": {"en": "View all tasks", "ar": "View all tasks"},
                        "description": {"en": "View all tasks", "ar": "View all tasks"},
                    },
                    {
                        "code": "administration.self.service.update.task",
                        "name": {"en": "Update all tasks", "ar": "Update all tasks"},
                        "description": {
                            "en": "Update all tasks",
                            "ar": "Update all tasks",
                        },
                    },
                    {
                        "code": "administration.self.service.update.task.status",
                        "name": {
                            "en": "Update status of the task",
                            "ar": "Update status of the task",
                        },
                        "description": {
                            "en": "Update status of the task",
                            "ar": "Update status of the task",
                        },
                    },
                    {
                        "code": "administration.self.service.create.task",
                        "name": {"en": "Create new task", "ar": "Create new task"},
                        "description": {
                            "en": "Create new task",
                            "ar": "Create new task",
                        },
                    },
                    {
                        "code": "administration.self.service.delete.task",
                        "name": {"en": "Delete task", "ar": "Delete task"},
                        "description": {"en": "Delete task", "ar": "Delete task"},
                    },
                ],
            },
            {
                "name": {"en": "Manage Committees", "ar": "Manage Committees"},
                "description": {"en": "Manage Committees", "ar": "Manage Committees"},
                "permissions": [
                    {
                        "code": "administration.committee.create",
                        "name": {"en": "Create", "ar": "Create"},
                        "description": {"en": "Create", "ar": "Create"},
                    },
                    {
                        "code": "administration.committee.update",
                        "name": {"en": "Update", "ar": "Update"},
                        "description": {"en": "Update", "ar": "Update"},
                    },
                    {
                        "code": "administration.committee.delete",
                        "name": {"en": "Delete", "ar": "Delete"},
                        "description": {"en": "Delete", "ar": "Delete"},
                    },
                    {
                        "code": "administration.committee.view",
                        "name": {"en": "View", "ar": "View"},
                        "description": {"en": "View", "ar": "View"},
                    },
                ],
                "triggers": [],
            },
            {
                "name": {"en": "Manage WorkFlow", "ar": "Manage WorkFlow"},
                "description": {"en": "Manage WorkFlow", "ar": "Manage WorkFlow"},
                "permissions": [
                    {
                        "code": "administration.workflow.create",
                        "name": {"en": "Create", "ar": "Create"},
                        "description": {"en": "Create", "ar": "Create"},
                    },
                    {
                        "code": "administration.workflow.update",
                        "name": {"en": "Update", "ar": "Update"},
                        "description": {"en": "Update", "ar": "Update"},
                    },
                    {
                        "code": "administration.workflow.delete",
                        "name": {"en": "Delete", "ar": "Delete"},
                        "description": {"en": "Delete", "ar": "Delete"},
                    },
                    {
                        "code": "administration.workflow.view",
                        "name": {"en": "View", "ar": "View"},
                        "description": {"en": "View", "ar": "View"},
                    },
                ],
                "triggers": [
                    {
                        "code": "administration.workflow.job.requisition",
                        "name": {"en": "Job Requisition", "ar": "Job Requisition"},
                        "description": {
                            "en": "Allow the user to create,edit job requisitions",
                            "ar": "Allow the user to create,edit job requisitions",
                        },
                    },
                    {
                        "code": "administration.workflow.general.requisition",
                        "name": {
                            "en": "General Requisition",
                            "ar": "General Requisition",
                        },
                        "description": {
                            "en": "Allow the user to create,edit general requisitions",
                            "ar": "Allow the user to create,edit general requisitions",
                        },
                    },
                    {
                        "code": "administration.workflow.offer.approval",
                        "name": {"en": "Offer Approval", "ar": "Offer Approval"},
                        "description": {
                            "en": "Allow the user to create,edit offer approvals",
                            "ar": "Allow the user to create,edit offer approvals",
                        },
                    },
                    {
                        "code": "administration.workflow.contract.approval",
                        "name": {"en": "Contract Approval", "ar": "Contract Approval"},
                        "description": {
                            "en": "Allow the user to create,edit contract approvals",
                            "ar": "Allow the user to create,edit contract approvals",
                        },
                    },
                    {
                        "code": "administration.workflow.rehire.approval",
                        "name": {"en": "Rehire Approval", "ar": "Rehire Approval"},
                        "description": {
                            "en": "Allow the user to create,edit rehire approvals",
                            "ar": "Allow the user to create,edit rehire approvals",
                        },
                    },
                    {
                        "code": "administration.workflow.relative.approval",
                        "name": {"en": "Relative Approval", "ar": "Relative Approval"},
                        "description": {
                            "en": "Allow the user to create,edit relative approvals",
                            "ar": "Allow the user to create,edit relative approvals",
                        },
                    },
                    {
                        "code": "administration.workflow.interview.approval",
                        "name": {
                            "en": "Interview Approval",
                            "ar": "Interview Approval",
                        },
                        "description": {
                            "en": "Allow the user to create,edit interview approvals",
                            "ar": "Allow the user to create,edit interview approvals",
                        },
                    },
                    {
                        "code": "administration.workflow.job.posting",
                        "name": {"en": "Job Posting", "ar": "Job Posting"},
                        "description": {
                            "en": "Allow the user to create,edit job posting",
                            "ar": "Allow the user to create,edit job posting",
                        },
                    },
                ],
            },
        ],
    },
    {
        "project": "python",
        "product": "Templates",
        "modules": [
            {
                "name": {"en": "Manage Email", "ar": "Manage Email"},
                "description": {"en": "Manage Email", "ar": "Manage Email"},
                "permissions": [
                    {
                        "code": "template.email.create",
                        "name": {"en": "create", "ar": "Create"},
                        "description": {"en": "Create", "ar": "Create"},
                    },
                    {
                        "code": "template.email.update",
                        "name": {"en": "Update", "ar": "Update"},
                        "description": {"en": "Update", "ar": "Update"},
                    },
                    {
                        "code": "template.email.delete",
                        "name": {"en": "Delete", "ar": "Delete"},
                        "description": {"en": "Delete", "ar": "Delete"},
                    },
                    {
                        "code": "template.email.view",
                        "name": {"en": "View", "ar": "View"},
                        "description": {"en": "View", "ar": "View"},
                    },
                ],
                "triggers": [],
            },
            {
                "name": {
                    "en": "Manage Evaluation Forms",
                    "ar": "Manage Evaluation Forms",
                },
                "description": {
                    "en": "Manage Evaluation Forms",
                    "ar": "Manage Evaluation Forms",
                },
                "permissions": [
                    {
                        "code": "template.evaluation.form.create",
                        "name": {"en": "create", "ar": "Create"},
                        "description": {"en": "Create", "ar": "Create"},
                    },
                    {
                        "code": "template.evaluation.form.update",
                        "name": {"en": "Update", "ar": "Update"},
                        "description": {"en": "Update", "ar": "Update"},
                    },
                    {
                        "code": "template.evaluation.form.delete",
                        "name": {"en": "Delete", "ar": "Delete"},
                        "description": {"en": "Delete", "ar": "Delete"},
                    },
                    {
                        "code": "template.evaluation.form.view",
                        "name": {"en": "View", "ar": "View"},
                        "description": {"en": "View", "ar": "View"},
                    },
                ],
                "triggers": [],
            },
            {
                "name": {"en": "Manage Offers", "ar": "Manage Offers"},
                "description": {"en": "Manage Offers", "ar": "Manage Offers"},
                "permissions": [
                    {
                        "code": "template.offers.create",
                        "name": {"en": "create", "ar": "Create"},
                        "description": {"en": "Create", "ar": "Create"},
                    },
                    {
                        "code": "template.offers.update",
                        "name": {"en": "Update", "ar": "Update"},
                        "description": {"en": "Update", "ar": "Update"},
                    },
                    {
                        "code": "template.offers.delete",
                        "name": {"en": "Delete", "ar": "Delete"},
                        "description": {"en": "Delete", "ar": "Delete"},
                    },
                    {
                        "code": "template.offers.view",
                        "name": {"en": "View", "ar": "View"},
                        "description": {"en": "View", "ar": "View"},
                    },
                ],
                "triggers": [],
            },
            {
                "name": {"en": "Manage Pipelines", "ar": "Manage Pipelines"},
                "description": {"en": "Manage Pipelines", "ar": "Manage Pipelines"},
                "permissions": [
                    {
                        "code": "template.pipelines.create",
                        "name": {"en": "create", "ar": "Create"},
                        "description": {"en": "Create", "ar": "Create"},
                    },
                    {
                        "code": "template.pipelines.update",
                        "name": {"en": "Update", "ar": "Update"},
                        "description": {"en": "Update", "ar": "Update"},
                    },
                    {
                        "code": "template.pipelines.delete",
                        "name": {"en": "Delete", "ar": "Delete"},
                        "description": {"en": "Delete", "ar": "Delete"},
                    },
                    {
                        "code": "template.pipelines.view",
                        "name": {"en": "View", "ar": "View"},
                        "description": {"en": "View", "ar": "View"},
                    },
                ],
                "triggers": [],
            },
            {
                "name": {"en": "Manage Questionnaire", "ar": "Manage Questionnaire"},
                "description": {
                    "en": "Manage Questionnaire",
                    "ar": "Manage Questionnaire",
                },
                "permissions": [
                    {
                        "code": "template.questionnaire.create",
                        "name": {"en": "create", "ar": "Create"},
                        "description": {"en": "Create", "ar": "Create"},
                    },
                    {
                        "code": "template.questionnaire.update",
                        "name": {"en": "Update", "ar": "Update"},
                        "description": {"en": "Update", "ar": "Update"},
                    },
                    {
                        "code": "template.questionnaire.delete",
                        "name": {"en": "Delete", "ar": "Delete"},
                        "description": {"en": "Delete", "ar": "Delete"},
                    },
                    {
                        "code": "template.questionnaire.view",
                        "name": {"en": "View", "ar": "View"},
                        "description": {"en": "View", "ar": "View"},
                    },
                ],
                "triggers": [],
            },
            {
                "name": {"en": "Manage Requirements", "ar": "Manage Requirements"},
                "description": {
                    "en": "Manage Requirements",
                    "ar": "Manage Requirements",
                },
                "permissions": [
                    {
                        "code": "template.requirements.create",
                        "name": {"en": "create", "ar": "Create"},
                        "description": {"en": "Create", "ar": "Create"},
                    },
                    {
                        "code": "template.requirements.update",
                        "name": {"en": "Update", "ar": "Update"},
                        "description": {"en": "Update", "ar": "Update"},
                    },
                    {
                        "code": "template.requirements.delete",
                        "name": {"en": "Delete", "ar": "Delete"},
                        "description": {"en": "Delete", "ar": "Delete"},
                    },
                    {
                        "code": "template.requirements.view",
                        "name": {"en": "View", "ar": "View"},
                        "description": {"en": "View", "ar": "View"},
                    },
                ],
                "triggers": [],
            },
            {
                "name": {"en": "Manage Score Card", "ar": "Manage Score Card"},
                "description": {"en": "Manage Score Card", "ar": "Manage Score Card"},
                "permissions": [
                    {
                        "code": "template.score.card.create",
                        "name": {"en": "create", "ar": "Create"},
                        "description": {"en": "Create", "ar": "Create"},
                    },
                    {
                        "code": "template.score.card.update",
                        "name": {"en": "Update", "ar": "Update"},
                        "description": {"en": "Update", "ar": "Update"},
                    },
                    {
                        "code": "template.score.card.delete",
                        "name": {"en": "Delete", "ar": "Delete"},
                        "description": {"en": "Delete", "ar": "Delete"},
                    },
                    {
                        "code": "template.score.card.view",
                        "name": {"en": "View", "ar": "View"},
                        "description": {"en": "View", "ar": "View"},
                    },
                ],
                "triggers": [],
            },
            {
                "name": {"en": "Manage Teams", "ar": "Manage Teams"},
                "description": {"en": "Manage Teams", "ar": "Manage Teams"},
                "permissions": [
                    {
                        "code": "template.teams.create",
                        "name": {"en": "create", "ar": "Create"},
                        "description": {"en": "Create", "ar": "Create"},
                    },
                    {
                        "code": "template.teams.update",
                        "name": {"en": "Update", "ar": "Update"},
                        "description": {"en": "Update", "ar": "Update"},
                    },
                    {
                        "code": "template.teams.delete",
                        "name": {"en": "Delete", "ar": "Delete"},
                        "description": {"en": "Delete", "ar": "Delete"},
                    },
                    {
                        "code": "template.teams.view",
                        "name": {"en": "View", "ar": "View"},
                        "description": {"en": "View", "ar": "View"},
                    },
                ],
                "triggers": [],
            },
        ],
    },
    {
        "project": "python",
        "product": "Visa",
        "modules": [
            {
                "name": {"en": "Manage Visa Request", "ar": "Manage Visa Request"},
                "description": {
                    "en": "Manage Visa Request",
                    "ar": "Manage Visa Request",
                },
                "permissions": [],
                "triggers": [
                    {
                        "code": "visa.request.reservation",
                        "name": {
                            "en": "Request Visa Reservation",
                            "ar": "Request Visa Reservation",
                        },
                        "description": {
                            "en": "Request new visa reservation from GR",
                            "ar": "Request new visa reservation from GR",
                        },
                    },
                    {
                        "code": "visa.request.reservation.view",
                        "name": {
                            "en": "View Visa Reservation",
                            "ar": "View Visa Reservation",
                        },
                        "description": {
                            "en": "View reservation request and view the reserved visas",
                            "ar": "View reservation request and view the reserved visas",
                        },
                    },
                    {
                        "code": "visa.request.reservation.confirm",
                        "name": {
                            "en": "Confirm Visa Reservation",
                            "ar": "Confirm Visa Reservation",
                        },
                        "description": {
                            "en": "Approve visa reservation request",
                            "ar": "Approve visa reservation request",
                        },
                    },
                    {
                        "code": "visa.request.reservation.cancel",
                        "name": {
                            "en": "Cancel Visa Reservation",
                            "ar": "Cancel Visa Reservation",
                        },
                        "description": {
                            "en": "Reject/Decline visa reservation request",
                            "ar": "Reject/Decline visa reservation request",
                        },
                    },
                    {
                        "code": "visa.request.reservation.onbehalf",
                        "name": {"en": "Reserve on Behalf", "ar": "Reserve on Behalf"},
                        "description": {
                            "en": "Request visa reservation on behalf of other users",
                            "ar": "Request visa reservation on behalf of other users",
                        },
                    },
                    {
                        "code": "visa.request.reservation.view.all",
                        "name": {
                            "en": "View All Reservation Requests",
                            "ar": "View All Reservation Requests",
                        },
                        "description": {
                            "en": "View all reservation requests that belong to other users",
                            "ar": "View all reservation requests that belong to other users",
                        },
                    },
                    {
                        "code": "visa.request.allocation",
                        "name": {
                            "en": "Request Visa Allocation",
                            "ar": "Request Visa Allocation",
                        },
                        "description": {
                            "en": "Request new visa allocation for a candidate",
                            "ar": "Request new visa allocation for a candidate",
                        },
                    },
                    {
                        "code": "visa.request.allocation.view",
                        "name": {
                            "en": "View Visa Allocation",
                            "ar": "View Visa Allocation",
                        },
                        "description": {
                            "en": "View allocation request",
                            "ar": "View allocation request",
                        },
                    },
                    {
                        "code": "visa.request.allocation.confirm",
                        "name": {
                            "en": "Confirm Visa Allocation",
                            "ar": "Confirm Visa Allocation",
                        },
                        "description": {
                            "en": "Approve visa allocation request",
                            "ar": "Approve visa allocation request",
                        },
                    },
                    {
                        "code": "visa.request.allocation.cancel",
                        "name": {
                            "en": "Cancel Visa Allocation",
                            "ar": "Cancel Visa Allocation",
                        },
                        "description": {
                            "en": "Reject/Withdraw visa allocation request",
                            "ar": "Reject/Withdraw visa allocation request",
                        },
                    },
                    {
                        "code": "visa.request.allocation.onbehalf",
                        "name": {
                            "en": "Allocate on Behalf",
                            "ar": "Allocate on Behalf",
                        },
                        "description": {
                            "en": "Request visa allocation on behalf of other users",
                            "ar": "Request visa allocation on behalf of other users",
                        },
                    },
                    {
                        "code": "visa.request.allocation.view.all",
                        "name": {
                            "en": "View All Allocation Requests",
                            "ar": "View All Allocation Requests",
                        },
                        "description": {
                            "en": "View all allocation requests that belong to other users",
                            "ar": "View all allocation requests that belong to other users",
                        },
                    },
                    {
                        "code": "visa.request.more.information",
                        "name": {
                            "en": "Request More Information",
                            "ar": "Request More Information",
                        },
                        "description": {
                            "en": "Request more information about the requests",
                            "ar": "Request more information about the requests",
                        },
                    },
                    {
                        "code": "visa.request.upload.attachments",
                        "name": {
                            "en": "Upload Attachments",
                            "ar": "Upload Attachments",
                        },
                        "description": {
                            "en": "Upload attachments in allocation/reservation requests",
                            "ar": "Upload attachments in allocation/reservation requests",
                        },
                    },
                    {
                        "code": "visa.request.view.attachments",
                        "name": {"en": "View Attachments", "ar": "View Attachments"},
                        "description": {
                            "en": "View attachments in allocation/reservation requests",
                            "ar": "View attachments in allocation/reservation requests",
                        },
                    },
                    {
                        "code": "visa.request.candidate.view",
                        "name": {
                            "en": "View Candidate Visa",
                            "ar": "View Candidate Visa",
                        },
                        "description": {
                            "en": "View the details of candidate visa",
                            "ar": "View the details of candidate visa",
                        },
                    },
                    {
                        "code": "visa.request.manage.status",
                        "name": {"en": "Manage Status", "ar": "Manage Status"},
                        "description": {
                            "en": "Move candidate visa across visa pipeline stages",
                            "ar": "Move candidate visa across visa pipeline stages",
                        },
                    },
                    {
                        "code": "visa.request.manage.pipeline",
                        "name": {"en": "Manage Pipeline", "ar": "Manage Pipeline"},
                        "description": {
                            "en": "Visa pipeline management",
                            "ar": "Visa pipeline management",
                        },
                    },
                    {
                        "code": "visa.request.mass.allocation",
                        "name": {"en": "Mass Allocation", "ar": "Mass Allocation"},
                        "description": {
                            "en": "Mass allocate visas for different applicants",
                            "ar": "Mass allocate visas for different applicants",
                        },
                    },
                ],
            },
            {
                "name": {"en": "Visa Blocks", "ar": "Visa Blocks"},
                "description": {"en": "Visa Blocks", "ar": "Visa Blocks"},
                "permissions": [
                    {
                        "code": "visa.blocks.create",
                        "name": {"en": "create", "ar": "Create"},
                        "description": {"en": "Create", "ar": "Create"},
                    },
                    {
                        "code": "visa.blocks.update",
                        "name": {"en": "Update", "ar": "Update"},
                        "description": {"en": "Update", "ar": "Update"},
                    },
                    {
                        "code": "visa.blocks.delete",
                        "name": {"en": "Delete", "ar": "Delete"},
                        "description": {"en": "Delete", "ar": "Delete"},
                    },
                    {
                        "code": "visa.blocks.view",
                        "name": {"en": "View", "ar": "View"},
                        "description": {"en": "View", "ar": "View"},
                    },
                ],
                "triggers": [],
            },
            {
                "name": {"en": "Visa Form", "ar": "Visa Form"},
                "description": {"en": "Visa Form", "ar": "Visa Form"},
                "permissions": [
                    {
                        "code": "visa.form.create",
                        "name": {"en": "create", "ar": "Create"},
                        "description": {"en": "Create", "ar": "Create"},
                    },
                    {
                        "code": "visa.form.update",
                        "name": {"en": "Update", "ar": "Update"},
                        "description": {"en": "Update", "ar": "Update"},
                    },
                    {
                        "code": "visa.form.delete",
                        "name": {"en": "Delete", "ar": "Delete"},
                        "description": {"en": "Delete", "ar": "Delete"},
                    },
                    {
                        "code": "visa.form.view",
                        "name": {"en": "View", "ar": "View"},
                        "description": {"en": "View", "ar": "View"},
                    },
                ],
                "triggers": [],
            },
            {
                "name": {"en": "Visa Lookup", "ar": "Visa Lookup"},
                "description": {"en": "Visa Lookup", "ar": "Visa Lookup"},
                "permissions": [
                    {
                        "code": "visa.lookup.create",
                        "name": {"en": "create", "ar": "Create"},
                        "description": {"en": "Create", "ar": "Create"},
                    },
                    {
                        "code": "visa.lookup.update",
                        "name": {"en": "Update", "ar": "Update"},
                        "description": {"en": "Update", "ar": "Update"},
                    },
                    {
                        "code": "visa.lookup.delete",
                        "name": {"en": "Delete", "ar": "Delete"},
                        "description": {"en": "Delete", "ar": "Delete"},
                    },
                    {
                        "code": "visa.lookup.view",
                        "name": {"en": "View", "ar": "View"},
                        "description": {"en": "View", "ar": "View"},
                    },
                ],
                "triggers": [],
            },
        ],
    },
]
