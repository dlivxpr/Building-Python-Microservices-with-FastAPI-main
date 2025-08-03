from fastapi import Depends
from repository.admin import AdminRepository
from repository.complaints import BadRecipeRepository
from repository.keywords import KeywordRepository
from repository.posts import PostRepository
from repository.recipes import RecipeRepository


def get_recipe_repo(repo=Depends(RecipeRepository)):
    return repo

def get_post_repo(repo=Depends(PostRepository)): 
    return repo

def get_users_repo(repo=Depends(AdminRepository)): 
    return repo

def get_keywords(keywords=Depends(KeywordRepository)): 
    return keywords

def get_bad_recipes(repo=Depends(BadRecipeRepository)): 
    return repo


