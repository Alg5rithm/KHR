from collections import deque

def dfs(start):
    # 첫 번째 시작 노드 방문처리
    visited[start] = True
    # 큐에 첫 번째 노드 삽입
    queue = deque([start])

    while queue :
        num = queue.popleft()
        for i in graph[num]:
            # 인접 노드를 방문하지 않았을 경우 큐에 넣고 방문 처리
            if visited[i] == False :
                queue.append(i)
                visited[i] = True
                global count
                count += 1


n= int(input())
m = int(input())

graph = []
for i in range(n+1):
    graph.append([])

for i in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
visited = [False] * (n+1)
count = 0
dfs(1)
print(count)
