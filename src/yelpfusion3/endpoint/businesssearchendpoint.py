from typing import List, Literal, Optional

import validators
from pydantic import conint, constr, validator
from requests import Response

from yelpfusion3.endpoint import supported_locales
from yelpfusion3.endpoint.endpoint import Endpoint
from yelpfusion3.model.business.businesssearch import BusinessSearch


class BusinessSearchEndpoint(Endpoint):
    """
    This endpoint returns up to 1000 businesses based on the provided search criteria. It has some basic information
    about the business. To get detailed information and reviews, please use the Business ID returned here and refer to
    :py:class:`~yelpfusion3.endpoint.businessdetailsendpoint.BusinessDetailsEndpoint` and
    :py:class:`~yelpfusion3.endpoint.reviewsendpoint.ReviewsEndpoint`.

    Note: at this time, the API does not return businesses without any reviews.
    """

    _path: str = "/businesses/search"

    term: Optional[constr(min_length=1, strip_whitespace=True)]  # type: ignore
    """
    Optional. Search term, for example ``food`` or ``restaurants``. The term may also be business names, such as
    ``Starbucks``. If term is not included the endpoint will default to searching across businesses from a small number
    of popular categories.
    """

    location: Optional[constr(min_length=1, strip_whitespace=True)]  # type: ignore
    """
    Required if either ``latitude`` or ``longitude`` is not provided. This string indicates the geographic area to be
    used when searching for businesses. Examples: ``New York City``, ``NYC``, ``350 5th Ave, New York, NY 10118``.
    Businesses returned in the response may not be strictly within the specified location.
    """

    latitude: Optional[float]
    """
    Required if ``location`` is not provided. Latitude of the location you want to search nearby.
    """

    longitude: Optional[float]
    """
    Required if ``location`` is not provided. Longitude of the location you want to search nearby.
    """

    radius: Optional[conint(gt=0, lt=40000)]  # type: ignore
    """
    Optional. A suggested search radius in meters. This field is used as a suggestion to the search. The actual search
    radius may be lower than the suggested radius in dense urban areas, and higher in regions of less business density.
    If the specified value is too large, a AREA_TOO_LARGE error may be returned. The max value is 40000 meters (about 25
    miles).
    """

    categories: Optional[str]
    """
    Optional. Categories to filter the search results with. See the list of supported categories. The category filter
    can be a list of comma delimited categories. For example, ``bars,french`` will filter by Bars OR French. The
    category identifier should be used (for example ``discgolf``, not ``Disc Golf``).
    """

    locale: Optional[str]
    """
    Optional. Specify the locale into which to localize the business information. See the list of supported locales.
    Defaults to ``en_US``.
    """

    limit: Optional[conint(gt=0, lt=50)]  # type: ignore
    """
    Optional. Number of business results to return. By default, it will return 20. Maximum is 50.
    """

    offset: Optional[conint(gt=0)]  # type: ignore
    """
    Optional. Offset the list of returned business results by this amount.
    """

    sort_by: Optional[Literal["best_match", "rating", "review_count", "distance"]]
    """
    Optional. Suggestion to the search algorithm that the results be sorted by one of the these modes: ``best_match``,
    ``rating``, ``review_count`` or ``distance``. The default is ``best_match``. Note that specifying the sort_by is a
    suggestion (not strictly enforced) to Yelp's search, which considers multiple input parameters to return the most
    relevant results. For example, the rating sort is not strictly sorted by the rating value, but by an adjusted rating
    value that takes into account the number of ratings, similar to a Bayesian average. This is to prevent skewing
    results to businesses with a single review.
    """

    price: Optional[str]
    """
    Optional. Pricing levels to filter the search result with: 1 = $, 2 = $$, 3 = $$$, 4 = $$$$. The price filter can be
    a list of comma delimited pricing levels. For example, ``1, 2, 3`` will filter the results to show the ones that are
    $, $$, or $$$.
    """

    open_now: Optional[bool]
    """
    Optional. Default to ``false``. When set to true, only return the businesses open now. Notice that ``open_at`` and
    ``open_now`` cannot be used together.
    """

    open_at: Optional[conint(gt=0)]  # type: ignore
    """
    Optional. An integer representing the Unix time in the same timezone of the search location. If specified, it will
    return business open at the given time. Notice that ``open_at`` and ``open_now`` cannot be used together.
    """

    attributes: Optional[str]
    """
    Optional. Try these additional filters to return specific search results!
    
        ``hot_and_new`` - popular businesses which recently joined Yelp
        
        ``request_a_quote`` - businesses which actively reply to Request a Quote inquiries
        
        ``reservation`` - businesses with Yelp Reservations bookings enabled on their profile page
        
        ``waitlist_reservation`` - businesses with Yelp Waitlist bookings enabled on their profile screen (iOS/Android)
        
        ``deals`` - businesses offering Yelp Deals on their profile page
        
        ``gender_neutral_restrooms`` - businesses which provide gender neutral restrooms
        
        ``open_to_all`` - businesses which are Open To All
        
        ``wheelchair_accessible`` - businesses which are Wheelchair Accessible
        
        You can combine multiple attributes by providing a comma separated like ``attribute1,attribute2``. If multiple
        attributes are used, only businesses that satisfy ALL attributes will be returned in search results. For
        example, the attributes ``hot_and_new,request_a_quote`` will return businesses that are Hot and New AND offer
        Request a Quote.
    """

    def get(self) -> BusinessSearch:
        response: Response = self._get()
        return BusinessSearch(**response.json())

    @validator("latitude")
    def _check_latitude(cls, v: float) -> float:
        """
        Validates that the ``latitude`` value is within [-90.0, 90.0].

        :param v: Latitude value corresponding to the center of the search location.
        :type v: float
        :raises ValueError: If ``latitude`` is outside of the accepted range of [-90.0, 90.0].
        :return: ``v`` if it's within the accepted range.
        :rtype: float
        """
        if validators.between(value=v, min=-90.0, max=90.0):
            return v
        raise ValueError("'latitude' outside of acceptable range of [-90.0, 90].")

    @validator("longitude")
    def _check_longitude(cls, v: float) -> float:
        """
        Validates that the ``longitude`` value is within [-180.0, 180.0].

        :param v: Longitude value corresponding to the center of the search location.
        :type v: float
        :raises ValueError: If ``longitude`` is outside of the accepted range of [-180.0, 180.0].
        :return: ``v`` if it's within the accepted range.
        :rtype: float
        """
        if validators.between(value=v, min=-180.0, max=180.0):
            return v
        raise ValueError("'longitude' outside of acceptable range of [-180.0, 180.0].")

    @validator("locale")
    def _check_locale(cls, v: str) -> str:
        """
        Validates that the ``locale`` is supported by Yelp Fusion API 3.
        See https://www.yelp.com/developers/documentation/v3/supported_locales

        :param v: Locale of the response body.
        :type v: str
        :raise ValueError: ``v`` is an unsupported locale value.
        :return: ``v`` if it's a supported locale.
        :rtype: str
        """
        if v not in supported_locales:
            raise ValueError("Unsupported 'locale' value.")
        return v

    @validator("price")
    def _check_price(cls, v: str) -> str:
        if v and v.strip():
            levels: List[str] = [level.strip() for level in v.split(sep=",")]
            if all(
                validators.between(value=int(level), min=1, max=4) for level in levels
            ):
                return ",".join(levels)
        raise ValueError("Malformed 'price' value.")

    @validator("attributes")
    def _check_attributes(cls, v: str) -> str:
        if v and v.strip():
            attributes: List[str] = [
                attribute.strip() for attribute in v.split(sep=",")
            ]
            if all(
                attribute
                in [
                    "hot_and_new",
                    "request_a_quote",
                    "reservation",
                    "waitlist_reservation",
                    "deals",
                    "gender_neutral_restrooms",
                    "open_to_all",
                    "wheelchair_accessible",
                ]
                for attribute in attributes
            ):
                return ",".join(attributes)
        raise ValueError("Malformed 'attributes' value.")
