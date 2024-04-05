import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().strip())))

def dfs():
    # 이동할 상, 하, 좌, 우 방향 정리
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    # queue 선언하고, 초기 값 넣기
    queue = deque()
    queue.append([0,0])
    
    while queue:
        # 제일 앞에 빼내기
        x, y = queue.popleft()
        # 상, 하, 좌, 우 넣기
        for k in range(4):
            nx, my = x + dx[k], y + dy[k]
            # 범위 안 벗어나고, 벽이 아닐때, 길을 간다.
            if(0<= nx < n and 0<= my < m and graph[nx][my] == 1):
                    graph[nx][my] = graph[x][y] + 1
                    queue.append([nx, my])
                
        
dfs()
print(graph[n-1][m-1])
    