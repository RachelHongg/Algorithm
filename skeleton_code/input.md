# 1. 배열 입력

## 1.1 배열 요소들이 띄어쓰기 되어 있을 경우
예시 코드
```
1 1 0 1 1
0 1 1 0 0
0 0 0 0 0
1 0 1 1 1
0 0 1 1 1
0 0 1 1 1
```
예시 답안 코드
```
graph = [[*map(int, sys.stdin.readline().split())] for _ in range(n)]

```
## 1.2 배열의 요소들이 띄어쓰기 되어 있지 않은 경우

### 1.2.1 배열이 숫자 요소인 경우
예시 코드
```
101111
101010
101011
111011
```
예시 답안 코드
```
graph = []
for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().strip())))
```
### 1.2.2 배열이 문자 요소인 경우
예시 코드
```
####
#JF#
#..#
#..#
```
예시 답안 코드
```
graph = []
for _ in range(n):
    graph.append(list(map(str,sys.stdin.readline().rstrip())))
```
위의 2.2.1과 다른 점은 str로 map을 형성해였고, rstrip()을 사용
