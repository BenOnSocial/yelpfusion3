from typing import Literal, Optional

import pycountry
from pydantic import confloat, conint, constr, validator
from requests import Response

from yelpfusion3.endpoint.endpoint import Endpoint
from yelpfusion3.model.business.businessmatches import BusinessMatches


class BusinessMatchesEndpoint(Endpoint):
    """
    This endpoint lets you match business data from other sources against businesses on Yelp, based on provided business
    information. For example, if you know a business's exact address and name, and you want to find that business and
    only that business on Yelp.

    Note: at this time, the API does not return businesses without any reviews.
    """

    _path: str = "/businesses/matches"

    name: constr(min_length=1, max_length=64, regex=r"^[\da-zA-Z\s\!#$%&+,./:?@']+$")  # type: ignore
    """
    Required. The name of the business. Maximum length is 64; only digits, letters, spaces, and !#$%&+,./:?@'
    are allowed.
    """

    address1: constr(min_length=0, max_length=64, regex=r"^[\da-zA-Z\s'/#&,.:]+$")  # type: ignore
    """
    Required. The first line of the business’s address. Maximum length is 64; only digits, letters, spaces, and
    '/#&,.: are allowed. The empty string "" is allowed; this will specifically match certain service businesses that
    have no street address.
    """

    address2: Optional[constr(min_length=0, max_length=64, regex=r"^[\da-zA-Z\s'/#&,.:]+$")]  # type: ignore
    """
    Optional. The second line of the business’s address. Maximum length is 64; only digits, letters, spaces, and
    '/#&,.: are allowed.
    """

    address3: Optional[constr(min_length=0, max_length=64, regex=r"^[\da-zA-Z\s'/#&,.:]+$")]  # type: ignore
    """
    Optional. The third line of the business’s address. Maximum length is 64; only digits, letters, spaces, and
    '/#&,.: are allowed.
    """

    city: constr(min_length=0, max_length=64, regex=r"^[\da-zA-Z\s'.()]+$")  # type: ignore
    """
    Required. The city of the business. Maximum length is 64; only digits, letters, spaces, and '.() are allowed.
    """

    state: constr(min_length=2, max_length=3, to_upper=True)  # type: ignore
    """
    Required. The ISO 3166-2 (with a few exceptions) state code of this business. Maximum length is 3.
    """

    country: constr(min_length=2, max_length=2, to_upper=True)  # type: ignore
    """
    Required. The ISO 3166-1 alpha-2 country code of this business. Maximum length is 2.
    """

    latitude: Optional[confloat(ge=-90.0, le=90.0)]  # type: ignore
    """
    Optional. The WGS84 latitude of the business in decimal degrees. Must be between -90 and +90.
    """

    longitude: Optional[confloat(ge=-180.0, le=180.0)]  # type: ignore
    """
    Optional. The WGS84 longitude of the business in decimal degrees. Must be between -180 and +180.
    """

    phone: Optional[constr(max_length=32, regex=r"^\+?\d+$")]  # type: ignore
    """
    Optional. The phone number of the business which can be submitted as (a) locally ­formatted with digits only
    (e.g., 016703080) or (b) internationally­ formatted with a leading + sign and digits only after (+35316703080).
    Maximum length is 32.
    """

    zip_code: Optional[str]
    """
    Optional. The Zip code of this business.
    """

    yelp_business_id: Optional[str]
    """
    Optional. Unique Yelp identifier of the business if available. Used as a hint when finding a matching business.
    """

    limit: Optional[conint(ge=1, le=10)]  # type: ignore
    """
    Optional. Maximum number of business results to return. By default, it will return 3. Minimum is 1, maximum is 10.
    """

    match_threshold: Optional[Literal["none", "default", "strict"]]
    """
    Optional. Specifies whether a match quality threshold should be applied to the matched businesses. Must be one of
    'none', 'default' or 'strict'.

        none: Do not apply any match quality threshold; all potential business matches will be returned.
        default: Apply a match quality threshold such that only very closely matching businesses will be returned.
        strict: Apply a very strict match quality threshold.
    """

    def get(self) -> BusinessMatches:
        response: Response = self._get()
        return BusinessMatches(**response.json())

    @validator("country")
    def check_country(cls, v: str) -> str:
        """
        Checks that "v" is a valid ISO 3166- alpha-2 country code.

        :param v: Two-letter country code.
        :type v: str
        :raise ValueError: If "v" is an invalid country code.
        :return: "v" if it passes validation.
        :rtype: str
        """

        if pycountry.countries.get(alpha_2=v):
            return v
        raise ValueError("Not a valid ISO 3166-1 alpha-2 country code.")
