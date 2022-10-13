import re
def solution(s):
    answer = []
    a = s.split("},")
    result = []
    for i in range(len(a)):
        temp = a[i].split(",")
        b = []
        for val in temp:
            c = re.sub(r'[^0-9]', '', val)
            b.append(int(c))
        result.append(b)
    result.sort(key = lambda x: len(x))
    
    answer.append(result[0][0])
    
    for i in range(1, len(result)):
        temp = result[i]
        for j in range(len(temp)):
            if temp[j] not in answer:
                answer.append(temp[j])
                break
            
    return answer
