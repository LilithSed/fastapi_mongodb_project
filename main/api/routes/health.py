# -*- coding: utf-8 -*-
from fastapi import APIRouter
from fastapi.responses import ORJSONResponse

router = APIRouter(tags=["Health Checks"])


@router.get("/")
async def root() -> ORJSONResponse:
    """
    Provides a simple health check at the root path.

    This endpoint is a basic health check to quickly determine if the service is up and running.

    Returns:
        ORJSONResponse: A JSON response with a 200 status code.
    """
    return ORJSONResponse(status_code=200, content=None)


@router.get("/healthz/liveness")
async def healthz_liveness() -> ORJSONResponse:
    """
    Provides a liveness probe for Kubernetes on Google Cloud Platform (GCP).

    This endpoint is used by Kubernetes to determine if the pod is running and able to serve
    requests.

    It should return a success code if the pod is up, regardless of the state of individual
    services or databases.

    Returns:
        ORJSONResponse: A JSON response with a 200 status code.
    """
    return ORJSONResponse(status_code=200, content=None)


@router.get("/healthz/readiness")
async def healthz_readiness() -> ORJSONResponse:
    """
    Provides a readiness probe for Kubernetes on Google Cloud Platform (GCP).

    This endpoint is used by Kubernetes to determine if the pod is ready to start accepting traffic.
    It should return a success code only if all required services, databases, and other dependencies
    are successfully running and initialized.

    Returns:
        ORJSONResponse: A JSON response with a 200 status code.
    """
    return ORJSONResponse(status_code=200, content=None)
