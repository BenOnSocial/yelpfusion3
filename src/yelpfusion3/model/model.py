from pydantic import BaseModel


class Model(BaseModel):
    class Config:
        anystr_strip_whitespace = True
        min_anystr_length = 1
        validate_assignment = True
