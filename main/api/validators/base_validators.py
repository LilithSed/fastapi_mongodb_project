# -*- coding: utf-8 -*-
from main.api.validators.translatable_string_model import TranslatableStringModel


class Name(TranslatableStringModel):
    """
    A specific representation of the TranslatableStringModel for storing names.

    Attributes:
        root (dict[str, str]): A dictionary containing names in various languages.
            'en' and 'ar' keys are mandatory.

    Example:
        >>> name_data = {"en": "John Doe", "ar": "جون دو"}
        >>> name = Name.model_validate(name_data)
        >>> assert name.model_dump() == {"en": "John Doe", "ar": "جون دو"}
    """

    pass