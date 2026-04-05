from langchain_core.tools import tool
from pydantic import BaseModel, Field
from utils.figma_client import FigmaClient

class FigmaFetcherInput(BaseModel):
  """개발코드를 작성하기 위한 스키마"""
  file_key: str = Field(description="Figma로부터 객체를 들고 오기 위한 file_key")

@tool(args_schema=FigmaFetcherInput)
def figma_design_json_fetcher(file_key: str):
  """
  주어진 file_key에 해당하는 figma design JSON 데이터를 받아옵니다.
  """
  figma_client = FigmaClient()
  return figma_client.get_file_nodes_json(file_key)
