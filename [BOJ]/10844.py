n = int(input())
dp = [[0 for _ in range(10)]for _ in range(101)]
# dp[3][1] => 3자리 수. 마지막에 오늘 숫자가 1일 때 가능한 경우의 수.
num = 1000000000
for i in range(1,10):
    dp[1][i] = 1

dp[2][0] = 1
dp[2][1] = 1
dp[2][9] = 1
for i in range(2,9):
    dp[2][i] = 2

for i in range(3, 101):
    for j in range(10):
        if j == 0 :
            dp[i][j] = dp[i-1][1]
        elif j == 9 :
            dp[i][j] = dp[i-1][8]
        else :
            dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1]) % num

print(sum(dp[n])%num)
