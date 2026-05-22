import os
from dotenv import load_dotenv
from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# LOAD ENV FILE
load_dotenv()

### langchain imports
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")
os.environ["LANGCHAIN_TRACING_V2"] = "true"

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an intelligent helpful assistant and should help me out"),
        ("user", "Question:{question}")
    ]
)

st.title("Langchain Demo using Gemma Model")
input_text = st.text_input("Hey! what is on your mind?")

llm = Ollama(model="qwen2.5-coder:7b")

output_parser = StrOutputParser()

chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({"question": input_text}))