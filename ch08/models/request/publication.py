
from datetime import date
from typing import Dict, List

from pydantic import BaseModel


class PublicationReq(BaseModel):
    id: int
    name: str
    type: str
    vendor_id: int
    messenger_id: int     