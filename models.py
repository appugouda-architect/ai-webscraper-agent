from pydantic import BaseModel
from typing import List


class ScrapeRequest(BaseModel):
    topics: str
