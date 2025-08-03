from datetime import date
from uuid import UUID

from model.classifications import RecipeRating


class Post:
    def __init__(self, id: UUID, feedback: str, rating: RecipeRating, userId: UUID, date_posted: date):
       self.id = id 
       self.feedback = feedback
       self.rating = rating
       self.userId = userId
       self.date_posted = date_posted


