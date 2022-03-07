import sys
# 파이썬에서 재귀깊이가 제한되어있음. 다음 코드로 Recursion Error를 방지함.
sys.setrecursionlimit(10000)

def dfs(X, Y):
    if X < 0 or Y <0 or X >=N or Y >= M:
        return False
    
    if graph[X][Y] == 1 :
        graph[X][Y] = 0
        dfs(X+1, Y)
        dfs(X-1, Y)
        dfs(X, Y+1)
        dfs(X, Y-1)
        return True
    else:
        return False

T = int(input())

for i in range(T):

    M, N, K = map(int, input().split())
    graph = [[0 for col in range(M)] for row in range(N)]
    for i in range(K):
        X,Y = map(int, input().split())
        graph[Y][X] = 1
    count = 0

    for j in range(N):
        for i in range(M):
            if dfs(j, i) == True :
                count += 1
    print(count)
