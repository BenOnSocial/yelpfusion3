import os

import pytest

from yelpfusion3.client import Client
from yelpfusion3.endpoint.businessdetailsendpoint import BusinessDetailsEndpoint
from yelpfusion3.endpoint.businessmatchesendpoint import BusinessMatchesEndpoint
from yelpfusion3.endpoint.businesssearchendpoint import BusinessSearchEndpoint
from yelpfusion3.endpoint.phonesearchendpoint import PhoneSearchEndpoint
from yelpfusion3.endpoint.reviewsendpoint import ReviewsEndpoint
from yelpfusion3.endpoint.transactionsearchendpoint import TransactionSearchEndpoint
from yelpfusion3.model.business.businessdetails import BusinessDetails
from yelpfusion3.model.business.businessmatches import BusinessMatches
from yelpfusion3.model.business.businesssearch import BusinessSearch
from yelpfusion3.model.business.phonesearch import PhoneSearch
from yelpfusion3.model.business.reviews import Reviews
from yelpfusion3.model.business.transactionsearch import TransactionSearch


@pytest.mark.skipif(
    condition=not os.getenv("YELP_API_KEY"), reason="API key not configured"
)
class TestClient:
    def test_business_details(self) -> None:
        business_details_endpoint: BusinessDetailsEndpoint = Client.business_details(
            business_id="WavvLdfdP6g8aZTtbBQHTw"
        )

        business_details: BusinessDetails = business_details_endpoint.get()

        assert business_details.id == "WavvLdfdP6g8aZTtbBQHTw"
        assert business_details.alias == "gary-danko-san-francisco"
        assert business_details.name == "Gary Danko"
        assert business_details.phone == "+14157492060"
        assert business_details.location.address1 == "800 N Point St"
        assert business_details.location.address2 == ""
        assert business_details.location.address3 == ""
        assert business_details.location.city == "San Francisco"
        assert business_details.location.zip_code == "94109"
        assert business_details.location.country == "US"
        assert business_details.location.state == "CA"

    def test_business_matches(self) -> None:
        business_matches_endpoint: BusinessMatchesEndpoint = Client.business_matches(
            name="Gary Danko",
            address1="800 N Point St",
            city="San Francisco",
            state="CA",
            country="US",
        )

        business_matches: BusinessMatches = business_matches_endpoint.get()

        assert business_matches.businesses[0].id == "WavvLdfdP6g8aZTtbBQHTw"
        assert business_matches.businesses[0].alias == "gary-danko-san-francisco"
        assert business_matches.businesses[0].name == "Gary Danko"
        assert business_matches.businesses[0].phone == "+14157492060"
        assert business_matches.businesses[0].location.address1 == "800 N Point St"
        assert business_matches.businesses[0].location.address2 == ""
        assert business_matches.businesses[0].location.address3 == ""
        assert business_matches.businesses[0].location.city == "San Francisco"
        assert business_matches.businesses[0].location.zip_code == "94109"
        assert business_matches.businesses[0].location.country == "US"
        assert business_matches.businesses[0].location.state == "CA"

    def test_business_search_by_location(self) -> None:
        business_search_endpoint: BusinessSearchEndpoint = Client.business_search(
            location="20488 Stevens Creek Blvd, Cupertino, CA 95014"
        )
        business_search_endpoint.radius = 1609

        business_search: BusinessSearch = business_search_endpoint.get()

        assert business_search.total > 0
        assert all(
            business.location.city == "Cupertino"
            for business in business_search.businesses
        )

    def test_business_search_by_latitude_longitude(self) -> None:
        business_search_endpoint: BusinessSearchEndpoint = Client.business_search(
            latitude=37.32238222393683, longitude=-122.0306396484375
        )
        business_search_endpoint.radius = 1609

        business_search: BusinessSearch = business_search_endpoint.get()

        assert business_search.total > 0
        assert all(
            business.location.city == "Cupertino"
            for business in business_search.businesses
        )

    def test_business_search_missing_arguments_raises_error(self) -> None:
        with pytest.raises(ValueError):
            Client.business_search()

    def test_business_search_missing_longitude_raises_error(self) -> None:
        with pytest.raises(ValueError):
            Client.business_search(latitude=37.32238222393683)

    def test_business_search_missing_latitude_raises_error(self) -> None:
        with pytest.raises(ValueError):
            Client.business_search(longitude=-122.0306396484375)

    def test_phone_search(self) -> None:
        phone_search_endpoint: PhoneSearchEndpoint = Client.phone_search(
            phone="+14157492060"
        )

        phone_search: PhoneSearch = phone_search_endpoint.get()

        assert phone_search.total > 0
        assert phone_search.businesses[0].phone == "+14157492060"
        assert phone_search.businesses[0].id == "WavvLdfdP6g8aZTtbBQHTw"
        assert phone_search.businesses[0].alias == "gary-danko-san-francisco"
        assert phone_search.businesses[0].name == "Gary Danko"

    def test_phone_search_no_matches(self) -> None:
        phone_search_endpoint: PhoneSearchEndpoint = Client.phone_search(
            phone="+10000000000"
        )

        phone_search: PhoneSearch = phone_search_endpoint.get()

        assert phone_search.total == 0
        assert not phone_search.businesses

    def test_reviews(self) -> None:
        reviews_endpoint: ReviewsEndpoint = Client.reviews(
            business_id="WavvLdfdP6g8aZTtbBQHTw"
        )

        reviews: Reviews = reviews_endpoint.get()

        # "total" returns the total number of reviews that a business has.
        assert reviews.total > 3
        # The "reviews" list returns a maximum of 3 reviews.
        assert len(reviews.reviews) == 3
        assert "en" in reviews.possible_languages

    def test_transaction_search_by_location(self) -> None:
        transaction_search_endpoint: TransactionSearchEndpoint = (
            Client.transaction_search(
                location="20488 Stevens Creek Blvd, Cupertino, CA 95014"
            )
        )

        transaction_search: TransactionSearch = transaction_search_endpoint.get()

        assert transaction_search.total > 0
        assert all(
            "delivery" in business.transactions
            for business in transaction_search.businesses
        )

    def test_transaction_search_by_latitude_longitude(self) -> None:
        transaction_search_endpoint: TransactionSearchEndpoint = (
            Client.transaction_search(
                latitude=37.32238222393683, longitude=-122.0306396484375
            )
        )

        transaction_search: TransactionSearch = transaction_search_endpoint.get()

        assert transaction_search.total > 0
        assert all(
            "delivery" in business.transactions
            for business in transaction_search.businesses
        )

    def test_transaction_search_missing_arguments_raises_error(self) -> None:
        with pytest.raises(ValueError):
            Client.transaction_search()

    def test_transaction_search_missing_longitude_raises_error(self) -> None:
        with pytest.raises(ValueError):
            Client.transaction_search(latitude=37.32238222393683)

    def test_transaction_search_missing_latitude_raises_error(self) -> None:
        with pytest.raises(ValueError):
            Client.transaction_search(longitude=-122.0306396484375)
