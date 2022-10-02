import pytest

from yelpfusion3.endpoint.businesssearchendpoint import BusinessSearchEndpoint


class TestBusinessSearchEndpoint:
    def test_url_build(self) -> None:
        business_search_endpoint: BusinessSearchEndpoint = BusinessSearchEndpoint(
            term="coffee",
            location="san francisco",
            radius=25,
            limit=20,
            price="1,2",
        )

        assert (
            business_search_endpoint.url
            == "https://api.yelp.com/v3/businesses/search?term=coffee&location=san+francisco&radius=25&limit=20&price=1%2C2"
        )

    def test_unsupported_fields_ignored(self) -> None:
        business_search_endpoint: BusinessSearchEndpoint = BusinessSearchEndpoint(
            term="coffee",
            location="san francisco",
            radius=25,
            limit=20,
            price="1,2",
            unsupported="an unsupported field",
        )

        assert "unsupported" not in [
            key for key, value in dict(business_search_endpoint).items()
        ]
        assert (
            business_search_endpoint.url
            == "https://api.yelp.com/v3/businesses/search?term=coffee&location=san+francisco&radius=25&limit=20&price=1%2C2"
        )

    @pytest.mark.parametrize("latitude", [-90, 0, 90])
    def test_latitude_validation(self, latitude: float) -> None:
        business_search_endpoint: BusinessSearchEndpoint = BusinessSearchEndpoint()

        business_search_endpoint.latitude = latitude

    @pytest.mark.parametrize("latitude", [-91, 91])
    def test_latitude_fails_validation(self, latitude: float) -> None:
        business_search_endpoint: BusinessSearchEndpoint = BusinessSearchEndpoint()

        with pytest.raises(ValueError):
            business_search_endpoint.latitude = latitude

    @pytest.mark.parametrize("longitude", [-180, 0, 180])
    def test_longitude_validation(self, longitude: float) -> None:
        business_search_endpoint: BusinessSearchEndpoint = BusinessSearchEndpoint()

        business_search_endpoint.longitude = longitude

    @pytest.mark.parametrize("longitude", [-181, 181])
    def test_longitude_fails_validation(self, longitude: float) -> None:
        business_search_endpoint: BusinessSearchEndpoint = BusinessSearchEndpoint()

        with pytest.raises(ValueError):
            business_search_endpoint.longitude = longitude

    @pytest.mark.parametrize(
        "locale",
        [
            "es_ES",
            "en_US",
            "fr_FR",
        ],
    )
    def test_locale_validation(self, locale: str) -> None:
        business_search_endpoint: BusinessSearchEndpoint = BusinessSearchEndpoint()

        business_search_endpoint.locale = locale

    def test_locale_fails_validation(self) -> None:
        business_search_endpoint: BusinessSearchEndpoint = BusinessSearchEndpoint()

        with pytest.raises(ValueError):
            business_search_endpoint.locale = "xx_XX"

    @pytest.mark.parametrize(
        "price, expected",
        [
            ("1", "1"),
            ("2", "2"),
            ("3", "3"),
            ("4", "4"),
            ("2,3", "2,3"),
            ("2, 3", "2,3"),
            ("  2  , 3    ", "2,3"),
        ],
    )
    def test_price_validation(self, price: str, expected: str) -> None:
        business_search_endpoint: BusinessSearchEndpoint = BusinessSearchEndpoint()

        business_search_endpoint.price = price

        assert business_search_endpoint.price == expected

    @pytest.mark.parametrize(
        "price", ["0", "5", "4,5", "0,1", "invalid", "", " ", None]
    )
    def test_price_fails_validation(self, price: str) -> None:
        business_search_endpoint: BusinessSearchEndpoint = BusinessSearchEndpoint()

        with pytest.raises(ValueError):
            business_search_endpoint.price = price

    @pytest.mark.parametrize(
        "attributes, expected",
        [
            ("hot_and_new", "hot_and_new"),
            ("request_a_quote", "request_a_quote"),
            ("reservation", "reservation"),
            ("waitlist_reservation", "waitlist_reservation"),
            ("deals", "deals"),
            ("gender_neutral_restrooms", "gender_neutral_restrooms"),
            ("open_to_all", "open_to_all"),
            ("wheelchair_accessible", "wheelchair_accessible"),
            (
                "hot_and_new,reservation,open_to_all",
                "hot_and_new,reservation,open_to_all",
            ),
            (
                " hot_and_new , reservation , open_to_all  ",
                "hot_and_new,reservation,open_to_all",
            ),
        ],
    )
    def test_attributes_validation(self, attributes: str, expected: str) -> None:
        business_search_endpoint: BusinessSearchEndpoint = BusinessSearchEndpoint()

        business_search_endpoint.attributes = attributes

        assert business_search_endpoint.attributes == expected

    @pytest.mark.parametrize("attributes", ["unsupported_attribute", "", " ", None])
    def test_attributes_fails_validation(self, attributes: str) -> None:
        business_search_endpoint: BusinessSearchEndpoint = BusinessSearchEndpoint()

        with pytest.raises(ValueError):
            business_search_endpoint.attributes = attributes
