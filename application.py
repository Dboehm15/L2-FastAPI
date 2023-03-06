from main.chatGPT import client
from fastapi import FastAPI

app = FastAPI()
app.include_router(client.router)


@app.get('/')
async def index():
    return 'http://127.0.0.1:8000/docs'
