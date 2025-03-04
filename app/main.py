from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from app.startup import start_up_connect


@asynccontextmanager
async def lifespan(_app: FastAPI):

    print("Starting Blackjack-Player")
    start_up_connect(game_url="http://127.0.0.1:5000",
                     own_url="http://127.0.0.1:5001")

    yield

    print("Shutting down player")

app = FastAPI(title="Blackjack-Battle-Player", lifespan=lifespan)

@app.get("/")
async def root():
    return {"message": "Hello from blackjack player"}

@app.get("/connection-check")
async def connection_check():
    return


def start():
    """
    Start a uvicorn server using the FastAPI app
    :return:
    """
    uvicorn.run("app.main:app", host="0.0.0.0", port=5000, reload=True)

def start_dev():
    uvicorn.run("app.main:app", host="127.0.0.1", port=5001, reload=True)

