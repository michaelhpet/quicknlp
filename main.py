"""Main module."""
from fastapi import FastAPI
from constants import algorithms
from models.summarization import Summarization
from models.paraphrasing import Paraphrasing
from models.grammar_checking import GrammarChecking


app = FastAPI()


@app.get("/")
async def root_get():
    """GET /."""
    return {
        "status": "success",
        "message": "Welcome to QuickNLP!",
        "data": None
    }


@app.get("/algorithms")
def algorithms_get():
    """GET all available algorithms."""
    return {
        "status": "success",
        "data": [
            Paraphrasing.describe(),
            Summarization.describe(),
            GrammarChecking.describe()
        ],
    }


@app.post("/summarization")
def summarization_post():
    """POST a corpus for summarization algorithm."""
    summary = Summarization("Hello World", name="Michael Peter", format="pdf")
    print(summary)
    return {
        "status": "success",
        "data": summary.__dict__
    }
