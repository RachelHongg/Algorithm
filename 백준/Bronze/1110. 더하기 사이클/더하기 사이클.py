import sys

n = int(sys.stdin.readline())
num = n
cnt = 0
res = 0

while True:
    num_1 = num // 10
    num_2 = num % 10

    num_3 = (num_1 + num_2) % 10

    res = num_2 * 10 + num_3
    cnt += 1
    if res == n:
        break
    else: num =res

print(cnt)