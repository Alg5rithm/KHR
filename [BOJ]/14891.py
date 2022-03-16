from collections import deque

def check_right(num, vec):
    # 가장 오른쪽 톱니바퀴까지 검사. 4번째 톱니바퀴(index:3)를 넘어가거나 극이 같으면 회전x
    if num == 3 :
        return 
    if li[num][2] == li[num+1][6]:
        return
    else:
        check_right(num+1, vec*(-1))
        li[num+1].rotate(vec)

def check_left(num, vec):
    if num == 0 :
        return
    if li[num][6] == li[num-1][2]:
        return
    else:
        check_left(num-1, vec*(-1))
        li[num-1].rotate(vec)

li = []
for _ in range(4):
    li.append(deque(map(int, input())))

k = int(input())
for _ in range(k):
    num, vec = map(int, input().split()) # 1:시계, -1:반시계
    num -= 1
    
    check_right(num, vec*(-1))
    check_left(num,vec*(-1))
    li[num].rotate(vec)
    result = 0
for i in range(len(li)):
    if li[i][0] == 1:
        result += 2**i
print(result)
