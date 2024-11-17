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

    # Define the prompt template for health tips and reminders
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a helpful assistant who provides daily health tips and reminders."),
            ("user", "Give me a health tip or reminder for today: {question}")
        ]
    )

    # Initialize your model (replace Ollama with a Langsmith API model if needed)
    llm = Ollama(model="llama2")  # Use an open-source model

    # Chain the prompt with the model
    chain = prompt | llm

    # Streamlit Framework
    st.title('Daily Health Tips and Reminders')
    input_text = st.text_input("Ask for a health tip or reminder:")

    if input_text:
        # Get a health tip or reminder based on the user's request
        response = chain.invoke({'question': input_text})
        if response:
            st.write(f"Health Tip/Reminder: {response}")
        else:
            st.write("Sorry, I couldn't generate a response.")
    else:
        st.write("Please enter a question to get your health tip or reminder.")
