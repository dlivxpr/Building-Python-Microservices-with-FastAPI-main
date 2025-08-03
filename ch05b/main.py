from api import attendance, gym, login
from fastapi import FastAPI

app = FastAPI()
app.include_router(login.router, prefix='/ch05')
app.include_router(attendance.router, prefix='/ch05')
app.include_router(gym.router, prefix='/ch05')

