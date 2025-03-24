# -*- coding: utf-8 -*-
import os
from typing import Optional

from pydantic_settings import BaseSettings


class MonitoringEnvironment(BaseSettings):
    """
    Configuration settings for monitoring services.

    Attributes:
        enable_google_cloud_logging (bool): Flag to enable Google Cloud Logging,
            fetched from environment variable ENABLE_GOOGLE_CLOUD_LOGGING. Defaults to False.
        enable_prometheus_metrics (bool): Flag to enable Prometheus metrics,
            fetched from environment variable ENABLE_PROMETHEUS_METRICS. Defaults to False.
    """

    enable_google_cloud_logging: bool = bool(
        os.getenv("ENABLE_GOOGLE_CLOUD_LOGGING", "0")
    )
    enable_prometheus_metrics: bool = bool(os.getenv("ENABLE_PROMETHEUS_METRICS", "0"))


class Settings(BaseSettings):
    """
    Configuration class to manage application settings, sourced from environment
        variables.

    Attributes:
        project_id (str): The ID associated with the project.
        mongo_uri (str): The URI for the MongoDB server.
        db_name (str): The name of the database.
        sentry_dsn (str): The DSN used for connecting to Sentry for error logging.
        environment (str): The environment in which the application is running
            (e.g., production, staging).

    Note:
        All attributes are sourced from environment variables during
            class instantiation.
    """
    project_id: str = os.getenv("PROJECT_ID")
    mongo_uri: str = os.getenv("DB_SRV_URI")
    db_name: str = os.getenv("DB_NAME")
    environment: str = os.getenv("ENVIRONMENT")
    sentry_dsn: Optional[str] = os.getenv("SENTRY_DSN")
    server_env: Optional[str] = os.getenv("SERVER_ENV", "local")
    monitoring: MonitoringEnvironment = MonitoringEnvironment()

    backend_base_url: str = os.getenv("BACKEND_BASE_URL")


settings = Settings()
