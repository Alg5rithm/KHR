from collections import deque
def dfs(x, y):
    queue = deque([[x,y]])

    # 체스가 움직이는 범위
    dx = [-1,-2,-2,-1,+1,+2,+2,+1]
    dy = [-2,-1,+1,+2,-2,-1,+1,+2]
    while queue:
        temp = queue.popleft()
        x = temp[0]
        y = temp[1]

        # 원하는 위치에 도착하면 리턴
        if x == move_x and y == move_y :
            print(chess[x][y])
            return 

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]            

            # 범위내의 데이터라면 거리+1 해주고 queue에 데이터 추가
            if nx >= 0 and ny >= 0 and nx < l and ny < l:
                if chess[nx][ny]==0:
                    chess[nx][ny] = chess[x][y] + 1
                    queue.append([nx,ny])

            nx = nx - dx[i]
            ny = ny - dy[i]
        

T = int(input()) #TestCase


for _ in range(T):

    l = int(input()) # 체스판의 한 변의 길이

    # 현재 위치, 이동하려는 칸의 위치

    x, y = map(int, input().split())
    move_x, move_y = map(int, input().split())

    chess = [[0 for _ in range(l)] for _ in range(l)]
    dfs(x, y)
