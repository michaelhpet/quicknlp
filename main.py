"""Main module."""
from fastapi import FastAPI
from constants import algorithms


app = FastAPI()


@app.get("/")
async def root_get():
    """GET hello world."""
    return {
        "status": "success",
        "message": "Hello World"
    }


@app.get("/algorithms")
def algorithms_get():
    """GET all available algorithms."""
    return {
        "status": "success",
        "data": algorithms,
        "name": name
    }
