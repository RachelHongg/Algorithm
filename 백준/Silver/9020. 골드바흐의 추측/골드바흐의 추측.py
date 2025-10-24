import sys
import math

n = int(sys.stdin.readline())
arr = list(int(sys.stdin.readline()) for _ in range(n))

box = [1] * 10001
box[0] = 0
box[1] = 0

for i in range(2, 101):
    j = 2
    if(box[i] == 1):
        while(i * j < 10001):
            box[i * j] = 0      
            j = j + 1

result = []

for i in range(10001):
    if(box[i] == 1):
        result.append(i)
        
for num in arr:
    x = num // 2
    y = num // 2
    while(True): 
        if(x in result):
            if(y in result):
                print(x, y)
                break
        x = x - 1
        y = y + 1
        