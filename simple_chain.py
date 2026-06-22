import os

from apikey import OPENAI_API_KEY, OPENAI_API_BASE_URL
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
os.environ["OPENAI_API_BASE_URL"] = OPENAI_API_BASE_URL

st.title('Medium Article Generator')
topic = st.text_input('Input your topic of interest')
language = st.text_input('Input your language of choice')

title_template = PromptTemplate(
    input_variables = ['topic', 'language'],
    template = 'Give me a medium article title on {topic} in {language} language.'
)

llm = ChatOpenAI(temperature=0.9,model='gpt-4o')
title_chain = title_template | llm | StrOutputParser()

if topic:
    #response = llm(title_template.format(topic=topic,language='french'))
    response = title_chain.invoke({"topic": topic, "language": language})
    st.write(response)