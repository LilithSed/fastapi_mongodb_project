# -*- coding: utf-8 -*-
import sentry_sdk
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from main.api.config.settings import settings
from main.api.routes import health
from main.api.routes.accounts import account
from main.api.routes.users import user

# Set URL prefix for API.
url_prefix = "/setup"

# Initialize the FastAPI application with settings and endpoints.
app = FastAPI(
    title="Setup API",
    version="1.0.0",
    openapi_url=f"{url_prefix}/openapi.json",
    docs_url=f"{url_prefix}/docs/swagger",
    redoc_url=f"{url_prefix}/docs/redoc",
)


# Mapping environments to their respective traces sample rates
traces_sample_rate = {"production": 0.2, "staging": 0.5}.get(settings.environment, None)
profiles_sample_rate = {"production": 1.0, "staging": 1.0}.get(
    settings.environment, None
)

# Check if the environment is either staging or production
if settings.environment in ["staging", "production"]:
    # Initialize Sentry SDK with appropriate settings
    sentry_sdk.init(
        dsn=settings.sentry_dsn,
        environment=settings.environment,
        # Set traces_sample_rate to 1.0 to capture 100%
        # of transactions for performance monitoring.
        traces_sample_rate=traces_sample_rate,
        # Set profiles_sample_rate to 1.0 to profile 100%
        # of sampled transactions.
        # We recommend adjusting this value in production.
        profiles_sample_rate=profiles_sample_rate,
    )

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router)

app.include_router(
    user.router,
    prefix=f"{url_prefix}/users",
)

app.include_router(
    account.router,
    prefix=f"{url_prefix}/account",
)



















app.include_router(
    candidate_mailbox.router,
    prefix=f"{url_prefix}/mailbox",
    dependencies=[Depends(auth.verify)],
)

app.include_router(
    webhooks.router,
    prefix=f"{url_prefix}/mailbox",
    dependencies=[Depends(auth.verify)],
)

app.include_router(
    meetings.router,
    prefix=f"{url_prefix}/meeting",
    dependencies=[Depends(auth.verify)],
)

app.include_router(
    job_requisitions.router,
    prefix=f"{url_prefix}/job-requisition",
    dependencies=[Depends(auth.verify)],
)

app.include_router(
    approvals.router,
    prefix=f"{url_prefix}/approvals",
    dependencies=[Depends(auth.verify)],
)


app.include_router(
    profiles_collections.router,
    prefix=f"{url_prefix}/profiles-collections",
    dependencies=[Depends(auth.verify)],
)

app.include_router(
    candidates.router,
    prefix=f"{url_prefix}/candidates",
    dependencies=[Depends(auth.verify)],
)

app.include_router(
    hiring_chat.router,
    prefix=f"{url_prefix}/hiring/chat",
    # dependencies=[Depends(auth.verify)],
)

app.include_router(
    tasks.router,
    prefix=f"{url_prefix}/task-management/tasks",
    dependencies=[Depends(auth.verify)],
)

app.include_router(
    onboarding_space.router,
    prefix=f"{url_prefix}/onboarding/space",
    dependencies=[Depends(auth.verify)],
)

app.include_router(
    onboarding_module.router,
    prefix=f"{url_prefix}/onboarding/module",
    dependencies=[Depends(auth.verify)],
)

app.include_router(
    onboarding_members.router,
    prefix=f"{url_prefix}/onboarding/members",
    dependencies=[Depends(auth.verify)],
)

app.include_router(
    onboarding_tasks.router,
    prefix=f"{url_prefix}/onboarding/tasks",
    dependencies=[Depends(auth.verify)],
)

app.include_router(
    onboarding_completion.router,
    prefix=f"{url_prefix}/onboarding/candidate/completion",
)

app.include_router(
    onboarding_employees.router,
    prefix=f"{url_prefix}/onboarding/employee/completion",
)

app.include_router(
    scorecard_candidates.router,
    prefix=f"{url_prefix}/scorecard/candidates",
    dependencies=[Depends(auth.verify)],
)

app.include_router(
    scorecard.router,
    prefix=f"{url_prefix}/scorecard",
    dependencies=[Depends(auth.verify)],
)

app.include_router(
    scorecard_candidates_evaluation.router,
    prefix=f"{url_prefix}/scorecard/evaluation",
    dependencies=[Depends(auth.verify)],
)

