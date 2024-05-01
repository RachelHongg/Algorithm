import sys

def move(n, x, y):
    if n == 1:
        print(f"{x} {y}")
        return 0
    if n > 1:
        move(n - 1, x, 6 -x -y)
        print(f"{x} {y}")
        move(n - 1, 6 -x -y, y)
    return 0

n = int(sys.stdin.readline())
print(2 ** n - 1)
if n <= 20:
    move(n, 1, 3)