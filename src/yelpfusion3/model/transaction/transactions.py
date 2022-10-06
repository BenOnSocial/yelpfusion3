from yelpfusion3.model.business.specialhours import SpecialHours

test_data = {
    "date": "2019-02-07",
    "is_closed": None,
    "start": "1600",
    "end": "2000",
    "is_overnight": False,
}


def test_deserialize() -> None:
    special_hours = SpecialHours(**test_data)

    assert special_hours.date == "2019-02-07"
    assert not special_hours.is_closed
    assert special_hours.start == "1600"
    assert special_hours.end == "2000"
    assert not special_hours.is_overnight
