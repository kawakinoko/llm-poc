from langchain.agents import create_agent
from factory import get_llm
from tools.figma_fetcher import figma_design_json_fetcher
from tools.llm import ask_user

SERVER_HOST = 'localhost'
SERVER_PORT = 11434
FIGMA_PROMPT_FILE_NAME = "prompts/figma_system.md"
FILE_KEY_TEMPLATE = "{{file_key}}"

class FigmaAgent:
  def __init__(self, file_key):
    try:
      figma_prompt_file = open(FIGMA_PROMPT_FILE_NAME, "r", encoding="utf-8")
      self.agent = create_agent(
          model=get_llm(
              model_name="qwen3.5:9b",
              temperature=0.1,
              max_tokens=4096,
              base_url=f"http://{SERVER_HOST}:{SERVER_PORT}/v1",
              api_key="not-needed"
          ),
          tools=[
            figma_design_json_fetcher,
            ask_user
          ],
          system_prompt=figma_prompt_file.read().replace(FILE_KEY_TEMPLATE, file_key)
      )
    except FileNotFoundError as e:
      raise e

  def invoke(self, prompt):
    message = {"role": "user", "content": prompt}
    return self.agent.invoke({"messages": [message]})
