from typing import List, Optional

import pycountry
from pydantic import constr, validator

from yelpfusion3.model.model import Model


class Location(Model):
    """
    The location of this business, including address, city, state, zip code and country.
    """

    address1: Optional[constr(strip_whitespace=True)] = None  # type: ignore
    """
    Street address of this business.
    """

    address2: Optional[constr(strip_whitespace=True, min_length=0)] = None  # type: ignore
    """
    Street address of this business, continued.
    """

    address3: Optional[constr(strip_whitespace=True, min_length=0)] = None  # type: ignore
    """
    Street address of this business, continued.
    """

    city: str
    """
    City of this business.
    """

    zip_code: str
    """
    Zip code of this business.
    """

    country: str
    """
    ISO 3166-1 alpha-2 country code of this business.
    """

    state: str
    """
    ISO 3166-2 (with a few exceptions) state code of this business.
    """

    display_address: List[str]
    """
    Array of strings that if organized vertically give an address that is in the standard address format for the
    business's country.
    """

    cross_streets: Optional[constr(strip_whitespace=True, min_length=0)] = None  # type: ignore
    """
    Cross streets for this business. (Only used in business details search results.)
    """

    @validator("country")
    def _check_country(cls, v: str) -> str:
        """
        Checks that ``v`` is a valid ISO 3166- alpha-2 country code.

        :param v: Two-letter country code.
        :type v: str
        :raise ValueError: If ``v`` is an invalid country code.
        :return: ``v`` if it passes validation.
        :rtype: str
        """

        if pycountry.countries.get(alpha_2=v):
            return v
        raise ValueError("Not a valid ISO 3166-1 alpha-2 country code.")
