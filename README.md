# Medium Article Generator

A beginner-friendly LangChain project that demonstrates how to connect an OpenAI chat model to Streamlit, build simple prompt chains, compose sequential chains, and use tools through a LangChain agent.

## Features

- Generate Medium-style article titles from a topic.
- Generate titles in a selected language.
- Use a simple LangChain chain with `PromptTemplate`, `ChatOpenAI`, and `StrOutputParser`.
- Use a sequential chain where one LLM call generates a title and the next LLM call generates an article from that title.
- Use a LangChain agent with Wikipedia search and math tool support.

## Project Structure

```text
MediumArticleGenerator/
├── agents.py
├── apikey.py
├── app.py
├── requirements.txt
├── sequential_chains.py
├── simple_chain.py
└── README.md
```

## Files

- `app.py`: Basic Streamlit app that generates a Medium article title using `ChatOpenAI`.
- `simple_chain.py`: Demonstrates a simple LangChain pipeline: prompt -> LLM -> string output.
- `sequential_chains.py`: Demonstrates a sequential workflow: topic -> generated title -> generated article.
- `agents.py`: Demonstrates a LangChain agent using Wikipedia search and a calculator tool.
- `apikey.py`: Stores local API configuration. Do not upload real API keys to GitHub.
- `requirements.txt`: Python dependencies for the project.

## Setup

### 1. Clone the Repository

```powershell
git clone <your-repository-url>
cd MediumArticleGenerator
```

### 2. Create and Activate a Virtual Environment

On Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, run this once in the same terminal:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```powershell
pip install -r requirements.txt
```

### 4. Configure API Keys

Create an `apikey.py` file in the project root:

```python
OPENAI_API_KEY = "your-api-key-here"
OPENAI_API_BASE_URL = "your-api-base-url-here"
```

If you are using the default OpenAI API, your base URL is usually:

```python
OPENAI_API_BASE_URL = "https://api.openai.com/v1"
```

Important: do not commit your real `apikey.py` file to GitHub.

## How to Run

### Run the Basic Streamlit App

```powershell
streamlit run app.py
```

### Run the Simple Chain Example

```powershell
streamlit run simple_chain.py
```

### Run the Sequential Chain Example

```powershell
streamlit run sequential_chains.py
```

### Run the Agent Example

```powershell
python .\agents.py
```

Then enter a task, for example:

```text
when did the titanic sink and how many years have passed since then
```

## LangChain Concepts Used

### Chat Model

The project uses `ChatOpenAI` from `langchain_openai`:

```python
llm = ChatOpenAI(model="gpt-4o", temperature=0.9)
```

### Prompt Template

Prompt templates are used to insert user input into reusable prompts:

```python
PromptTemplate(
    input_variables=["topic"],
    template="Give me a medium article title on {topic}"
)
```

### Simple Chain

A simple chain performs one LLM task:

```text
Input -> Prompt -> LLM -> Output
```

### Sequential Chain

A sequential chain connects multiple steps:

```text
Topic -> Generate Title -> Generate Article
```

In this project, the generated title from the first chain is passed into the second chain to generate the article.

### Agent

The agent example uses tools so the model can decide when to search Wikipedia or perform math calculations.

## Security Notes

- Never upload real API keys to GitHub.
- Add `apikey.py` to `.gitignore` before publishing the repository.
- Prefer environment variables or secret managers for production projects.

## Requirements

Main dependencies include:

- `streamlit`
- `langchain`
- `langchain-openai`
- `langchain-community`
- `openai`
- `wikipedia`
- `numexpr`

See `requirements.txt` for the full dependency list.

## Future Improvements

- Add a `.gitignore` file to prevent committing secrets and cache files.
- Move API keys from `apikey.py` to environment variables.
- Add input validation for topic and language fields.
- Add a cleaner Streamlit UI for selecting model, language, and temperature.
- Save generated articles to a local file or database.