import sys

n, s = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
sum = cnt = 0

def back(k, sum):    # k번째 배열을 탐색
    global cnt
    # basecase
    if (k == n):
        if (sum == s):
            cnt += 1
        return 
    # k번째 수를 sum에 합칠지? 말지?
    # 경우 1) 합치는 경우
    is_sum = sum + arr[k]
    back(k + 1, is_sum)
    # 경우 2) 합치지 않는 경우
    not_sum = sum
    back(k + 1, not_sum)

back(0, 0)
if (s == 0):
    print(cnt - 1)
else:
    print(cnt)
