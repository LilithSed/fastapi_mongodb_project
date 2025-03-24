# -*- coding: utf-8 -*-
import json
import uuid

from datetime import datetime
from typing import  Any, Dict
from uuid import UUID

from fastapi import HTTPException, status

from main.api.models.users.user_requests import (
    CreateUserRequest,
    GetUserRequest,
    UpdateUserRequest,
    GetUsersRequest,
    UpdatePersonalSettingsRequest,
    BulkDeleteUsersRequest,
)
from main.api.helpers.utils import get_user_uuid, generate_password
from main.api.repositories.accounts.account_repository import AccountRepository
from main.api.repositories.users.user_repository import UserRepository
from main.api.validators.service_result import ServiceResult


class UserService:
    def __init__(self):
        self.account_repository = AccountRepository()
        self.user_repository = UserRepository()

    @staticmethod
    def check_is_registered(token: str) -> ServiceResult:
        """
        Check if the user is registered

        Args:

            token (str): The token of the user

        Returns:

            ServiceResult: A service result containing the status code and data.
        """
        user_uuid = get_user_uuid(token)

        if user_uuid:
            is_registered = True
        else:
            is_registered = False

        data = {"is_registered": is_registered}

        return ServiceResult(status_code=status.HTTP_200_OK, data=data)

    def create_user(
        self,
        item: CreateUserRequest,
        account_uuid: UUID,
        invited_by: UUID,
    ) -> ServiceResult:
        """
        Creates a new user, saves their information in the database,
            and adds them to Auth0.

        Args:
            item (CreateUserRequest): A Pydantic item containing information about
                the user to be created.
            account_uuid (UUID): The unique identifier of the account to
                which the user belongs.
            invited_by (UUID): The unique identifier of the user who
                invited the new user.

        Returns:
            ServiceResult: A ServiceResult object containing the
            status code and data.

        Steps:
        1. Generate a unique user UUID.
        2. Check if the email already exists; if so, return an error.
        3. Check if the code already exists within the specified account; if so,
            return an error.
        4. Create a dictionary representing the system user with provided information.
        5. Specify the user query with the generated user UUID.
        6. Specify the user data with information provided in the item.
        7. Save the user data in the database.
        8. Retrieve the created user from the database.
        9. Return a ServiceResult with the updated user data.
        """
        # Step 1: Generate a unique user UUID.
        user_uuid = uuid.uuid4()

        # Step 2: Check if the email already exists; if so, return an error.
        user = self.user_repository.get_user_by_email(email=item.email)
        if user:
                data = dict(
                    error_key="email",
                    key="user_email_exist",
                )

                return ServiceResult(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    data=data,
                )

        # Step 3: Check if the code already exists within the
        # specified account; if so, return an error.
        user = self.user_repository.validate_user_code(
            code=item.code,
            account_uuid=account_uuid,
        )
        if user:
            data = dict(
                error_key="code",
                key="code_exist",
            )

            return ServiceResult(
                status_code=status.HTTP_400_BAD_REQUEST,
                data=data,
            )

        # Step 4: Create a dictionary representing the system
        # user with provided information.
        system_user = dict(
            first_name=item.first_name.model_dump(),
            last_name=item.last_name.model_dump(),
            code=item.code,
            status=item.status,
            is_master=False,
            is_main_user=False,
        )

        # Step 5: Specify the user query with the generated user UUID.
        user_query = dict(
            uuid=user_uuid,
        )

        # Step 6: Specify the user data with information provided in the item.
        user_data = dict(
            email=item.email,
            password=generate_password(),
            account_uuid=account_uuid,
            type=item.type,
            provider_membership_type=item.provider_membership_type,
            system_user=system_user,
            invited_by=invited_by,
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )

        # Step 7: Save the user data in the database.
        self.user_repository.create_user(query=user_query, data=user_data)

        # Step 8: Retrieve the created user from the database.
        user = self.user_repository.get_user(
            uuid=user_uuid,
            status=None,
            invite_status=None,
        )

        # Step 9: Return a ServiceResult with the updated user data.
        return ServiceResult(
            status_code=status.HTTP_201_CREATED,
            data=user
        )

    def get_user(self, item: GetUserRequest) -> ServiceResult:
        """
        This service is used to view a user details

        Args:
            item (GetUserRequest): Pydantic item

        Return:
            ServiceResult
        """
        data = self.user_repository.get_user(
            uuid=item.uuid,
            invite_status=None,
        )

        user_projection = {
            "_id": 0,
            "system_user.first_name": 1,
            "system_user.last_name": 1,
        }

        # Get user data (Invited by) details
        if data:
            if "invited_by" in data:
                user_details = self.user_repository.get_user(
                    uuid=data["invited_by"], projection=user_projection
                )

                data.update({"invited_by": user_details})

        return ServiceResult(status_code=status.HTTP_200_OK, data=data)

    def update_user(
        self,
        item: UpdateUserRequest,
        account_uuid: UUID,
    ) -> ServiceResult:
        """
        Updates an existing user's information and saves the changes in the database.

        Args:
            item (UpdateUserRequest): A Pydantic item containing information
                to update the user.
            account_uuid (UUID): The unique identifier of the account to
                which the user belongs.

        Returns:
            ServiceResult: A ServiceResult object containing the
                status code and data.

        Steps:
        1. Check if the provided user UUID exists; if not, return an error.
        2. Check if the provided user code already exists within the
            specified account; if so, return an error.
        3. Create a dictionary representing the system user with updated information.
        4. Specify the user query with the provided user UUID.
        5. Specify the user data with updated information.
        6. Save the updated user data in the database.
        7. Retrieve the updated user from the database.
        8. Return a ServiceResult with the updated user data.
        """
        # Step 1: Check if the provided user UUID exists; if not, return an error.
        user = self.user_repository.get_user(
            uuid=item.uuid,
            status=None,
            invite_status=None,
        )
        if not user:
            data = dict(
                error_key="user_uuid",
                key="invalid_uuid",
            )

            return ServiceResult(
                status_code=status.HTTP_400_BAD_REQUEST,
                data=data,
            )

        is_master = False
        if "is_master" in user["system_user"]:
            is_master = user["system_user"]["is_master"]

        # Step 2: Check if the provided user code already exists within the
        # specified account; if so, return an error.
        user_code = self.user_repository.validate_user_code(
            code=item.code, account_uuid=account_uuid
        )

        if user_code and item.code != user["system_user"]["code"]:
            data = dict(
                error_key="code",
                key="code_exist",
            )

            return ServiceResult(
                status_code=status.HTTP_400_BAD_REQUEST,
                data=data,
            )

        # Step 3: Create a dictionary representing the system user
        # with updated information.
        system_user = dict(
            first_name=item.first_name.model_dump(),
            last_name=item.last_name.model_dump(),
            code=item.code,
            status=item.status,
            invite_status=item.invite_status,
            is_master=user["system_user"].get("is_master", False),
            is_main_user=user["system_user"].get("is_main_user", False),
        )

        # Step 4: Specify the user query with the provided user UUID.
        user_query = dict(
            uuid=item.uuid,
        )

        # Step 5: Specify the user data with updated information.
        user_data = dict(
            type=item.type,
            system_user=system_user,
            updated_at=datetime.now(),
        )

        # Step 6: Save the updated user data in the database.
        self.user_repository.update_user(query=user_query, data=user_data)

        # Step 7: Retrieve the updated user from the database.
        user = self.user_repository.get_user(uuid=item.uuid)

        # Step 8: Return a ServiceResult with the updated user data.
        return ServiceResult(
            status_code=status.HTTP_200_OK,
            data=user
        )

    def delete_user(self, item: GetUserRequest, account_uuid: UUID) -> ServiceResult:
        """
        Deletes a user from the database.

        Args:
            item (GetUserRequest): A Pydantic item containing information about
                the user to be deleted.
            account_uuid (UUID): The unique identifier of the account to
                which the user belongs.

        Returns:
            ServiceResult: A ServiceResult object containing the
                status code and data.

        Steps:
        1. Check if the provided user UUID exists; if not, return an error.
        2. Validate the user is not the main user.
        3. Delete the user from the database.
        4. Return a ServiceResult with the deleted user's UUID.
        """

        # Step 1: Check if the provided user UUID exists; if not, return an error.
        user = self.user_repository.get_user(
            uuid=item.uuid,
            status=None,
            invite_status=None,
        )
        if not user:
            data = dict(
                error_key="user_uuid",
                key="invalid_uuid",
            )

            return ServiceResult(
                status_code=status.HTTP_400_BAD_REQUEST,
                data=data,
            )

        system_user = user["system_user"]
        # Step 2: Validate the user is not the main user.
        if "is_main_user" in system_user and system_user["is_main_user"]:
            data = dict(
                error_key="uuid",
                key="delete_main_user",
            )

            return ServiceResult(
                status_code=status.HTTP_400_BAD_REQUEST,
                data=data,
            )

        # Step 3: Delete the user from the database.
        deleted_doc = self.user_repository.delete_user(user_uuid=item.uuid)

        # Step 4: Return a ServiceResult with the deleted user's UUID.
        data = {"user_uuid": item.uuid}
        return ServiceResult(status_code=status.HTTP_200_OK, data=data)

    def bulk_delete_users(
        self,
        item: BulkDeleteUsersRequest,
        account_uuid: UUID,
    ) -> ServiceResult:
        """
        Deletes multiple users with the specified details.

        Args:
            item (BulkDeleteUsersRequest): An object containing information for
                deleting the users.
            account_uuid (UUID): The unique identifier of the account to
                which the users belong.

        Returns:
            ServiceResult: Contains the result of the deletion process, including status code and data.

        Steps:
        1. Retrieve all users matching the given UUIDs from the repository.
        2. Identify UUIDs not found in the database.
        3. Identify users that cannot be deleted (main users).
        4. Prepare list of UUIDs to delete.
        5. Delete the valid users from the database.
        6. Return a ServiceResult with appropriate status code and data.
        """
        # Step 1: Retrieve all users matching the given UUIDs.
        users = self.user_repository.get_users(
            uuids=item.uuids,
            account_uuid=account_uuid,
            status=None,
            invite_status=None,
        )

        # Create a map of existing users with UUIDs as UUID objects.
        user_map = {UUID(str(u["uuid"])): u for u in users}

        # Step 2: Identify UUIDs not found in the database.
        existing_uuids = set(user_map.keys())  # Set of UUID objects
        requested_uuids = set(item.uuids)  # Set of UUID objects
        not_found_uuids = [str(uuid) for uuid in requested_uuids - existing_uuids]

        # Step 3: Identify users that cannot be deleted (main users).
        # Fetch system_user data for all users in bulk.
        user_system_data = {}

        # Collect user data
        for user_uuid, user in user_map.items():
            system_user = user.get("system_user", {})
            user_system_data[user_uuid] = system_user

        # Check for main users.
        main_user_uuids = [
            uuid
            for uuid, system_user in user_system_data.items()
            if system_user.get("is_main_user", False)
        ]

        # Step 4: Prepare list of UUIDs to delete.
        non_deletable_uuids = set(main_user_uuids)
        uuids_to_delete = list(existing_uuids - non_deletable_uuids)

        if not_found_uuids:
            data = {
                "error_key": "uuid",
                "key": "invalid_uuid",
            }

        if main_user_uuids:
            data = {
                "error_key": "uuid",
                "key": "delete_main_user",
            }

        # Step 5: Delete the valid users from the database
        if uuids_to_delete:
            self.user_repository.bulk_delete_users(user_uuids=uuids_to_delete)

        # Step 6: Prepare data to return
        data = {"user_uuid": [str(uuid) for uuid in uuids_to_delete]}

        return ServiceResult(status_code=status.HTTP_200_OK, data=data)

    def get_users(self, item: GetUsersRequest, account_uuid: UUID) -> ServiceResult:
        """
        Retrieves details for multiple users based on the provided parameters.

        Args:
            item (GetUsersRequest): A Pydantic item containing parameters for
                the user retrieval.
            account_uuid (UUID): The unique identifier of the account for which user
                details are requested.

        Returns:
            ServiceResult: An object containing the result of the user retrieval
                process, including status code and data.

        Steps:
        1. Get the total count of documents (users) based on the provided
            account UUID.
        2. Return a ServiceResult with the retrieved users, current page, limit,
            and total count.

        """
        # Step 1: Retrieve users from the repository using the provided
        # account UUID, page, and limit.
        results = self.user_repository.get_all_users(
            account_uuid=account_uuid,
            status=item.status,
            invite_status=item.invite_status,
            search_query=item.query,
            user_type=item.type,
            page=item.page,
            limit=item.limit
        )

        # Specify the projection.
        projection = {
            "_id": 0,
            "name": 1,
        }

        user_projection = {
            "_id": 0,
            "system_user.first_name": 1,
            "system_user.last_name": 1,
        }

        for _user in results["users"]:
            # Get user data (Invited by) details
            if "invited_by" in _user:
                user_details = self.user_repository.get_user(
                    uuid=_user["invited_by"], projection=user_projection
                )

                _user.update({"invited_by": user_details})

        # Step 2: Return a ServiceResult with the retrieved clusters,
        # current page, limit, and total count.
        data = {
            "result": results["users"],
            "current_page": item.page,
            "limit": item.limit,
            "total": results["count"],
        }

        return ServiceResult(status_code=status.HTTP_200_OK, data=data)

    def verify_user(self, email: str) -> ServiceResult:
        """
        Verifies and completes the user registration process.

        Args:
            email (str): The email address of the user to be verified.

        Returns:
            ServiceResult: An object containing the result of the verification process.

        """
        user = self.user_repository.get_user_by_email(email=email)

        if user:
            user_query = {"email": user["email"]}
            user_data = {
                "system_user.invite_status": "completed"
            }

            self.user_repository.update_many_users(query=user_query, data=user_data)

            # Get user data.
            user = self.user_repository.get_user(uuid=user["uuid"])

            return ServiceResult(
                status_code=status.HTTP_200_OK,
                data=user
            )

        return ServiceResult(status_code=status.HTTP_400_BAD_REQUEST)

    def update_personal_settings(
        self, item: UpdatePersonalSettingsRequest, user_uuid: UUID
    ):
        """
        Updates an existing user_info entry.

        Args:
            item (UpdatePersonalSettingsRequest): Information for the user_info entry to update.
            user_uuid (UUID): UUID of the user updating the entry.

        Returns:
            ServiceResult: Result of the update operation, containing the updated user_info data or error details.
        """
        # Step 1: Validate the user_info UUID.
        user_info = self.user_repository.get_user(uuid=item.uuid)
        if not user_info:
            data = dict(
                error_key="user_uuid",
                key="invalid_uuid",
            )

            return ServiceResult(
                status_code=status.HTTP_400_BAD_REQUEST,
                data=data,
            )
        existing_system_user = user_info.get("system_user", {})

        user_info_query = dict(uuid=item.uuid)
        system_user = dict(
            middle_name=item.middle_name,
            description=item.description,
            phone=item.phone,
            time_zone=item.time_zone
        )

        updated_system_user = {**existing_system_user, **system_user}
        user_data = dict(
            system_user=updated_system_user,
            updated_at=datetime.now(),
            updated_by=user_uuid,
        )

        self.user_repository.update_personal_settings(
            query=user_info_query,
            data=user_data,
        )

        _user_info = self.user_repository.get_user(uuid=item.uuid)

        # Return a ServiceResult with the created role data.
        return ServiceResult(status_code=status.HTTP_200_OK, data=_user_info)