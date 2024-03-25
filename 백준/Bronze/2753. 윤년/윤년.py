year = int(input())

def isLeap(x):
    if (x % 400 == 0 or (x % 4 == 0 and x % 100 != 0)):
        return 1
    else:
        return 0

a= isLeap(year)
print(a)