from collections import deque
def dfs(V) :
    visited[V] = True
    print(V, end= ' ')
    for i in graph[V] :
        if visited[i] == False:
            dfs(i)

def bfs(start) :
    queue = deque([start])
    visited[start] = True

    while queue :
        num = queue.popleft()
        
        print(num, end= ' ')
        for i in graph[num] :
            if visited[i] == False :
                queue.append(i)
                visited[i] = True



N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for i in range(M):
    num1, num2 = map(int, input().split())
    graph[num1].append(num2)
    graph[num2].append(num1)

for i in range(1, N+1):
    graph[i] = sorted(graph[i])


dfs(V)
visited = [False] * (N+1)
print()
bfs(V)
