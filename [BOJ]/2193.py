N = int(input())
# 이친수 조건 1. 이친수는 0으로 시작하지 않는다.
# 조건 2. 1이 두 번 연속으로 나타나지 않는다. 즉, 11을 부부 문자열로 가지지 않는다.
# ex 1) 0010101 : 조건1에 어긋남.
# ex 2) 101101 : 조건2에 어긋남.
# N자리 이친수의 개수를 출력.


dp = [[0 for _ in range(2)] for _ in range(91)]

dp[1][1] = 1
dp[2][0] = 1
dp[3][1] = 1
dp[3][0] = 1

# dp[i][0]은 i자리수의 마지막 숫자가 0이고, dp[i][1]은 i자리수의 마지막 숫자가 1.
# dp[i][0]은 앞자리가 0,1 모든 경우에 쓸 수 있고 dp[i][1]은 바로 앞 자리 수가 0일 경우에만 쓸 수 있다.
for i in range(4, 91):
    dp[i][0] = dp[i-1][0] + dp[i-1][1]
    dp[i][1] = dp[i-1][0]

print(sum(dp[N]))
