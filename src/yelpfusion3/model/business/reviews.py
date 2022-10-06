from datetime import datetime
from typing import List, Literal, Optional

from pydantic import HttpUrl, NonNegativeInt, constr

from yelpfusion3.model.model import Model


class User(Model):
    """
    A user who wrote a review.
    """

    id: constr(strip_whitespace=True, min_length=1)  # type: ignore
    """
    ID of the user.
    """

    profile_url: HttpUrl
    """
    URL of the user's profile.
    """

    name: constr(strip_whitespace=True, min_length=1)  # type: ignore
    """
    User screen name (first name and first initial of last name).
    """

    image_url: Optional[HttpUrl] = None
    """
    URL of the user's profile photo.
    """


class Review(Model):
    """
    A review excerpt for a given business.
    """

    id: constr(strip_whitespace=True, min_length=1)  # type: ignore
    """
    A unique identifier for this review.
    """

    text: constr(strip_whitespace=True, min_length=0)  # type: ignore
    """
    Text excerpt of this review.
    """

    url: HttpUrl
    """
    URL of this review.
    """

    rating: Literal[1, 2, 3, 4, 5]
    """
    Rating of this review.
    """

    time_created: datetime
    """
    The time that the review was created in PST.
    """

    user: User
    """
    The user who wrote the review.
    """


class Reviews(Model):
    """
    Review excerpts for a given business.
    """

    total: NonNegativeInt
    """
    The total number of reviews that the business has.
    """

    possible_languages: List[str]
    """
    A list of languages for which the business has at least one review.
    """

    reviews: List[Review]
    """
    A list of up to three reviews of this business.
    """
