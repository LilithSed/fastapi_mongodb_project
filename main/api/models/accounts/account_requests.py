# -*- coding: utf-8 -*-
from typing import List, Literal, Optional
from uuid import UUID

from pydantic import BaseModel


class CreateAccountRequest(BaseModel):
    """
    Represents a request to create a new Account.

    Attributes:
    - company_size (Literal): The Company Size of the Account:
        level_one = '0-20'
        level_two = '21-50'
        level_three = '51-100'
        level_four = '101-200'
        level_five = '201-500'
        level_six = '501-1000'
        level_seven = '1001-2000'
        level_eight = '2001-5000'
        level_ten = '5001-10000'
        level_eleven = '10000+'
    - domain (str): The account domain URL.
    - is_with_integrations (bool): Whether the account is associated with an integration
    - name (str): The name of the Account
    - structure (Literal): The structure of the Account in terms of branches

    Usage Example:
    create_request = CreateAccountRequest(
        company_size="level_one",
        domain="example.com",
        industries=[
            "18a2baca-ec92-49b2-8a7d-bcc42d8de8a6",
            "0ccfb985-15c2-474c-9c87-d3e5e51a1fe5",
        ],
        is_with_integrations=False,
        name="Example Account",
        structure="level_one"
    )
    """
    company_size: Literal[
        "level_one",
        "level_two",
        "level_three",
        "level_four",
        "level_five",
        "level_six",
        "level_seven",
        "level_eight",
        "level_nine",
        "level_ten",
    ]
    domain: str
    is_with_integrations: bool
    name: str
    description: Optional[str] = "Default Description"
    structure: Literal["level_one", "level_two", "level_three", "level_four"]
