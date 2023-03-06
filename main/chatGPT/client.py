from main.chatGPT.model import Prompt, Ingredient, Recipe, Steps
from main.chatGPT.configs import promptList, footer
from main.chatGPT.chatGPT import gpt
from fastapi import APIRouter
from typing import List
import random
import json

router = APIRouter()


@router.post("/recipe")
def getRecipe(ingredient: List[Ingredient]) -> Recipe:
    randomInt = random.randint(0, len(promptList) - 1)
    prompt = Prompt(question=promptList[randomInt], ingredients=ingredient)
    ingredientString = ''

    for item in prompt.ingredients:
        ingredientString += str(item.name) + ' '

    question = str(prompt.question) + ' ' + ingredientString[:-1] + footer

    response = gpt(question)
    data = json.loads(response)
    stepsList = []

    for step in data['steps']:
        stepsList.append(Steps(name=step['name'], value=step['value']))

    suggestion = Recipe(name=data['name'], description=data['description'], steps=stepsList)

    return suggestion
