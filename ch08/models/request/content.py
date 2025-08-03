from datetime import date
from typing import Dict, List

from pydantic import BaseModel


class ContentReq(BaseModel):
    id: int
    publication_id: int
    headline: str
    content: str
    content_type: str
    date_published: date