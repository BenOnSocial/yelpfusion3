from pydantic import BaseModel


class Model(BaseModel):
    """
    Basic base class for all model implementations.
    """

    class Config:
        anystr_strip_whitespace = True
        min_anystr_length = 1
        validate_assignment = True
