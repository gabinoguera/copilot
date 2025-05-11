# Developing a simple chatbot using the OpenAI API and FastAPI
import os
from openai import OpenAI
from fastapi import FastAPI, HTTPException
from fastapi.params import Body
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve the OpenAI API key from environment variables
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Initialize FastAPI app
app = FastAPI()

# Example endpoint to handle chat requests
@app.post("/chat")
async def chat(user_message: str = Body(..., embed=True)):
    try:
        # Call the OpenAI API
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": user_message}],
            temperature=0.7,
            max_tokens=100
        )
        # Return just the message content
        return {"response": response.choices[0].message.content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
