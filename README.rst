yelpfusion3 Documentation
=========================

.. image:: https://dl.circleci.com/status-badge/img/gh/BenOnSocial/yelpfusion3/tree/main.svg?style=shield
   :alt: CI build

.. image:: https://codecov.io/gh/BenOnSocial/yelpfusion3/branch/main/graph/badge.svg?token=LFX14ACT4Y
   :alt: Code Coverage

.. image:: https://readthedocs.org/projects/yelpfusion3/badge/?version=latest
   :alt: Documentation Status

*yelpfusion3* is a Python 3 wrapper for the
`Yelp Fusion 3 API <https://www.yelp.com/developers/documentation/v3/get_started>`_.

Installation
------------

.. code-block:: console

   python -m pip install --upgrade pip
   python -m pip install --upgrade yelpfusion3

Yelp API Key
------------

Sign up for a `Yelp Developers <https://www.yelp.com/developers>`_ account. Yelp's
`Authentication <https://www.yelp.com/developers/documentation/v3/authentication>`_ documentation describes how to
create a new private API key.


Basic Usage
-----------

Set the `YELP_API_KEY` environment variable to be your private API key. Setting the `YELP_API_KEY` environment variable
is currently the only supported method for supplying
your API key to the `yelpfusion3` client.

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

License
-------

yelpfusion3 is released under the MIT License.
