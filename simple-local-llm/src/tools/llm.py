
def ask_user(question: str) -> str:
  """사용자에게 질문을 던지고 답변을 받아옵니다."""
  print(f"\n🤖 [AI 질문]: {question}")
  user_response = input("👤 [내 답변]: ")
  return user_response