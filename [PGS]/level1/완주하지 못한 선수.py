# 방법 1 : 참가자와 완주자 목록을 정렬하고, 처음부터 순회하며 맞지 않는 경우가 완주하지 못한 사람

# def solution(participant, completion):
#     answer = ''
#     participant.sort()
#     completion.sort()
    
#     for i in range(len(completion)):
#         if(participant[i] != completion[i]):
#             answer = participant[i]
#             return answer
    
#     answer = participant[len(participant)-1]
#     return answer

# 방법 2 : hash를 사용하는 방법. 참가자 목록을 해쉬화하고, 이를 key값으로 설정한 dictionary를 생성.
# 참가자 목록에서 이를 해쉬화한 값을 계속 뺌 -> 남은 수가 key값

def solution(participant, completion):
    answer = ''
    hashmap = {}
    sumhash = 0
    
    for value in participant:
        hashmap[hash(value)] = value
        sumhash += hash(value)
        
    for value in completion:
        sumhash -= hash(value)
    
    
    return hashmap[sumhash]
