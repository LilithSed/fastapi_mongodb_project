# -*- coding: utf-8 -*-
from importlib import import_module
from typing import Optional, Union

from fastapi import Header, Request, status
from fastapi.responses import ORJSONResponse

from main.api.helpers.exception import Error




def get_translation_message(locale, key):
    """
    Retrieves a translated message based on a given locale and translation key.

    This function attempts to import a module based on the provided locale and fetches
    the translation message corresponding to the key. If the locale does not exist or
    there's an error fetching the translation, it defaults to the English translation.

    Args:
        locale (str): The language code representing the desired translation, e.g., 'en', 'fr'.
        key (str): The translation key for which the message is to be fetched.

    Returns:
        str: The translated message or the key itself if the translation is not found.

    Raises:
        None: If the translation isn't found, it defaults to English without raising an
        exception.
    """
    try:
        module = import_module(f"setup.api.translations.{locale}")
        return module.MESSAGES.get(key, key)
    except (ModuleNotFoundError, AttributeError):
        # Fallback to English or any other default language if translation not found
        module = import_module("setup.api.translations.en")
        return module.MESSAGES.get(key, key)


class ResponseFactory:
    def __init__(self, locale: str = "en"):
        self.locale = locale

    @staticmethod
    def create_response(
        status_code: int,
        content: dict = None,
        message: str = None,
        data: dict = None,
        meta: dict = None,
        error: dict = None,
    ) -> ORJSONResponse:
        """
        Constructs a standardized response based on the provided parameters.

        Args:
            status_code (int): HTTP status code for the response.
            content (dict).
            message (str): Response message. Auto-resolves to localized message.
            data (dict, optional): Primary data payload for the response. Defaults to None.
            meta (dict, optional): Metadata related to the data payload. Defaults to None.
            error (dict, optional): Error details if an error is triggered. Defaults to None.

        Returns:
            ORJSONResponse: The standardized API response.
        """
        # content = {"message": message}
        content = content if content else {}

        if data or data == {}:
            data = None if data == {} else data
            content["data"] = data
        if meta:
            content["meta"] = meta
        if error:
            content["error"] = error

        return ORJSONResponse(status_code=status_code, content=content)

    def process_trace(self, data: Optional[Union[list, dict]]) -> list:
        """
        Process trace data and return a list of dictionaries containing error keys and messages.

        Args:
            data (Optional[Union[list, dict]]): The trace data to process, can be either a list of dictionaries
                or a single dictionary.

        Returns:
            list: A list of dictionaries, each containing the 'error_key' and 'error_message' extracted
                from the input data.

        Example:
            [{'error_key': 'ERR001', 'error_message': 'Translated ERR001_MESSAGE'}]
        """
        trace = []

        if isinstance(data, list):
            for item in data:
                if not data:
                    continue
                trace.append(
                    {
                        "error_key": item["error_key"],
                        "error_message": get_translation_message(
                            self.locale, item["key"]
                        ),
                    }
                )

        elif isinstance(data, dict):
            trace_data = {}
            for key, value in data.items():
                if key == "key":
                    trace_data["error_message"] = get_translation_message(
                        self.locale,
                        value,
                    )
                    trace_data["error_key"] = data.get("error_key")

            trace = [trace_data]

        return trace

    def success(self, data: dict = None) -> ORJSONResponse:
        """
        Args:
            data (dict): Data payload for the success response.

        Returns:
            ORJSONResponse: The success response.
        """
        message = get_translation_message(self.locale, "operation_successful")
        return ResponseFactory.create_response(
            status.HTTP_200_OK, data=data, message=message
        )

    @staticmethod
    def created(
        data: dict = None,
        full_payload: bool = False,
        created_status: bool = True,
    ) -> ORJSONResponse:
        """
        Constructs a 201 Created response.

        Args:
            data (dict): Data payload indicating the resource that was created.
            full_payload (bool): Specify whether to retrieve the created data or not.
            created_status (bool): Check if the data is created successfully or not. It is
            used with pubsub, so when some data doesn't exist, we have to return
            status equal to 201 and the created: False.

        Returns:
            ORJSONResponse: The created resource response.
        """
        content = {"created": created_status}
        _ = content.update({"data": data}) if full_payload else None

        return ResponseFactory.create_response(status.HTTP_201_CREATED, content=content)

    @staticmethod
    def updated(data: dict = None, full_payload: bool = False) -> ORJSONResponse:
        """
        Constructs a 202 updated response.

        Args:
            data (dict): Data payload indicating the resource that was updated.
            full_payload (bool)

        Returns:
            ORJSONResponse: The updated resource response.
        """
        content = {"updated": True}
        _ = content.update({"data": data}) if full_payload else None

        return ResponseFactory.create_response(
            status.HTTP_202_ACCEPTED, content=content
        )

    @staticmethod
    def deleted(data: dict = None, full_payload: bool = False) -> ORJSONResponse:
        """
        Constructs a 200 OK response to indicate successful deletion along with a message.

        Args:
            data (dict): Data payload indicating the resource that was updated.
            full_payload (bool)

        Returns:
            ORJSONResponse: The response with a message indicating successful deletion.
        """
        content = {"deleted": True}
        _ = content.update({"data": data}) if full_payload else None

        return ResponseFactory.create_response(
            status.HTTP_202_ACCEPTED, content=content
        )

    def bad_request(
        self,
        data: dict | list = None,
        message_key: str = "bad_request",
        skip_trace: bool = False,
    ) -> ORJSONResponse:
        """
        Constructs a 400 Bad Request response.

        Returns:
            ORJSONResponse: The bad request response.
        """
        message = get_translation_message(self.locale, message_key)

        if skip_trace:
            trace = []
        else:
            trace = self.process_trace(data=data)

        content = {"message": message, "trace": trace}
        return ResponseFactory.create_response(
            status.HTTP_400_BAD_REQUEST, content=content
        )

    def unauthorized(
        self,
        data: dict | list = None,
        message_key: str = "unauthorized",
    ) -> ORJSONResponse:
        """
        Constructs a 401 Unauthorized response.

        Returns:
            ORJSONResponse: The unauthorized response.
        """
        message = get_translation_message(self.locale, message_key)

        if data is None:
            content = {"message": message}
        else:
            trace = self.process_trace(data=data)
            content = {"message": message, "trace": trace}

        return ResponseFactory.create_response(
            status.HTTP_401_UNAUTHORIZED, content=content
        )

    def forbidden(
        self,
        data: dict | list = None,
        message_key: str = "forbidden",
    ) -> ORJSONResponse:
        """
        Constructs a 403 forbidden response.

        Returns:
            ORJSONResponse: The forbidden response.
        """
        message = get_translation_message(self.locale, message_key)

        if data is None:
            content = {"message": message}
        else:
            trace = self.process_trace(data=data)
            content = {"message": message, "trace": trace}

        return ResponseFactory.create_response(
            status.HTTP_403_FORBIDDEN, content=content
        )

    def not_found(
        self,
        request: Request = None,
        data: dict | list = None,
        message_key: str = "not_found",
        skip_trace: bool = False,
    ) -> ORJSONResponse:
        """
        Constructs a 404 Not Found response.

        Args:
            request (Request, optional): Details of the incoming request (e.g., URL, method).
            data (dict, optional): Additional data for tracing purposes.
            message_key (str, optional): The key of the translation message
        Returns:
            ORJSONResponse: The constructed Not Found response.

        Notes:
            - If `data` is provided, the `trace` includes key-value pairs from the data.
            - If `data` is not provided, the `trace` includes the URL from the `request`.
        """
        message = get_translation_message(self.locale, message_key)

        if skip_trace:
            trace = []
        else:
            if isinstance(data, dict):
                trace = [f"{key}: {value}" for key, value in data.items()]

            else:
                trace = [str(request.url)]

        content = {"message": message, "trace": trace}
        return ResponseFactory.create_response(
            status.HTTP_404_NOT_FOUND, content=content
        )

    def method_not_allowed(
        self,
        request: Request = None,
        data: dict = None,
    ) -> ORJSONResponse:
        """
        Constructs a 405 Method Not Allowed response.

        Args:
            request (Request, optional): The request causing the method not allowed response.
            data (dict, optional): Additional data for tracing purposes.

        Returns:
            ORJSONResponse: The constructed Method Not Allowed response.

        Notes:
            - If `data` is provided, the `trace` includes from the data error message.
            - If `data` is not provided, the `trace` includes the URL and method from the `request`.
        """
        message = get_translation_message(self.locale, "method_not_allowed")
        if data:
            error_message = get_translation_message(self.locale, data["key"])
            trace = [error_message]

        else:
            trace = [str(request.url), str(request.method)]

        content = {"message": message, "trace": trace}

        return ResponseFactory.create_response(
            status.HTTP_405_METHOD_NOT_ALLOWED, content=content
        )

    def conflict(self, data: dict) -> ORJSONResponse:
        """
        Constructs a 409 conflict response.

        Returns:
            ORJSONResponse: The conflict response.
        """
        message = get_translation_message(self.locale, data["key"])
        trace = self.process_trace(data=data)

        content = {"message": message, "trace": trace}
        return ResponseFactory.create_response(
            status.HTTP_409_CONFLICT, content=content
        )

    @staticmethod
    def internal_server_error(exc=None) -> ORJSONResponse:
        """
        Constructs a 500 Internal Server Error response.

        Returns:
            ORJSONResponse: The internal server error response.
        """
        if exc:
            error = Error.get_system_exception()
        else:
            error = None
        return ResponseFactory.create_response(
            status.HTTP_500_INTERNAL_SERVER_ERROR, content=error
        )

    @staticmethod
    def single_data(data: Union[dict, None]) -> ORJSONResponse:
        """
        Constructs a response for a single data retrieval.

        Args:
            data (dict): Data payload for the single data item.

        Returns:
            ORJSONResponse: The single data retrieval response.
        """
        if data is None:
            data = {}
        return ResponseFactory.create_response(status.HTTP_200_OK, content=data)

    @staticmethod
    def list_data(
        result: list, current_page: int, limit: int, total: int
    ) -> ORJSONResponse:
        """
        Constructs a response for a list data retrieval with pagination information.

        Args:
            result (list): List of data items/documents to be returned.
            current_page (int): The current page number.
            limit (int): The maximum number of data items/documents to be returned per page.
            total (int): The total number of data items/documents available.

        Returns:
            ORJSONResponse: The list data retrieval response with pagination metadata.
        """
        total_pages = (total + limit - 1) // limit
        meta = {
            "current_page": current_page,
            "limit": limit,
            "total": total,
            "total_pages": total_pages,
        }
        content = {"meta": meta, "results": result}

        return ResponseFactory.create_response(status.HTTP_200_OK, content=content)


def get_response_factory(
    accept_language: str = Header(default="en"),
) -> ResponseFactory:
    """
    Creates and returns a ResponseFactory instance configured with the appropriate locale
    for message translations based on the "Accept-Language" HTTP header.

    This function is intended to be used as a dependency in FastAPI routes to easily obtain
    a ResponseFactory instance with the correct locale for generating localized responses.

    Args:
        accept_language (str, optional): The value of the "Accept-Language" HTTP header,
            indicating the preferred language/locale of the client. Defaults to "en".

    Returns:
        ResponseFactory: A ResponseFactory instance configured to use translations for
        the specified locale.
    """
    return ResponseFactory(locale=accept_language)
