N = int(input())
dp = [[0]*3 for _ in range(N)]
R, G, B = map(int, input().split())
dp[0][0] = R
dp[0][1] = G
dp[0][2] = B
for i in range(1, N):
    # dp에 누적최소값을 넣어준다.
    R, G, B = map(int, input().split())
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + R
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + G
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + B

print(min(min(dp[N-1][0], dp[N-1][1]), dp[N-1][2]))
