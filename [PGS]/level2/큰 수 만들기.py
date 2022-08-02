
def solution(number, k):
    answer = ''
    array = list(number)  
    stack = list(array.pop(0))
    
    for i in range(len(array)):
        if array[i] > stack[-1]:
          # stack의 top인 값보다 클 때 앞에 있는 값 삭제(pop) 해줌
            while stack and stack[-1] < array[i] and k > 0:
                stack.pop()
                k -= 1
                if k == 0 :
                    break
            # 현재 값 push
            stack.append(array[i])
        # k가 0이거나 현재 값이 이전 값(top)보다 작으면 푸쉬
        elif k == 0 or array[i] <= stack[-1]:
            stack.append(array[i])
    # 예외사항 처리 : "4321" -> "432"
    while k > 0:
        stack.pop()
        k -= 1
    answer = ''.join(stack)
    return answer
