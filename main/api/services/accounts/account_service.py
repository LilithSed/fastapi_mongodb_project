# -*- coding: utf-8 -*-
import socket
import uuid

from datetime import datetime
from uuid import UUID

from fastapi import status

from main.api.repositories.accounts.account_repository import AccountRepository
from main.api.helpers.utils import generate_translation_object
from main.api.models.accounts.account_requests import CreateAccountRequest
from main.api.repositories.users.user_repository import UserRepository
from main.api.validators.service_result import ServiceResult


class AccountService:
    def __init__(self):
        self.account_repository = AccountRepository()
        self.user_repository = UserRepository()

    @staticmethod
    def domain_exists(domain: str) -> bool:
        """Check if a domain has a valid DNS record.

        This function verifies whether a given domain exists by checking its DNS resolution.
        It attempts to resolve the domain name to an IP address using `socket.gethostbyname()`.

        Args:
            domain (str): The domain name to check (e.g., "example.com").

        Returns:
            bool: True if the domain has a valid DNS record, False otherwise.

        Example:
             domain_exists("google.com")
            True
             domain_exists("nonexistentdomain12345.com")
            False

        Note:
            - This function only verifies DNS existence. It does not check if a website is live.
            - If the domain exists but has no DNS records, it will return False.
        """
        try:
            socket.gethostbyname(domain)
            return True
        except socket.gaierror:
            return False

    def create_account(
        self,
        item: CreateAccountRequest,
        user_uuid: UUID,
    ):
        """
        Creates a new account with the specified details.

        Args:
            item (CreateAccountRequest): An object containing information for
                creating the account.
            user_uuid (UUID): The user UUID.

        Returns:
            ServiceResult: An object containing the result of the account creation
                process, including status code and data.

        Steps:
        1. Prepare the data to be saved.
        2. Create an account in the database with the prepared data.
        3. Update account details in the database.
        4. Return a ServiceResult with the created account, clusters, companies, and u
            ser data.
        """
        # Generate a new UUID for the account.
        account_uuid = uuid.uuid4()
        account_query = dict(uuid=account_uuid)

        # Generate translation objects for name and description.
        name = generate_translation_object(item.name)
        description = generate_translation_object(item.description)

        # Create an account in the database with the prepared data.
        account_data = dict(
            name=name,
            description=description,
            domain=item.domain.lower(),
            status=True,
            created_by=user_uuid,
            activated_at=datetime.now(),
            created_at=datetime.now(),
            updated_at=datetime.now(),
            company_size=item.company_size,
            structure=item.structure,
        )

        # Save data in the DB.
        self.account_repository.create_account(query=account_query, data=account_data)

        account = self.account_repository.get_account(account_uuid=account_uuid)
        account.update({"logo_uri": None})

        # Return a ServiceResult with the created account.
        results = dict(account=account)
        return ServiceResult(
            status_code=status.HTTP_201_CREATED,
            data=results
        )

    def get_account_details(
        self,
        user_uuid: UUID,
    ):
        """
        Retrieves account details, including associated companies and clusters,
            for a given user.

        Args:
            user_uuid (UUID): The unique identifier of the user for whom
                account details are requested.

        Returns:
            ServiceResult: An object containing the result of the account details
                retrieval process, including status code and data.
        """
        # Retrieve users details from the repository using the provided user UUID.
        user_details = self.user_repository.get_user(uuid=user_uuid)

        # Provider_accounts list contains all accounts related to agency.
        provider_accounts = []
        has_provider = False

        results = dict(
            account={},
            user={},
            provider_accounts=provider_accounts,
            has_provider=has_provider,
        )

        try:
            all_users = self.user_repository.get_users_be_email(
                email=user_details["email"]
            )
            for _user_details in all_users:
                # Attempt to extract the account UUID from the user details.
                account_uuid = _user_details["account_uuid"]

                # Get account, company, and cluster details from the database.
                account = self.account_repository.get_account(account_uuid=account_uuid)
                account.update({"logo_uri": None})

                if _user_details["type"] == "agency":
                    # Refers the user is invited as a provider.
                    results["has_provider"] = True

                result = dict(
                    account=account,
                    user=_user_details,
                )

                if _user_details["type"] == "agency":
                    provider_accounts.append(result)
                else:
                    # Add the data to account, user to main item.
                    results.update(**result)

        except (KeyError, TypeError, AttributeError):
            # Handle exceptions (KeyError, TypeError, AttributeError) that may occur
            # while extracting or retrieving data. Return empty data in such cases.
            results = dict(account={}, user={}, accounts=[])

        # Check user details is empty and provider_accounts, in this case the user is
        # invited as a provider, and isn't an employee on another account, so display
        # only the user details without any details for account and companies.
        if not results["user"] and not provider_accounts:
            results["user"] = user_details

        return ServiceResult(status_code=status.HTTP_200_OK, data=results)
