import sys

n, m = map(int,sys.stdin.readline().split())
visited = [False] * (n + 1)
box = []

def backtracking(box):
    if len(box) == m:
        print(*box)
        return
    for i in range(1, n + 1):   
        if visited[i] == False:
            # 자식 노드로 이동
            visited[i] = True
            box.append(i)
            backtracking(box)
            # 부모노드로 이동
            box.pop()
            visited[i] = False

backtracking(box)