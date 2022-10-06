from typing import Optional
from urllib.parse import urlencode

from pydantic import constr, validator
from requests import Response

from yelpfusion3.endpoint import supported_locales
from yelpfusion3.endpoint.endpoint import Endpoint
from yelpfusion3.model.business.reviews import Reviews
from yelpfusion3.settings import Settings


class ReviewsEndpoint(Endpoint):
    """
    This endpoint returns up to three review excerpts for a given business ordered by Yelp's default sort order.

    Note: at this time, the API does not return businesses without any reviews.
    """

    _path: str = "/businesses/{business_id}/reviews"

    business_id: constr(min_length=1, regex=r"^[A-Za-z0-9\-]+$", strip_whitespace=True)  # type: ignore
    """
    Unique Yelp ID of the business to query for.
    """

    locale: Optional[str]
    """
    Optional. Specify the locale into which to localize the business information. See the list of supported locales.
    Defaults to ``en_US``.
    """

    @property
    def url(self) -> str:
        """
        Constructs a URL to the reviews endpoint with the given query parameters.

        :return: Yelp Fusion API 3 endpoint URL.
        :rtype: str
        """
        non_none_fields = {
            key: value
            for key, value in self.dict().items()
            if value is not None and key != "business_id"
        }
        parameters = urlencode(query=non_none_fields)
        settings: Settings = Settings()
        path: str = self._path.format(business_id=self.business_id)

        if parameters:
            return f"{settings.base_url}{path}?{parameters}"
        else:
            return f"{settings.base_url}{path}"

    def get(self) -> Reviews:
        response: Response = self._get()
        return Reviews(**response.json())

    @validator("locale")
    def _check_locale(cls, v: str) -> str:
        """
        Validates that the locale is supported by Yelp Fusion API 3.
        See https://www.yelp.com/developers/documentation/v3/supported_locales

        :param v: Locale of the response body.
        :type v: str
        :raise ValueError: ``v`` is an unsupported locale value.
        :return: ``v`` if it's a supported locale.
        :rtype: str
        """
        if v not in supported_locales:
            raise ValueError("Unsupported 'locale' value.")
        return v
