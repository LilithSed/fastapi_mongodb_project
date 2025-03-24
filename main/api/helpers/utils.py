# -*- coding: utf-8 -*-
import jwt
import random
import string

from typing import Any, Dict
from uuid import UUID

from fastapi import HTTPException, status

from main.api.constants.languages_codes import LANGUAGES_CODES
from main.api.repositories.users.user_repository import UserRepository


def get_auth0_id(token: str) -> str:
    """
    Get Auth0 ID from user token.

    Args:
        token (str): The User Token.

    Returns:
        str: The Auth0 ID
    """
    try:
        token = token.replace("Bearer ", "")
        decoded_token = jwt.decode(token, options={"verify_signature": False})

        # Accessing the subject (user ID)
        # it returns the id as follows: auth0|45569545
        auth0_id = decoded_token.get("sub")
        return auth0_id

    except (jwt.exceptions.ExpiredSignatureError, jwt.exceptions.DecodeError):
        raise HTTPException(
            detail="Invalid token!",
            status_code=status.HTTP_401_UNAUTHORIZED,
        )


def get_user_uuid(token: str) -> UUID:
    """
    Get user_uuid from user token.

    Args:
        token (str): The User Token.

    Returns:
        user_uuid
    """
    try:
        user_repository = UserRepository()
        token = token.replace("Bearer ", "")
        decoded_token = jwt.decode(token, options={"verify_signature": False})

        # Accessing the subject (user ID)
        # it returns the id as follows: auth0|45569545
        auth0_id = decoded_token.get("sub")
        auth0_id = auth0_id.split("|")[-1]

        user_uuid = user_repository.get_user_uuid(auth0_id=auth0_id)
        return user_uuid

    except (jwt.exceptions.ExpiredSignatureError, jwt.exceptions.DecodeError):
        raise HTTPException(
            detail="Invalid token!",
            status_code=status.HTTP_401_UNAUTHORIZED,
        )


def generate_password(n=15) -> str:
    """
    Generates a random password of n characters with at least one uppercase letter,
       one symbol, and one number.

    Returns:
       str: A string containing the generated password.
    """
    # Generate required components.
    uppercase_chars = random.choices(string.ascii_uppercase, k=3)
    symbol_chars = random.choices(string.punctuation, k=3)
    digit_chars = random.choices(string.digits, k=3)

    # Fill the rest with random choices of all allowed characters.
    remaining_length = n - (len(uppercase_chars) + len(symbol_chars) + len(digit_chars))
    other_chars = random.choices(
        string.ascii_letters + string.digits + string.punctuation, k=remaining_length
    )

    # Combine all parts and shuffle
    password_list = uppercase_chars + symbol_chars + digit_chars + other_chars
    random.shuffle(password_list)

    password = "".join(password_list)

    if password == "":
        password = "NMYZ@LqMMprx#E93mHRrZnXeKkfnYT"

    return password


def generate_translation_object(value: str) -> Dict[Any, str]:
    """
    Generate a translation object for name and description, if English is the only
     provided value.

    Args:
        value (str): English translation.

    Returns:
        Dict[Any, str]
    """
    languages_codes = LANGUAGES_CODES

    translation_object = {}

    for code in languages_codes:
        if code == "en":
            translation_object.update({"en": value})
        else:
            translation_object.update({code: None})

    return translation_object