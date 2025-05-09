#developing a simple chatbot using the OpenAI API and FastAPI
import os
import openai
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize FastAPI app
app = FastAPI()

#Initialize OpenAI client
# Set the OpenAI API key from environment variable

# Example usage of the openai package
openai.api_key = os.getenv("OPENAI_API_KEY")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers

# Define a Pydantic model for the request body
class ChatRequest(BaseModel):
    messages: List[dict]  # List of message dictionaries
    model: str = "gpt-3.5-turbo"  # Default model


)
