# 헷갈린 부분
# 1) 행렬 순서
# 2) def bfs 없이함.

import sys
from collections import deque

n, m = map(int,sys.stdin.readline().split())
vis = [[0 for _ in range(m)] for _ in range(n)]
board = []

res_num = 0
res_cnt = 0

for i in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    board.append(row)

def bfs(startX, startY):
    queue = deque()
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

            
    vis[startX][startY] = 1
    queue.append((startX,startY))
    x, y = startX, startY

    cnt = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            mx = x + dx[i]
            ny = y + dy[i]
            if(mx < 0 or mx >= n or ny < 0 or ny >= m): continue
            if(board[mx][ny] != 1 or vis[mx][ny] == 1): continue
            vis[mx][ny] = 1
            queue.append((mx, ny))
            cnt += 1
    return cnt
            
            
for i in range(n):
    for j in range(m):
        if(board[i][j] == 1 and vis[i][j] != 1):
            res_num += 1
            res_cnt = max(res_cnt, bfs(i, j))

print(res_num)
print(res_cnt)