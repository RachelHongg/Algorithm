import sys
import heapq

node = int(sys.stdin.readline())
edge = int(sys.stdin.readline())

graph = [[] for _ in range(node + 1)]

distance = [987654321] * (node + 1)

for _ in range(edge):
    start, end, cost = map(int, sys.stdin.readline().split())
    graph[start].append((cost, end))

fin_start, fin_end = map(int, sys.stdin.readline().split())


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue
        
        for nd, nx in graph[now]:
            if dist + nd < distance[nx]:
                distance[nx] = dist + nd
                heapq.heappush(q, (dist+nd, nx))
    return distance

dijkstra(fin_start)
print(distance[fin_end])
