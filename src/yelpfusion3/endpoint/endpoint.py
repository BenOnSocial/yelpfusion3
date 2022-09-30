from urllib.parse import urlencode

from pydantic import BaseModel
from yelpfusion3.endpoint import base_url


class Endpoint(BaseModel):
    """
    TODO
    """

    class Config:
        validate_assignment = True

    _path: str

    def url(self) -> str:
        """
        Constructs a URL to the business search endpoint with the given query parameters.

        :return: Yelp Fusion API 3 endpoint URL.
        :rtype: str
        """
        non_none_fields = {
            key: value for key, value in self.dict().items() if value is not None
        }
        parameters = urlencode(query=non_none_fields)
        return f"{base_url}{self._path}?{parameters}"
