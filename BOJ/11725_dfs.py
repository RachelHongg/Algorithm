import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

N = int(input())
E = [[] for _ in range(N+1)]
for _ in range(N-1):
    a ,b = map(int, input().split())
    E[a].append(b)
    E[b].append(a)

visited = [False]*(N+1)
answer = [0]*(N+1)


def dfs(E,v,visited):
    visited[v] = True
    for i in E[v]:
        if not visited[i]:
            answer[i] = v
            dfs(E, i, visited)

dfs(E,1,visited)

for i in range(2,N+1):
    print(answer[i])
        
