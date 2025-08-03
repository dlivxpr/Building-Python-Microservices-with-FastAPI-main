from datetime import date

from models.data.ratings_enum import AmbianceRatingScale
from pydantic import BaseModel


class AmbianceRateReq(BaseModel):
    question_id: int
    rate: AmbianceRatingScale
    date_rated: date 
    profile_id: int