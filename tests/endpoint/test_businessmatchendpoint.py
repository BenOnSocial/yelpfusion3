import pytest

from yelpfusion3.endpoint.businessmatchendpoint import BusinessMatchEndpoint


class TestBusinessMatchEndpoint:
    def test_url_build(self) -> None:
        business_match_endpoint: BusinessMatchEndpoint = BusinessMatchEndpoint(
            name="Gary Danko",
            address1="800 N Point St",
            city="San Francisco",
            state="CA",
            country="US",
        )

        assert (
            business_match_endpoint.url()
            == "https://api.yelp.com/v3/businesses/matches?name=Gary+Danko&address1=800+N+Point+St&city=San+Francisco&state=CA&country=US"
        )

    def test_country_init_fails_validation(self) -> None:
        with pytest.raises(ValueError):
            BusinessMatchEndpoint(
                name="Gary Danko",
                address1="800 N Point St",
                city="San Francisco",
                state="CA",
                country="ZZ",
            )

    def test_country_fails_validation(self) -> None:
        business_match_endpoint: BusinessMatchEndpoint = BusinessMatchEndpoint(
            name="Gary Danko",
            address1="800 N Point St",
            city="San Francisco",
            state="CA",
            country="US",
        )

        with pytest.raises(ValueError):
            business_match_endpoint.country = "ZZ"
