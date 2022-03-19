import heapq
INF = int(1e9)
V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V+1)]
distance = [INF] * (V+1)

for _ in range(E):
    u,v,w = map(int, input().split())
    # u에서 v로 가는 가중치 w
    graph[u].append((v,w))

# print(graph)
# print(distance)
def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start)) 
    while q:
        # 거리, 현재 노드
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
dijkstra(K)

for i in range(1, V+1):
    if distance[i] == 1e9:
        print("INF")
    else:
        print(distance[i])
