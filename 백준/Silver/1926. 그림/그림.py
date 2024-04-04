# visit 체크 안하고, graph를 1 -> 0 으로 바꿔버리자!
import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = [[*map(int, sys.stdin.readline().split())] for _ in range(n)]
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

res_cnt = res_num = 0

def bfs(startX, startY):
    queue = deque()
    cnt = 1
    queue.append([startX, startY])
    graph[startX][startY] = 0
    x, y =startX, startY
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx, my = x + dx[k], y + dy[k]
            if(0<= nx < n and 0<= my < m and graph[nx][my] == 1):
                cnt += 1
                queue.append((nx, my))
                graph[nx][my] = 0
    return cnt
            
for i in range(n):
    for j in range(m):
        if(graph[i][j] == 1):
            res_cnt = max(res_cnt, bfs(i, j))
            res_num += 1

print(res_num)
print(res_cnt)