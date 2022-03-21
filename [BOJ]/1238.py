import heapq
INF = int(1e9)
N, M, X = map(int, input().split())
graph = [[]for _ in range(N+1)]
distance = [INF] * (N+1)
for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v,w))

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q :
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

li = [0] * (N+1)
re = None
for i in range(1, N+1):
    distance = [INF] * (N+1)
    dijkstra(i)
    if i == X :
        re = distance
    # i -> X로 가는 최소비용
    li[i] = distance[X]

temp = []
for i in range(1, N+1):
    temp.append(li[i] + re[i])
print(max(temp))
