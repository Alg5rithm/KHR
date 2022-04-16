import heapq
import sys
INF = int(1e9)
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
distance = [INF]* (n+1)
path = [[] for _ in range(n+1)]

for _ in range(m):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v,w)) # 출발 도시, 도착 도시, 버스 비용

s, f = map(int, input().split()) # 출발점, 도착점

def dijkstra(start):
    q = []
    heapq.heappush(q, [0, start])
    distance[start] = 0

    while q :
        dist, now = heapq.heappop(q)
        if dist > distance[now] :
            continue
        for i in graph[now]:
            cost = i[1] + dist
            if cost < distance[i[0]]:
                path[i[0]]=now
                distance[i[0]] = cost
                heapq.heappush(q, [cost, i[0]])

dijkstra(s)

answer = []
temp = f
while temp != s :
    answer.append(temp)
    temp = path[temp]
answer.append(s)

print(distance[f])
print(len(answer))
answer.reverse()
for i in answer :
    print(i, end=' ')