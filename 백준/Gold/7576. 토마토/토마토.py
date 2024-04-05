import sys
from collections import deque

# 가로 M, 세로 N
m, n = map(int, sys.stdin.readline().split())
# graph 입력받기
graph = [[*map(int, sys.stdin.readline().split())] for _ in range(n)]

# 동시에 시작하기에 시작점을 미리 받자!
queue = deque()
for i in range(n):
    for j in range(m):
        if( graph[i][j] == 1): 
            queue.append([i, j])

def bfs():
    # 상, 하, 좌, 우 선언해주기
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    # queue 안의 값 빼고, 넣고 로직 수행
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx, my = x + dx[k], y + dy[k]
            # 범위 밖에 있을때,
            if(0<= nx < n and 0 <= my < m and graph[nx][my] == 0):
                graph[nx][my] = graph[x][y] + 1
                queue.append([nx, my])

def main():
    res = 0
    for i in range(n):
        for j in range(m):
            if(graph[i][j] == 0): 
                return(-1)
            res = max(res, graph[i][j])
    return (res - 1)

bfs()
print(main())
    