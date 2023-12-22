import sys
input = sys.stdin.readline
from collections import deque
sys.setrecursionlimit(10**6)

def dfs(visited, v, color1, color2):    
    visited[v] = color1
    for i in q[v]:
        # 색 중복일 때
        if visited[i] == color1:
            return False
        # 방문 안했을 때
        if visited[i] == False:
            result = dfs(visited, i, color2, color1)
            if not result:
                return False
    return True

T = int(input())

for _ in range(T):
    result = True
    N, V = map(int, input().split())
    visited = [False] * (N+1)
    q = [[] for _ in range(N+1)]
    for _ in range(V):
        a, b = map(int, input().split())
        q[a].append(b)
        q[b].append(a)
    for a in range(1, N+1):
        if visited[a] == False:
            result = dfs(visited, a, "RED", "BLACK")
            if not result:
                break
            
    if not result:
        print("NO")
    else:
        print("YES")
        
