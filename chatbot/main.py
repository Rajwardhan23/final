import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain_community.chains import RunnableSequence
from config import ollama_llm
from apscheduler.schedulers.background import BackgroundScheduler
import time
import threading

# Define the prompt template for health tips
health_tip_prompt = PromptTemplate(
    input_variables=["input", "history"],
    template=""" 
You are a Daily Health Tips and Reminders Chatbot. 
Your role is to provide personalized health tips, reminders, and motivation for users to maintain a healthy lifestyle. 
Given the conversation history below and user input, provide a helpful response.

History:
{history}

User input: {input}

Response:
"""
)

# Initialize conversation memory
memory = ConversationBufferMemory(memory_key="history", input_key="input")

# Create the RunnableSequence, which is the updated approach
runnable_sequence = health_tip_prompt | ollama_llm

# Function to handle user queries
def get_health_tip_response(user_input):
    response = runnable_sequence.invoke({"input": user_input, "history": memory.load_memory_variables({})})
