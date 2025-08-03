import asyncio
from datetime import date

import rx.operators as ops
from config.db.gino_db import db
from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from models.data.nsms import Customer, Subscription
from models.request.subscription import SubscriptionReq
from repository.subscription import (SubscriptionCustomerRepository,
                                     SubscriptionRepository)
from rx.scheduler.eventloop import AsyncIOScheduler
from services.subscription import fetch_records, fetch_subscription

router = APIRouter()




@router.post("/subscription/add", )
async def add_subscription(req: SubscriptionReq):
    subscription_dict = req.dict(exclude_unset=True)
    repo = SubscriptionRepository()
    result = await repo.insert_subscription(subscription_dict)
    if result == True: 
        return req 
    else: 
        return JSONResponse(content={'message':'update trainer profile problem encountered'}, status_code=500)

@router.get("/subscription/list/all")
async def list_all_subscriptions():
    repo = SubscriptionRepository()
    result = await repo.get_all_subscription();
    result_map = [u.to_dict() for u in result]
    return result_map

@router.post("/subscription/dated")
async def list_dated_subscription(min_date:date, max_date:date):
     
    loop = asyncio.get_event_loop()
    observable = await fetch_subscription(min_date, max_date, loop)
    
    observable.subscribe(
       on_next=lambda item: print("Subscription details: {}.".format(item)),
       scheduler=AsyncIOScheduler(loop)
    )
    
@router.get("/subscription/monitor/total")
async def list_all_customer_subscription():
   
    loop = asyncio.get_event_loop()
    observable = fetch_records(5, loop)
    
    observable.subscribe(
       on_next=lambda item: print("The total amount sold: {}.".format(item)),
       scheduler=AsyncIOScheduler(loop)
    )
    return {"content": "Background task created."}