# Import necessary modules from FastAPI
import os
from dotenv import load_dotenv
from fastapi import FastAPI
from ask import ask
from fastapi.middleware.cors import CORSMiddleware
# Create an instance of the FastAPI class
app = FastAPI()
# os.environ['OPENAI_API_KEY'] = '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'

origins = [
    "http://localhost:3000",  # React app
    "http://localhost:8000",  # FastAPI server
    "http://localhost:8080",  # Vue.js app
    "http://localhost:5000",  # Angular app
    'https://portfolio-new-eight-delta.vercel.app',
    'https://basudev.in',
    'https://www.basudev.in'
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
    print(os.environ['OPENAI_API_KEY'])
    res=ask(question)
    return res