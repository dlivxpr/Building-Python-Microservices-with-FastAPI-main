import sys

from containers.multiple_containers import RecipeAppContainer
from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from repository.admin import AdminRepository

router = APIRouter()

@router.get("/admin/logs/visitors/list")
@inject
def list_logs_visitors(adminservice: AdminRepository = Depends(Provide[RecipeAppContainer.admincontainer.adminservice])): 
    logs_visitors_json = jsonable_encoder(adminservice.query_logs_visitor())
    return logs_visitors_json

container = RecipeAppContainer()
container.wire(modules=[sys.modules[__name__]])