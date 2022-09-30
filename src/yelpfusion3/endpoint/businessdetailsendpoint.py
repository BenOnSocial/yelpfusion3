from typing import Optional
from urllib.parse import urlencode

from pydantic import constr, validator

from yelpfusion3.endpoint import base_url, supported_locales
from yelpfusion3.endpoint.endpoint import Endpoint


class BusinessDetailsEndpoint(Endpoint):
    """
    This endpoint returns detailed business content. Normally, you would get the Business ID from /businesses/search,
    /businesses/search/phone, /transactions/{transaction_type}/search or /autocomplete. To retrieve review excerpts for
    a business, please refer to our Reviews endpoint (/businesses/{id}/reviews)

    Note: at this time, the API does not return businesses without any reviews.
    """

    _path: str = "/businesses"

    business_id: constr(min_length=1, regex=r"^[A-Za-z0-9\-]+$", strip_whitespace=True)  # type: ignore
    """
    Unique Yelp ID of the business to query for.
    """

    locale: Optional[str]
    """
    Optional. Specify the locale into which to localize the business information. See the list of supported locales.
    Defaults to en_US.
    """

    def url(self) -> str:
        """
        Constructs a URL to the business search endpoint with the given query parameters.

        :return: Yelp Fusion API 3 endpoint URL.
        :rtype: str
        """
        non_none_fields = {
            key: value
            for key, value in self.dict().items()
            if value is not None and key != "business_id"
        }
        parameters = urlencode(query=non_none_fields)
        if parameters:
            return f"{base_url}{self._path}/{self.business_id}?{parameters}"
        else:
            return f"{base_url}{self._path}/{self.business_id}"

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
