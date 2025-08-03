from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from model.classifications import Category, Origin
from model.recipes import Recipe
from pydantic import BaseModel
from service.factory import get_recipe_service


class IngredientReq(BaseModel):
    id: UUID 
    name:str
    qty : int
    measure : str
      
        
class RecipeReq(BaseModel):
    id: UUID 
    name: str
    ingredients: List[IngredientReq]
    cat: Category
    orig : Origin
     
        
router = APIRouter()

@router.post("/recipes/insert")
def insert_recipe(recipe: RecipeReq, handler=Depends(get_recipe_service)): 
    json_dict = jsonable_encoder(recipe)
    rec = Recipe(**json_dict)
    handler.add_recipe(rec)
    return JSONResponse(content=json_dict, status_code=200)

@router.get("/recipes/list/all")
def get_all_recipes(handler=Depends(get_recipe_service)):
    return handler.get_recipes()