app.include_router(
    scorecard_candidates_decision.router,
    prefix=f"{url_prefix}/scorecard/decision",
    dependencies=[Depends(auth.verify)],
)

app.include_router(
    central_test.router,
    prefix=f"{url_prefix}/integrations/centraltest",
)

app.include_router(
    google_talent.router,
    prefix=f"{url_prefix}/integrations/google-talent",
)

app.include_router(
    talent.router,
    prefix=f"{url_prefix}/integrations/talent",
)

app.include_router(
    testlify.router,
    prefix=f"{url_prefix}/integrations/testlify",
)

app.include_router(
    google_analytics.router,
    prefix=f"{url_prefix}/integrations/google-analytics",
)

app.include_router(
    google_meet.router,
    prefix=f"{url_prefix}/integrations/google-meet",
)

app.include_router(
    indeed.router,
    prefix=f"{url_prefix}/integrations/indeed",
)

app.include_router(
    ms_teams.router,
    prefix=f"{url_prefix}/integrations/ms-teams",
)

app.include_router(
    upside.router,
    prefix=f"{url_prefix}/integrations/upside",
)

app.include_router(
    deel.router,
    prefix=f"{url_prefix}/integrations/deel",
)

app.include_router(
    zoom.router,
    prefix=f"{url_prefix}/integrations/zoom",
)

app.include_router(
    domain_routes.router,
    prefix=f"{url_prefix}/branding/domain",
    tags=["Domain Management"],
    # dependencies=[Depends(auth.verify)],
)


app.include_router(
    about_us_block_routes.router,
    prefix=f"{url_prefix}/branding/block",
    tags=["Block Management CRUDs"],
    # dependencies=[Depends(auth.verify)],
)

app.include_router(
    assignment_completion_block_routes.router,
    prefix=f"{url_prefix}/branding/block",
    tags=["Block Management CRUDs"],
    # dependencies=[Depends(auth.verify)],
)

app.include_router(
    candidate_verification_routes.router,
    prefix=f"{url_prefix}/branding/candidate-verification",
    tags=["Site and Workspace Configuration and Publishing"],
    # dependencies=[Depends(auth.verify)],
)

app.include_router(
    configuration_routes.router,
    prefix=f"{url_prefix}/branding/configuration",
    tags=["Site and Workspace Configuration and Publishing"],
    # dependencies=[Depends(auth.verify)],
)


app.include_router(
    categories_block_routes.router,
    prefix=f"{url_prefix}/branding/block",
    tags=["Block Management CRUDs"],
    # dependencies=[Depends(auth.verify)],
)

app.include_router(
    faq_block_routes.router,
    prefix=f"{url_prefix}/branding/block",
    tags=["Block Management CRUDs"],
    # dependencies=[Depends(auth.verify)],
)

app.include_router(
    footer_block_routes.router,
    prefix=f"{url_prefix}/branding/block",
    tags=["Block Management CRUDs"],
    # dependencies=[Depends(auth.verify)],
)

app.include_router(
    job_catalog_categories_block_routes.router,
    prefix=f"{url_prefix}/branding/block",
    tags=["Block Management CRUDs"],
    # dependencies=[Depends(auth.verify)],
)

app.include_router(
    job_catalog_search_and_filters_block_routes.router,
    prefix=f"{url_prefix}/branding/block",
    tags=["Block Management CRUDs"],
    # dependencies=[Depends(auth.verify)],
)

app.include_router(
    job_description_block_routes.router,
    prefix=f"{url_prefix}/branding/block",
    tags=["Block Management CRUDs"],
    # dependencies=[Depends(auth.verify)],
)

app.include_router(
    gallery_block_routes.router,
    prefix=f"{url_prefix}/branding/block",
    tags=["Block Management CRUDs"],
    # dependencies=[Depends(auth.verify)],
)

app.include_router(
    grid_block_routes.router,
    prefix=f"{url_prefix}/branding/block",
    tags=["Block Management CRUDs"],
    # dependencies=[Depends(auth.verify)],
)

app.include_router(
    hero_block_routes.router,
    prefix=f"{url_prefix}/branding/block",
    tags=["Block Management CRUDs"],
    # dependencies=[Depends(auth.verify)],
)


