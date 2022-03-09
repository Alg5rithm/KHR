import copy
import sys
sys.setrecursionlimit(10000)
def dfs(li, val, x, y):
    if x < 0 or y <0 or x >= n or y >= n:
        return False
    if li[x][y] == val :
        li[x][y] = 'X'
        dfs(li, val,x+1, y)
        dfs(li, val,x-1, y)
        dfs(li, val,x, y+1)
        dfs(li, val,x,y-1)
        return True
    else:
        return False



n = int(input())

graph = []
for i in range(n):
    graph.append(list(input()))

temp = copy.deepcopy(graph)
count = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] != 'X':
            if dfs(graph, graph[i][j], i,j) == True:
                count += 1

for i in range(n):
    for j in range(n):
        if temp[i][j] == 'G':
            temp[i][j] = 'R'
count_2 = 0

for i in range(n):
    for j in range(n):
        if temp[i][j] != 'X':
            if dfs(temp, temp[i][j], i,j) == True:
                count_2 += 1

print(count, count_2)
