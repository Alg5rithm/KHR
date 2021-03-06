import sys
sys.setrecursionlimit(100000)
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

n, m = map(int, sys.stdin.readline().split())
parent = [0] * (n+1)

for i in range(1, n+1):
    parent[i] = i

for _ in range(m):
    x, y, z = map(int, sys.stdin.readline().split())
    if x == 0 :
        union_parent(y, z)

    else:
        x1 = find_parent(y)
        x2 = find_parent(z)
        if x1 == x2 :
            print("YES")
        else:
            print("NO")
