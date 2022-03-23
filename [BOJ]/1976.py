import sys
sys.setrecursionlimit(15000)
def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N = int(input()) # 도시의 수. 200이하
M = int(input()) # 여행 계획에 속한 도시들의 수. 1000이하
parent = [0] * (N+1)
for i in range(N):
    parent[i] = i

# i번째 줄의 j번째 수는 i번 도시와 j번 도시의 연결 정보를 의미.
# 1이면 연결, 0이면 연결x. A와 B가 연결되어있으면, B와 A도 연결.
temp = []
for _ in range(N):
    temp.append(list(map(int, sys.stdin.readline().split())))

li = [] 
for i in range(N):
    for j in range(N):
        if temp[i][j] == 1:
            union_parent(i+1,j+1)
    
# 여행 계획
plan = list(map(int, input().split()))

flag = True 
for i in range(0, len(plan)-1):
    if find_parent(plan[i]) != find_parent(plan[i+1]):
        flag = False
        break

if flag == True:
    print("YES")
else:
    print("NO")