app.include_router(
    review_block_routes.router,
    prefix=f"{url_prefix}/branding/block",
    tags=["Block Management CRUDs"],
    # dependencies=[Depends(auth.verify)],
)

app.include_router(
    map_block_routes.router,
    prefix=f"{url_prefix}/branding/block",
    tags=["Block Management CRUDs"],
    # dependencies=[Depends(auth.verify)],
)

app.include_router(
    navbar_block_routes.router,
    prefix=f"{url_prefix}/branding/block",
    tags=["Block Management CRUDs"],
    # dependencies=[Depends(auth.verify)],
)


app.include_router(
    news_block_routes.router,
    prefix=f"{url_prefix}/branding/block",
    tags=["Block Management CRUDs"],
    # dependencies=[Depends(auth.verify)],
)

app.include_router(
    openings_block_routes.router,
    prefix=f"{url_prefix}/branding/block",
    tags=["Block Management CRUDs"],
    # dependencies=[Depends(auth.verify)],
)


app.include_router(
    rating_block_routes.router,
    prefix=f"{url_prefix}/branding/block",
    tags=["Block Management CRUDs"],
    # dependencies=[Depends(auth.verify)],
)

app.include_router(
    numbers_block_routes.router,
    prefix=f"{url_prefix}/branding/block",
    tags=["Block Management CRUDs"],
    # dependencies=[Depends(auth.verify)],
)

app.include_router(
    partners_block_routes.router,
    prefix=f"{url_prefix}/branding/block",
    tags=["Block Management CRUDs"],
    # dependencies=[Depends(auth.verify)],
)

app.include_router(
    quotes_block_routes.router,
    prefix=f"{url_prefix}/branding/block",
    tags=["Block Management CRUDs"],
    # dependencies=[Depends(auth.verify)],
)

app.include_router(
    cookies_block_routes.router,
    prefix=f"{url_prefix}/branding/block",
    tags=["Block Management CRUDs"],
    # dependencies=[Depends(auth.verify)],
)

app.include_router(
    social_media_block_routes.router,
    prefix=f"{url_prefix}/branding/block",
    tags=["Block Management CRUDs"],
    # dependencies=[Depends(auth.verify)],
)

app.include_router(
    stories_block_routes.router,
    prefix=f"{url_prefix}/branding/block",
    tags=["Block Management CRUDs"],
    # dependencies=[Depends(auth.verify)],
)

app.include_router(
    team_block_routes.router,
    prefix=f"{url_prefix}/branding/block",
    tags=["Block Management CRUDs"],
    # dependencies=[Depends(auth.verify)],
)

app.include_router(
    page_reference_routes.router,
    prefix=f"{url_prefix}/branding/reference",
    tags=["Page Reference CRUD and Publishing"],
    # dependencies=[Depends(auth.verify)],
)

app.include_router(
    page_routes.router,
    prefix=f"{url_prefix}/branding/page",
    tags=["Page Retrieval"],
    # dependencies=[Depends(auth.verify)],
)


app.include_router(
    general_block_routes.router,
    prefix=f"{url_prefix}/branding",
    tags=["General Block Sections"],
    # dependencies=[Depends(auth.verify)],
)

app.include_router(
    candidate_verification_block_routes.router,
    prefix=f"{url_prefix}/branding/block",
    tags=["Block Management CRUDs"],
    # dependencies=[Depends(auth.verify)],
)

app.include_router(
    benefits_block_routes.router,
    prefix=f"{url_prefix}/branding/block",
    tags=["Block Management CRUDs"],
    # dependencies=[Depends(auth.verify)],
)

app.include_router(
    rms.router,
    prefix=f"{url_prefix}/rms",
    # dependencies=[Depends(auth.verify)],
)

app.include_router(
    providers.router,
    prefix=f"{url_prefix}/provider",
    # dependencies=[Depends(auth.verify)],
)

app.include_router(
    members.router,
    prefix=f"{url_prefix}/provider/members",
    # dependencies=[Depends(auth.verify)],
)

app.include_router(
    initial_approval.router,
    prefix=f"{url_prefix}/initial-approval",
    # dependencies=[Depends(auth.verify)],
)

app.include_router(
    global_search.router,
    prefix=f"{url_prefix}/global-search",
    dependencies=[Depends(auth.verify)],
)

app.include_router(smtp_setting.router, prefix=f"{url_prefix}/smtp")

