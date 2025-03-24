# -*- coding: utf-8 -*-
from typing import Any, Dict, List, Optional
from uuid import UUID

from main.api.classes.database import MongoDBConnection


class RBACRepository(MongoDBConnection):
    """
    This Class implements the RBAC  repository
    """

    def __init__(self):
        super().__init__()

        # Load collection
        self.rbac_collection = self.get_mongo_collection("company_role_based_access")

    def get_role_by_code(
        self, code: str, company_uuid: UUID
    ) -> Optional[Dict[str, Any]]:
        """
        Fetches a role record based on the role code and company UUID.

        Args:
            code (str): The role code.
            company_uuid (UUID): The company UUID.

        Returns:
            Optional[Dict[str, Any]]: The role record if found, None otherwise.
        """
        query = {"code": code, "company_uuid": company_uuid}

        # Remove _id from the result
        projection = {"_id": 0}

        # Fetch the data from DB
        document = self.rbac_collection.find_one(query, projection=projection)

        return document

    def create_rbac(self, query: Dict[str, Any], data: Dict[str, Any]) -> None:
        """
        Create a new RBAC in the database.py.

        Args:
            query (Dict[str, Any]): A query that matches the document to update.
            data (Dict[str, Any]): The modifications to apply.

        Returns:
            None
        """
        self.rbac_collection.update_one(
            query,
            {"$set": {**data}},
            upsert=True,
        )

    def update_rbac(self, query: Dict[str, Any], data: Dict[str, Any]) -> None:
        """
        Update RBAC in the database.py.

        Args:
            query (Dict[str, Any]): A query that matches the document to update.
            data (Dict[str, Any]): The modifications to apply.

        Returns:
            None
        """
        self.rbac_collection.update_one(
            query,
            {"$set": {**data}},
            upsert=False,
        )

    def bulk_update_rbac(
        self, company_uuids: List[UUID], update_data: Dict[str, Any]
    ) -> int:
        """
        Bulk update the RBAC details for the given companies.

        Args:
            company_uuids (List[UUID]): A list of company UUIDs to update.
            update_data (Dict[str, Any]): The data to update for the companies.

        Returns:
            int: The number of documents updated.
        """
        query = {"uuid": {"$in": company_uuids}}
        result = self.rbac_collection.update_many(query, {"$set": update_data})
        return result.modified_count

    def get_rbac(
        self,
        rbac_uuid: UUID,
        projection: Optional[Dict[str, Any]] = None,
        company_uuid: Optional[UUID] = None,
    ) -> Optional[Dict[str, Any]]:
        """
        Get RBAC Details by UUID.

        Args:
            rbac_uuid (UUID): RBAC UUID, to be used in DB query.
            projection (Dict[str, Any]): What to project from the DB
            company_uuid (UUID): Company UUID.

        Returns:
            Dict[str, Any]: MongoDB document representing the RBAC  details.
        """
        query = {"uuid": rbac_uuid}

        if company_uuid:
            query.update({"company_uuid": company_uuid})

        if not projection:
            # Remove _id from the result
            projection = {"_id": 0}

        # Fetch the data from DB
        document = self.rbac_collection.find_one(query, projection=projection)

        return document

    def get_rbac_by_template_uuids(
        self, template_uuids: List[UUID]
    ) -> List[Dict[str, Any]]:
        """
        Get all companies using any of the provided template UUIDs.

        Args:
            template_uuids (List[UUID]): A list of template UUIDs to check.

        Returns:
            List[Dict[str, Any]]: List of companies that are using the templates.
        """
        query = {"role_based_access_template_uuid": {"$in": template_uuids}}
        projection = {"_id": 0}

        # Fetch all companies in a single query
        cursor = self.rbac_collection.find(query, projection=projection)
        docs = [doc for doc in cursor]
        return docs

    def validate_role_code(
        self, company_uuid: UUID, code: str
    ) -> Optional[Dict[str, Any]]:
        """
        Validate the template Code on company level.

        Args:
            company_uuid (UUID): Company UUID, to be used in DB query.
            code (str): Template Code to be validated

        Returns:
            Dict[str, Any]: MongoDB document representing the RBAC Template details.
        """
        query = {"company_uuid": company_uuid, "code": code}

        # Remove _id from the result
        projection = {"_id": 0}

        # Fetch the data from DB
        document = self.rbac_collection.find_one(query, projection=projection)

        return document

    def delete_rbac(self, rbac_uuid: UUID) -> Optional[Dict[str, Any]]:
        """
        Delete RBAC Details by UUID.

        Args:
            rbac_uuid (UUID): RBAC UUID, to be used in DB query.

        Returns:
            Dict[str, Any]: MongoDB document representing the RBAC  details.
        """
        query = {"uuid": rbac_uuid}

        # Remove _id from the result
        projection = {"_id": 0}

        # Fetch the data from DB
        document = self.rbac_collection.find_one_and_delete(
            query, projection=projection
        )

        return document

    def get_rbacs_by_uuids(
        self,
        uuids: List[UUID],
        status: bool = True,
        projection: Optional[Dict[str, Any]] = None,
    ) -> List[Optional[dict[str, Any]]]:
        """
        Retrieves users from the RBAC collection by UUIDs.

        Args:
            uuids (List[UUID]): List of UUIDs identifying users.
            status (bool, optional): User status to filter by. Defaults to True.
            projection (Optional[Dict[str, Any]], optional): Projection to specify or
             restrict fields to be included in the result.

        Returns:
            List[Optional[Dict[str, Any]]]: List of dictionaries containing user
             information.
        """
        query = {"uuid": {"$in": uuids}, "status": status}

        if not projection:
            # Remove _id from the result
            projection = {"_id": 0}

        cursor = self.rbac_collection.find(query, projection)
        docs = list(cursor)

        return docs

    def get_all_rbac(
        self,
        account_uuid: UUID,
        page: int,
        limit: int,
        company_uuid: UUID,
        use_for: str,
        accept_language: str,
        status: Optional[bool] = None,
        search_query: Optional[str] = None,
    ) -> Optional[dict[str, Any]]:
        """
        Get all RBAC data for a specific account with pagination.

        Args:
            account_uuid (UUID): The unique identifier for the account to which
             RBAC are linked.
            page (int): The page number for pagination.
            limit (int): The limit of clusters per page.
            company_uuid (UUID): The unique identifier for the company uuid
            status (Optional[bool]): The status of record
            use_for (str): The type of clusters to return.
            search_query (Optional[str]): search query
            accept_language (str): language code

        Returns:
            RepositoryResult: A RepositoryResult object containing RBAC  data.
        """

        query = {
            "account_uuid": account_uuid,
            "company_uuid": company_uuid,
        }

        if status:
            query.update(
                {
                    "status": status,
                }
            )

        if search_query:
            query.update(
                {f"name.{accept_language}": {"$regex": search_query, "$options": "i"}}
            )

        if use_for == "dropdown":
            query.update({"status": True})

        # Calculate the skip values based on the page number and limit
        skip_value = (page - 1) * limit
        cursor = (
            self.rbac_collection.find(query, {"_id": 0}).limit(limit).skip(skip_value)
        )

        rbac = [doc for doc in cursor if doc]
        count = self.rbac_collection.count_documents(query)

        results = dict(
            rbac=rbac,
            count=count,
        )

        return results

    def get_document_count(self, query: Dict[str, Any]) -> int:
        """
        Count the documents based on a specific query.

        Args:
            query: The query used to count the documents.

        Returns:
            RepositoryResult: A RepositoryResult object with the count of documents.
        """

        count = self.rbac_collection.count_documents(query)

        return count

    def get_rbac_by_template_uuid(self, template_uuid: UUID) -> List[Dict[str, Any]]:
        """
        Get Roles Details by RBAC template UUID.

        Args:
            template_uuid (UUID): Template UUID, to be used in DB query.

        Returns:
            Dict[str, Any]: MongoDB document representing the role details.
        """
        query = {"role_based_access_template_uuid": template_uuid}

        # Remove _id from the result
        projection = {"_id": 0}

        # Fetch the data from DB
        cursor = self.rbac_collection.find(query, projection=projection)
        docs = [doc for doc in cursor]

        return docs

    def get_bulk_rbac(
        self, uuids: List[UUID], company_uuid: Optional[UUID] = None
    ) -> List[Dict[str, Any]]:
        """
        Retrieve multiple RBAC details by their UUIDs.

        Args:
            uuids (List[UUID]): The UUIDs of the RBAC entries.
            company_uuid (UUID, optional): The UUID of the company for filtering.

        Returns:
            List[Dict[str, Any]]: The retrieved RBAC entries.
        """
        query = {"uuid": {"$in": uuids}}
        if company_uuid:
            query["company_uuid"] = company_uuid

        projection = {"_id": 0}  # Exclude the MongoDB _id field if not needed
        documents = list(self.rbac_collection.find(query, projection))
        return documents

    def bulk_delete_rbac(self, uuids: List[UUID]) -> int:
        """
        Delete multiple RBAC entries in a single operation.

        Args:
            uuids (List[UUID]): The UUIDs of the RBAC entries to be deleted.

        Returns:
            int: The number of documents deleted.
        """
        query = {"uuid": {"$in": uuids}}
        result = self.rbac_collection.delete_many(query)
        return result.deleted_count
