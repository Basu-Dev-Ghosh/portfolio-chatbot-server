# Import necessary modules from FastAPI

from fastapi import FastAPI
from ask import ask
from fastapi.middleware.cors import CORSMiddleware

# Create an instance of the FastAPI class
app = FastAPI()

origins = [
    "http://localhost:3000",  # React app
    "http://localhost:8000",  # FastAPI server
    "http://localhost:8080",  # Vue.js app
    "http://localhost:5000",  # Angular app
    'https://portfolio-new-eight-delta.vercel.app'
    # Add more origins if needed
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/ask")
def read_question(question: str):
    res=ask(question)
    return res