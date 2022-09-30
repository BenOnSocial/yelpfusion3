from pydantic import BaseModel, confloat


class Coordinates(BaseModel):
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
