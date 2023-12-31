N = int(input())
stairs = [0] * 301

for i in range(N):
    a = int(input())
    stairs[i+1] = a

dp = [0] * 301

dp[1] = stairs[1]
dp[2] = stairs[1] + stairs[2]
dp[3] = stairs[3] + max(stairs[1], stairs[2])
for i in range(4, N+1):
    dp[i] = max(dp[i-3] + stairs[i-1], dp[i-2]) + stairs[i]

print(dp[N])