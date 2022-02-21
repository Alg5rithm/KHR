n = int(input())
li = list(map(int, input().split()))

dp = [0] * n

dp[0] = li[0]

for i in range(1, n):
    if dp[i-1] < 0 :
        dp[i] = li[i]
    else:
        
        dp[i] = li[i] + dp[i-1]
        
        if dp[i] < 0 : 
            dp[i] = 0
        
print(max(dp))
