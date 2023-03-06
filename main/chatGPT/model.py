from pydantic import BaseModel
from typing import List


class Ingredient(BaseModel):
    name: str


class Prompt(BaseModel):
    question: str
    ingredients: List[Ingredient]


class Steps(BaseModel):
    name: str
    value: str


class Recipe(BaseModel):
    name: str
    description: str
    steps: List[Steps]