from typing import Optional

from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    api_key: Optional[str] = Field(..., env="YELP_API_KEY")
    base_url: str = "https://api.yelp.com/v3"

    @property
    def headers(self) -> dict:
        return {"Authorization": f"Bearer {self.api_key}"}
