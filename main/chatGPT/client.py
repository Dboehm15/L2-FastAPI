from main.chatGPT.model import Meal, Ingredient
from fastapi import APIRouter
from typing import List

router = APIRouter()


@router.post("/recipe")
def getRecipe(ingredient: List[Ingredient]) -> Meal:
    meal = Meal(name="Hamburger", ingredients=ingredient)

    return meal
