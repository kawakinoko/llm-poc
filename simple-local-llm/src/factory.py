import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from pydantic import SecretStr

load_dotenv()

def get_llm(model_name="", temperature=0.7, max_tokens=1024, base_url=None,
    api_key: str = None):
  raw_key = api_key or os.getenv("OPENAI_API_KEY")
  secret_api_key = SecretStr(raw_key) if raw_key else None
  return ChatOpenAI(
      model=model_name,
      base_url=base_url,
      temperature=temperature,
      api_key=secret_api_key,
      max_tokens=max_tokens
  )
