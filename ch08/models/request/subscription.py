from datetime import date
from typing import Dict, List

from pydantic import BaseModel


class SubscriptionReq(BaseModel):
    id: int
    customer_id: int
    branch: str
    price: float
    qty: int
    date_purchased: date