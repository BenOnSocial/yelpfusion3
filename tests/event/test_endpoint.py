import pytest

from yelpfusion3.event.endpoint import EventSearchEndpoint, SupportedCategories
from yelpfusion3.event.model import EventSearch


class TestSupportedCategories:
    @pytest.mark.parametrize(
        "category",
        [
            "music",
            "visual-arts",
            "performing-arts",
            "film",
            "lectures-books",
            "fashion",
            "food-and-drink",
            "festivals-fairs",
            "charities",
            "sports-active-life",
            "nightlife",
            "kids-family",
            "other",
        ],
    )
    def test_contains(self, category: str) -> None:
        assert SupportedCategories.contains(category)

    def test_contains_fails(self) -> None:
        assert not SupportedCategories.contains("not-supported")


class TestEventSearchEndpoint:
    def test_url(self) -> None:
        event_search_endpoint: EventSearchEndpoint = EventSearchEndpoint()

        assert event_search_endpoint.url == "https://api.yelp.com/v3/events"

    @pytest.mark.parametrize(
        "categories",
        [
            "music",
            "food-and-drink",
            "visual-arts,food-and-drink,festivals-fairs,kids-family",
            "sports-active-life,nightlife",
        ],
    )
    def test_valid_categories(self, categories: str) -> None:
        event_search_endpoint: EventSearchEndpoint = EventSearchEndpoint()

        #  Model validation will raise an error if "categories" is malformed or contains invalid categories.
        event_search_endpoint.categories = categories

    @pytest.mark.parametrize(
        "categories",
        [
            "not-supported",
            "music,not-supported",
            "visual-arts,food-and-drink,not-supported,festivals-fairs,kids-family",
        ],
    )
    def test_invalid_categories(self, categories: str) -> None:
        event_search_endpoint: EventSearchEndpoint = EventSearchEndpoint()

        with pytest.raises(ValueError):
            event_search_endpoint.categories = categories

    def test_radius_too_large(self) -> None:
        event_search_endpoint: EventSearchEndpoint = EventSearchEndpoint()

        with pytest.raises(ValueError):
            event_search_endpoint.radius = 40001
