from collections import deque

def bfs(x, y):
    queue = deque([[x,y]])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1 ,1]
    # li: 인구이동이 이뤄진 좌표 담을 배열
    # count: 인구이동이 이뤄진 횟수
    # sum_val: 연합국의 합

    li = []
    count = 0
    sum_val = 0
    while queue:
        x_y = queue.popleft()
        x1 = x_y[0]
        y1 = x_y[1]
        li.append([x1,y1])
        visited[x][y] = True
        count += 1
        sum_val += graph[x1][y1]
        for i in range(4):
            x2 = x1 + dx[i]
            y2 = y1 + dy[i]

            if x2<0 or y2<0 or x2>=N or y2>=N:
                x2 = x1
                y2 = y1
                continue
            else:
                if visited[x2][y2] == False:
                    val = abs(graph[x1][y1] - graph[x2][y2])
                    
                    if L <= val <= R:
                        visited[x2][y2] = True
                        queue.append([x2, y2])
                
                x2 = x1
                y2 = y1

    return count, sum_val, li

N, L, R = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int,input().split())))
result = 0
num = 0

while True:
    move = False
    visited = [[False for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j] == False :
                count, sum_val, li = bfs(i, j)
                if len(li) > 1:
                    move = True
                for x in li :
                    graph[x[0]][x[1]] = sum_val // count
    if move == False:
        break
    result += 1

print(result)
