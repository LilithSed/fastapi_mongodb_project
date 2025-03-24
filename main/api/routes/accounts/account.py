# -*- coding: utf-8 -*-
from fastapi import APIRouter, Depends, Header, status
from fastapi.responses import ORJSONResponse

from main.api.factories.response_factory import ResponseFactory, get_response_factory
from main.api.helpers.utils import get_user_uuid
from main.api.models.accounts.account_requests import CreateAccountRequest
from main.api.services.accounts.account_service import AccountService

router = APIRouter(tags=["Accounts APIs"])


@router.post("/")
async def setup_account(
    item: CreateAccountRequest,
    authorization: str = Header(..., description="User authentication token"),
    account_service: AccountService = Depends(AccountService),
    response_factory: ResponseFactory = Depends(get_response_factory),
) -> ORJSONResponse:
    """
    This endpoint to set up new account.

    Returns:
        ORJSONResponse
    """
    try:
        # Get user_uuid.
        user_uuid = get_user_uuid(authorization)

        service_result = account_service.create_account(
            item=item, user_uuid=user_uuid
        )

        if service_result.status_code == status.HTTP_400_BAD_REQUEST:
            return response_factory.bad_request(data=service_result.data)

        return response_factory.created(service_result.data)

    except (TypeError, KeyError, RuntimeError, ValueError, NameError) as exc:
        return response_factory.internal_server_error(exc)


@router.get("/details")
async def get_account_details(
    authorization: str = Header(..., description="User authentication token"),
    account_service: AccountService = Depends(AccountService),
    response_factory: ResponseFactory = Depends(get_response_factory),
) -> ORJSONResponse:
    """
    This endpoint to Get the details of the account based on the token provided.

    Returns:

        ORJSONResponse
    """
    try:
        # Get user_uuid.
        user_uuid = get_user_uuid(authorization)

        service_result = account_service.get_account_details(user_uuid=user_uuid)
        return response_factory.single_data(service_result.data)

    except (TypeError, KeyError, RuntimeError, ValueError, NameError) as exc:
        return response_factory.internal_server_error(exc)
