import pytest

from yelpfusion3.category.endpoint import CategoryDetailsEndpoint


class TestCategoryDetailsEndpoint:
    def test_url(self) -> None:
        category_details_endpoint: CategoryDetailsEndpoint = CategoryDetailsEndpoint(alias="hotdogs")

        assert category_details_endpoint.url == "https://api.yelp.com/v3/categories/hotdogs"

    def test_url_locale(self) -> None:
        category_details_endpoint: CategoryDetailsEndpoint = CategoryDetailsEndpoint(alias="hotdogs", locale="fr_FR")

        assert category_details_endpoint.url == "https://api.yelp.com/v3/categories/hotdogs?locale=fr_FR"

    def test_locale_fails_validation(self) -> None:
        category_details_endpoint: CategoryDetailsEndpoint = CategoryDetailsEndpoint(alias="hotdogs")

        with pytest.raises(ValueError):
            category_details_endpoint.locale = "zz_ZZ"

    def test_missing_required_arguments(self) -> None:
        with pytest.raises(ValueError):
            CategoryDetailsEndpoint()
