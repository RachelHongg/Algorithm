import sys
from collections import deque

result = []

def bfs(w, h, visited, maps):
    num = 0 
    queue = deque()
    for i in range(h):
        for j in range(w):
            if visited[i][j] == -1 and maps[i][j] == 1:
                num += 1
                queue.append([i, j])
                visited[i][j] = num
                while queue:
                    x, y = queue.popleft()
                    direction = [(-1,-1), (-1,0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
                    for dx, dy in direction:
                        nx = x + dx
                        ny = y + dy
                        if (0 <= nx < h and 0 <= ny < w):
                            if(visited[nx][ny] == -1 and maps[nx][ny] == 1):
                                queue.append([nx, ny])
                                visited[nx][ny] = num
    
    return num

while True:
    w, h = map(int, sys.stdin.readline().split())
    if (w == 0 and h == 0):
        break
    maps = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
    visited = [[-1] * w for _ in range(h)]
    res = bfs(w, h, visited, maps)
    result.append(res)

for r in result:
    print(r)