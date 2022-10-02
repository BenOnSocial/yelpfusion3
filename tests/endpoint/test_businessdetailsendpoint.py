import pytest

from yelpfusion3.endpoint.businessdetailsendpoint import BusinessDetailsEndpoint


class TestBusinessDetailsEndpoint:
    @pytest.mark.parametrize(
        "business_id",
        [
            "WavvLdfdP6g8aZTtbBQHTw",
            "gary-danko-san-francisco",
        ],
    )
    def test_url_build(self, business_id: str) -> None:
        business_details_endpoint: BusinessDetailsEndpoint = BusinessDetailsEndpoint(
            business_id=business_id
        )

        assert (
            business_details_endpoint.url
            == f"https://api.yelp.com/v3/businesses/{business_id}"
        )

    def test_url_build_with_locale(self) -> None:
        business_details_endpoint: BusinessDetailsEndpoint = BusinessDetailsEndpoint(
            business_id="WavvLdfdP6g8aZTtbBQHTw", locale="en_US"
        )

        assert (
            business_details_endpoint.url
            == "https://api.yelp.com/v3/businesses/WavvLdfdP6g8aZTtbBQHTw?locale=en_US"
        )

    @pytest.mark.parametrize(
        "business_id",
        [
            "W vvLdfdP6g8aZTtbBQHTw",
            "W@vvLdfdP6g8aZTtbBQHTw",
            "gary danko-san-francisco",
            "gary_danko-san-francisco",
        ],
    )
    def test_url_build_fails_on_malformed_id(self, business_id: str) -> None:
        with pytest.raises(ValueError):
            BusinessDetailsEndpoint(business_id=business_id)

    def test_locale_init_validation(self) -> None:
        business_details_endpoint: BusinessDetailsEndpoint = BusinessDetailsEndpoint(
            business_id="WavvLdfdP6g8aZTtbBQHTw", locale="en_US"
        )

        assert business_details_endpoint.locale == "en_US"

    def test_locale_validation(self) -> None:
        business_details_endpoint: BusinessDetailsEndpoint = BusinessDetailsEndpoint(
            business_id="WavvLdfdP6g8aZTtbBQHTw"
        )

        business_details_endpoint.locale = "en_US"

        assert business_details_endpoint.locale == "en_US"

    def test_locale_fails_validation(self) -> None:
        business_details_endpoint: BusinessDetailsEndpoint = BusinessDetailsEndpoint(
            business_id="WavvLdfdP6g8aZTtbBQHTw"
        )

        with pytest.raises(ValueError):
            business_details_endpoint.locale = "zz_ZZ"
