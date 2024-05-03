import sys
n = int(sys.stdin.readline())
rightUp = [0] * (2 * n - 1)
rightDown = [0] * (2 * n - 1)
col = [0] * n
cnt = 0

def nQueen(i):
    global cnt
    if i == n:
        cnt += 1
        return
    for j in range(n):
            dif = i - j
            sum = i + j
            # 가능한 경우의 수
            if(col[j] == 0 and rightUp[sum] == 0 and rightDown[n - 1 - dif] == 0):
                # 퀸의 말을 놓았을때(자식 노드)
                rightUp[sum] = 1
                rightDown[n - 1 - dif] = 1
                col[j] = 1
                nQueen(i + 1)
                # 퀸의 말 뺐을때(부모 노드)
                rightUp[sum] = 0
                rightDown[n - 1 - dif] = 0
                col[j] = 0
            
    

nQueen(0)
print(cnt)


