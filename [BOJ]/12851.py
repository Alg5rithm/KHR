from collections import deque
def bfs():
  queue = deque()
  queue.append(n)
  distance[n][0] = 0
  distance[n][1] = 1
  while queue:
    x = queue.popleft()
    temp = [x-1, x+1, x*2]
    # 4, 6, 10

    for i in temp:
      if 0 <= i <= MAX and distance[i][0] == -1:
        distance[i][0] = distance[x][0] + 1
        distance[i][1] = distance[x][1]
        queue.append(i)
      elif 0 <= i <= MAX and distance[i][0] == distance[x][0] + 1:
        distance[i][1] += distance[x][1]

n, k = map(int, input().split())
MAX = 100000
distance = [[-1,0] for _ in range(MAX + 1)]
bfs()
print(distance[k][0])
print(distance[k][1])
