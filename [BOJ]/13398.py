n = int(input())
a = list(map(int, input().split()))
dp = [[0, 0] for _ in range(n)]

# 0 : 숫자 하나를 지웠을 때의 최대값
# 1 : 숫자 안지웠을 경우

dp[0][0] = a[0]
dp[0][1] = a[0]

for i in range(1, n):
    dp[i][1] = max(dp[i-1][1] + a[i], a[i])
    dp[i][0] = max(dp[i-1][1], dp[i-1][0] + a[i])

print(max(max(dp)))
