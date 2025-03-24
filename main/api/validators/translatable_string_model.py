# -*- coding: utf-8 -*-
from pydantic import field_validator, RootModel


class TranslatableStringModel(RootModel[dict[str, str]]):
    """A base model for multi-language string fields."""

    @field_validator("root")
    def validate_required_languages(cls, value):
        """
        Validate that the provided dictionary contains the required languages.

        Args:
            value (dict[str, str]): The dictionary to validate.

        Returns:
            dict[str, str]: The validated dictionary.

        Raises:
            ValueError: If the required language keys are not present.
        """
        if "en" not in value and "ar" not in value:
            raise ValueError("Either 'en' or 'ar' language is required.")

        return value