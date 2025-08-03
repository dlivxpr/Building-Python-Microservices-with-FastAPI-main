from datetime import date
from typing import List

from pydantic import BaseModel


class PurchaseReq(BaseModel): 
    purchase_id: int
    buyer_id: int 
    book_id: int 
    items: int 
    price: float 
    date_purchased: date
    
 