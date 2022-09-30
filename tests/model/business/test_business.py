import pytest

from yelpfusion3.model.business.business import Business

test_data: dict = {
    "id": "E8RJkjfdcwgtyoPMjQ_Olg",
    "alias": "four-barrel-coffee-san-francisco",
    "name": "Four Barrel Coffee",
    "image_url": "https://s3-media1.fl.yelpcdn.com/bphoto/e_urruIKpneV8yAXkAK9RA/o.jpg",
    "is_closed": False,
    "url": "https://www.yelp.com/biz/four-barrel-coffee-san-francisco?adjust_creative=iLXKG_naOtwkmDCMRoHImA&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=iLXKG_naOtwkmDCMRoHImA",
    "review_count": 2154,
    "categories": [{"alias": "coffee", "title": "Coffee & Tea"}],
    "rating": 4.0,
    "coordinates": {"latitude": 37.7670169511878, "longitude": -122.42184275},
    "transactions": ["delivery"],
    "price": "$$",
    "location": {
        "address1": "375 Valencia St",
        "address2": "",
        "address3": "",
        "city": "San Francisco",
        "zip_code": "94103",
        "country": "US",
        "state": "CA",
        "display_address": ["375 Valencia St", "San Francisco, CA 94103"],
    },
    "phone": "+14158964289",
    "display_phone": "(415) 896-4289",
    "distance": 1452.8696502343696,
}


class TestBusiness:
    def test_deserialization(self) -> None:
        business: Business = Business(**test_data)

        assert business.id == "E8RJkjfdcwgtyoPMjQ_Olg"
        assert business.alias == "four-barrel-coffee-san-francisco"
        assert business.name == "Four Barrel Coffee"
        assert (
            business.image_url
            == "https://s3-media1.fl.yelpcdn.com/bphoto/e_urruIKpneV8yAXkAK9RA/o.jpg"
        )
        assert not business.is_closed
        assert (
            business.url
            == "https://www.yelp.com/biz/four-barrel-coffee-san-francisco?adjust_creative=iLXKG_naOtwkmDCMRoHImA&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=iLXKG_naOtwkmDCMRoHImA"
        )
        assert business.review_count == 2154
        assert business.categories[0].alias == "coffee"
        assert business.categories[0].title == "Coffee & Tea"
        assert business.rating == 4.0
        assert business.coordinates.latitude == 37.7670169511878
        assert business.coordinates.longitude == -122.42184275
        assert business.transactions == ["delivery"]
        assert business.price == "$$"
        assert business.location.address1 == "375 Valencia St"
        assert not business.location.address2
        assert not business.location.address3
        assert business.location.city == "San Francisco"
        assert business.location.zip_code == "94103"
        assert business.location.country == "US"
        assert business.location.state == "CA"
        assert business.location.display_address[0] == "375 Valencia St"
        assert business.location.display_address[1] == "San Francisco, CA 94103"
        assert business.phone == "+14158964289"
        assert business.display_phone == "(415) 896-4289"
        assert business.distance == 1452.8696502343696

    def test_distance_fails_validation(self) -> None:
        invalid_test_data: dict = test_data.copy()
        invalid_test_data["distance"] = -1.0

        with pytest.raises(ValueError):
            Business(**invalid_test_data)

    @pytest.mark.parametrize("rating", [-1.0, 0.1, 5.1, 6.0])
    def test_rating_fails_validation(self, rating: float) -> None:
        invalid_test_data: dict = test_data.copy()
        invalid_test_data["rating"] = rating

        with pytest.raises(ValueError):
            Business(**invalid_test_data)

    def test_location_country_fails_validation(self) -> None:
        invalid_test_data: dict = test_data.copy()
        invalid_test_data["location"]["country"] = "ZZ"

        with pytest.raises(ValueError):
            Business(**invalid_test_data)
