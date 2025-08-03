import asyncio
import multiprocessing

import rx
from config.db.gino_db import db
from fastapi import APIRouter, Depends, FastAPI
from fastapi.responses import JSONResponse
from models.data.nsms import Publication, Sales
from models.request.sales import SalesReq
from repository.sales import SalesRepository
from rx.scheduler import ThreadPoolScheduler
from rx.scheduler.eventloop import AsyncIOScheduler
from services.sales import create_observable

thread_count = multiprocessing.cpu_count()
thread_pool_scheduler = ThreadPoolScheduler(thread_count)

thread_count = multiprocessing.cpu_count()
thread_pool_scheduler = ThreadPoolScheduler(thread_count)

router = APIRouter()


    
@router.post("/sales/add")
async def add_sales(req: SalesReq):
    sales_dict = req.dict(exclude_unset=True)
    repo = SalesRepository()
    result = await repo.insert_sales(sales_dict)
    if result == True: 
        return req 
    else: 
        return JSONResponse(content={'message':'update trainer profile problem encountered'}, status_code=500)
    
    
@router.get("/sales/list/quota")
async def list_sales_by_quota():
    loop = asyncio.get_event_loop()
    observer = create_observable(loop)
    
    observer.subscribe(
        on_next=lambda value: print("Received Instruction to buy {0}".format(value)),
        on_completed=lambda: print("Completed trades"),
        on_error=lambda e: print(e),
        scheduler = AsyncIOScheduler(loop)   
    )
    
    return {"message": "Notification sent in the background"}