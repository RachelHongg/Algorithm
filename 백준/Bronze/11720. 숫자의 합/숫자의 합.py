N = int(input())
num = int(input())
sum = 0

for i in range(N-1, -1, -1):
    sum += num // 10**i
    if(num == 0):
        break
    num = num % 10**i 

print(sum) 