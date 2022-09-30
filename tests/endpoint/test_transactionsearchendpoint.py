import pytest

from yelpfusion3.endpoint.transactionsearchendpoint import TransactionSearchEndpoint


class TestTransactionSearchEndpoint:
    def test_url_location_build(self) -> None:
        transaction_search_endpoint: TransactionSearchEndpoint = (
            TransactionSearchEndpoint(location="800 N Point St San Francisco CA")
        )

        assert (
            transaction_search_endpoint.url()
            == "https://api.yelp.com/v3/transactions/delivery/search?location=800+N+Point+St+San+Francisco+CA"
        )

    def test_url_latitude_longitude_build(self) -> None:
        transaction_search_endpoint: TransactionSearchEndpoint = (
            TransactionSearchEndpoint(latitude=37.80587, longitude=-122.42058)
        )

        assert (
            transaction_search_endpoint.url()
            == "https://api.yelp.com/v3/transactions/delivery/search?latitude=37.80587&longitude=-122.42058"
        )

    @pytest.mark.parametrize("latitude", [-91.0, 92.0])
    def test_latitude_fails_validation(self, latitude: float) -> None:
        with pytest.raises(ValueError):
            TransactionSearchEndpoint(latitude=latitude, longitude=-122.42058)

    @pytest.mark.parametrize("longitude", [-181.0, 182.0])
    def test_longitude_fails_validation(self, longitude: float) -> None:
        with pytest.raises(ValueError):
            TransactionSearchEndpoint(latitude=37.80587, longitude=longitude)
