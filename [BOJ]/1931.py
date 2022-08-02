n = int(input())

S = []

for _ in range(n):
    a, b = map(int, input().split())
    S.append((a,b))
S.sort(key=lambda x: x[0])
S.sort(key=lambda x: x[1])

count = 1
x, y = S[0][0], S[0][1]
for i in range(1, len(S)):
    a, b = S[i][0], S[i][1]
    if a >= y :
        count += 1
        x, y = a, b

print(count)
