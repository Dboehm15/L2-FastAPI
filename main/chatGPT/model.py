from pydantic import BaseModel
from typing import List, Dict


class Ingredient(BaseModel):
    name: str


class Meal(BaseModel):
    name: str
    ingredients: List[Ingredient]
