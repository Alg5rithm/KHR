import sys
T = int(input())

for i in range(T):
    N = int(input())
    li = []
    for j in range(N):
        A, B = map(int, sys.stdin.readline().split())
        li.append([A, B])
    
    li.sort(key= lambda x: (x[0], x[1]))
    
    num = li[0][1] # 기준

    count = 1

    for j in range(1, N):
        if li[j][1] < num :
            num = li[j][1]
            count += 1

    print(count)
