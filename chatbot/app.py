from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.outPut_parsers import Stroutputparser

import streamlit as st
import os
import dotenv import load_dotenv


os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")

# Prompt Template   

prompt=ChatPromptTemplate.from.messages(
    [
        ("system","You are the helpful assistant. Please response to the queries")
        ("user","Quetions:{question}")
    ]
)

# Streamlit Freamework

st.title('langchain Demo with OPENAI API')
input_text = st.text_input("Search the topic you want")

#openai llm
llm=ChatOpenAI(model="gpt-3.5-turbo")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))
