import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

std = n // 2 + 1
res = 0
heavy_list = [[] for _ in range(n+1)]
light_list = [[] for _ in range(n+1)]

for _ in range(m):
    heavy, light = map(int, sys.stdin.readline().split())
    heavy_list[light].append(heavy)
    light_list[heavy].append(light)

def dfs(list, root):
    cnt = 0
    visited[root] = True
    stack = deque()
    stack.append(root)
    while stack:
        ele = stack.pop()
        for i in list[ele]:
            if not visited[i]:
                cnt += 1
                visited[i] = True
                stack.append(i)
    return cnt

for i in range(n+1):
    visited = [False] * (n+1)
    if(dfs(heavy_list, i) >= std): res += 1
    if(dfs(light_list, i) >= std): res += 1
print(res)
    