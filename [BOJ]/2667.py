def dfs(x, y):
    # 범위를 벗어나는 경우 바로 False 리턴
    if x<0 or y<0 or x>=n or y>=n: 
        return False 

    # 단지가 있는 곳 (=1)인 경우 방문처리를 해주고(=0)
    # 단지 가구 수를 증가 시켜준다
    # 상하좌우를 탐색하면서 1인 곳 방문하도록 처리
    if graph[x][y] == 1:
        graph[x][y] = 0
        global result
        result += 1
        dfs(x+1,y)
        dfs(x-1,y)
        dfs(x,y+1)
        dfs(x,y-1)
        return True
    else : 
        return False
    


n = int(input())

graph = []

for i in range(n):
    graph.append(list(map(int, input())))
count = 0
result = 0
li = []
# count : 총 단지수, result : 단지내 집의 수, li : 단지내 집의 수를 담을 배열

for i in range(n):
    for j in range(n):

        if dfs(i, j) == True:
            li.append(result)
            count += 1
            result = 0

print(count)
li.sort()

for value in li :
    print(value)
