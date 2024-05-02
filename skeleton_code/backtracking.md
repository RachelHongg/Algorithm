```python
def 재귀함수(x):
  if 정답이라면? :
    정답 출력 또는 저장 등
  else : 정답이 아니라면?
    for 뻗을 수 있는 모든 자식 노드에 대해서:
      if 정답이 유망하다면 :
        자식노드로 이동
        재귀함수(x + 1)
        부모노드로 이동
```

# Tip
## 자식/부모노드로 이동시 
- `stack 이용시`

  자식노드로 이동: stack.append()

  부모노드로 이동: stack.pop()
- `visited 이용시`

  자식노드로 이동: visited[i] = True `+` stack.append()

  부모노드로 이동: vistied[i] = False `+` stack.pop()

---
Reference: https://jie0025.tistory.com/455
