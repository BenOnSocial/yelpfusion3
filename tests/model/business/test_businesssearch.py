from yelpfusion3.model.business.businesssearch import BusinessSearch

test_data = {
    "businesses": [
        {
            "id": "DaOQgNk4LjN2gbvYrLQGvA",
            "alias": "rise-and-grind-coffee-and-tea-san-francisco-6",
            "name": "Rise & Grind Coffee and Tea",
            "image_url": "https://s3-media3.fl.yelpcdn.com/bphoto/P3nSiVthgTWO4zZJjMsdkg/o.jpg",
            "is_closed": False,
            "url": "https://www.yelp.com/biz/rise-and-grind-coffee-and-tea-san-francisco-6?adjust_creative=iLXKG_naOtwkmDCMRoHImA&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=iLXKG_naOtwkmDCMRoHImA",
            "review_count": 373,
            "categories": [{"alias": "coffee", "title": "Coffee & Tea"}],
            "rating": 4.5,
            "coordinates": {"latitude": 37.7737156, "longitude": -122.4660674},
            "transactions": ["delivery", "pickup"],
            "price": "$$",
            "location": {
                "address1": "785 8th Ave",
                "address2": None,
                "address3": "",
                "city": "San Francisco",
                "zip_code": "94118",
                "country": "US",
                "state": "CA",
                "display_address": ["785 8th Ave", "San Francisco, CA 94118"],
            },
            "phone": "+14157801579",
            "display_phone": "(415) 780-1579",
            "distance": 2974.448388088878,
        },
        {
            "id": "-NbDKVqG170J19MqSQ5q_A",
            "alias": "the-mill-san-francisco",
            "name": "The Mill",
            "image_url": "https://s3-media2.fl.yelpcdn.com/bphoto/3mYaiweH3tRKTLSLj24hVA/o.jpg",
            "is_closed": False,
            "url": "https://www.yelp.com/biz/the-mill-san-francisco?adjust_creative=iLXKG_naOtwkmDCMRoHImA&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=iLXKG_naOtwkmDCMRoHImA",
            "review_count": 1283,
            "categories": [
                {"alias": "coffee", "title": "Coffee & Tea"},
                {"alias": "bakeries", "title": "Bakeries"},
                {"alias": "desserts", "title": "Desserts"},
            ],
            "rating": 4.0,
            "coordinates": {
                "latitude": 37.7764801534107,
                "longitude": -122.437750024358,
            },
            "transactions": ["delivery"],
            "price": "$$",
            "location": {
                "address1": "736 Divisadero St",
                "address2": "",
                "address3": "",
                "city": "San Francisco",
                "zip_code": "94117",
                "country": "US",
                "state": "CA",
                "display_address": ["736 Divisadero St", "San Francisco, CA 94117"],
            },
            "phone": "+14153451953",
            "display_phone": "(415) 345-1953",
            "distance": 1736.2808394903705,
        },
        {
            "id": "lL-3T2fZIP_oCYC-uc074w",
            "alias": "flywheel-coffee-roasters-san-francisco",
            "name": "Flywheel Coffee Roasters",
            "image_url": "https://s3-media2.fl.yelpcdn.com/bphoto/hNFgdE_XYbZdH_ZcesWurg/o.jpg",
            "is_closed": False,
            "url": "https://www.yelp.com/biz/flywheel-coffee-roasters-san-francisco?adjust_creative=iLXKG_naOtwkmDCMRoHImA&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=iLXKG_naOtwkmDCMRoHImA",
            "review_count": 539,
            "categories": [
                {"alias": "coffee", "title": "Coffee & Tea"},
                {"alias": "coffeeroasteries", "title": "Coffee Roasteries"},
            ],
            "rating": 4.0,
            "coordinates": {
                "latitude": 37.769681598837636,
                "longitude": -122.45350500151754,
            },
            "transactions": ["delivery"],
            "price": "$$",
            "location": {
                "address1": "672 Stanyan St",
                "address2": "",
                "address3": "",
                "city": "San Francisco",
                "zip_code": "94117",
                "country": "US",
                "state": "CA",
                "display_address": ["672 Stanyan St", "San Francisco, CA 94117"],
            },
            "phone": "+14156824023",
            "display_phone": "(415) 682-4023",
            "distance": 1789.386184315149,
        },
    ],
    "total": 5900,
    "region": {
        "center": {"longitude": -122.43644714355469, "latitude": 37.76089938976322}
    },
}


class TestBusinessSearch:
    def test_deserialization(self) -> None:
        business_search: BusinessSearch = BusinessSearch(**test_data)

        assert business_search.total == 5900
        assert business_search.region.center.longitude == -122.43644714355469
        assert business_search.region.center.latitude == 37.76089938976322

        assert business_search.businesses[0].id == "DaOQgNk4LjN2gbvYrLQGvA"
        assert (
            business_search.businesses[0].alias
            == "rise-and-grind-coffee-and-tea-san-francisco-6"
        )
        assert business_search.businesses[0].review_count == 373
        assert business_search.businesses[0].display_phone == "(415) 780-1579"
        assert business_search.businesses[0].distance == 2974.448388088878
