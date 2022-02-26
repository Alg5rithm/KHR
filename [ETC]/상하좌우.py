n = int(input())
li = list(input().split())

x, y = 1, 1

move = ['R', 'U', 'L', 'D']
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

for val in li :
    for i in range(len(move)):
        if move[i] == val :
            x = x + dx[i]
            y = y + dy[i]
            
        if (x <= 0 or x >= n) or (y <= 0 or y>=n):
            x = x - dx[i]
            y = y - dy[i]
print(x, y)
