from collections import deque
n, k = map(int, input().split())
MAX = 100000
def bfs():
  queue = deque()
  queue.append(n)
  while queue:
    x = queue.popleft()
    if x == k:
      print(distance[x])
      break
    temp = [x-1, x+1, x*2]
    for j in temp:
      if 0 <= j <= MAX and distance[j] == 0:
        distance[j] = distance[x] + 1
        queue.append(j)
      

distance = [0] * (MAX + 1)
bfs()
