from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langserve import add_routes
import uvicorn
from langchain_ollama import OllamaLLM  # Updated import for Ollama model
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI(
    title="Ollama Langchain Server",
    version="1.0",
    description="A simple API Server using Ollama model"
)

# Initialize the Ollama model (using the updated class)
llm = OllamaLLM(model="llama2")

# Prompt
prompt = ChatPromptTemplate.from_template("Write me a {type} about {topic} with 100 words.")

# Use the pipe operator to create a chain (prompt | model)
model_chain = prompt | llm

# Add routes for generating text with Ollama
add_routes(
    app,
    model_chain,  # Pass the chain directly
    path="/poem"
)

# Main entry point
if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
