from datetime import datetime

from yelpfusion3.model.business.reviews import Review, Reviews

test_review_data = {
    "id": "xAG4O7l-t1ubbwVAlPnDKg",
    "rating": 5,
    "user": {
        "id": "W8UK02IDdRS2GL_66fuq6w",
        "profile_url": "https://www.yelp.com/user_details?userid=W8UK02IDdRS2GL_66fuq6w",
        "image_url": "https://s3-media3.fl.yelpcdn.com/photo/iwoAD12zkONZxJ94ChAaMg/o.jpg",
        "name": "Ella A.",
    },
    "text": "Went back again to this place since the last time i visited the bay area 5 months ago, and nothing has changed. Still the sketchy Mission, Still the cashier...",
    "time_created": "2016-08-29 00:41:13",
    "url": "https://www.yelp.com/biz/la-palma-mexicatessen-san-francisco?hrid=hp8hAJ-AnlpqxCCu7kyCWA&adjust_creative=0sidDfoTIHle5vvHEBvF0w&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_reviews&utm_source=0sidDfoTIHle5vvHEBvF0w",
}


class TestReview:
    def test_deserialization(self) -> None:
        review: Review = Review(**test_review_data)

        assert review.id == "xAG4O7l-t1ubbwVAlPnDKg"
        assert review.rating == 5
        assert (
            review.text
            == "Went back again to this place since the last time i visited the bay area 5 months ago, and nothing has changed. Still the sketchy Mission, Still the cashier..."
        )
        assert review.time_created == datetime(2016, 8, 29, 0, 41, 13)
        assert (
            review.url
            == "https://www.yelp.com/biz/la-palma-mexicatessen-san-francisco?hrid=hp8hAJ-AnlpqxCCu7kyCWA&adjust_creative=0sidDfoTIHle5vvHEBvF0w&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_reviews&utm_source=0sidDfoTIHle5vvHEBvF0w"
        )
        assert review.user.id == "W8UK02IDdRS2GL_66fuq6w"
        assert (
            review.user.profile_url
            == "https://www.yelp.com/user_details?userid=W8UK02IDdRS2GL_66fuq6w"
        )
        assert (
            review.user.image_url
            == "https://s3-media3.fl.yelpcdn.com/photo/iwoAD12zkONZxJ94ChAaMg/o.jpg"
        )
        assert review.user.name == "Ella A."


test_reviews_data = {
    "reviews": [
        {
            "id": "xAG4O7l-t1ubbwVAlPnDKg",
            "rating": 5,
            "user": {
                "id": "W8UK02IDdRS2GL_66fuq6w",
                "profile_url": "https://www.yelp.com/user_details?userid=W8UK02IDdRS2GL_66fuq6w",
                "image_url": "https://s3-media3.fl.yelpcdn.com/photo/iwoAD12zkONZxJ94ChAaMg/o.jpg",
                "name": "Ella A.",
            },
            "text": "Went back again to this place since the last time i visited the bay area 5 months ago, and nothing has changed. Still the sketchy Mission, Still the cashier...",
            "time_created": "2016-08-29 00:41:13",
            "url": "https://www.yelp.com/biz/la-palma-mexicatessen-san-francisco?hrid=hp8hAJ-AnlpqxCCu7kyCWA&adjust_creative=0sidDfoTIHle5vvHEBvF0w&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_reviews&utm_source=0sidDfoTIHle5vvHEBvF0w",
        },
        {
            "id": "1JNmYjJXr9ZbsfZUAgkeXQ",
            "rating": 4,
            "user": {
                "id": "rk-MwIUejOj6LWFkBwZ98Q",
                "profile_url": "https://www.yelp.com/user_details?userid=rk-MwIUejOj6LWFkBwZ98Q",
                "image_url": None,
                "name": "Yanni L.",
            },
            "text": 'The "restaurant" is inside a small deli so there is no sit down area. Just grab and go.\n\nInside, they sell individually packaged ingredients so that you can...',
            "time_created": "2016-09-28 08:55:29",
            "url": "https://www.yelp.com/biz/la-palma-mexicatessen-san-francisco?hrid=fj87uymFDJbq0Cy5hXTHIA&adjust_creative=0sidDfoTIHle5vvHEBvF0w&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_reviews&utm_source=0sidDfoTIHle5vvHEBvF0w",
        },
        {
            "id": "SIoiwwVRH6R2s2ipFfs4Ww",
            "rating": 4,
            "user": {
                "id": "rpOyqD_893cqmDAtJLbdog",
                "profile_url": "https://www.yelp.com/user_details?userid=rpOyqD_893cqmDAtJLbdog",
                "image_url": None,
                "name": "Suavecito M.",
            },
            "text": "Dear Mission District,\n\nI miss you and your many delicious late night food establishments and vibrant atmosphere.  I miss the way you sound and smell on a...",
            "time_created": "2016-08-10 07:56:44",
            "url": "https://www.yelp.com/biz/la-palma-mexicatessen-san-francisco?hrid=m_tnQox9jqWeIrU87sN-IQ&adjust_creative=0sidDfoTIHle5vvHEBvF0w&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_reviews&utm_source=0sidDfoTIHle5vvHEBvF0w",
        },
    ],
    "total": 3,
    "possible_languages": ["en"],
}


class TestReviews:
    def test_deserialization(self) -> None:
        reviews: Reviews = Reviews(**test_reviews_data)

        assert reviews.total == 3
        assert reviews.possible_languages == ["en"]
        assert reviews.reviews[1].id == "1JNmYjJXr9ZbsfZUAgkeXQ"
        assert reviews.reviews[1].rating == 4
        assert (
            reviews.reviews[1].text
            == 'The "restaurant" is inside a small deli so there is no sit down area. Just grab and go.\n\nInside, they sell individually packaged ingredients so that you can...'
        )
        assert reviews.reviews[1].time_created == datetime(2016, 9, 28, 8, 55, 29)
        assert (
            reviews.reviews[1].url
            == "https://www.yelp.com/biz/la-palma-mexicatessen-san-francisco?hrid=fj87uymFDJbq0Cy5hXTHIA&adjust_creative=0sidDfoTIHle5vvHEBvF0w&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_reviews&utm_source=0sidDfoTIHle5vvHEBvF0w"
        )
