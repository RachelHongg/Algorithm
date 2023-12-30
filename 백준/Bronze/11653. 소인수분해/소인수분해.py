N = int(input())
res = []

while(True):
    if(N == 1):
        break
    for div in range(2, 10**7):
        if(N % div == 0):
            res.append(div)
            N = N // div
            break
res.sort()
for i in res:
    print(i)