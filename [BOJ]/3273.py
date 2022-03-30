import sys
n = int(input()) # 수열의 크기
li = list(map(int, sys.stdin.readline().split()))
x = int(input())

li.sort()

# 1 2 3 5 7 9 10 11 12
result = 0
count = 0
start = 0
end = n-1
while start < end :
    if li[start] + li[end] == x:
        count += 1
        start += 1
        end -= 1
    elif li[start] + li[end] > x:
        end -= 1
    else:
        start += 1


print(count)
