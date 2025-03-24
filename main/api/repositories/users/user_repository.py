# -*- coding: utf-8 -*-
from typing import Any, Dict, List, Literal, Optional
from uuid import UUID

from main.api.classes.database import MongoDBConnection


class UserRepository(MongoDBConnection):
    """
    This Class implements the User repository
    """

    def __init__(self):
        super().__init__()

        # Load collection
        self.user_cl = self.get_mongo_collection("users")

    def create_user(self, query: Dict[str, Any], data: Dict[str, Any]) -> None:
        """
        Create a new User in the database.

        Args:
            query (Dict[str, Any]): A query that matches the document to update.
            data (Dict[str, Any]): The modifications to apply.

        Returns:
            None
        """
        self.user_cl.update_one(
            query,
            {"$set": {**data}},
            upsert=True,
        )

    def update_user(
        self,
        query: Dict[str, Any],
        data: Dict[str, Any] = None,
        update_operation: Optional[Dict[str, Any]] = None,
    ) -> None:
        """
        Update User in the database.

        Args:
            query (Dict[str, Any]): A query that matches the document to update.
            data (Dict[str, Any]): The modifications to apply.
            update_operation: (Optional[Dict[str, Any]): update dictionary using when
              we use like "$push" operation instead of "$set" .

        Returns:
            None
        """
        if update_operation:
            update = update_operation
        else:
            update = {"$set": {**data}}

        self.user_cl.update_one(
            filter=query,
            update=update,
            upsert=False,
        )

    def update_many_users(
        self,
        query: Dict[str, Any],
        data: Dict[str, Any] = None,
        update_operation: Optional[Dict[str, Any]] = None,
    ) -> None:
        """
        Update Users in the database.

        Args:
            query (Dict[str, Any]): A query that matches the document to update.
            data (Dict[str, Any]): The modifications to apply.
            update_operation: (Optional[Dict[str, Any]): update dictionary using when
              we use like "$push" operation instead of "$set" .

        Returns:
            None
        """
        if update_operation:
            update = update_operation
        else:
            update = {"$set": {**data}}

        self.user_cl.update_many(
            filter=query,
            update=update,
            upsert=False,
        )

    def get_user(
        self,
        uuid: UUID,
        account_uuid: UUID = None,
        projection: Optional[Dict[str, Any]] = None,
        status: Optional[bool] = True,
        invite_status: Optional[str] = "completed",
    ) -> Optional[dict[str, Any]]:
        """
        Get the name of user based on uuid

        Args:
            uuid: The unique identifier of the user
            account_uuid (UUID): Unique Account identifier.
            projection (Dict[str, Any]): What to project from the DB
            status (Optional[bool]): Indicates if the user is active or not
            invite_status (Optional[str])

        Return:
            dict( en="values", ar="values")
        """
        query = {"uuid": uuid}

        if account_uuid:
            query.update({"account_uuid": account_uuid})

        if status is not None:
            query.update({"system_user.status": status})

        if invite_status is not None:
            query.update({"system_user.invite_status": invite_status})

        if not projection:
            # Remove _id from the result
            projection = {"_id": 0}

        elif "_id" not in projection:
            projection.update({"_id": 0})

        document = self.user_cl.find_one(query, projection)

        return document

    def get_users(
        self,
        uuids: List[UUID],
        account_uuid: UUID = None,
        projection: Optional[Dict[str, Any]] = None,
        status: Optional[bool] = True,
        invite_status: Optional[str] = "completed",
    ) -> List[Dict[str, Any]]:
        """
        Get users based on a list of UUIDs.

        Args:
            uuids (List[UUID]): List of user UUIDs.
            account_uuid (UUID): Unique Account identifier.
            projection (Dict[str, Any]): Fields to project from the DB.
            status (Optional[bool]): Indicates if the user is active or not.
            invite_status (Optional[str])

        Returns:
            List[Dict[str, Any]]: List of user documents.
        """
        query = {"uuid": {"$in": uuids}}

        if account_uuid:
            query.update({"account_uuid": account_uuid})

        if status is not None:
            query.update({"system_user.status": status})

        if invite_status is not None:
            query.update({"system_user.invite_status": invite_status})

        if not projection:
            projection = {"_id": 0}

        cursor = self.user_cl.find(query, projection)
        documents = list(cursor)

        return documents

    def get_user_roles(self, uuid: UUID, company_uuid: UUID):
        """
        Retrieves roles of a user for a specific company.

        Args:
            uuid (UUID): UUID of the user.
            company_uuid (UUID): UUID of the company.

        Returns:
            Dict[str, Any]: Dictionary containing user roles information.
        """
        query = {"uuid": uuid}
        projection = {
            "_id": 0,
            "is_master": "$system_user.is_master",
            # Project the list of roles' UUIDs
            "roles": {
                "$arrayElemAt": [
                    {
                        "$map": {
                            "input": {
                                "$filter": {
                                    "input": "$system_user.access",
                                    "as": "item",
                                    "cond": {
                                        "$eq": ["$$item.company_uuid", company_uuid]
                                    },
                                }
                            },
                            "as": "filtered_access",
                            "in": "$$filtered_access.roles",
                        }
                    },
                    0,
                ],
            },
        }

        result = self.user_cl.find_one(filter=query, projection=projection)
        if isinstance(result, dict):
            if "is_master" not in result:
                result["is_master"] = False

            if "roles" not in result:
                result["roles"] = []

        else:
            result = {"is_master": False, "roles": []}

        return result

    def get_user_by_type(
        self, uuid: UUID, type: str, projection: Optional[Dict[str, Any]] = None
    ) -> Optional[dict[str, Any]]:
        """
        Get the name of user based on uuid and type

        Args:
            uuid (UUID): The unique identifier of the user
            type (str): The user type
            projection (Dict[str, Any]): What to project from the DB

        Return:
            dict( en="values", ar="values")
        """
        query = {"uuid": uuid, "type": type}

        if not projection:
            # Remove _id from the result
            projection = {"_id": 0}

        document = self.user_cl.find_one(query, projection)

        return document

    def get_user_name(self, uuid: UUID) -> Optional[dict[str, Any]]:
        """
        Get the name of user based on uuid

        Args:
            uuid: The unique identifier of the user

        Return:
            dict( en="values", ar="values")
        """
        query = {"uuid": uuid}

        projection = {
            "_id": 0,
            "first_name": "$system_user.first_name",
            "last_name": "$system_user.last_name",
        }

        document = self.user_cl.find_one(query, projection)
        return document

    def get_user_by_account_uuid(
        self,
        uuid: UUID,
        account_uuid: UUID,
        projection: Optional[Dict[str, Any]] = None,
    ) -> Optional[dict[str, Any]]:
        """
        Get the name of user based on uuid

        Args:
            uuid(UUID): The unique identifier of the user
            account_uuid (UUID): The unique identifier of the account UUID
            projection (Dict[str, Any]): What to project from the DB

        Return:
            dict( en="values", ar="values")
        """
        query = {"uuid": uuid, "account_uuid": account_uuid}

        if not projection:
            # Remove _id from the result
            projection = {"_id": 0}

        document = self.user_cl.find_one(query, projection)

        return document

    def get_main_user(self, account_uuid: UUID) -> Optional[dict[str, Any]]:
        """
        Get the name of user based on uuid

        Args:
            account_uuid: The unique identifier of the account
        Return:
            dict( en="values", ar="values")
        """
        query = {"account_uuid": account_uuid, "system_user.is_main_user": True}

        projection = {"_id": 0}

        document = self.user_cl.find_one(query, projection)

        return document

    def get_user_by_email(
        self,
        email: str,
        account_uuid: UUID = None,
    ) -> Optional[dict[str, Any]]:
        """
        Get the name of user based on email

        Args:
            email: The user email
            account_uuid (UUID): Account UUID.
        Return:
            dict( en="values", ar="values")

        Notes:
            - if any condition is added to this function, it will affect
              invite_provider function.
        """
        query = {"email": email}

        if account_uuid:
            query.update({"account_uuid": account_uuid})

        projection = {
            "_id": 0,
        }
        document = self.user_cl.find_one(query, projection)

        return document

    def get_users_be_email(
        self,
        email: str,
        account_uuid: UUID = None,
        projection: Optional[Dict[str, Any]] = None,
        status: Optional[bool] = True,
        invite_status: Optional[str] = "completed",
    ) -> Optional[List[dict[str, Any]]]:
        """
        Get users details be user email

        Args:
            email: The user email
            account_uuid (UUID): Unique Account identifier.
            projection (Dict[str, Any]): What to project from the DB
            status (Optional[bool]): Indicates if the user is active or not
            invite_status (Optional[str])

        Return:
            list
        """
        query = {"email": email}

        if account_uuid:
            query.update({"account_uuid": account_uuid})

        if status is not None:
            query.update({"system_user.status": status})

        if invite_status is not None:
            query.update({"system_user.invite_status": invite_status})

        if not projection:
            # Remove _id from the result
            projection = {"_id": 0}

        elif "_id" not in projection:
            projection.update({"_id": 0})

        cursor = self.user_cl.find(query, projection)
        documents = list(cursor)

        return documents

    def get_user_in_different_accounts_by_email(
        self,
        email: str,
        account_uuid: UUID,
        provider_membership_types: List[Literal["admin", "member"]],
        employee_type: Literal["employee", "agency", "university"],
    ) -> Optional[dict[str, Any]]:
        """
        Get the user on another accounts if it has the same email
        This is used for agency.

        Args:
            email: The user email
            account_uuid (UUID): Account UUID.
            provider_membership_types (List[Literal["admin", "member"]]).
            employee_type (str): employee, agency, university
        Return:
            dict( en="values", ar="values")

        Notes:
            - if any condition is added to this function, it will affect
              invite_provider function.
        """
        or_query = [{"provider_membership_type": {"$in": provider_membership_types}}]
        if employee_type:
            or_query.append({"type": employee_type})

        query = {"email": email, "account_uuid": {"$ne": account_uuid}, "$or": or_query}

        projection = {
            "_id": 0,
        }
        document = self.user_cl.find_one(query, projection)

        return document

    def validate_user_code(
        self, code: str, account_uuid: UUID
    ) -> Optional[Dict[str, Any]]:
        """
        Check if the user code is exist on account level

        Args:
            code (str): User Code, to be used in DB query.
            account_uuid (UUID): Account UUID, to be used in DB query.

        Returns:
            Dict[str, Any]: MongoDB document representing the company details.
        """
        query = {"system_user.code": code, "account_uuid": account_uuid}

        # Remove _id from the result
        projection = {"_id": 0}

        # Fetch the data from DB
        document = self.user_cl.find_one(query, projection=projection)

        return document

    def get_user_uuid(self, auth0_id: str) -> UUID | None:
        """
        Get the User UUID based on auth0_id

        Args:
            auth0_id (str): The generated id from Auth0

        Return:
            UUID: The User UUID
        """
        query = {"system_user.id": auth0_id}
        projection = {"_id": 0, "uuid": 1}
        document = self.user_cl.find_one(query, projection)

        if document:
            return document["uuid"]

        return None

    def get_user_details(self, auth0_id: str) -> Dict[str, Any] | None:
        """
        Get the User details based on auth0_id

        Args:
            auth0_id (str): The generated id from Auth0

        Return:
            Dict[str, Any]: The User details
        """
        query = {"system_user.id": auth0_id}
        projection = {"_id": 0}

        document = self.user_cl.find_one(query, projection)

        return document

    def is_active_user(self, user_uuid: UUID) -> bool:
        """
        Check if the user is active or not

        Args:
            user_uuid (UUID): The User UUID

        Return:
            bool
        """
        query = {"system_user.status": True, "uuid": user_uuid}
        projection = {"_id": 0}

        document = self.user_cl.find_one(query, projection)
        if document:
            return True
        return False

    def get_user_position(self, user_uuid: UUID) -> UUID | None:
        """
        Get user position based on user_uuid

        Args:
            user_uuid (UUID): The User UUID

        Return:
            bool
        """
        query = {"uuid": user_uuid}

        projection = {"_id": 0}

        document = self.user_cl.find_one(query, projection)

        if document:
            try:
                position_uuid = document["system_user"]["position_uuid"]
                return position_uuid
            except (KeyError, TypeError):
                return None

        return None

    def delete_user(self, user_uuid: UUID) -> Optional[dict[str, Any]]:
        """
        Delete the user data based on uuid

        Args:
            user_uuid (UUID): The unique identifier of the user
        Return:
            dict( en="values", ar="values")
        """
        query = {"uuid": user_uuid}
        projection = {
            "_id": 0,
        }
        document = self.user_cl.find_one_and_delete(query, projection)

        return document

    def bulk_delete_users(self, user_uuids: List[UUID]) -> List[Dict[str, Any]]:
        """
        Bulk delete users based on a list of UUIDs.

        Args:
            user_uuids (List[UUID]): List of user UUIDs.

        Returns:
            List[Dict[str, Any]]: List of deleted user documents.
        """
        query = {"uuid": {"$in": user_uuids}}
        projection = {"_id": 0, "system_user": 1}

        # Fetch and delete the users
        cursor = self.user_cl.find(query, projection)
        deleted_users = list(cursor)
        self.user_cl.delete_many(query)

        return deleted_users

    def delete_many_users(self, user_uuids: List[UUID]) -> bool:
        """
        Delete many users based on the uuids

        Args:
            user_uuids (List[UUID]): The unique identifiers of the users
        Return:
            bool
        """
        query = {"uuid": {"$in": user_uuids}}
        delete_users = self.user_cl.delete_many(query)
        if delete_users.deleted_count > 0:
            return True

        return False

    def check_if_role_exist(self, role_uuid: UUID):
        """
        Check if any user have the provided role

        Args:
            role_uuid (UUID): The unique identifier of the role
        Return:
            dict( en="values", ar="values")
        """
        query = {"system_user.access.roles": {"$in": [role_uuid]}}

        projection = {
            "_id": 0,
        }
        document = self.user_cl.find_one(query, projection)

        return document

    def check_roles_in_use(self, role_uuids: List[UUID]) -> List[UUID]:
        """
        Check if any user has any of the provided roles.

        Args:
            role_uuids (List[UUID]): The list of role UUIDs to check.

        Returns:
            List[UUID]: A list of role UUIDs that are associated with users.
        """
        query = {"system_user.access.roles": {"$in": role_uuids}}
        projection = {"_id": 0, "system_user.access.roles": 1}

        documents = self.user_cl.find(query, projection)
        roles_in_use = []

        for doc in documents:
            roles_in_use.extend(doc["system_user"]["access"]["roles"])

        # Filter only the roles that are in the role_uuids list
        roles_in_use = list(set(roles_in_use) & set(role_uuids))

        return roles_in_use

    def get_all_users(
        self,
        account_uuid: UUID,
        page: int,
        limit: int,
        status: Optional[bool] = None,
        invite_status: Optional[str] = None,
        search_query: Optional[str] = None,
        user_type: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        Get all users data for a specific account with pagination.

        Args:
            account_uuid (UUID): The unique identifier for the account to which
             users are linked.
            page (int): The page number for pagination.
            limit (int): The limit of clusters per page.
            status (bool): The user status.
            invite_status (bool): Invite status of the user.
            search_query(str): The search query.
            user_type(str): The user type.

        Returns:
            RepositoryResult: A RepositoryResult object containing users data.
        """

        query = {"account_uuid": account_uuid}

        # Get master User data.
        master_query = {"account_uuid": account_uuid, "system_user.is_master": True}
        master_user_uuids = self.user_cl.find(master_query, {"_id": 0})
        if master_user_uuids:
            master_user_uuids = [doc["uuid"] for doc in master_user_uuids]

        # Query by invite_status.
        if invite_status:
            query.update({"system_user.invite_status": invite_status})

        # Query by status.
        if status:
            query.update({"system_user.status": status})

        # Search by query
        if search_query:
            query.update(
                {
                    "$or": [
                        {
                            "system_user.first_name.en": {
                                "$regex": f"{search_query}",
                                "$options": "i",
                            }
                        },
                        {
                            "system_user.last_name.en": {
                                "$regex": f"{search_query}",
                                "$options": "i",
                            }
                        },
                    ]
                },
            )

        if user_type is not None:
            query.update({"type": user_type})

        # Calculate the skip values based on the page number and limit
        skip_value = (page - 1) * limit
        cursor = self.user_cl.find(query, {"_id": 0}).limit(limit).skip(skip_value)

        users = [doc for doc in cursor if doc]

        # Get the count.
        count = self.user_cl.count_documents(query)

        results = dict(users=users, count=count)

        return results

    def get_document_count(self, query: Dict[str, Any]) -> int:
        """
        Count the documents based on a specific query.

        Args:
            query: The query used to count the documents.

        Returns:
            RepositoryResult: A RepositoryResult object with the count of documents.
        """

        count = self.user_cl.count_documents(query)

        return count

    def get_users_by_company(
        self, company_uuid: UUID, page: int, limit: int
    ) -> Optional[dict[str, Any]]:
        """
        Get the name of users based on company uuid

        Args:
            company_uuid: The unique identifier of the company
            page (int): The page number for pagination.
            limit (int): The limit of clusters per page.
        Return:
            dict( en="values", ar="values")
        """
        query = {"system_user.access.company_uuid": company_uuid}

        projection = {"_id": 0, "system_user.first_name": 1, "system_user.last_name": 1}

        # Calculate the skip values based on the page number and limit
        skip_value = (page - 1) * limit
        cursor = self.user_cl.find(query, projection).limit(limit).skip(skip_value)

        users = [doc for doc in cursor if doc]

        # Get the count
        count = self.user_cl.count_documents(query)

        results = dict(users=users, count=count)

        return results

    def get_user_by_company(
        self,
        company_uuid: UUID,
        user_uuid: UUID,
    ) -> Optional[dict[str, Any]]:
        """
        Get the name of user based on company uuid

        Args:
            company_uuid (UUID): The unique identifier of the company
            user_uuid (UUID): The unique identifier of the user

        Return:
            dict( en="values", ar="values")
        """
        query = {
            "uuid": user_uuid,
            "$or": [
                {"system_user.access.company_uuid": company_uuid},
                {"system_user.is_master": True},
            ],
        }

        projection = {"_id": 0}

        document = self.user_cl.find_one(query, projection=projection)

        return document

    def get_users_by_role(
        self,
        role_uuid: UUID,
        page: int,
        limit: int,
        search_query: Optional[str] = None,
    ) -> Optional[dict[str, Any]]:
        """
        Get the users data based on role uuid

        Args:
            role_uuid (UUID): The unique identifier of the role
            page (int): The page number for pagination.
            limit (int): The limit of users per page.
            search_query (str): The search query

        Return:
            Optional[dict[str, Any]]
        """
        query = {"system_user.access.roles": {"$in": [role_uuid]}}

        # Search by query
        if search_query:
            query.update(
                {
                    "$or": [
                        {
                            "system_user.first_name.en": {
                                "$regex": f"{search_query}",
                                "$options": "i",
                            }
                        },
                        {
                            "system_user.last_name.en": {
                                "$regex": f"{search_query}",
                                "$options": "i",
                            }
                        },
                    ]
                },
            )

        projection = {
            "_id": 0,
            "system_user.first_name": 1,
            "system_user.last_name": 1,
            "system_user.position_uuid": 1,
        }

        # Calculate the skip values based on the page number and limit
        skip_value = (page - 1) * limit
        cursor = self.user_cl.find(query, projection).limit(limit).skip(skip_value)

        users = [doc for doc in cursor if doc]

        # Get the count
        count = self.user_cl.count_documents(query)

        results = dict(users=users, count=count)

        return results

    def update_personal_settings(
        self, query: Dict[str, Any], data: Dict[str, Any]
    ) -> None:
        """
        Updates an existing User's Info entry in the database.

        Args:
            query (Dict[str, Any]): A query that matches the User entry to update.
            data (Dict[str, Any]): The modifications to apply to the User settings entry.

        Returns:
            None
        """
        self.user_cl.update_one(query, {"$set": data})  # Use "$set" for updates

    def get_users_by_position(
        self,
        position_uuid: UUID,
        account_uuid: Optional[UUID] = None,
        company_uuid: Optional[UUID] = None,
        projection: Optional[Dict[str, Any]] = None,
    ) -> List[UUID]:
        """
        Get the name of user based on uuid

        Args:
            position_uuid: The unique identifier of the position_uuid
            account_uuid: The unique identifier of the account_uuid
            company_uuid: The unique identifier of the company_uuid
            projection (Dict[str, Any]): What to project from the DB

        Return:
            dict( en="values", ar="values")
        """
        query = {"system_user.position_uuid": position_uuid}

        # Update the query for account_uuid and company_uuid
        for item in [account_uuid, company_uuid]:
            if item:
                query.update({f"{item}": item})

        if not projection:
            # Remove _id from the result
            projection = {"_id": 0}

        elif "_id" not in projection:
            projection.update({"_id": 0})

        cursor = self.user_cl.find(query, projection)

        users = [doc["uuid"] for doc in cursor if doc]

        return users

    def get_users_by_role_uuid(
        self,
        role_uuid: UUID,
        account_uuid: Optional[UUID] = None,
        company_uuid: Optional[UUID] = None,
        projection: Optional[Dict[str, Any]] = None,
    ) -> List[UUID]:
        """
        Get list of users based on role uuid

        Args:
            role_uuid: The unique identifier of the role_uuid
            account_uuid: The unique identifier of the account_uuid
            company_uuid: The unique identifier of the company_uuid
            projection (Dict[str, Any]): What to project from the DB

        Return:
            dict( en="values", ar="values")
        """
        query = {"system_user.access.roles": {"$in": [role_uuid]}}

        # Update the query for account_uuid and company_uuid
        for item in [account_uuid, company_uuid]:
            if item:
                query.update({f"{item}": item})

        if not projection:
            # Remove _id from the result
            projection = {"_id": 0}

        elif "_id" not in projection:
            projection.update({"_id": 0})

        cursor = self.user_cl.find(query, projection)

        users = [doc["uuid"] for doc in cursor if doc]

        return users

    def get_users_by_positions(
        self,
        position_uuids: List[UUID],
        account_uuid: Optional[UUID] = None,
        company_uuid: Optional[UUID] = None,
        projection: Optional[Dict[str, Any]] = None,
    ) -> List[UUID]:
        """
        Get the users details based on position uuids

        Args:
            position_uuids: The unique identifier of the position_uuids
            account_uuid: The unique identifier of the account_uuid
            company_uuid: The unique identifier of the company_uuid
            projection (Dict[str, Any]): What to project from the DB

        Return:
            dict( en="values", ar="values")
        """
        query = {"system_user.position_uuid": {"$in": position_uuids}}

        # Update the query for account_uuid and company_uuid
        for item in [account_uuid, company_uuid]:
            if item:
                query.update({f"{item}": item})

        if not projection:
            # Remove _id from the result
            projection = {"_id": 0}

        elif "_id" not in projection:
            projection.update({"_id": 0})

        cursor = self.user_cl.find(query, projection)

        users = [doc for doc in cursor if doc]

        return users

    def get_users_by_uuids(
        self,
        user_uuids: List[UUID],
    ) -> List[dict[str, Any]]:
        """
        Get the email of user based on uuids

        Args:
            user_uuids: The unique identifier of the user_uuid

        Return:
            List[dict[str, Any]]
        """
        query = {"uuid": {"$in": user_uuids}}

        # Remove _id from the result
        projection = {"_id": 0, "uuid": 1, "email": 1}

        cursor = self.user_cl.find(query, projection)

        users = [doc for doc in cursor]

        return users

    def bulk_remove_device_tokens(self, tokens_to_remove: List[Dict[str, Any]]) -> int:
        """
        Remove multiple device tokens from the users' documents.

        Args:
            tokens_to_remove (List[Dict[str, Any]]): A list of dictionaries with 'user_uuid' and 'token' to be removed.

        Example:
            tokens_to_remove = [
                {"user_uuid": "some-uuid-1", "token": "token1"},
                {"user_uuid": "some-uuid-2", "token": "token2"}
            ]

        Returns:
            int: The number of documents modified.
        """
        if not tokens_to_remove:
            return 0

        # Step 1: Create a list of user UUIDs and the corresponding tokens to remove
        user_uuids = [token_info["user_uuid"] for token_info in tokens_to_remove]
        tokens_to_remove = [token_info["token"] for token_info in tokens_to_remove]

        # Step 2: Create a query that matches any of the users in the list
        query = {
            "uuid": {"$in": user_uuids},
            "device_tokens.token": {"$in": tokens_to_remove},
        }

        # Step 3: Create the update operation to remove the tokens from device_tokens
        update_operation = {
            "$pull": {"device_tokens": {"token": {"$in": tokens_to_remove}}}
        }

        # Step 4: Execute the update operation for all matched documents
        result = self.user_cl.update_many(query, update_operation)

        # Step 5: Return the number of modified documents
        return result.modified_count

    def get_head_of_department(
        self,
        position_uuid: UUID,
        account_uuid: UUID,
        projection: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        query = {
            "account_uuid": account_uuid,
            "system_user.position_uuid": position_uuid,
            "system_user.head_of_department": True,
        }

        if not projection:
            # Remove _id from the result
            projection = {"_id": 0}

        head_of_department = self.user_cl.find_one(query, projection)

        return head_of_department
