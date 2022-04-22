#첫째 줄에 민규가 구매하려고 하는 카드의 개수 N.

N = int(input())

# 둘째 줄부터 pi가 p1부터 pn까지 순서대로 주어진다.

P = list(map(int, input().split()))
P.insert(0, 0)

dp = [0] * (N+1)

for i in range(N+1):
    for j in range(i+1):
        dp[i] = max(P[i-j] + dp[j], dp[i])

print(dp[N])
