from agents.manager import ManagerAgent
import os

def run_agent(query):
    agent = ManagerAgent()
    agent.invoke(query)

if __name__ == '__main__':
    run_agent(f"""
    다음 file_key를 사용해서 Figma design을 읽고 분석해서 frontend 코드로 작성해줘.
    file_key: {os.getenv('FIGMA_FILE_KEY')} 
    """)

