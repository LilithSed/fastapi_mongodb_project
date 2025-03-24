# -*- coding: utf-8 -*-
import sys
import traceback


class Error:
    """
    A utility class to handle and manage system exceptions for the application.

    Provides methods to extract and format system exception details.
    """

    @staticmethod
    def get_system_exception():
        """
        Captures the current system exception, formats it, and raises it as an HTTPException.

        Raises:
            HTTPException: An exception with a 500 status code and detailed error message.
        """

        exc_type, exc_value, exc_traceback = sys.exc_info()

        message = f"{exc_type}: {exc_value}"

        # Extract and format the traceback information as a list of strings
        trace_back = traceback.extract_tb(exc_traceback)
        formatted_traceback = [
            f"{filename}, line {lineno}, in {name} {line}"
            for filename, lineno, name, line in trace_back
        ]

        internal_error = {
            "message": message,
            "trace": formatted_traceback,
        }
        return internal_error
