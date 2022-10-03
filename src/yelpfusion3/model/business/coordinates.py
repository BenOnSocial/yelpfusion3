from pydantic import confloat

from yelpfusion3.model.model import Model


class Coordinates(Model):
    """
    The coordinates of this business.
    """

    latitude: confloat(ge=-90.0, le=90.0)  # type: ignore
    """
    The latitude of this business.
    """

    longitude: confloat(ge=-180.0, le=180.0)  # type: ignore
    """
    The longitude of this business.
    """
