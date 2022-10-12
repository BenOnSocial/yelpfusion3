from datetime import datetime
from typing import Dict, List, Literal, Optional

from pydantic import confloat, conint, constr, validator
from requests import Response

from yelpfusion3.endpoint import Endpoint
from yelpfusion3.event.model import EventSearch


class SupportedCategories:
    """
    A collection of categories supported by the Yelp Fusion API's Event Search endpoint.
    See `Supported Categories <https://www.yelp.com/developers/documentation/v3/event_categories_list>`_
    """

    categories: Dict = {
        "Music": "music",
        "Visual Arts": "visual-arts",
        "Performing Arts": "performing-arts",
        "Film": "film",
        "Lectures & Books": "lectures-books",
        "Fashion": "fashion",
        "Food & Drink": "food-and-drink",
        "Festivals & Fairs": "festivals-fairs",
        "Charities": "charities",
        "Sports & Active Life": "sports-active-life",
        "Nightlife": "nightlife",
        "Kids & Family": "kids-family",
        "Other": "other",
    }

    @staticmethod
    def contains(
        value: constr(strip_whitespace=True, to_lower=True, min_length=1)
    ) -> bool:
        return value in SupportedCategories.categories.values()


class EventSearchEndpoint(Endpoint):
    """
    This endpoint returns events based on the provided search criteria.
    """

    _path: str = "/events"

    locale: Optional[str] = None
    """
    Optional. Specify the locale to return the event information in. See the list of supported locales. Defaults to
    ``en_US``.
    """

    offset: Optional[int] = None
    """
    Optional. Offset the list of returned events by this amount.
    """

    limit: Optional[conint(ge=0, le=50)] = None
    """
    Optional. Number of events results to return. By default, it will return ``3``. Maximum is ``50``.
    """

    sort_by: Optional[Literal["desc", "asc"]] = None
    """
    Optional. Sort by either descending or ascending order. By default, it returns results in descending order.
    Possible values are:
    
        ``desc`` - sort by descending order
        
        ``asc`` - sort by ascending order
    """

    sort_on: Optional[Literal["popularity", "time_start"]] = None
    """
    Optional. Sort on popularity or time start. By default, sorts on ``popularity``. Possible values are:
    
        ``popularity``

        ``time_start``
    """

    start_date: Optional[datetime] = None
    """
    Optional. Unix timestamp. Will return events that only begin at or after the specified time. Value must be in the
    range ``-2208960000`` <= ``start_date`` <= ``221845420800``.
    """

    end_date: Optional[datetime] = None
    """
    Optional. Unix timestamp. Will return events that only end at or before the specified time. Value must be in the
    range ``-2208960000`` <= ``end_date`` <= ``221845420800``.
    """

    categories: Optional[constr(to_lower=True)] = None
    """
    Optional. The category filter can be a list of comma delimited categories to get OR'd results that include the
    categories provided. See :py:class:`~yelpfusion3.event.endpoint.SupportedCategories`.
    """

    is_free: Optional[bool] = None
    """
    Optional. Filter whether the events are free to attend. By default no filter is applied so both free and paid events
    will be returned.
    """

    location: Optional[constr(min_length=1)] = None
    """
    Optional. Specifies the combination of "address, neighborhood, city, state or zip, optional country" to be used when
    searching for events.
    """

    latitude: Optional[confloat(ge=-90.0, le=90.0)] = None
    """
    Optional. Latitude of the location you want to search nearby. If latitude is provided, longitude is required too.
    """

    longitude: Optional[confloat(ge=-180.0, le=180.0)] = None
    """
    Optional. Longitude of the location you want to search nearby. If longitude is provided, latitude is required too.
    """

    radius: Optional[conint(gt=0, le=40000)] = None
    """
    Optional. Search radius in meters. If the value is too large, a ``AREA_TOO_LARGE`` error may be returned. The max
    value is ``40000`` meters (about 25 miles).
    """

    excluded_events: Optional[constr(min_length=1)] = None
    """
    Optional. List of event ids. Events associated with these event ids in this list will not show up in the response.
    """

    def get(self) -> EventSearch:
        response: Response = self._get()
        print(response.json())
        return EventSearch(**response.json())

    @validator("categories")
    def _check_categories(cls, v: str) -> str:
        """
        Checks that ``v`` is a valid list of supported categories.

        :param v: Comma-separated list of categories.
        :type v: str
        :raise ValueError: If at least one category in the list is unsupported.
        :return: A normalized list of categories.
        :rtype: str
        """

        # We could have done the validation in the "regex" argument to constr(), but it would be a lot more complicated
        # and not very readable.
        categories: List[str] = [
            category.strip() for category in v.split(sep=",") if category.strip()
        ]

        if all(SupportedCategories.contains(category) for category in categories):
            return ",".join(categories)

        raise ValueError("'categories' field contains unsupported categories.")
