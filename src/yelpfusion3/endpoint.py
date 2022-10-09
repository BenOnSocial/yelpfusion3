from abc import abstractmethod
from urllib.parse import quote, urlencode

import requests
from pydantic import BaseModel
from requests import Response

from yelpfusion3.model import Model
from yelpfusion3.settings import Settings


class Endpoint(BaseModel):
    """
    Basic base class for all endpoint implementations.
    """

    class Config:
        anystr_strip_whitespace = True
        min_anystr_length = 1
        validate_assignment = True

    _path: str

    @property
    def url(self) -> str:
        """
        Constructs a URL to the business search endpoint with the given query parameters.

        :return: Yelp Fusion API 3 endpoint URL.
        :rtype: str
        """
        non_none_fields = {
            key: value for key, value in self.dict().items() if value is not None
        }
        parameters = urlencode(query=non_none_fields, quote_via=quote)
        settings = Settings()
        return f"{settings.base_url}{self._path}?{parameters}"

    @abstractmethod
    def get(self) -> Model:
        pass  # pragma: no cover

    def _get(self) -> Response:
        return requests.get(url=self.url, headers=Settings().headers)
