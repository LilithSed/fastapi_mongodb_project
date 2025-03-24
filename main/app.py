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