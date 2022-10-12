def dfs(x, y):
  global count
  if x >= n or y >= n or x < 0 or y < 0 :
    return False
  if graph[x][y] == 1:
    graph[x][y] = 0
    count += 1
    dfs(x+1, y)
    dfs(x-1, y)
    dfs(x, y+1)
    dfs(x, y-1)
    return True


n = int(input())
graph = []
for _ in range(n):
  graph.append(list(map(int, list(input()))))
count = 0
answer = 0
li = []
for i in range(n):
  for j in range(n):
    if dfs(i, j):
      answer += 1
      li.append(count)
      count = 0

li.sort()
print(answer)
for i in li:
  print(i)
