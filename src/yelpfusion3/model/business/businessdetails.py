from typing import List, Literal, Optional

from pydantic import BaseModel, HttpUrl, NonNegativeInt, confloat, validator

from yelpfusion3.model.business.category import Category
from yelpfusion3.model.business.coordinates import Coordinates
from yelpfusion3.model.business.hours import Hours
from yelpfusion3.model.business.location import Location
from yelpfusion3.model.business.specialhours import SpecialHours


class BusinessDetails(BaseModel):
    """
    Detailed information about a business.
    """

    id: str
    """
    Unique Yelp ID of this business. Example: '4kMBvIEWPxWkWKFN__8SxQ'
    """

    alias: str
    """
    Unique Yelp alias of this business. Can contain unicode characters. Example: 'yelp-san-francisco'.
    """

    name: str
    """
    Name of this business.
    """

    image_url: Optional[HttpUrl] = None
    """
    URL of photo for this business.
    """

    is_claimed: bool
    """
    Whether business has been claimed by a business owner
    """

    is_closed: bool
    """
    Whether business has been (permanently) closed
    """

    url: HttpUrl
    """
    URL for business page on Yelp.
    """

    phone: str
    """
    Phone number of the business.
    """

    display_phone: str
    """
    Phone number of the business formatted nicely to be displayed to users. The format is the standard phone number
    format for the business's country.
    """

    review_count: NonNegativeInt
    """
    Number of reviews for this business.
    """

    categories: List[Category]
    """
    A list of category title and alias pairs associated with this business.
    """

    rating: confloat(ge=0.0, le=5.0)  # type: ignore
    """
    Rating for this business (value ranges from 1, 1.5, ... 4.5, 5).
    """

    location: Location
    """
    The location of this business, including address, city, state, zip code and country.
    """

    coordinates: Optional[Coordinates] = None
    """
    The coordinates of this business.
    """

    photos: Optional[List[HttpUrl]]
    """
    URLs of up to three photos of the business.
    """

    price: Literal["$", "$$", "$$$", "$$$$"]
    """
    Price level of the business. Value is one of $, $$, $$$ and $$$$.
    """

    hours: Optional[List[Hours]] = None
    """
    Opening hours of the business.
    """

    transactions: List[Literal["pickup", "delivery", "restaurant_reservation"]]
    """
    A list of Yelp transactions that the business is registered for. Current supported values are "pickup", "delivery",
    and "restaurant_reservation".
    """

    special_hours: Optional[List[SpecialHours]] = None
    """
    Out of the ordinary hours for the business that apply on certain dates. Whenever these are set, they will override
    the regular business hours found in the 'hours' field.
    """

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
