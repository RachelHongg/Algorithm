### 체크 사항
1. visit 방문 체크하는 배열 꼭 필요한가? <- 메모리 사용량 줄일 수 있는 기회...! graph와 통합해보는 시도해보자
2. 동시에 bfs를 시작하고 싶을때에는 queue를 미리 담아놓고, bfs를 시작하자. ex) 백준 7576번 예제3 이용하기
3. 행과 열 헷갈리지 않기..! `상하`는 행(n), `좌우`는 열(m)으로 fix 시키자
---
# BFS 코드
visit 없이 하나로 합친 경우, 0인 경우 벽, 1이 경로인 경우

```python
from collections from deque()

def bfs():

  # 상,하,좌,우 선언
  dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

  # queue 만들어주기
  queue = deque()
  deque.append([처음으로 넣는 큐])

  # 이제 하나씩 빼면서
  while queue:
    # 처음에 빼면서 시작
    x, y = queue.popleft()        

    for k in range(4):
      nx, my = x + dx[k], y + dy[k]

      # 여기에서 달라짐 -> 범위 안에 있고, [0, n], [0, m], 벽이 아닌 경우, 여기에 경우엔 graph가 1인 경우
      if(0 <= nx < n and 0 <= my < m and graph[nx][my] == 1):
        graph[nx][my] = graph[x][y] + 1
        deque.append([nx][my])
  
```  
