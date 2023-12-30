# 8진수일떄
def oct2dec(N):
    print(int(N, 8))

# 10진수일때
def dec(N):
    print(int(N))
    
# 16진수일때
def hex2dec(N):
    print(int(N, 16))
    
N = input()
list = []

for i in map(str, str(N)):
    list.append(i)

# 몇진수인지 판단하기
def define():
    if(list[0] == '0'):
        if(list[1] == 'x'):
            return hex2dec(N)
        else:
            return oct2dec(N)
    else:
        return dec(N)

define()