import os

from apikey import OPENAI_API_KEY, OPENAI_API_BASE_URL
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_community.agent_toolkits.load_tools import load_tools
import wikipedia

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
os.environ["OPENAI_API_BASE_URL"] = OPENAI_API_BASE_URL

llm = ChatOpenAI(model="gpt-4o", temperature=0.0)

@tool
def wikipedia_search(query: str) -> str:
	"""Search Wikipedia for a topic and return a short summary."""
	try:
		return wikipedia.summary(query, sentences=3)
	except Exception as error:
		return f"Wikipedia search failed: {error}"


tools = [wikipedia_search] + load_tools(["llm-math"], llm=llm)

agent = create_agent(
	model=llm,
	tools=tools,
	system_prompt="Use the available tools when useful. If Wikipedia search fails, answer from your own knowledge.",
	debug=True,
)

prompt = input("Wikipedia Research Task: ")

response = agent.invoke({"messages": [{"role": "user", "content": prompt}]})
print(response["messages"][-1].content)