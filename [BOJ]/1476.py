e, s, m = map(int, input().split())

array = [[[0 for _ in range(19)] for _ in range(28)] for _ in range(15)]

num = 1
i, j ,k = 0, 0, 0
while num <= 7980 :
    i += 1
    if i >= 15:
        i = 0
    j += 1
    if j >= 28 :
        j = 0
    k += 1
    if k >= 19 :
        k = 0
    
    if array[i-1][j-1][k-1] == 0:
        array[i-1][j-1][k-1] = num
    num += 1


print(array[e-1][s-1][m-1])
