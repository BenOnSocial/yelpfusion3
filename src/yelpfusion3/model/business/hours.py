from typing import List, Literal

from pydantic import validator

from yelpfusion3.model.model import Model


class DetailedHours(Model):
    """
    Opening hours of the business for a given day of the week.
    """

    is_overnight: bool = False
    """
    Whether the business opens overnight or not. When this is true, the end time will be lower than the start time.
    """

    start: str
    """
    Start of the opening hours in a day, in 24-hour clock notation, like 1000 means 10 AM.
    """

    end: str
    """
    End of the opening hours in a day, in 24-hour clock notation, like 2130 means 9:30 PM.
    """

    day: Literal[0, 1, 2, 3, 4, 5, 6]
    """
    From 0 to 6, representing day of the week from Monday to Sunday. Notice that you may get the same day of the week
    more than once if the business has more than one opening time slots.
    """

    @validator("start")
    def check_start(cls, v: str) -> str:
        value = int(v)
        if 0 <= value <= 2400:
            return v
        raise ValueError("Not a valid start time.")

    @validator("end")
    def check_end(cls, v: str) -> str:
        value = int(v)
        if 0 <= value <= 2400:
            return v
        raise ValueError("Not a valid end time.")


class Hours(Model):
    """
    Opening hours of the business.
    """

    open: List[DetailedHours] = []
    """
    Opening hours of the business.
    """

    hours_type: Literal["REGULAR"]
    """
    The type of the opening hours information. Right now, this is always REGULAR.
    """

    is_open_now: bool
    """
    Whether the business is currently open or not.
    """
