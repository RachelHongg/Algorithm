import sys

n, r, c = map(int,sys.stdin.readline().split())
res = 0

def zNum(n, r, c, res):
    if (n == 1):
        print (2 * r + c + res)
        return
        
    tmp = 2**(n - 1)
    if (r < tmp and c < tmp):
        zNum(n - 1, r, c, res)
    if (r < tmp and c >= tmp):
        zNum(n - 1, r, c - tmp, res + tmp**2)
    if (r >= tmp and c < tmp):
        zNum(n - 1, r - tmp, c, res + 2 * tmp**2)
    if (r >= tmp and c >= tmp):
        zNum(n - 1, r - tmp, c - tmp, res + 3 * tmp**2)

zNum(n, r, c, res)