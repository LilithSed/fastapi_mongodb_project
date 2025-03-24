# -*- coding: utf-8 -*-
from uuid import UUID

from fastapi import APIRouter, Depends, Header, Query, Request, status
from fastapi.responses import ORJSONResponse

from main.api.helpers.utils import get_user_uuid
from main.api.factories.response_factory import get_response_factory, ResponseFactory
from main.api.middleware.rbac_middlware import RBACMiddleware
from main.api.models.users.user_requests import (
    BulkDeleteUsersRequest,
    CreateUserRequest,
    GetUserRequest,
    GetUsersRequest,
    UpdatePersonalSettingsRequest,
    UpdateUserRequest
)
from main.api.services.users.user_service import UserService

router = APIRouter(tags=["Users APIs"])


@router.get("/registered")
async def check_is_registered(
    authorization: str = Header(..., description="User authentication token"),
    user_service: UserService = Depends(UserService),
    response_factory: ResponseFactory = Depends(get_response_factory),
) -> ORJSONResponse:
    """
    This endpoint is a basic check if the user is registered or not.

    Returns:

        ORJSONResponse
    """
    try:
        service_result = user_service.check_is_registered(authorization)
        return response_factory.single_data(service_result.data)

    except (TypeError, KeyError, RuntimeError, ValueError) as exc:
        return response_factory.internal_server_error(exc)


@router.post("/", dependencies=[Depends(RBACMiddleware("administration.user.create"))])
async def create_user(
    item: CreateUserRequest,
    authorization: str = Header(..., description="User authentication token"),
    accept_account: UUID = Header(..., description="The UUID of the account"),
    user_service: UserService = Depends(UserService),
    response_factory: ResponseFactory = Depends(get_response_factory),
    full_payload: bool = Query(False, description="Whether to return data"),
) -> ORJSONResponse:
    """
    This endpoint is a basic check if the user is registered or not.

    Returns:
        ORJSONResponse
    """
    try:
        # Get user_uuid.
        user_uuid = get_user_uuid(authorization)

        service_result = user_service.create_user(
            item=item,
            account_uuid=accept_account,
            invited_by=user_uuid
        )

        if service_result.status_code == status.HTTP_400_BAD_REQUEST:
            return response_factory.bad_request(data=service_result.data)

        return response_factory.created(service_result.data, full_payload)

    except (TypeError, KeyError, RuntimeError, ValueError) as exc:
        return response_factory.internal_server_error(exc)


@router.get("/view", dependencies=[Depends(RBACMiddleware("administration.user.view"))])
async def get_user(
    item: GetUserRequest = Depends(),
    user_service: UserService = Depends(UserService),
    response_factory: ResponseFactory = Depends(get_response_factory),
) -> ORJSONResponse:
    """
    This endpoint to get user details.

    Returns:

        ORJSONResponse
    """
    try:
        service_result = user_service.get_user(item=item)
        return response_factory.single_data(service_result.data)

    except (TypeError, KeyError, RuntimeError, ValueError) as exc:
        return response_factory.internal_server_error(exc)


@router.put("/", dependencies=[Depends(RBACMiddleware("administration.user.update"))])
async def update_user(
    item: UpdateUserRequest,
    accept_account: UUID = Header(..., description="The UUID of the account"),
    user_service: UserService = Depends(UserService),
    response_factory: ResponseFactory = Depends(get_response_factory),
    full_payload: bool = Query(False, description="Whether to return data"),
) -> ORJSONResponse:
    """
    This endpoint to update user data.

    Returns:
        ORJSONResponse
    """
    try:
        service_result = user_service.update_user(
            item=item, account_uuid=accept_account
        )

        if service_result.status_code == status.HTTP_400_BAD_REQUEST:
            return response_factory.bad_request(data=service_result.data)

        return response_factory.updated(service_result.data, full_payload)

    except (TypeError, KeyError, RuntimeError, ValueError, NameError) as exc:
        return response_factory.internal_server_error(exc)


