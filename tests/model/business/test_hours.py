from typing import Dict, List, Union

import pytest

from yelpfusion3.model.business.hours import DetailedHours

test_data: List[dict] = [
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
]


class TestDetailedHours:
    def test_deserialization(self) -> None:
        test_detailed_hours: Dict[str, Union[bool, int, str]] = test_data[0]["open"][
            0
        ].copy()
        detailed_hours: DetailedHours = DetailedHours(**test_detailed_hours)

        assert not detailed_hours.is_overnight
        assert detailed_hours.start == "1730"
        assert detailed_hours.end == "2200"
        assert detailed_hours.day == 0

    @pytest.mark.parametrize("start", ["-1", "2401"])
    def test_start_fails_validation(self, start: str) -> None:
        test_detailed_hours: Dict[str, Union[bool, int, str]] = test_data[0]["open"][
            0
        ].copy()
        test_detailed_hours["start"] = start

        with pytest.raises(ValueError):
            DetailedHours(**test_detailed_hours)

    @pytest.mark.parametrize("end", ["-1", "2401"])
    def test_end_fails_validation(self, end: str) -> None:
        test_detailed_hours: Dict[str, Union[bool, int, str]] = test_data[0]["open"][
            0
        ].copy()
        test_detailed_hours["end"] = end

        with pytest.raises(ValueError):
            DetailedHours(**test_detailed_hours)
