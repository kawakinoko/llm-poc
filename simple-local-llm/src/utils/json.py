def simplify_json(node):
  """
  Figma 노드에서 프론트엔드 분석에 꼭 필요한 정보만 추출하는 재귀 함수
  """
  # 1. 현재 노드에서 추출할 기본 속성
  simplified = {
    "name": node.get("name"),
    "type": node.get("type"),
  }

  # 2. 텍스트 노드인 경우 내용 추가
  if node.get("type") == "TEXT":
    simplified["content"] = node.get("characters", "")

  # 3. 컴포넌트나 버튼 여부 판단에 도움되는 속성 (선택적)
  if "visible" in node and not node["visible"]:
    return None  # 보이지 않는 요소는 분석에서 제외

  # 4. 자식 노드가 있다면 재귀적으로 처리
  if "children" in node:
    children_list = []
    for child in node["children"]:
      simplified_child = simplify_json(child)
      if simplified_child:
        children_list.append(simplified_child)

    if children_list:
      simplified["children"] = children_list

  return simplified