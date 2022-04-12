import sys
sys.setrecursionlimit(10000)
def bfs(x, y):
    if x < 0 or y < 0 or x >= M or y >= N :
        return False
    else:
        if square[x][y] == 0:
            square[x][y] = 1
            global area
            area += 1
            bfs(x+1, y)
            bfs(x-1, y)
            bfs(x, y+1)
            bfs(x, y-1)
            return True
        else:
            return False

M, N, K = map(int, input().split())

square = [[0 for _ in range(N)] for _ in range(M)]

for _ in range(K):
    firstPoint_x, firstPoint_y, lastPoint_x, lastPoint_y = map(int, input().split())
    for i in range(firstPoint_y, lastPoint_y):
        for j in range(firstPoint_x, lastPoint_x):
            square[i][j] = 1

count = 0
area = 0

array = []
for i in range(M):
    for j in range(N):
        if bfs(i,j) == True:
            count += 1
            array.append(area)
            area = 0
print(count)
array.sort()

for i in range(len(array)):
    print(array[i], end=' ')
