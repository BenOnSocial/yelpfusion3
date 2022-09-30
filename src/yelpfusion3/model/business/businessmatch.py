from typing import Optional

from pydantic import BaseModel

from yelpfusion3.model.business.coordinates import Coordinates
from yelpfusion3.model.business.location import Location


class BusinessMatch(BaseModel):
    """
    A Yelp business matching the inputs.
    """

    id: str
    """
    Unique Yelp ID of this business. Example: '4kMBvIEWPxWkWKFN__8SxQ'
    """

    alias: str
    """
    Unique Yelp alias of this business. Can contain unicode characters.
    """

    name: str
    """
    Name of this business.
    """

    location: Location
    """
    Street, city, state, country, etc. Same as the "location" in search.
    """

    coordinates: Optional[Coordinates]
    """
    Latitude and longitude, if available. Same as the "coordinates" in search.
    """

    phone: str
    """
    The business's phone number.
    """
