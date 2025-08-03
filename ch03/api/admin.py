import sys

from containers.single_container import Container
from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from repository.admin import AdminRepository

router = APIRouter()

@router.get("/admin/login/details/list")
@inject
def list_login_details(adminservice: AdminRepository = Depends(Provide[Container.adminservice])): 
    login_details_json = jsonable_encoder(adminservice.query_login_details()) 
    return login_details_json


@router.get("/admin/user/profiles/list")
@inject
def list_user_profiles(adminservice: AdminRepository = Depends(Provide[Container.adminservice])): 
    user_profiles_json = jsonable_encoder(adminservice.query_user_profiles()) 
    return user_profiles_json

container = Container()
container.wire(modules=[sys.modules[__name__]])

