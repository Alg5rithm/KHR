def solution(numbers, target):
    answer = 0
    # 0부터 시작 -> numbers를 순회하며 +, - 해준 결과를 저장함
    
    array = [0]
    
    for num in numbers:
        temp = []
        for i in array:
            temp.append(i+num)
            temp.append(i-num)
        array = temp
    
    for val in array:
        if val == target:
            answer += 1
    return answer
