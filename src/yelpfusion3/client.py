from __future__ import annotations

from typing import Optional

from pydantic import constr

from yelpfusion3.business.endpoint import (
    BusinessDetailsEndpoint,
    BusinessMatchesEndpoint,
    BusinessSearchEndpoint,
    PhoneSearchEndpoint,
    ReviewsEndpoint,
    TransactionSearchEndpoint,
)


class Client:
    """
    Client is a collection of factory methods that create :py:class:`~yelpfusion3.endpoint.Endpoint` objects used to
    interact with Yelp Fusion endpoints. Function parameters provide guidance on which endpoint parameters are required.
    Optional parameters can be added to the instantiated object by setting their respective fields.
    """

    @staticmethod
    def business_details(business_id: str) -> BusinessDetailsEndpoint:
        """
        Creates a new :py:class:`~yelpfusion3.business.endpoint.BusinessDetailsEndpoint` object used to interact with
        the Yelp Business Details REST endpoint.

        :param business_id: Unique Yelp ID of the business to query for.
        :type business_id: str
        :return: An endpoint wrapper for the Yelp Business Details REST endpoint.
        :rtype: BusinessDetailsEndpoint
        """

        return BusinessDetailsEndpoint(business_id=business_id)

    @staticmethod
    def business_matches(
        name: constr(min_length=1, max_length=64, regex=r"^[\da-zA-Z\s\!#$%&+,./:?@']+$"),  # type: ignore
        address1: constr(min_length=0, max_length=64, regex=r"^[\da-zA-Z\s'/#&,.:]+$"),  # type: ignore
        city: constr(min_length=0, max_length=64, regex=r"^[\da-zA-Z\s'.()]+$"),  # type: ignore
        state: constr(min_length=2, max_length=3, to_upper=True),  # type: ignore
        country: constr(min_length=2, max_length=2, to_upper=True),  # type: ignore
    ) -> BusinessMatchesEndpoint:
        """
        Creates a new :py:class:`~yelpfusion3.business.endpoint.BusinessMatchesEndpoint` object used to interact with
        the Yelp Business Matches REST endpoint.

        :param name: The name of the business. Maximum length is 64; only digits, letters, spaces, and
            ``!#$%&+,­./:?@'`` are allowed.
        :type name: str
        :param address1: The first line of the business’s address. Maximum length is 64; only digits, letters, spaces,
            and ``­’/#&,.:`` are allowed. The empty string "" is allowed; this will specifically match certain service
            businesses that have no street address.
        :type address1: str
        :param city: The city of the business. Maximum length is 64; only digits, letters, spaces, and ``­’.()`` are
            allowed.
        :type city: str
        :param state: The ISO 3166-2 (with a few exceptions) state code of this business.
        :type state: str
        :param country: The ISO 3166-1 alpha-2 country code of this business.
        :type country: str
        :return: An endpoint wrapper for the Yelp Business Match REST endpoint.
        :rtype: BusinessMatchEndpoint
        """

        return BusinessMatchesEndpoint(
            name=name,
            address1=address1,
            city=city,
            state=state,
            country=country,
        )

    @staticmethod
    def business_search(
        location: Optional[str] = None,
        latitude: Optional[float] = None,
        longitude: Optional[float] = None,
    ) -> BusinessSearchEndpoint:
        """
        Creates a new :py:class:`~yelpfusion3.business.endpoint.BusinessSearchEndpoint` object used to interact with the
        Yelp Business Search REST endpoint.

        :param location: This string indicates the geographic area to be used when searching for businesses.
            Examples: ``New York City``, ``NYC``, ``350 5th Ave, New York, NY 10118``. (Required if either ``latitude``
            or ``longitude`` is not provided.)
        :type location: str
        :param latitude: Latitude of the location you want to search nearby. (Required if ``location`` is not provided.)
        :type latitude: float
        :param longitude: Longitude of the location you want to search nearby. (Required if ``location`` is not
            provided.)
        :type longitude: float
        :return: An endpoint wrapper for the Yelp Business Search REST endpoint.
        :rtype: BusinessSearchEndpoint
        """

        if location:
            return BusinessSearchEndpoint(location=location)
        elif latitude and longitude:
            return BusinessSearchEndpoint(latitude=latitude, longitude=longitude)
        else:
            raise ValueError("Missing required argument(s).")

    @staticmethod
    def phone_search(phone: constr(strip_whitespace=True, min_length=12, regex=r"^\+\d+")) -> PhoneSearchEndpoint:  # type: ignore
        """
        Creates a new :py:class:`~yelpfusion3.business.endpoint.PhoneSearchEndpoint` object used to interact with the
        Yelp Phone Search REST endpoint.

        :param phone: Phone number of the business you want to search for. It must start with + and include the country
            code, like ``+14159083801``.
        :type phone: str
        :return: An endpoint wrapper for the Yelp Phone Search REST endpoint.
        :rtype: PhoneSearchEndpoint
        """

        return PhoneSearchEndpoint(phone=phone)

    @staticmethod
    def reviews(business_id: str) -> ReviewsEndpoint:
        """
        Creates a new :py:class:`~yelpfusion3.business.endpoint.ReviewsEndpoint` object used to interact with the Yelp
        Reviews REST endpoint.

        :param business_id: Unique Yelp ID of the business to query for.
        :type business_id: str
        :return: An endpoint wrapper for the Yelp Reviews REST endpoint.
        :rtype: ReviewsEndpoint
        """
        return ReviewsEndpoint(business_id=business_id)

    @staticmethod
    def transaction_search(
        location: Optional[str] = None,
        latitude: Optional[float] = None,
        longitude: Optional[float] = None,
    ) -> TransactionSearchEndpoint:
        """
        Creates a new :py:class:`~yelpfusion3.business.endpoint.TransactionSearchEndpoint` object used to interact with
        the Yelp Transaction Search REST endpoint.

        :param location: This string indicates the geographic area to be used when searching for businesses.
            Examples: ``New York City``, ``NYC``, ``350 5th Ave, New York, NY 10118``. (Required if either ``latitude``
            or ``longitude`` is not provided.)
        :type location: str
        :param latitude: Latitude of the location you want to search nearby. (Required if ``location`` is not provided.)
        :type latitude: float
        :param longitude: Longitude of the location you want to search nearby. (Required if ``location`` is not
            provided.)
        :type longitude: float
        :return: An endpoint wrapper for the Yelp Transaction Search REST endpoint.
        :rtype: TransactionSearchEndpoint
        """

        if location:
            return TransactionSearchEndpoint(location=location)
        elif latitude and longitude:
            return TransactionSearchEndpoint(latitude=latitude, longitude=longitude)
        else:
            raise ValueError("Missing required argument(s).")
