from __future__ import annotations

from typing import Optional

from yelpfusion3.endpoint.businessdetailsendpoint import BusinessDetailsEndpoint
from yelpfusion3.endpoint.businessmatchesendpoint import BusinessMatchesEndpoint
from yelpfusion3.endpoint.businesssearchendpoint import BusinessSearchEndpoint
from yelpfusion3.endpoint.phonesearchendpoint import PhoneSearchEndpoint
from yelpfusion3.endpoint.transactionsearchendpoint import TransactionSearchEndpoint


class Client:
    """
    Client is a collection of factory methods that create Endpoint objects used to interact with Yelp Fusion endpoints.
    Function parameters provide guidance on which endpoint parameters are required. Optional parameters can be added
    to the instantiated object by setting their respective fields.
    """

    @staticmethod
    def business_details(business_id: str) -> BusinessDetailsEndpoint:
        """
        Creates a new BusinessDetailsEndpoint object used to interact with the Yelp Business Details REST endpoint.

        :param business_id: Unique Yelp ID of the business to query for.
        :type business_id: str
        :return: An endpoint wrapper for the Yelp Business Details REST endpoint.
        :rtype: BusinessDetailsEndpoint
        """
        return BusinessDetailsEndpoint(business_id=business_id)

    @staticmethod
    def business_matches(
        name: str, address1: str, city: str, state: str, country: str
    ) -> BusinessMatchesEndpoint:
        """
        Creates a new BusinessMatchesEndpoint object used to interact with the Yelp Business Matches REST endpoint.

        :param name:
        :type name:
        :param address1:
        :type address1:
        :param city:
        :type city:
        :param state:
        :type state:
        :param country:
        :type country:
        :return:
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
        if location:
            return BusinessSearchEndpoint(location=location)
        elif latitude and longitude:
            return BusinessSearchEndpoint(latitude=latitude, longitude=longitude)
        else:
            raise ValueError("Missing required argument(s).")

    @staticmethod
    def phone_search(phone: str) -> PhoneSearchEndpoint:
        return PhoneSearchEndpoint(phone=phone)

    @staticmethod
    def transaction_search(
        location: Optional[str] = None,
        latitude: Optional[float] = None,
        longitude: Optional[float] = None,
    ) -> TransactionSearchEndpoint:
        if location:
            return TransactionSearchEndpoint(location=location)
        elif latitude and longitude:
            return TransactionSearchEndpoint(latitude=latitude, longitude=longitude)
        else:
            raise ValueError("Missing required argument(s).")
