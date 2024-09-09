import sys
from collections import deque

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
a, b = map(int, sys.stdin.readline().split())

visited = [-1 for _ in range(n)]

def bfs():
    queue = deque()
    # 초기 a 시작점
    visited[a - 1] = 0
    queue.append(a - 1)
    while queue:
        now = queue.popleft()
        # 오른쪽으로 탐색
        for i in range(now, n, arr[now]):
            if visited[i] == -1:
                visited[i] = visited[now] + 1
                queue.append(i)
                if i == b -1:
                    return visited[i]
        # 왼쪽으로 탐색
        for j in range(now, -1, -arr[now]):
            if visited[j] == -1:
                visited[j] = visited[now] + 1
                queue.append(j)
                if j == b -1:
                    return visited[j]
    return -1

print(bfs())