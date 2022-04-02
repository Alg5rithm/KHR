N = int(input())

flag = False
k = 1000001
num = ''
for i in range(k):
    num = str(i)
    j = len(num)-1
    result = i
    while j >= 0 :
        result += int(num[j])
        j-=1
    if result == N:
        flag = True
        break

if flag:
    print(num)
else:
    print(0)
