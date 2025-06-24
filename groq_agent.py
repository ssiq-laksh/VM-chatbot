import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_experimental.agents import create_pandas_dataframe_agent
from data_loader import load_vm_data

load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

if not groq_api_key:
    raise ValueError("GROQ_API_KEY not found in .env file")

df = load_vm_data()

llm = ChatGroq(
    groq_api_key=groq_api_key,
    model_name="llama3-70b-8192",
    temperature=0
)

agent = create_pandas_dataframe_agent(
    llm,
    df,
    verbose=True,
    agent_type="openai-tools",
    allow_dangerous_code=True
)


def get_answer(question: str) -> str:
    try:
        return agent.run(question)
    except Exception as e:
        return f"Error processing question: {e}"
