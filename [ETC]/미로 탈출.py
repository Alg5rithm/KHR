from collections import deque

def bfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0,-1, 1]
    queue = deque([[x, y]])
    visited[x][y] = True
    print(queue)
    while queue:
        
        # 상하좌우 돌면서 1인 인덱스를 append
        temp = queue.popleft()
        print(temp)
        
        x = temp[0]
        y = temp[1]

        value = graph[x][y]+1
        for i in range(4):

            # temp = graph[x][y]
            x = x + dx[i]
            y = y + dy[i]

            if x >=0 and x < N  and y >= 0 and y < M:
                if graph[x][y] == 1 and visited[x][y] == False:

                    graph[x][y] = value
                    visited[x][y] = True
                    queue.append([x,y])

            x = x - dx[i]
            y = y - dy[i]



    

N, M = map(int,input().split())

graph = []
for i in range(N):
    graph.append(list(map(int,input())))

visited = []
for i in range(N):
    visited.append([False] * M)

bfs(0, 0)
print(graph[N-1][M-1])
