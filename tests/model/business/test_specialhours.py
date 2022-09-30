from typing import Dict, Union

import pytest

from yelpfusion3.model.business.specialhours import SpecialHours

test_data: Dict[str, Union[bool, None, str]] = {
    "date": "2019-02-07",
    "is_closed": None,
    "start": "1600",
    "end": "2000",
    "is_overnight": False,
}


class TestSpecialHours:
    def test_deserialize(self) -> None:
        special_hours = SpecialHours(**test_data)

        assert special_hours.date == "2019-02-07"
        assert not special_hours.is_closed
        assert special_hours.start == "1600"
        assert special_hours.end == "2000"
        assert not special_hours.is_overnight

    @pytest.mark.parametrize("start", ["-1", "2401"])
    def test_start_fails_validation(self, start: str) -> None:
        test_special_hours: Dict[str, Union[bool, None, str]] = test_data.copy()
        test_special_hours["start"] = start

        with pytest.raises(ValueError):
            SpecialHours(**test_special_hours)

    @pytest.mark.parametrize("end", ["-1", "2401"])
    def test_end_fails_validation(self, end: str) -> None:
        test_special_hours: Dict[str, Union[bool, None, str]] = test_data.copy()
        test_special_hours["end"] = end

        with pytest.raises(ValueError):
            SpecialHours(**test_special_hours)
