from datetime import date

from models.data.ratings_enum import FoodRatingScale
from pydantic import BaseModel


class FoodRateReq(BaseModel):
    rate: FoodRatingScale
    date_rated: date 
    profile_id: int