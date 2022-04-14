N = int(input())
local = list(map(int, input().split()))
max_val = int(input())

start = 0 
end = max(local)
result = 0
while start <= end :
    total = 0
    mid = (start + end) // 2

    for x in local :
        if x <= mid :
            total += x
        else:
            total += mid
    
    if total > max_val:
        end = mid-1
    else:
        result = mid
        start = mid + 1
print(result)
