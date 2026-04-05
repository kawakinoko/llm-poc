from langchain.agents import create_agent
from factory import get_llm

SERVER_HOST = 'localhost'
SERVER_PORT = 11434
DEV_PROMPT_FILE_NAME = "prompts/dev_system.md"

class DevAgent:
  def __init__(self):
    try:
      dev_prompt_file = open(DEV_PROMPT_FILE_NAME, "r", encoding="utf-8")
      self.agent = create_agent(
          model=get_llm(
              model_name="qwen3.5:9b",
              temperature=0.1,
              max_tokens=4096,
              base_url=f"http://{SERVER_HOST}:{SERVER_PORT}/v1",
              api_key="not-needed"
          ),
          tools=[],
          system_prompt=dev_prompt_file.read()
      )
    except FileNotFoundError as e:
      raise e

  def invoke(self, prompt):
    message = {"role": "user", "content": prompt}
    return self.agent.invoke({"messages": [message]})