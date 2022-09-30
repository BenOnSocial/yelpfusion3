from typing import List

from pydantic import BaseModel

from yelpfusion3.model.business.business import Business
from yelpfusion3.model.business.coordinates import Coordinates


class Region(BaseModel):
    """
    Suggested area in a map to display results in.
    """

    center: Coordinates
    """
    Center position of map area.
    """


class BusinessSearch(BaseModel):
    total: int
    """
    Total number of business Yelp finds based on the search criteria. Sometimes, the value may exceed 1000. In such
    case, you still can only get up to 1000 businesses using multiple queries and combinations of the "limit" and
    "offset" parameters.
    """

    businesses: List[Business]
    """
    List of business Yelp finds based on the search criteria.
    """

    region: Region
    """
    Suggested area in a map to display results in.
    """
