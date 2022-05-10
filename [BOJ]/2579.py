import sys
N = int(input())

stairs = []

for _ in range(N):
    stairs.append(int(sys.stdin.readline()))

dp = [0] * N

if N == 1 :
    print(stairs[0])
elif N == 2 :
    print(stairs[0] + stairs[1])
else:
    dp[0] = stairs[0]
    dp[1] = stairs[1] + stairs[0]
    dp[2] = max(stairs[0]+stairs[2], stairs[1] + stairs[2])

    for i in range(3, N):
        dp[i] = max(dp[i-2]+stairs[i], stairs[i] + stairs[i-1] + dp[i-3])
    print(dp[N-1])
