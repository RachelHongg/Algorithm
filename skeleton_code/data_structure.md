# 자료구조 
## `python`으로 구현

---
< 면접에서 손코딩 대비용 >
### 큐
`언제 사용` bfs 구현시 사용

`무엇으로 구현` deque나 list로 구현가능

1) deque 사용
```python
from collections import deque

queue = deque()
# 큐의 rear에 새로운 데이터 삽입: enqueue
deque.append()
# 큐의 front에서 데이터 삭제: dequeue
deque.popleft()

```

2) list 사용
```python
queue = []
# 큐의 rear에 새로운 데이터 삽입: enqueue
queue.append()
# 큐의 front에서 데이터 삭제: dequeue
queue.pop(0)
```

### 배열

### 연결리스트

### 스택

### 힙

### 트리

### 그래프

### 해시
