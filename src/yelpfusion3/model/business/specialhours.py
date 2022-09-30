from datetime import datetime
from typing import Optional

from pydantic import BaseModel, validator


class SpecialHours(BaseModel):
    """
    Out of the ordinary hours for the business that apply on certain dates. Whenever these are set, they will override
    the regular business hours found in the 'hours' field.
    """

    date: str
    """
    An ISO8601 date string representing the date for which these special hours apply.
    """

    is_closed: Optional[bool]
    """
    Whether this particular special hour represents a date where the business is closed.
    """

    start: str
    """
    Start of the opening hours in a day, in 24-hour clock notation, like 1000 means 10 AM.
    """

    end: str
    """
    End of the opening hours in a day, in 24-hour clock notation, like 2130 means 9:30 PM.
    """

    is_overnight: bool
    """
    Whether the special hours time range spans across midnight or not. When this is true, the end time will be lower
    than the start time.
    """

    @validator("date")
    def check_date(cls, v: str) -> str:
        """
        Validates the date field for proper format. (YY-MM-DD)

        :param v: String representation of a calendar day. ("YY-MM-DD")
        :type v: str
        :raise ValueError: If "v" is a malformed string.
        :return: "v" if it's a valid date string.
        :rtype: str
        """
        # If the date string is malformed, an exception will be raised so we don't need to.
        datetime.strptime(v, "%Y-%m-%d")
        return v

    @validator("start")
    def check_start(cls, v: str) -> str:
        """
        Validates the start field for proper format and checks that it properly represents a time. (HHMM)

        :param v: 4-digit string representing the time. (HHMM)
        :type v: str
        :raise ValueError: If "v" is outside of the 0000-2400 value range.
        :return: "v" if it's a valid time string.
        :rtype: str
        """
        value = int(v)
        if 0 <= value <= 2400:
            return v
        raise ValueError("Not a valid start time.")

    @validator("end")
    def check_end(cls, v: str) -> str:
        """
        Validates the end field for proper format and checks that it properly represents a time. (HHMM)

        :param v: 4-digit string representing the time. (HHMM)
        :type v: str
        :raise ValueError: If "v" is outside of the 0000-2400 value range.
        :return: "v" if it's a valid time string.
        :rtype: str
        """
        value = int(v)
        if 0 <= value <= 2400:
            return v
        raise ValueError("Not a valid end time.")
