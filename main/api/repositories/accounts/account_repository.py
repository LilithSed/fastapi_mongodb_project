# -*- coding: utf-8 -*-
from typing import Any, Dict, Optional
from uuid import UUID

from main.api.classes.database import MongoDBConnection


class AccountRepository(MongoDBConnection):
    """
    This Class implements the Account repository
    """

    def __init__(self):
        super().__init__()

        # Load collection
        self.account_collection = self.get_mongo_collection("accounts")

    def create_account(self, query: Dict[str, Any], data: Dict[str, Any]) -> None:
        """
        Create a new Account in the database.

        Args:
            query (Dict[str, Any]): A query that matches the document to update.
            data (Dict[str, Any]): The modifications to apply.

        Returns:
            None
        """
        self.account_collection.update_one(
            query,
            {"$set": {**data}},
            upsert=True,
        )

    def get_account(self, account_uuid: UUID) -> Optional[Dict[str, Any]]:
        """
        Get Account Details by UUID.

        Args:
            account_uuid (str): Account UUID, to be used in DB query.

        Returns:
            Dict[str, Any]: MongoDB document representing the account details.
        """
        query = {"uuid": account_uuid}

        # Remove _id from the result
        projection = {"_id": 0}

        # Fetch the data from DB
        document = self.account_collection.find_one(query, projection=projection)

        return document

    def get_account_name(self, account_uuid, return_as_dict: bool = None):
        """
        Get the account name
        Args:
            account_uuid: Account UUID
            return_as_dict: to return it as a dict or as a string

        Returns:
            Dict, None
        """

        document = self.account_collection.find_one(
            {"uuid": account_uuid}, {"_id": 0, "name": 1}
        )

        if document:
            if return_as_dict:
                account_name = document["name"]
            else:
                account_name = document["name"]["en"]
            return account_name

        return None

    def validate_domain(self, domain: str) -> Optional[Dict[str, Any]]:
        """
        Validate the domain value.

        Args:
            domain (str): Account domain, to be used in DB query.

        Returns:
            Dict[str, Any]: MongoDB document representing the account details.
        """
        query = {"domain": domain}

        # Remove _id from the result
        projection = {"_id": 0}

        # Fetch the data from DB
        document = self.account_collection.find_one(query, projection=projection)

        return document

    def update_account(self, query: Dict[str, Any], data: Dict[str, Any]) -> None:
        """
        Update Account in the database.

        Args:
            query (Dict[str, Any]): A query that matches the document to update.
            data (Dict[str, Any]): The modifications to apply.

        Returns:
            None
        """
        self.account_collection.update_one(
            query,
            {"$set": {**data}},
            upsert=True,
        )

    def delete_account(self, account_uuid: UUID) -> Optional[Dict[str, Any]]:
        """
        Delete the Account from DB by UUID.

        Args:
            account_uuid (str): Visa Stage UUID, to be used in DB query.

        Returns:
            Dict[str, Any]: MongoDB document representing the deleted account.
        """
        query = {"uuid": account_uuid}

        # Remove _id from the result
        projection = {"_id": 0}

        # Fetch the data from DB
        document = self.account_collection.find_one_and_delete(
            query, projection=projection
        )

        return document
