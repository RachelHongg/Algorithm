s = input()

arr = list(s)
res = [ 0 ] * 26

# 각 알파벳의 아스키코드(97 ~ 122)를 차례로 res 배열(0~25)에 담는다.
for e in arr:
    i = ord(e) - 97
    res[i] += 1

print(*res)