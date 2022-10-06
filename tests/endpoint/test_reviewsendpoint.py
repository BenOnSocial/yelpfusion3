import pytest

from yelpfusion3.endpoint.reviewsendpoint import ReviewsEndpoint


class TestReviewsEndpoint:
    def test_url_build(self) -> None:
        reviews_endpoint: ReviewsEndpoint = ReviewsEndpoint(
            business_id="WavvLdfdP6g8aZTtbBQHTw"
        )

        assert (
            reviews_endpoint.url
            == "https://api.yelp.com/v3/businesses/WavvLdfdP6g8aZTtbBQHTw/reviews"
        )

    def test_url_build_with_locale(self) -> None:
        reviews_endpoint: ReviewsEndpoint = ReviewsEndpoint(
            business_id="WavvLdfdP6g8aZTtbBQHTw"
        )
        reviews_endpoint.locale = "fr_FR"

        assert (
            reviews_endpoint.url
            == "https://api.yelp.com/v3/businesses/WavvLdfdP6g8aZTtbBQHTw/reviews?locale=fr_FR"
        )

    def test_locale_fails_validation(self) -> None:
        reviews_endpoint: ReviewsEndpoint = ReviewsEndpoint(
            business_id="WavvLdfdP6g8aZTtbBQHTw"
        )

        with pytest.raises(ValueError):
            reviews_endpoint.locale = "zz_ZZ"
