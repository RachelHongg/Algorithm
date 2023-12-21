import sys
sys.setrecursionlimit(10**5)

node = int(sys.stdin.readline())
tree = [[] for _ in range(node + 1)]
result = [] * (node + 1)
visited = [0] * (node + 1)

for i in range(1, node):
    start_edge, end_edge = map(int, sys.stdin.readline().split())
    tree[start_edge].append(end_edge)
    tree[end_edge].append(start_edge)

def dfs(graph, v):
    for i in graph[v]:
        if visited[i] == 0:
            visited[i] = v
            dfs(graph, i)

dfs(tree, 1)

for i in range(2, node + 1):
    print(visited[i])