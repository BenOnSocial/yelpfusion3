from typing import Optional

from pydantic import constr, validator
from requests import Response

from yelpfusion3.endpoint import supported_locales
from yelpfusion3.endpoint.endpoint import Endpoint
from yelpfusion3.model.business.phonesearch import PhoneSearch


class PhoneSearchEndpoint(Endpoint):
    """
    This endpoint returns a list of businesses based on the provided phone number. It is possible for more than one
    business to have the same phone number (for example, chain stores with the same +1 800 phone number).

    Note: at this time, the API does not return businesses without any reviews.
    """

    _path: str = "/businesses/search/phone"

    phone: constr(strip_whitespace=True, min_length=12, regex=r"^\+\d+")  # type: ignore
    """
    Required. Phone number of the business you want to search for. It must start with + and include the country code,
    like +14159083801.
    """

    locale: Optional[str]
    """
    Optional. Specify the locale into which to localize the business information. See the list of supported locales.
    Defaults to en_US.
    """

    def get(self) -> PhoneSearch:
        response: Response = self._get()
        return PhoneSearch(**response.json())

    @validator("locale")
    def check_locale(cls, v: str) -> str:
        """
        Validates that the locale is supported by Yelp Fusion API 3.
        See https://www.yelp.com/developers/documentation/v3/supported_locales

        :param v: Locale of the response body.
        :type v: str
        :raise ValueError: "v" is an unsupported locale value.
        :return: "v" if it's a supported locale.
        :rtype: str
        """
        if v not in supported_locales:
            raise ValueError("Unsupported 'locale' value.")
        return v
