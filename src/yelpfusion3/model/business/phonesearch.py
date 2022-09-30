from typing import List

from pydantic import BaseModel, NonNegativeInt

from yelpfusion3.model.business.business import Business


class PhoneSearch(BaseModel):
    """
    A list of businesses based on the provided phone number.
    """

    total: NonNegativeInt
    """
    The total number of business Yelp finds based on the search criteria. Sometimes, the value may exceed 1000. In such
    case, you still can only get up to 1000 businesses.
    """

    businesses: List[Business]
    """
    A list of business Yelp finds based on the search criteria.
    """
