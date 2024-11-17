import os
import streamlit as st
from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama  # Using Ollama as the open-source LLM

# Load environment variables
load_dotenv()

# Streamlit Framework
st.title('LangChain Demo with Open-Source LLM (Ollama)')

# Get user input
input_text = st.text_input("Search the topic you want")

# Check if the input is provided
if input_text:
    # Initialize the open-source LLM model (Ollama in this case)
    llm = Ollama(model="llama2")  # Use a specific open-source model like LLaMA or Ollama
    
    # Create a prompt template
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are the helpful assistant. Please respond to the queries."),
            ("user", "Questions: {question}")
        ]
    )
    
    # Build the chain with the open-source model
    chain = prompt | llm

    # Run the chain and display output
    response = chain.invoke({'question': input_text})
    if response:
        st.write(response)
    else:
        st.write("Sorry, I couldn't generate a response.")
else:
    st.write("Please enter a question.")
