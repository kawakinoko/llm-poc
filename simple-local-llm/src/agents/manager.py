from langchain.agents import create_agent
from factory import get_llm
from tools.figma_inspector import figma_design_inspector
from tools.codegen import frontend_generator
from tools.llm import ask_user

SERVER_HOST = 'localhost'
SERVER_PORT = 11434
MANAGER_PROMPT_FILE_NAME = "prompts/manager_system.md"

class ManagerAgent:
  def __init__(self):
    try:
      manager_prompt_file = open(MANAGER_PROMPT_FILE_NAME, "r", encoding="utf-8")
      self.agent = create_agent(
          model=get_llm(
              model_name="qwen3.5:9b",
              temperature=0.1,
              max_tokens=4096,
              base_url=f"http://{SERVER_HOST}:{SERVER_PORT}/v1",
              api_key="not-needed"
          ),
          tools=[
            figma_design_inspector,
            frontend_generator,
            ask_user
          ],
          system_prompt=manager_prompt_file.read()
      )
    except FileNotFoundError as e:
      raise e

  def invoke(self, prompt):
    message = {"role": "user", "content": prompt}
    return self.agent.invoke({"messages": [message]})
