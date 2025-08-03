
from datetime import date
from typing import Dict, List

from pydantic import BaseModel


class AdminReq(BaseModel):
    
    id: int
    firstname: str
    lastname: str
    age: int
    date_started: date
    status: int
    login_id: int
    birthday: date