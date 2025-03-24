# -*- coding: utf-8 -*-
import os
import pytest


def pytest_sessionstart(session):
    """
    This function is a pytest hook that is called at the beginning of the test session.

    It checks if tests should be skipped locally based on environment variables.

    Args:
        session: pytest session object.

    Returns:
        None
    """
    if os.getenv("SKIP_TESTS", False):
        if os.getenv("DB_NAME", "") == "main_db":
            pytest.exit("Tests are skipped locally.")
