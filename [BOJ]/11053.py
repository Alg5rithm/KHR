# 수열 A의 크기
N = int(input())

# 둘째 줄에 수열 A를 이루는 Ai가 주어진다. (1<=Ai<=1000)
A = list(map(int, input().split()))
# A의 가장 긴 증가하는 부분 수열의 길이를 출력한다.
dp = [1] * N

for i in range(len(A)):
    for j in range(0, i):
        if A[i] > A[j] :
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))
