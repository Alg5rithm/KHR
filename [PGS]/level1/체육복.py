def solution(n, lost, reserve):
    answer = 0
    # n : 전체 학생의 수
    # lost : 체육복이 없는 학생 번호
    # reserve : 가지고 있는 학생 번호
    
    array = [1 for _ in range(n+1)]
    
    
    for val in reserve:
        array[val] = 2
        
    for val in lost:
        if array[val] == 2:
            array[val] = 1
        else:
            array[val] = 0
    
    for i in range(1, n+1):
        if array[i] == 0:
            if i == 0:
                if array[i+1] == 2:
                    array[i] = 1
                    array[i+1] = 1
            else:
                if i < n:
                    if array[i-1] == 2:
                        array[i-1] = 1
                        array[i] = 1
                    elif array[i+1] == 2:
                        array[i+1] = 1
                        array[i] = 1
                else:
                    if array[i-1] == 2:
                        array[i-1] = 1
                        array[i] = 1
        
    for i in range(1, n+1):
        if array[i] >= 1:
            answer += 1
    
    return answer
