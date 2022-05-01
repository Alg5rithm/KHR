N = int(input())
A = list(map(int, input().split()))

dp = [1 for _ in range(N)]


for i in range(1, N):
    index = 0
    for j in range(i) :
        if A[i] > A[j] :
            dp[i] = max(dp[i], dp[j] + 1)
index = max(dp)
print(index)
li = []
for i in range(N-1, -1, -1):
    if dp[i] == index :
        li.append(A[i])
        index -= 1

li.reverse()

for v in li :
    print(v, end=' ')
