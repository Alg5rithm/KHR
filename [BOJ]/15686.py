# 0 : 빈 칸, 1: 집, 2: 치킨집
from itertools import combinations

def calcChickenDistance(x, y):
    return abs(x[0]-y[0]) + abs(x[1]-y[1])

N, M = map(int, input().split())

city = []
for _ in range(N):
    city.append(list(map(int, input().split())))


house = []
chicken = []

for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            house.append((i,j))
        elif city[i][j] == 2 :
            chicken.append((i,j))

combination_chicken = list(combinations(chicken, M))
chicken_distance = [0 for _ in range(len(combination_chicken))]

for i in house:
    for j in range(len(combination_chicken)):
        min_distance = 999
        for k in combination_chicken[j] :
            distance = calcChickenDistance(i,k)
            min_distance=min(distance, min_distance)
        chicken_distance[j] += min_distance
print(min(chicken_distance))
