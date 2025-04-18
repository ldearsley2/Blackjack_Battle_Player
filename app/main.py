import logging
from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from app.routes import router

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(_app: FastAPI):
    """
    Define the lifespan of the FastAPI app, everything after yield occurs on app shutdown.
    :param _app:
    :return:
    """
    logger.info("Starting Blackjack_Player")

    yield

    logger.info("Shutting down Blackjack_Player")


app = FastAPI(title="Blackjack-Battle-Player", lifespan=lifespan)
app.include_router(router)


def start():
    """
    Start a uvicorn server using the FastAPI app
    :return:
    """
    uvicorn.run("app.main:app", host="0.0.0.0", port=5000, reload=True)


def start_dev():
    """
    Start a local uvicorn servicer using the FastAPI app
    :return:
    """
    uvicorn.run("app.main:app", host="127.0.0.1", port=5001)
