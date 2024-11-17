import os
import streamlit as st
from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama

# Load the Langsmith API key from the .env file
load_dotenv()
api_key = os.getenv("LANGSMITH_API_KEY")

if api_key is None:
    st.write("API key is missing! Please check your .env file.")
else:
    os.environ["LANGSMITH_API_KEY"] = api_key  # Pass to environment if needed

    # Define the prompt template for Health Tips and Reminders
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", 
             """You are a health assistant chatbot specializing in providing daily health tips and reminders.
                You can answer user queries related to general health, fitness, mental wellness, diet, and daily health tips.
                Additionally, give a random daily health tip when the user interacts."""),
            ("user", "Questions: {question}")
        ]
    )

    # Initialize your model (replace Ollama with a Langsmith API model if needed)
    llm = Ollama(model="llama2")  # Using open-source model, replace with Langsmith API model if needed

    # Chain the prompt with the model
    chain = prompt | llm

    # Streamlit Framework
    st.title('Daily Health Tips and Reminders Chatbot')
    st.write("Welcome! I can provide you with health tips and reminders. Ask me anything related to health and wellness!")

    # Input section for user query
    input_text = st.text_input("What health-related question do you have today?")

    # Providing responses and random health tips
    if input_text:
        # Generate response from the chatbot
        response = chain.invoke({'question': input_text})

        if response:
            st.write("### Response:")
            st.write(response)
        else:
            st.write("Sorry, I couldn't generate a response.")

        # Generate a daily health tip
        health_tips = [
            "Remember to drink at least 8 glasses of water today to stay hydrated.",
            "Take a 5-minute break every hour to stretch and move your body.",
            "Include a serving of fruits and vegetables in your meals for balanced nutrition.",
            "Try deep breathing exercises for 5 minutes to reduce stress.",
            "Aim to get at least 7-8 hours of sleep tonight for better recovery and health.",
            "Spend a few minutes today practicing gratitude to boost your mental well-being.",
            "Limit your screen time before bed to improve sleep quality.",
            "Incorporate a short walk into your daily routine for cardiovascular health.",
            "Start your day with a healthy breakfast to kickstart your metabolism.",
            "Practice good posture to prevent back and neck pain."
        ]

        # Display a random health tip
        import random
        random_tip = random.choice(health_tips)
        st.write("### Daily Health Tip:")
        st.write(random_tip)

    else:
        st.write("Please enter a health-related question to get started.")
