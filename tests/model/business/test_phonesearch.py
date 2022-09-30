from yelpfusion3.model.business.phonesearch import PhoneSearch

test_data = {
    "businesses": [
        {
            "id": "WavvLdfdP6g8aZTtbBQHTw",
            "alias": "gary-danko-san-francisco",
            "name": "Gary Danko",
            "image_url": "https://s3-media0.fl.yelpcdn.com/bphoto/eyYUz3Xl7NtcJeN7x7SQwg/o.jpg",
            "is_closed": False,
            "url": "https://www.yelp.com/biz/gary-danko-san-francisco?adjust_creative=iLXKG_naOtwkmDCMRoHImA&utm_campaign=yelp_api_v3&utm_medium=api_v3_phone_search&utm_source=iLXKG_naOtwkmDCMRoHImA",
            "review_count": 5733,
            "categories": [
                {"alias": "newamerican", "title": "American (New)"},
                {"alias": "french", "title": "French"},
                {"alias": "wine_bars", "title": "Wine Bars"},
            ],
            "rating": 4.5,
            "coordinates": {"latitude": 37.80587, "longitude": -122.42058},
            "transactions": [],
            "price": "$$$$",
            "location": {
                "address1": "800 N Point St",
                "address2": "",
                "address3": "",
                "city": "San Francisco",
                "zip_code": "94109",
                "country": "US",
                "state": "CA",
                "display_address": ["800 N Point St", "San Francisco, CA 94109"],
            },
            "phone": "+14157492060",
            "display_phone": "(415) 749-2060",
        }
    ],
    "total": 1,
}


class TestPhoneSearch:
    def test_deserialization(self) -> None:
        phone_search: PhoneSearch = PhoneSearch(**test_data)

        assert phone_search.total == 1

        assert phone_search.businesses[0].id == "WavvLdfdP6g8aZTtbBQHTw"
        assert phone_search.businesses[0].alias == "gary-danko-san-francisco"
        assert phone_search.businesses[0].name == "Gary Danko"
        assert phone_search.businesses[0].review_count == 5733
        assert phone_search.businesses[0].rating == 4.5
        assert phone_search.businesses[0].coordinates.latitude == 37.80587
        assert phone_search.businesses[0].coordinates.longitude == -122.42058
