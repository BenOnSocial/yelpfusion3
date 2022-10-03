from typing import List, Literal, Optional

from pydantic import HttpUrl, NonNegativeInt, confloat, validator

from yelpfusion3.model.business.category import Category
from yelpfusion3.model.business.coordinates import Coordinates
from yelpfusion3.model.business.location import Location
from yelpfusion3.model.model import Model


class Business(Model):
    """
    Details for a business found with a business search.
    """

    categories: List[Category]
    """
    A list of category title and alias pairs associated with this business.
    """

    coordinates: Optional[Coordinates] = None
    """
    The coordinates of this business.
    """

    display_phone: str
    """
    Phone number of the business formatted nicely to be displayed to users. The format is the standard phone number
    format for the business's country.
    """

    distance: Optional[float] = None
    """
    Distance in meters from the search location. This returns meters regardless of the locale.
    """

    id: str
    """
    Unique Yelp ID of this business. Example: '4kMBvIEWPxWkWKFN__8SxQ'
    """

    alias: str
    """
    Unique Yelp alias of this business. Can contain unicode characters. Example: 'yelp-san-francisco'.
    """

    image_url: Optional[HttpUrl] = None
    """
    URL of photo for this business.
    """

    is_closed: bool
    """
    Whether business has been (permanently) closed
    """

    location: Location
    """
    The location of this business, including address, city, state, zip code and country.
    """

    name: str
    """
    Name of this business.
    """

    phone: Optional[str] = None
    """
    Phone number of the business.
    """

    price: Optional[Literal["$", "$$", "$$$", "$$$$"]] = None
    """
    Price level of the business. Value is one of $, $$, $$$ and $$$$.
    """

    rating: confloat(ge=0.0, le=5.0)  # type: ignore
    """
    Rating for this business (value ranges from 1, 1.5, ... 4.5, 5).
    """

    review_count: NonNegativeInt
    """
    Number of reviews for this business.
    """

    url: HttpUrl
    """
    URL for business page on Yelp.
    """

    transactions: List[Literal["pickup", "delivery", "restaurant_reservation"]]
    """
    A list of Yelp transactions that the business is registered for. Current supported values are "pickup", "delivery",
    and "restaurant_reservation".
    """

    @validator("distance")
    def check_distance(cls, v: float) -> float:
        """
        Checks that "distance" is non-negative.

        :param v: Distance in meters from the search location.
        :type v: float
        :raise ValueError: If "v" is a negative float.
        :return: "v" if it's non-negative.
        :rtype: float
        """
        if v <= 0.0:
            raise ValueError("Cannot have a negative distance.")
        return v

    @validator("rating")
    def check_rating(cls, v: float) -> float:
        """
        Checks that the "rating" value is within the range of 1, 1.5, ... 4.5, 5.

        :param v: Rating for the business.
        :type v: float
        :raise ValueError: If "v" not in the range of 1, 1.5, ... 4.5, 5.
        :return: "v" if it's in the range of 1, 1.5, ... 4.5, 5.
        :rtype: float
        """
        # Avoid using NumPy for this. It's probably overkill here.
        if v in [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]:
            return v
        raise ValueError("Invalid rating value.")
