N = int(input())
P = list(map(int, input().split()))

# DP[i] : i개의 카드를 구매할 때의 최소경비

# N=4일때
# 카드 한장 구매 => DP[1] = P[1]
# 카드 두장 구매 => DP[2] = min(P1 + DP[1], P2)
# 카드 세장 구매 => DP[3] = min(P1 + DP[2], P2 + DP[1], P3 + DP[0])

P.insert(0, 0)
DP = [10000001]*(N+1)
DP[0] = 0
DP[1] = P[1]

for i in range(2, N+1):
    for j in range(1, i+1):
        DP[i] = min(P[j] + DP[i-j], DP[i])

print(DP[N])
