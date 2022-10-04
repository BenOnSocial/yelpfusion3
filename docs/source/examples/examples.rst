Endpoint Usage
==============

Getting detailed information about a business
---------------------------------------------

The `Business Details endpoint <https://www.yelp.com/developers/documentation/v3/business>`_ returns detailed business
content, given its unique Yelp business ID. Here's an example showing how to get this information for Gary Danko in
San Francisco.

.. code-block:: python
    :caption: Get details for a business using its unique Yelp business ID

    from yelpfusion3.client import Client
    from yelpfusion3.endpoint.businessdetailsendpoint import BusinessDetailsEndpoint
    from yelpfusion3.model.business.businessdetails import BusinessDetails

    # Get business details for Gary Danko in San Francisco using its Yelp business ID.
    business_details_endpoint: BusinessDetailsEndpoint = Client.business_details(
        "WavvLdfdP6g8aZTtbBQHTw"
    )

    business_details: BusinessDetails = business_details_endpoint.get()


Finding businesses around a given address
-----------------------------------------

The `Business Search endpoint <https://www.yelp.com/developers/documentation/v3/business_search>`_ returns up to 1,000
businesses based on the provided search criteria. Here's an example showing how to search for businesses within a mile
radius of a given street address.

.. code-block:: python
    :caption: Find businesses within a 1,609 meter (~1 mile) radius of a given address

    business_search_endpoint: BusinessSearchEndpoint = Client.business_search(
        location="800 N Point St, San Francisco, CA 94109"
    )
    business_search_endpoint.radius = 1609

    business_search: BusinessSearch = business_search_endpoint.get()
