from datetime import date

from pydantic import BaseModel


class AttendanceMemberReq(BaseModel):
    id: int
    member_id: int
    timeout:str
    timein:str
    date_log:date