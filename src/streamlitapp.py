from dotenv import load_dotenv
load_dotenv()

from langchain_community.llms import Ollama
import  streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

## Prompt Design
prompt = ChatPromptTemplate(
    [
        ("system","Provide correct solution or answer based on user input"),
        ("user","Question: {question}")

    ]
)
### Design the Streamlit Framework
st.title("Chat Bot Using Streamlit")
input = st.text_input("Write Your Question ")

### Create a Model
model = Ollama(model="gemma:2b")

parser = StrOutputParser()

chain = prompt|model|parser

if input:
    st.write(chain.invoke({"question":input}))