from fastapi import FastAPI, HTTPException
from enum import Enum
from pydantic import BaseModel
from typing import Dict, Union
# https://www.youtube.com/watch?v=SORiTsvnU28&ab_channel=ArjanCodes
app = FastAPI()


class Category(Enum):
    TOOLS = 'tools'
    CONSUMABLES = 'consumables'


class Item(BaseModel):
    name: str
    price: float
    count: int
    id: int
    category: Category


items = {
    0: Item(name='Hammer', price=9.99, count=20, id=0, category=Category.TOOLS),
    1: Item(name='Pliers', price=5.99, count=20, id=1, category=Category.TOOLS),
    2: Item(name='Nails', price=1.99, count=100, id=2, category=Category.CONSUMABLES),
}


@app.get('/')
async def index() -> Dict[str, Dict[int, Item]]:
    return {'items': items}


@app.get('/items/{item_id}')
async def query_item_by_id(item_id: int) -> Item:
    if item_id not in items:
        raise HTTPException(
            status_code=404, detail=f'Item with {item_id=} does not exist.'
        )
    return items[item_id]


@app.post("/")
def add_item(item: Item) -> Dict[str, Item]:
    if item.id in items:
        HTTPException(status_code=400, detail=f"Item with {item.id=} already exists.")

    items[item.id] = item
    return {"added": item}

