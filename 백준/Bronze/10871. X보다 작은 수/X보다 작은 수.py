n, x = map(int, input().split())
arr = list(map(int, input().split()))

res = []

for i in arr:
    if(i < x):
        res.append(i)

print(*res)
