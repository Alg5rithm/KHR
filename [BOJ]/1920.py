def binary_search(array, target, start, end):
    if start > end :
        return 0
    mid = (start + end)//2
    if array1[mid] == target :
        return 1
    elif array1[mid] > target :
        return binary_search(array1, target, start, mid-1)
    else:
        return binary_search(array1, target, mid+1, end)



n = int(input())
array1 = list(map(int,input().split()))
array1.sort()

m = int(input())
array2 = list(map(int,input().split()))

for i in range(m):
    print(binary_search(array1, array2[i], 0, n-1))
