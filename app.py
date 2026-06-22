import os
from apikey import OPENAI_API_KEY, OPENAI_API_BASE_URL
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate


os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
os.environ["OPENAI_API_BASE_URL"] = OPENAI_API_BASE_URL 

st.title("Medium Article Generator")
topic = st.text_input("Enter your topic:", key="topic_input")

title_template = PromptTemplate(
    input_variables=["topic","Language"],
    template="Generate a Medium article title for the topic: {topic} in {Language} language."
)
llm = ChatOpenAI(model="gpt-4o", temperature=0.9)

if topic:
    response = llm.invoke(title_template.format(topic=topic, Language='chinese'))
    st.write(response.content)
    