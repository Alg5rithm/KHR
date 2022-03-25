import sys
from collections import deque
queue = deque()

def bfs():
    dx = [1,-1,0,0,0,0]
    dy = [0,0,1,-1,0,0]
    dz = [0,0,0,0,1,-1]

    while queue:
        x,y,z = queue.popleft()
        for i in range(6):
            a = x + dx[i]
            b = y + dy[i]
            c = z + dz[i]

            if 0<=a<H and 0<=b<N and 0<=c<M :
                if graph[a][b][c] == 0:
                    graph[a][b][c] = graph[x][y][z] + 1
                    queue.append([a,b,c])     
       
M, N, H = map(int, input().split())
graph = [[] for _ in range(H)]

for i in range(H):
    for j in range(N):
        graph[i].append(list(map(int, sys.stdin.readline().split())))

for i in range(H):
    for j in range(N):
        for k in range(M):
            if graph[i][j][k] == 1:
                queue.append([i,j,k])
bfs()

flag = 0
max_val = 0
for i in range(H):
    for j in range(N):
        for k in range(M):
            if graph[i][j][k] == 0:
                flag = -1
                break
            else:
                max_val = max(max_val, graph[i][j][k])

if flag == -1 :
    print(flag)
else:
    print(max_val - 1)
