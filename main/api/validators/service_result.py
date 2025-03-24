# -*- coding: utf-8 -*-
from pydantic import BaseModel
from typing import Union


class ServiceResult(BaseModel):
    """
    Represents the result of a service operation.

    Attributes:
        data (Union[dict, list, None]): The data returned by the service.
        status_code (Union[int, None]): The HTTP status code associated with the result.
    """

    status_code: int = None
    data: Union[dict, list, str, int, bool, None] = None
