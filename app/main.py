"""Module for QuickNLP REST API server."""
from fastapi import FastAPI
from app.algorithms import algorithms
from app.algorithms.summarization import Summarization
from app.algorithms.paraphrasing import Paraphrasing
from app.algorithms.grammar_checking import GrammarChecking
from app.schemas import Body


app = FastAPI()


@app.get("/")
async def root():
    """# Quick NLP.

    QuickNLP is a natural language processing service that takes
    plain text and transforms it into meaningful information in
    desired format using a range of NLP algoritms.
    """
    return {
        "status": "success",
        "message": "Welcome to QuickNLP!",
        "data": None
    }


@app.get("/algorithms")
def describe():
    """Get metadata for all available algorithms."""
    return {
        "status": "success",
        "data": algorithms,
    }


@app.get("/paraphrasing")
def describe_paraphrasing():
    """Get metadata for the paraphrasing algorithm."""
    return {
        "status": "success",
        "data": Paraphrasing.describe()
    }


@app.post("/paraphrasing")
def paraphrasing(body: Body):
    """Post a corpus for paraphrasing algorithm."""
    paraphrase = Paraphrasing(body.corpus, **body.options.__dict__)
    return {
        "status": "success",
        "data": paraphrase.__dict__
    }


@app.get("/summarization")
def describe_summarization():
    """Get metadata for the summarization algorithm."""
    return {
        "status": "success",
        "data": Summarization.describe()
    }


@app.post("/summarization")
def summarization(body: Body):
    """Post a corpus for summarization algorithm."""
    summary = Summarization(body.corpus)
    return {
        "status": "success",
        "data": summary.__dict__
    }


@app.get("/grammar-checking")
def describe_grammar_checking():
    """Get metadata for the grammar checking algorithm."""
    return {
        "status": "success",
        "data": GrammarChecking.describe()
    }


@app.post("/grammar-checking")
def grammar_checking(body: Body):
    """Post a corpus for grammar checking algorithm."""
    grammar_check = GrammarChecking(body.corpus)
    return {
        "status": "success",
        "data": grammar_check.__dict__
    }
