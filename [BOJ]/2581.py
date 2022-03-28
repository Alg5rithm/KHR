import math
M = int(input())
N = int(input())

array = [True for _ in range(N+1)]
array[1] = False
for i in range(2, int(math.sqrt(N))+1):
    if array[i] == True :
        j = 2
        while i*j <= N:
            array[i*j] = False
            j += 1

result = []
for i in range(M, N+1):
    if array[i] == True:
        result.append(i)

if not result:
    print(-1)
else:
    print(sum(result), result[0])
