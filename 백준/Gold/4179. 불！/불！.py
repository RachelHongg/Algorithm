import sys
from collections import deque

# n 은 미로 행의 개수, m는 열의 개수
n, m = map(int, sys.stdin.readline().split())

# R 줄 동안 미로 행
graph = []
for _ in range(n):
    graph.append(list(map(str,sys.stdin.readline().rstrip())))


fire_map = [[0 for _ in range(m)] for _ in range(n)]
jh_map = [[0 for _ in range(m)] for _ in range(n)]

def bfs():
    # 상하좌우 퍼져나가기
    dx, dy = [-1, 1, 0, 0], [0, 0, 1, -1]
    # queue 안에서 로직 수행
    while queue:
        x, y, color = queue.popleft()
        for k in range(4):
            nx, my = x + dx[k], y + dy[k]
            # 범위 내에 있고, 벽이 아닐때
            if(0<= nx < n and 0<= my < m and graph[nx][my] != "#"):
                if(color == "F" and fire_map[nx][my] == 0):
                    queue.append([nx, my, "F"])
                    fire_map[nx][my] = 1
                if(color == "J" and fire_map[nx][my] == 0 and jh_map[nx][my] == 0):
                    queue.append([nx, my, "J"])
                    jh_map[nx][my] = jh_map[x][y] + 1
fire = []
# 초기방문 표시까지...!
for i in range(n):
    for j in range(m):
        if graph[i][j] == "F":
            each_fire = [i, j, "F"]
            fire.append(each_fire)
            fire_map[i][j] = 1
        if graph[i][j] == "J":
            jeehon = [i, j, "J"]
            jh_map[i][j] = 1

def escape():
    global res
    for i in range(n):
        if(jh_map[i][0] != 0):
            res.append(jh_map[i][0])
        if(jh_map[i][m - 1] != 0):
            res.append(jh_map[i][m - 1])

    for j in range(m):
        if(jh_map[0][j] != 0):
            res.append(jh_map[0][j])
        if(jh_map[n - 1][j] != 0):
            res.append(jh_map[n - 1][j])
    return res

# 동시에 넣는 거라서, queue 선언을 bfs밖으로 뺌.
queue = deque()
queue.extend(fire)
queue.append(jeehon)
# print(queue)
bfs()
# print(jh_map)
res = []
escape()
# print(res)
if(len(res) != 0): print(min(res))
else: print("IMPOSSIBLE")