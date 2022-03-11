import sys
sys.setrecursionlimit(15000)

def dfs(x, y, val):
    if x<0 or y<0 or x>=n or y>=n:
        return False
    
    if graph[x][y] > val and visited[x][y] == False:
        visited[x][y] = True
        dfs(x+1, y, val)
        dfs(x-1, y, val)
        dfs(x, y+1, val)
        dfs(x, y-1, val)
        return True
    else:
        return False


n = int(input())
graph = []
visited = [[False for col in range(n)] for row in range(n)]

#높이는 1이상 100이하의 정수
maxVal = 1
minVal = 101
for i in range(n):
    graph.append(list(map(int, input().split())))
maxVal = max(max(graph))
minVal = min(min(graph))
li = []


if maxVal == minVal :
    # 아무 지역도 물에 잠기지 않을 수도 있다. 예를 들어,
    # 2 
    # 1 1
    # 1 1 인 경우 하나의 영역으로 1이 됨.
    print(1)
else:
    # 최대 높이부터 1까지 안전 구역을 구함
    for k in range(maxVal, 0, -1):
        count = 0
        for i in range(n):
            for j in range(n):
                if dfs(i,j,k) == True:
                    count += 1
        li.append(count)
        visited = [[False for col in range(n)] for row in range(n)]

    # 리스트에 담은 안전 구역들 중 제일 큰 값 출력
    print(max(li))
