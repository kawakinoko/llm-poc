from langchain_core.tools import tool
from pydantic import BaseModel, Field
from agents.sub_agents.dev_agent import DevAgent


class DevInput(BaseModel):
  """개발코드를 작성하기 위한 스키마"""
  requirements: str = Field(description="Frontend 코드를 작성하기 위한 요구사항")

@tool(args_schema=DevInput)
def frontend_generator(requirements: str):
  """
  입력된 요구사항을 바탕으로 react 코드를 작성합니다.
  """
  dev_agent = DevAgent()
  result = dev_agent.invoke(requirements)
  output = result["messages"][-1].content
  print("✅ [frontend_generator result]")
  print(output)
