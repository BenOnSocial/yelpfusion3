from typing import List, Optional

from yelpfusion3.model.business.coordinates import Coordinates
from yelpfusion3.model.business.location import Location
from yelpfusion3.model.model import Model


class BusinessMatch(Model):
    """
    A Yelp business matching the inputs.
    """

    id: str
    """
    Unique Yelp ID of this business. Example: ``4kMBvIEWPxWkWKFN__8SxQ``
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
    Street, city, state, country, etc. Same as the ``location`` in search.
    """

    coordinates: Optional[Coordinates] = None
    """
    Latitude and longitude, if available. Same as the ``coordinates`` in search.
    """

    phone: str
    """
    The business's phone number.
    """


class BusinessMatches(Model):
    """
    List of Yelp business matches.
    """

    businesses: List[BusinessMatch]
    """
    List of Yelp business matches.
    """
