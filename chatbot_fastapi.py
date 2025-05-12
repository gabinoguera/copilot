# Developing a simple chatbot using the OpenAI API and FastAPI
import os
from openai import OpenAI
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve the OpenAI API key from environment variables
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Initialize FastAPI app
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Define a Pydantic model for the request body
class ChatRequest(BaseModel):
    user_message: str

# Define a Pydantic model for the response body
class ChatResponse(BaseModel):  
    id: str
    object: str
    created: int
    model: str
    choices: List[dict]
    usage: dict

# Example endpoint to handle chat requests
@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        # Call the OpenAI API
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": request.user_message}],
            temperature=0.7,
            max_tokens=100,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
        )
        # Map the response to the ChatResponse model
        return response.model_dump()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Para iniciar el servidor en GitHub Codespaces, ejecuta:
# uvicorn chatbot_fastapi:app --host 0.0.0.0 --port 8000 --reload
