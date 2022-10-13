import pytest

from yelpfusion3.event.endpoint import EventLookupEndpoint, EventSearchEndpoint


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


class TestEventLookupEndpoint:
    def test_url(self) -> None:
        event_lookup_endpoint: EventLookupEndpoint = EventLookupEndpoint(
            id="oakland-saucy-oakland-restaurant-pop-up"
        )

        assert (
            event_lookup_endpoint.url
            == "https://api.yelp.com/v3/events/oakland-saucy-oakland-restaurant-pop-up"
        )

    def test_url_locale(self) -> None:
        event_lookup_endpoint: EventLookupEndpoint = EventLookupEndpoint(
            id="oakland-saucy-oakland-restaurant-pop-up",
            locale="fr_FR"
        )

        assert (
            event_lookup_endpoint.url
            == "https://api.yelp.com/v3/events/oakland-saucy-oakland-restaurant-pop-up?locale=fr_FR"
        )
