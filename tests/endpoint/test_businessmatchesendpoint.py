import pytest

from yelpfusion3.endpoint.businessmatchesendpoint import BusinessMatchesEndpoint


class TestBusinessMatchesEndpoint:
    def test_url_build(self) -> None:
        business_matches_endpoint: BusinessMatchesEndpoint = BusinessMatchesEndpoint(
            name="Gary Danko",
            address1="800 N Point St",
            city="San Francisco",
            state="CA",
            country="US",
        )

        assert (
            business_matches_endpoint.url
            == "https://api.yelp.com/v3/businesses/matches?name=Gary+Danko&address1=800+N+Point+St&city=San+Francisco&state=CA&country=US"
        )

    def test_country_init_fails_validation(self) -> None:
        with pytest.raises(ValueError):
            BusinessMatchesEndpoint(
                name="Gary Danko",
                address1="800 N Point St",
                city="San Francisco",
                state="CA",
                country="ZZ",
            )

    def test_country_fails_validation(self) -> None:
        business_match_endpoint: BusinessMatchesEndpoint = BusinessMatchesEndpoint(
            name="Gary Danko",
            address1="800 N Point St",
            city="San Francisco",
            state="CA",
            country="US",
        )

        with pytest.raises(ValueError):
            business_match_endpoint.country = "ZZ"
