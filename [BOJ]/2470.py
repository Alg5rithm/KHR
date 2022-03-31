import sys

n = int(input())
data = list(map(int, sys.stdin.readline().split()))
data.sort()
start = 0
end = n - 1
min_val = 2000000001
a = 0 # 결과값1
b = 0 # 결과값2

# start가 end보다 작은 경웅에 진행
while start < end:
    num = data[start]+ data[end]
    # num의 절대값이 현재 제일 0에 가까운 수 min_val보다 작다면
    # a와 b에 현재 위치의 값을 업데이트한다.
    if abs(num) < min_val :
        min_val = abs(num)
        a = data[start]
        b = data[end]
        # 만약 num이 0이면 더이상 진행할 필요가 없으므로 종료.
        if num == 0 :
            break
    
    # 두 개의 값을 더했을 때 0보다 작다면 큰 값이 필요하므로 start+1
    # 0보다 크면 더 작은 값이 필요하므로 end -1
    if num < 0:
        start += 1
    else:
        end -= 1
print(a, b)
    
