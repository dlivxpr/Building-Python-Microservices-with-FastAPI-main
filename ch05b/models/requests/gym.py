from datetime import date

from pydantic import BaseModel


class GymClassReq(BaseModel): 
 
    id: int
    name: str
    member_id: int
    trainer_id: int
    approved : int
    
    
