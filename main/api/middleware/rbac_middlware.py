# -*- coding: utf-8 -*-
import jwt

from fastapi import Header, HTTPException, Request, Response, status
from fastapi.responses import ORJSONResponse

from main.api.factories.response_factory import get_translation_message
from main.api.helpers.utils import get_auth0_id
from main.api.repositories.users.user_repository import UserRepository
from main.api.repositories.roles.rbac_repository import RBACRepository


class RBACMiddleware:
    """
    This Middleware to authenticate and authorize user.

    Steps:
       1- Fetch user details from the token
       2- Check if user is active or not.
       3- Check if user has a permission to this endpoint or not.
    """

    def __init__(self, permission_code=None):
        self.user_details = None
        self.user_uuid = None
        self.user_repository = UserRepository()
        self.rbac_repository = RBACRepository()
        self.permission_code = permission_code

    async def __call__(
        self,
        request: Request,
        authorization: str = Header(...),
        accept_language: str = Header("en"),
        accept_account: str = Header(...),
    ):
        """
        This method will be called direct once we call
        RBACMiddleware()
        Args:
            request: HTTP request, used to get request METHOD and company uuid
            authorization: Bearer token, user local token send in each request

        """
        self.accept_language = accept_language

        try:
            # Fetch user data from the token
            user = self.get_user_details(authorization)

            if self.user_details is not None and user is False:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail=get_translation_message(
                        locale=self.accept_language, key="invalid_token"
                    ),
                )

            # Check if user is active or not, if user is Inactive return 401
            is_active = self.is_active()
            if not is_active:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail=get_translation_message(
                        locale=self.accept_language, key="inactive_user"
                    ),
                )

            # Check if user has a permission to this endpoint or not,
            # if not authorized return 401
            if self.permission_code:
                # Assign company_uuid based on request method
                if request.method == "GET":
                    company_uuid = request.query_params.get("company_uuid")
                else:
                    data = await request.json()
                    company_uuid = data.get("company_uuid")

                authorized = self.check_permission(
                    company_uuid=company_uuid,
                )

                if not authorized:
                    raise HTTPException(
                        status_code=status.HTTP_401_UNAUTHORIZED,
                        detail=get_translation_message(
                            locale=self.accept_language, key="unauthorized"
                        ),
                    )

        except (RuntimeError, KeyError, AttributeError, TypeError) as e:
            return Response(content=str(e), status_code=500)

    def get_user_details(self, authorization: str) -> bool | ORJSONResponse:
        """
        Fetch user details from the token

        Args:
            authorization (str): user access token.

        Returns:
            bool | ORJSONResponse
        """
        try:
            auth0_id = get_auth0_id(authorization)
            auth0_id = auth0_id.split("|")[-1]

            document = self.user_repository.get_user_details(auth0_id=auth0_id)

            if document:
                self.user_details = document
                self.user_uuid = document["uuid"]
                return True

            return False

        except (jwt.exceptions.ExpiredSignatureError, jwt.exceptions.DecodeError):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=get_translation_message(
                    locale=self.accept_language, key="invalid_token"
                ),
            )

    def is_active(self) -> bool:
        """
        Check if user is active or not, from user collection.

        Returns:
          bool
        """
        try:
            # Check if the user is active
            document = self.user_repository.is_active_user(user_uuid=self.user_uuid)

            return document

        except KeyError as e:
            raise HTTPException(detail=str(e), status_code=500)

    def check_permission(self, company_uuid: str):
        """
        Check if user has a permission to this endpoint or not.
        First we will check if the user is master user.

        Args:
            company_uuid (str): The Company UUID

        Returns:
            bool
        """
        try:

            # Get user access data
            user_data = self.user_repository.get_user(
                uuid=self.user_uuid,
            )

            if user_data:
                system_user = user_data["system_user"]
                roles = []
                # If the user is master return True without check any permission
                if "is_master" in system_user:
                    return True

                # Get the user access
                access = user_data["system_user"]["access"]
                for _access in access:
                    # Get the roles for the company_uuid if it's not None
                    if company_uuid:
                        if str(_access["company_uuid"]) == company_uuid:
                            roles = _access["roles"]
                            break
                    else:
                        # If there's no company_uuid then check the permission codes
                        # for the whole access. This case happens when we have
                        # functionalities on account level
                        roles.extend(_access["roles"])

                # Loop over the roles to get the permission_codes
                for _role in roles:
                    role_details = self.rbac_repository.get_rbac(rbac_uuid=_role)
                    if role_details:
                        permission_codes = role_details["permission_codes"]
                        # Check if the permission code exist in permission_codes list
                        if self.permission_code in permission_codes:
                            return True
            return False

        except KeyError as e:
            raise HTTPException(detail=str(e), status_code=500)
