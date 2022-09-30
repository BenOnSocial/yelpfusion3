import pytest

from yelpfusion3.endpoint.phonesearchendpoint import PhoneSearchEndpoint


class TestPhoneSearchEndpoint:
    def test_url_build(self) -> None:
        phone_search_endpoint: PhoneSearchEndpoint = PhoneSearchEndpoint(
            phone="+14159083801"
        )

        assert (
            phone_search_endpoint.url()
            == "https://api.yelp.com/v3/businesses/search/phone?phone=%2B14159083801"
        )

    def test_locale_init_validation(self) -> None:
        phone_search_endpoint: PhoneSearchEndpoint = PhoneSearchEndpoint(
            phone="+14159083801", locale="en_US"
        )

        assert phone_search_endpoint.locale == "en_US"

    def test_locale_validation(self) -> None:
        phone_search_endpoint: PhoneSearchEndpoint = PhoneSearchEndpoint(
            phone="+14159083801"
        )

        phone_search_endpoint.locale = "en_US"

        assert phone_search_endpoint.locale == "en_US"

    def test_locale_fails_validation(self) -> None:
        phone_search_endpoint: PhoneSearchEndpoint = PhoneSearchEndpoint(
            phone="+14159083801"
        )

        with pytest.raises(ValueError):
            phone_search_endpoint.locale = "zz_ZZ"
