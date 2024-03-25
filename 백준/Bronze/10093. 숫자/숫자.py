a, b = map(int, input().split())

res = []

if (a == b):
    print(0)
elif (a < b):
    for i in range(a+1, b):
        res.append(i)
    print(len(res))
    print(*res)
else:
    for i in range(b + 1, a):
        res.append(i)
    print(len(res))
    res.sort()
    print(*res)