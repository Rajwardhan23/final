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

    # Define the prompt template
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are the helpful assistant. Please respond to the queries."),
            ("user", "Questions: {question}")
        ]
    )

    # Initialize your model (replace Ollama with a Langsmith API model if needed)
    llm = Ollama(model="llama2")  # Use an open-source model

    # Chain the prompt with the model
    chain = prompt | llm

    # Streamlit Framework
    st.title('LangChain Demo with Langsmith Model')
    input_text = st.text_input("Search the topic you want")

    if input_text:
        response = chain.invoke({'question': input_text})
        if response:
            st.write(response)
        else:
            st.write("Sorry, I couldn't generate a response.")
    else:
        st.write("Please enter a question.")