@router.delete(
    "/", dependencies=[Depends(RBACMiddleware("administration.user.delete"))]
)
async def delete_user(
    item: GetUserRequest,
    accept_account: UUID = Header(..., description="The UUID of the account"),
    user_service: UserService = Depends(UserService),
    response_factory: ResponseFactory = Depends(get_response_factory),
    full_payload: bool = Query(False, description="Whether to return data"),
) -> ORJSONResponse:
    """
    This endpoint to delete user details.

    Returns:
        ORJSONResponse
    """
    try:
        service_result = user_service.delete_user(
            item=item, account_uuid=accept_account
        )

        if service_result.status_code == status.HTTP_400_BAD_REQUEST:
            return response_factory.bad_request(data=service_result.data)

        return response_factory.deleted(service_result.data, full_payload)

    except (TypeError, KeyError, RuntimeError, ValueError) as exc:
        return response_factory.internal_server_error(exc)


@router.delete(
    "/bulk", dependencies=[Depends(RBACMiddleware("administration.user.delete"))]
)
async def bulk_delete_users(
    item: BulkDeleteUsersRequest,
    accept_account: UUID = Header(..., description="The UUID of the account"),
    user_service: UserService = Depends(UserService),
    response_factory: ResponseFactory = Depends(get_response_factory),
    full_payload: bool = Query(False, description="Whether to return data"),
) -> ORJSONResponse:
    """
    This endpoint allows bulk deletion of users.

    Returns:

        ORJSONResponse
    """
    try:
        service_result = user_service.bulk_delete_users(
            item=item, account_uuid=accept_account
        )

        if service_result.status_code == status.HTTP_400_BAD_REQUEST:
            return response_factory.bad_request(data=service_result.data)

        return response_factory.deleted(service_result.data, full_payload)

    except (TypeError, KeyError, RuntimeError, ValueError) as exc:
        return response_factory.internal_server_error(exc)


@router.get("/", dependencies=[Depends(RBACMiddleware("administration.user.view"))])
async def get_users(
    item: GetUsersRequest = Depends(),
    accept_account: UUID = Header(..., description="The UUID of the account"),
    response_factory: ResponseFactory = Depends(get_response_factory),
    user_service: UserService = Depends(UserService),
):
    """
    This service is used to retrieve all users
    """
    try:
        service_result = user_service.get_users(
            item=item, account_uuid=accept_account
        )

        return response_factory.list_data(**service_result.data)
    except (TypeError, KeyError, RuntimeError, ValueError) as exc:
        return response_factory.internal_server_error(exc)


@router.post("/verify")
async def verify_user(
    request: Request,
    user_service: UserService = Depends(UserService),
    response_factory: ResponseFactory = Depends(get_response_factory),
    full_payload: bool = Query(False, description="Whether to return data"),
) -> ORJSONResponse:
    """
    This endpoint verify user details.

    Returns:

        ORJSONResponse
    """
    try:
        body = await request.json()
        email = body["params"]["data"]["email"]

        service_result = user_service.verify_user(email=email)

        if service_result.status_code == status.HTTP_400_BAD_REQUEST:
            return response_factory.bad_request(data=service_result.data)

        return response_factory.updated(service_result.data, full_payload)

    except (TypeError, KeyError, RuntimeError, ValueError, NameError) as exc:
        return response_factory.internal_server_error(exc)


@router.put("/personal-settings")
async def update_personal_settings(
    item: UpdatePersonalSettingsRequest,
    authorization: str = Header(..., description="User authentication token"),
    personal_settings_service: UserService = Depends(UserService),
    response_factory: ResponseFactory = Depends(get_response_factory),
    full_payload: bool = Query(False, description="Whether to return data"),
) -> ORJSONResponse:
    """
    This endpoint to update User's Personal Info data.

    Returns:

        ORJSONResponse
    """
    try:
        # Get user_uuid
        user_uuid = get_user_uuid(authorization)

        service_result = personal_settings_service.update_personal_settings(
            item=item, user_uuid=user_uuid
        )
        if service_result.status_code == status.HTTP_400_BAD_REQUEST:
            return response_factory.bad_request(data=service_result.data)

        return response_factory.updated(service_result.data, full_payload)

    except (
        TypeError,
        KeyError,
        RuntimeError,
        ValueError,
        NameError,
        AttributeError,
    ) as exc:
        return response_factory.internal_server_error(exc)
