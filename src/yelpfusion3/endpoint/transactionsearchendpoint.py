from typing import Optional

from pydantic import confloat, constr
from requests import Response

from yelpfusion3.endpoint.endpoint import Endpoint
from yelpfusion3.model.business.transactionsearch import TransactionSearch


class TransactionSearchEndpoint(Endpoint):
    """
    This endpoint returns a list of businesses which support food delivery transactions.

    Note: at this time, the API does not return businesses without any reviews.
    """

    _path = "/transactions/delivery/search"

    latitude: Optional[confloat(ge=-90.0, le=90.0)]  # type: ignore
    """
    Required when location isn't provided. Latitude of the location you want to deliver to.
    """

    longitude: Optional[confloat(ge=-180.0, le=180.0)]  # type: ignore
    """
    Required when location isn't provided. Longitude of the location you want to deliver to.
    """

    location: Optional[constr(min_length=1, strip_whitespace=True)]  # type: ignore
    """
    Required when latitude and longitude aren't provided. Address of the location you want to deliver to.
    """

    def get(self) -> TransactionSearch:
        response: Response = self._get()
        return TransactionSearch(**response.json())
