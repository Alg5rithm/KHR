import sys
from collections import deque
sys.setrecursionlimit(10000)
def dfs(X, Y):
    if X<0 or Y<0 or X>=h or Y>=w:
        return False
    
    if graph[X][Y] == 1:
        graph[X][Y] = 0
        # 상하좌우 + 대각선 검사
        dfs(X+1, Y)
        dfs(X-1, Y)
        dfs(X, Y+1)
        dfs(X, Y-1)
        dfs(X-1, Y+1)
        dfs(X-1, Y-1)
        dfs(X+1, Y+1)
        dfs(X+1, Y-1)
        return True
    else:
        return False




while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0 :
        break
    count = 0
    graph = []
    for i in range(h):
        data = list(map(int, input().split()))
        graph.append(data)
    for i in range(h):
        for j in range(w):
            if dfs(i, j) == True:
                count += 1
    print(count)
