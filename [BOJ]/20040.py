import sys
sys.setrecursionlimit(10000)

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b :
        parent[b] = a
    else:
        parent[a] = b
# 점의 개수 n(3<=n<=500,000), 진행된 차례의 수 m(3<=m<=1,000,000)
n, m = map(int, input().split())
parent = [0] * n
for i in range(n):
    parent[i] = i

result = 0
cycle = False
for index in range(m):
    i, j = map(int, sys.stdin.readline().split())
    if find_parent(i) == find_parent(j):
        if result == 0:
            result = index + 1
    else:
        union_parent(i, j)

print(result)
