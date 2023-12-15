import sys
import heapq
input = sys.stdin.readline

N = int(input())
R = [tuple(sorted(map(int,input().split()))) for _ in range(N)]
L = int(input())

R = sorted(R, key=lambda x:(x[1], x[0]))

maxR = 0
heap = []

for road in R:
    # 길이가 L보다 크면 continue
    if(road[1] - road[0] > L):
        continue
    # 위의 조건 통과면 heap에 넣기
    heapq.heappush(heap,road)
    # 힙에 있는 요소 돌기
    while heapq:
    # 힙 제일 처음에 들어간 얘의 출발점이 방금들어간 힙의 첫번째 요소보다 작으면 pop
        if(heap[0][0] < road[1] - L):
            heapq.heappop(heap)
        else:
            break
    # 힙 안에 들어있는 cnt 세기
    cnt = len(heap)
    # maxR 갱신하기
    maxR = max(maxR, cnt)

print(maxR)