app.include_router(
    base_integrations.router,
    prefix=f"{url_prefix}/integrations",
    dependencies=[Depends(auth.verify)],
)

app.include_router(
    candidates_analytics.router,
    prefix=f"{url_prefix}/analytics/static",
    dependencies=[Depends(auth.verify)],
)

app.include_router(
    jobs_analytics.router,
    prefix=f"{url_prefix}/analytics/static",
    dependencies=[Depends(auth.verify)],
)

app.include_router(
    hiring_pipelines_analytics.router,
    prefix=f"{url_prefix}/analytics/static",
    dependencies=[Depends(auth.verify)],
)

app.include_router(
    tasks_analytics.router,
    prefix=f"{url_prefix}/analytics/static",
    dependencies=[Depends(auth.verify)],
)

app.include_router(
    vacancy_analytics.router,
    prefix=f"{url_prefix}/analytics/static",
    dependencies=[Depends(auth.verify)],
)

app.include_router(
    onboarding_analytics.router,
    prefix=f"{url_prefix}/analytics/static",
    dependencies=[Depends(auth.verify)],
)

app.include_router(
    scorecards_analytics.router,
    prefix=f"{url_prefix}/analytics/static",
    dependencies=[Depends(auth.verify)],
)

app.include_router(
    video_assessments_analytics.router,
    prefix=f"{url_prefix}/analytics/static",
    dependencies=[Depends(auth.verify)],
)

app.include_router(
    static_charts_templates.router,
    prefix=f"{url_prefix}/analytics/static",
    dependencies=[Depends(auth.verify)],
)

# job_requisition_analytics
app.include_router(
    job_requisition_analytics.router,
    prefix=f"{url_prefix}/analytics/static",
    dependencies=[Depends(auth.verify)],
)

# approval_analytics
app.include_router(
    approval_analytics.router,
    prefix=f"{url_prefix}/analytics/static",
    dependencies=[Depends(auth.verify)],
)

app.include_router(
    dynamic_metrics.router,
    prefix=f"{url_prefix}/analytics/dynamic",
    dependencies=[Depends(auth.verify)],
)

app.include_router(
    candidates_dynamic_analytics.router,
    prefix=f"{url_prefix}/analytics/dynamic",
    dependencies=[Depends(auth.verify)],
)

app.include_router(
    applicants_dynamic_analytics.router,
    prefix=f"{url_prefix}/analytics/dynamic",
    dependencies=[Depends(auth.verify)],
)

app.include_router(
    tasks_dynamic_analytics.router,
    prefix=f"{url_prefix}/analytics/dynamic",
    dependencies=[Depends(auth.verify)],
)

app.include_router(
    analytics_dashboards.router,
    prefix=f"{url_prefix}/analytics/dashboards",
    dependencies=[Depends(auth.verify)],
)

app.include_router(
    dashboard_rows.router,
    prefix=f"{url_prefix}/analytics/dashboard/rows",
    dependencies=[Depends(auth.verify)],
)

app.include_router(
    dashboard_insights.router,
    prefix=f"{url_prefix}/analytics/dashboard/insights",
    dependencies=[Depends(auth.verify)],
)

app.include_router(
    static_charts.router,
    prefix=f"{url_prefix}/analytics/dashboard/static-charts",
    dependencies=[Depends(auth.verify)],
)

app.include_router(
    text_charts.router,
    prefix=f"{url_prefix}/analytics/dashboard/text-charts",
    dependencies=[Depends(auth.verify)],
)

app.include_router(
    dynamic_charts.router,
    prefix=f"{url_prefix}/analytics/dashboard/dynamic-charts",
    dependencies=[Depends(auth.verify)],
)

# Candidate Side APIs
app.include_router(
    jobs.router,
    prefix=f"{url_prefix}/candidate-side",
)

app.include_router(
    candidate_profile.router,
    prefix=f"{url_prefix}/candidate-side",
)

app.include_router(
    system_notifications.router,
    prefix=f"{url_prefix}/system-notifications",
    # dependencies=[Depends(auth.verify)],
)
app.include_router(
    shared_resume.router,
    prefix=f"{url_prefix}/shared-resume",
)
app.include_router(
    job_tracker.router,
    prefix=f"{url_prefix}/job-tracker",
    dependencies=[Depends(auth.verify)],
)
