# -*- coding: utf-8 -*-
from datetime import date
from typing import Any, List, Literal, Optional
from uuid import UUID

from pydantic import BaseModel, field_validator, model_validator
from main.api.validators.base_validators import Name


class CreateUserRequest(BaseModel):
    """
    Represents a request to create a new User.

    Attributes:
    - type (Literal): The User Type.
    - status (Literal): The User Status.
    - code (str): The User Code.
    - email (str): The users email address.
    - first_name (Name): The User First Name.
    - last_name (Name): The User Last Name.

    Usage Example:
    create_request = CreateUserRequest(
        first_name={
            "en": "Jhon"
        },
        last_name={
            "en": "Doe"
        },
        status="active,
        code="525",
        type="employee"
    )
    """

    type: Literal["employee", "agency", "university", "remote_access"] = "employee"
    provider_membership_type: Optional[Literal["admin", "member"]] = None
    status: bool
    code: str
    email: str
    first_name: Name
    last_name: Name

    @model_validator(mode="before")
    @classmethod
    def validate_fields_(cls, data: Any) -> Any:
        """
        Validate 'provider_membership_type' based 'type'.

        Args:
            data (Any): Data containing 'page' and 'limit' values.

        Raises:
            ValueError: if type is "agency" and "provider_membership_type" is null.

        Returns:
            Any: The input data if validation passes.
        """
        user_type = data.get("type")
        provider_membership_type = data.get("provider_membership_type")
        if user_type == "agency" and not provider_membership_type:
            raise ValueError(
                "provider_membership_type should be 'admin' or 'member' when type is "
                "agency."
            )

        return data


class GetUserRequest(BaseModel):
    """
    Represents a request to retrieve a User by its UUID.

    Attributes:
    - uuid (UUID): The universally unique identifier of the Cluster.

    Usage Example:
    get_request = GetUserRequest(uuid=61c9571a-f82a-4141-8cb7-c8536aecaa03)
    """

    uuid: UUID


class BulkDeleteUsersRequest(BaseModel):
    """
    Represents a request to bulk delete users.

    Attributes:
    - uuids (List[UUID]): The list of UUIDs of the users to be deleted.
    """

    uuids: List[UUID]


class UpdateUserRequest(BaseModel):
    """
    Represents a request to Update a User.

    Attributes:
    - type (Literal): The User Type.
    - status (Literal): The User Status.
    - code (str): The User Code.
    - email (str): The users email address.
    - first_name (Name): The User First Name.
    - last_name (Name): The User Last Name.

    Usage Example:
    create_request = UpdateUserRequest(
        first_name={
            "en": "Jhon"
        },
        last_name={
            "en": "Doe"
        },
        status="active,
        code="525",
        type="employee"
    )
    """

    uuid: UUID
    type: Literal["employee", "agency", "university", "remote_access"]
    status: bool
    invite_status: Literal["pending", "completed"]
    code: str
    first_name: Name
    last_name: Name


class GetUsersRequest(BaseModel):
    """
    Represents a request to retrieve a list of users with optional pagination.

    Attributes:
    - page (int): The page number for pagination. Defaults to 1.
    - limit (int): The maximum number of clusters to retrieve per page. Defaults to 30.

    Usage Example:
    get_request = GetUsersRequest(page=1, limit=10)
    """

    status: Optional[bool] = None
    invite_status: Optional[Literal["pending", "completed"]] = None
    query: Optional[str] = None
    type: Optional[str] = None
    page: int = 1
    limit: int = 30

    @field_validator("page")
    def validate_page(cls, value):
        if value <= 0:
            value = 1
        return value


class UpdatePersonalSettingsRequest(BaseModel):
    """
    This Pydantic class represents a request to update personal settings for a users.

    Attributes:
        uuid (UUID): The UUID of the users whose personal settings are being updated.
        middle_name (Optional[str]): The middle name of the users (optional).
        description (str): The description or bio of the users.
        phone (int): The phone number of the users.
        time_zone (str): The time zone of the users.
    """

    uuid: UUID
    middle_name: Optional[str] = None
    description: Optional[str] = None
    phone: Optional[int] = None
    time_zone: Optional[str] = None
