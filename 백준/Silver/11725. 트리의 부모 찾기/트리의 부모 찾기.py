from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
E = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    E[a].append(b)
    E[b].append(a)
visited = [False]*(N+1)
answer = [0]*(N+1)

def bfs(E, v, vistied):
    q = deque([v])
    visited[v] = True
    while q:
        x = q.popleft()
        for i in E[x]:
            if not visited[i]:
                answer[i] = x
                q.append(i)
                visited[i] = True

bfs(E, 1, visited)

for i in range(2, N+1):
    print(answer[i])
