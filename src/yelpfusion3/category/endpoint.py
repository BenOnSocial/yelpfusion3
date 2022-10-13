from typing import Optional
from urllib.parse import urlencode

from pydantic import constr
from requests import Response

from yelpfusion3.category.model import CategoryDetails
from yelpfusion3.endpoint import Endpoint
from yelpfusion3.settings import Settings


class CategoryDetailsEndpoint(Endpoint):
    """
    This endpoint returns detailed information about the Yelp category specified by a Yelp category alias.
    """

    _path: str = "/categories/{alias}"

    locale: Optional[str]
    """
    Optional. Specify the locale to return the autocomplete suggestions in. See the list of supported locales. Defaults
    to ``en_US``.
    """

    alias: constr(min_length=1)
    """
    Required. Specify the alias of the category.
    """

    @property
    def url(self) -> str:
        """
        Constructs a URL to the category details endpoint with the given query parameters.

        :return: Yelp Fusion API 3 endpoint URL.
        :rtype: str
        """
        non_none_fields = {key: value for key, value in self.dict().items() if value is not None and key != "alias"}
        parameters = urlencode(query=non_none_fields)
        settings: Settings = Settings()
        path: str = self._path.format(alias=self.alias)

        if parameters:
            return f"{settings.base_url}{path}?{parameters}"
        else:
            return f"{settings.base_url}{path}"

    def get(self) -> CategoryDetails:
        response: Response = self._get()
        return CategoryDetails(**response.json())
