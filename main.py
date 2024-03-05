# Import necessary modules from FastAPI

from fastapi import FastAPI
from ask import ask
# Create an instance of the FastAPI class
app = FastAPI()

@app.get("/ask")
def read_question(question: str):
    res=ask(question)
    return res