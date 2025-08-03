from api import admin, login, members, trainers
from fastapi import FastAPI

app = FastAPI()
app.include_router(admin.router, prefix='/ch05')
app.include_router(members.router, prefix='/ch05')
app.include_router(trainers.router, prefix='/ch05')
app.include_router(login.router, prefix='/ch05')
