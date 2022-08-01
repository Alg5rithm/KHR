from collections import deque
def solution(priorities, location):
    answer = 0

    queue = deque(priorities)
    while len(queue) != 0:
        print(queue)
        flag = True
        for i in range(1, len(queue)):
            if queue[0] < queue[i]:
                flag = False
                break
        if flag == False : # 우선순위가 낮으면 뒤로보냄
            queue.append(queue[0])
            queue.popleft()
            if location == 0 :
                location += len(queue) -1
            else:
                location -= 1
        else: # 괜찮으면 pop
            answer += 1
            queue.popleft()
            if location == 0:
                break
            location -= 1
    
    return answer
 
