import sys 
sys.setrecursionlimit(10**6)
def dfs(start):
  global order
  visited[start] = True
  result[start] = order
  order += 1
  for i in graph[start]:
    if visited[i] == False:
      dfs(i)


n, m, r = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
  u, v = map(int, sys.stdin.readline().split())
  graph[u].append(v)
  graph[v].append(u)

result = [0] * (n+1)
order = 1

for value in graph:
  value.sort()

visited = [False] * (n+1)
dfs(r)

print(result)
for i in range(1, n+1):
  print(result[i])
