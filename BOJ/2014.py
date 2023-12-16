import sys
import heapq
input = sys.stdin.readline

K, N = map(int,input().split())
deci = list(map(int, input().split()))
heap = []

for d in deci:
    heapq.heappush(heap, d)

for _ in range(N):
    num = heapq.heappop(heap)
    for d in deci:
        numb = num * d
        heapq.heappush(heap, numb)
        if num % d == 0:
            break

print(num)
