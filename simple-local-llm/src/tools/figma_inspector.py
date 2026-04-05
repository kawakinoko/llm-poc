from langchain_core.tools import tool
from pydantic import BaseModel, Field
from agents.sub_agents.figma_agent import FigmaAgent
from utils.figma_client import FigmaClient

class FigmaInspectorInput(BaseModel):
  """개발코드를 작성하기 위한 스키마"""
  file_key: str = Field(description="Figma로부터 객체를 들고 오기 위한 file_key")
  prompt: str = Field(description="유저로부터 입력된 추가 prompt")

@tool(args_schema=FigmaInspectorInput)
def figma_design_inspector(file_key: str, prompt: str):
  """
  주어진 file_key에 대해 객체를 분석합니다.
  유저로부터의 prompt를 입력으로 받아서 분석에 추가적으로 이용하여 정확한 결과를 제출합니다.
  """
  figma_agent = FigmaAgent(file_key)
  result = figma_agent.invoke(prompt)
  output = result["messages"][-1].content
  print("✅ [figma_design_inspector result]")
  print(output)

