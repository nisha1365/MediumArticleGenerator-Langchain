import os

from apikey import OPENAI_API_KEY, OPENAI_API_BASE_URL
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.globals import set_verbose

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
os.environ["OPENAI_API_BASE_URL"] = OPENAI_API_BASE_URL
set_verbose(True)

st.title('Medium Article Generator')
topic = st.text_input('Input your topic of interest')

title_template = PromptTemplate(
    input_variables = ['topic'],
    template = 'Give me a medium article title on {topic}'
)

article_template = PromptTemplate(
    input_variables = ['title'],
    template = 'Give me a medium article for title: {title}'
)

llm = ChatOpenAI(temperature=0.9, model='gpt-4o')

title_chain = title_template | llm | StrOutputParser()

llm2 = ChatOpenAI(model='gpt-4o', temperature=0.9)

article_chain = article_template | llm2 | StrOutputParser()

overall_chain = title_chain | article_chain

if topic:    
    response = overall_chain.invoke({"topic": topic})
    st.write(response)