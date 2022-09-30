from typing import Dict

import pytest

from yelpfusion3.model.business.businessdetails import BusinessDetails

test_data = {
    "id": "WavvLdfdP6g8aZTtbBQHTw",
    "alias": "gary-danko-san-francisco",
    "name": "Gary Danko",
    "image_url": "https://s3-media2.fl.yelpcdn.com/bphoto/CPc91bGzKBe95aM5edjhhQ/o.jpg",
    "is_claimed": True,
    "is_closed": False,
    "url": "https://www.yelp.com/biz/gary-danko-san-francisco?adjust_creative=wpr6gw4FnptTrk1CeT8POg&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_lookup&utm_source=wpr6gw4FnptTrk1CeT8POg",  # NOQA
    "phone": "+14157492060",
    "display_phone": "(415) 749-2060",
    "review_count": 5296,
    "categories": [
        {"alias": "newamerican", "title": "American (New)"},
        {"alias": "french", "title": "French"},
        {"alias": "wine_bars", "title": "Wine Bars"},
    ],
    "rating": 4.5,
    "location": {
        "address1": "800 N Point St",
        "address2": "",
        "address3": "",
        "city": "San Francisco",
        "zip_code": "94109",
        "country": "US",
        "state": "CA",
        "display_address": ["800 N Point St", "San Francisco, CA 94109"],
        "cross_streets": "",
    },
    "coordinates": {"latitude": 37.80587, "longitude": -122.42058},
    "photos": [
        "https://s3-media2.fl.yelpcdn.com/bphoto/CPc91bGzKBe95aM5edjhhQ/o.jpg",
        "https://s3-media4.fl.yelpcdn.com/bphoto/FmXn6cYO1Mm03UNO5cbOqw/o.jpg",
        "https://s3-media4.fl.yelpcdn.com/bphoto/HZVDyYaghwPl2kVbvHuHjA/o.jpg",
    ],
    "price": "$$$$",
    "hours": [
        {
            "open": [
                {"is_overnight": False, "start": "1730", "end": "2200", "day": 0},
                {"is_overnight": False, "start": "1731", "end": "2200", "day": 1},
                {"is_overnight": False, "start": "1732", "end": "2200", "day": 2},
                {"is_overnight": False, "start": "1733", "end": "2200", "day": 3},
                {"is_overnight": False, "start": "1734", "end": "2200", "day": 4},
                {"is_overnight": False, "start": "1735", "end": "2200", "day": 5},
                {"is_overnight": False, "start": "1736", "end": "2200", "day": 6},
            ],
            "hours_type": "REGULAR",
            "is_open_now": False,
        }
    ],
    "transactions": [],
    "special_hours": [
        {
            "date": "2019-02-07",
            "is_closed": None,
            "start": "1600",
            "end": "2000",
            "is_overnight": False,
        }
    ],
}


class TestBusinessDetails:
    def test_deserialization(self) -> None:
        business_details: BusinessDetails = BusinessDetails(**test_data)

        assert business_details.hours[0].open[0].start == "1730"

    @pytest.mark.parametrize("rating", [-1.0, 0.1, 5.1, 6.0])
    def test_rating_fails_validation(self, rating: float) -> None:
        invalid_test_data: Dict[str, object] = test_data.copy()
        invalid_test_data["rating"] = rating

        with pytest.raises(ValueError):
            BusinessDetails(**invalid_test_data)
